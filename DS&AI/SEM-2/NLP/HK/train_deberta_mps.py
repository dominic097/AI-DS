"""
DeBERTa fine-tuning — Unified script for M4 MPS, Kaggle GPU, and RunPod H100
Auto-detects device and tunes model/batch/precision accordingly.

Device profiles:
  M4 MPS           : bf16=True,  batch=64,  MAX_LEN=128, deberta-v3-base
  Kaggle P100/T4   : fp16=False, batch=16,  MAX_LEN=256, deberta-v3-base
  Kaggle A100      : fp16=True,  batch=32,  MAX_LEN=512, deberta-v3-base
  RunPod H100 SXM  : bf16=True,  batch=32,  MAX_LEN=512, deberta-v3-large  ← MAX MODE
"""

# ── Kaggle CUDA compat shim (skip on MPS/CPU) ─────────────────────────────────
# PyTorch 2.5+ dropped sm_75 support. Reinstall torch==2.4.1 if on old GPU.
import sys, os, subprocess

_IS_KAGGLE = os.path.exists("/kaggle")
_IS_RUNPOD = not _IS_KAGGLE and os.path.exists("/workspace") and os.path.isdir("/workspace")
_H100_MODE = False   # set True below when H100 is detected

if _IS_KAGGLE and os.environ.get("TORCH_COMPAT_INSTALLED") != "1":
    _check = subprocess.run(
        [sys.executable, "-c",
         "import torch; c=torch.cuda.get_device_capability() if torch.cuda.is_available() else (9,0); "
         "v=tuple(int(x) for x in torch.__version__.split('+')[0].split('.')[:2]); "
         "print(c[0],v[0],v[1])"],
        capture_output=True, text=True
    )
    if _check.returncode == 0:
        _parts = _check.stdout.strip().split()
        _sm, _vmaj, _vmin = int(_parts[0]), int(_parts[1]), int(_parts[2])
        print(f"[compat] GPU sm={_sm}  PyTorch={_vmaj}.{_vmin}", flush=True)
        if _sm < 80 and (_vmaj > 2 or (_vmaj == 2 and _vmin >= 5)):
            print("[compat] Reinstalling torch for sm<80...", flush=True)
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-q",
                "torch==2.4.1+cu121", "--index-url", "https://download.pytorch.org/whl/cu121"
            ])
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-q",
                "transformers==4.44.2", "accelerate>=0.33.0,<0.35.0",
                "tokenizers>=0.19,<0.21", "sentencepiece",
            ])
            os.environ["TORCH_COMPAT_INSTALLED"] = "1"
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            os.environ["TORCH_COMPAT_INSTALLED"] = "1"

# DeBERTa-v3 needs sentencepiece — install if missing
try:
    import sentencepiece  # noqa: F401
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "sentencepiece"])

# MPS: allow ops without native MPS kernel to fall back to CPU
os.environ.setdefault("PYTORCH_ENABLE_MPS_FALLBACK", "1")
os.environ.setdefault("PYTORCH_MPS_HIGH_WATERMARK_RATIO", "0.0")  # unlock full unified memory
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

import re, gc, warnings
import numpy as np
import pandas as pd
import torch
import glob
from torch.utils.data import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    EarlyStoppingCallback,
)
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_predict
from sklearn.metrics import f1_score, accuracy_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from scipy.sparse import hstack, vstack

warnings.filterwarnings("ignore")

# ── Device detection ──────────────────────────────────────────────────────────
if torch.cuda.is_available():
    DEVICE     = "cuda"
    _sm        = torch.cuda.get_device_properties(0).major * 10 + \
                 torch.cuda.get_device_properties(0).minor
    GPU_NAME   = torch.cuda.get_device_name(0)
    VRAM_GB    = torch.cuda.get_device_properties(0).total_memory / 1e9
    if _sm >= 89:           # H100 SXM/PCIe — MAXIMUM MODE
        USE_FP16   = False
        USE_BF16   = True   # H100 native bf16 — faster and more stable than fp16
        MAX_LEN, BATCH_TRAIN, BATCH_EVAL, GRAD_ACCUM = 512, 64, 128, 1
        _H100_MODE = True
    elif _sm >= 80:         # A100
        USE_FP16   = True
        USE_BF16   = False
        MAX_LEN, BATCH_TRAIN, BATCH_EVAL, GRAD_ACCUM = 512, 32, 64, 1
        _H100_MODE = False
    else:                   # T4 / P100 — stay safe
        USE_FP16   = False
        USE_BF16   = False
        MAX_LEN, BATCH_TRAIN, BATCH_EVAL, GRAD_ACCUM = 256, 16, 32, 2
        _H100_MODE = False
    _mode_tag = "  [H100-MAX: deberta-v3-large]" if _H100_MODE else ""
    print(f"[device] CUDA  sm={_sm}  {GPU_NAME}  {VRAM_GB:.1f}GB  "
          f"fp16={USE_FP16}  bf16={USE_BF16}  MAX_LEN={MAX_LEN}  BATCH={BATCH_TRAIN}{_mode_tag}")

elif torch.backends.mps.is_available():
    DEVICE     = "mps"
    USE_FP16   = False
    USE_BF16   = True       # M-series native bfloat16
    MAX_LEN, BATCH_TRAIN, BATCH_EVAL, GRAD_ACCUM = 128, 64, 128, 1  # 128² attn = ~5x faster than 256
    print(f"[device] Apple MPS (M-series)  bf16={USE_BF16}  MAX_LEN={MAX_LEN}  BATCH={BATCH_TRAIN}")

else:
    DEVICE     = "cpu"
    USE_FP16   = False
    USE_BF16   = False
    MAX_LEN, BATCH_TRAIN, BATCH_EVAL, GRAD_ACCUM = 128, 8, 16, 4
    print("[device] CPU — this will be slow!")

print(f"[env]    PyTorch {torch.__version__}")

# ── Paths ──────────────────────────────────────────────────────────────────────
if _IS_KAGGLE:
    OUTPUT = "/kaggle/working"
    CKPT   = os.path.join(OUTPUT, "deberta_ckpt")

    def find_csv(name):
        for pat in [
            f"/kaggle/input/nlp-hackathon-product-reviews/{name}",
            f"/kaggle/input/nlp-hackathon-product-reviews/**/{name}",
            f"/kaggle/input/**/{name}",
        ]:
            m = glob.glob(pat, recursive=True)
            if m: return m[0]
        raise FileNotFoundError(f"{name} not found.\n" +
            "\n".join(glob.glob("/kaggle/input/**", recursive=True)[:30]))

    print("\nInput tree:")
    for f in sorted(glob.glob("/kaggle/input/**", recursive=True)):
        print(" ", f)

    TRAIN_CSV = find_csv("train.csv")
    TEST_CSV  = find_csv("test.csv")
elif _IS_RUNPOD:
    # RunPod: upload train.csv and test.csv to /workspace/ before running
    OUTPUT    = "/workspace"
    CKPT      = os.path.join(OUTPUT, "deberta_ckpt")
    TRAIN_CSV = os.path.join(OUTPUT, "train.csv")
    TEST_CSV  = os.path.join(OUTPUT, "test.csv")
    print(f"[RunPod] TRAIN: {TRAIN_CSV}")
    print(f"[RunPod] TEST:  {TEST_CSV}")
else:
    BASE      = os.path.dirname(os.path.abspath(__file__))
    OUTPUT    = BASE
    CKPT      = os.path.join(BASE, "deberta_ckpt")
    TRAIN_CSV = os.path.join(BASE, "train (1).csv")
    TEST_CSV  = os.path.join(BASE, "test.csv")

print(f"TRAIN: {TRAIN_CSV}")
print(f"TEST:  {TEST_CSV}")

# ── Hyper-params ───────────────────────────────────────────────────────────────
# H100 max-mode: deberta-v3-large + longer context + more PL rounds
if _H100_MODE:
    MODEL_NAME   = "microsoft/deberta-v3-large"   # 400M params — ~0.002–0.003 F1 gain over base
    LR           = 1e-5    # scaled 2× for batch=64 (linear scaling rule)
    WARMUP_RATIO = 0.06
    PL_ROUNDS    = 3       # one extra pseudo-labeling round
    CONF         = 0.90    # slightly looser confidence → more pseudo-labels
    TFIDF_W      = 0.08    # trust large model more; less lexical blending
else:
    MODEL_NAME   = "microsoft/deberta-v3-base"
    LR           = 1e-5
    WARMUP_RATIO = 0.1
    PL_ROUNDS    = 2
    CONF         = 0.92
    TFIDF_W      = 0.12

EPOCHS       = 50
WEIGHT_DECAY = 0.01
PATIENCE     = 5
SEED         = 42

print(f"[config] MODEL={MODEL_NAME}  LR={LR}  MAX_LEN={MAX_LEN}  "
      f"PL_ROUNDS={PL_ROUNDS}  CONF={CONF}  TFIDF_W={TFIDF_W}")

# ── Data ───────────────────────────────────────────────────────────────────────
train_df = pd.read_csv(TRAIN_CSV)
test_df  = pd.read_csv(TEST_CSV)
print(f"\nTrain: {train_df.shape}  |  Test: {test_df.shape}")
print(train_df["Rating"].value_counts().to_string())


def clean(t):
    if not isinstance(t, str): return ""
    return re.sub(r"\s+", " ", t.lower()).strip()


def make_text(df):
    """Title × 3 + Review — title is highly predictive for sentiment."""
    return ((df["Review_Title"].fillna("") + " ") * 3 + df["Review"].fillna("")).apply(clean)


train_df["text"] = make_text(train_df)
test_df["text"]  = make_text(test_df)

# ── TF-IDF baseline (blended into final probs) ─────────────────────────────────
print("\n── TF-IDF + LR baseline ──")
all_texts  = pd.concat([train_df["text"], test_df["text"]], ignore_index=True)
wt = TfidfVectorizer(analyzer="word",    ngram_range=(1, 3), sublinear_tf=True,
                     max_features=200_000, min_df=1, token_pattern=r"(?u)\b\w+\b")
ct = TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 5), sublinear_tf=True,
                     max_features=150_000, min_df=2)
wt.fit(all_texts); ct.fit(all_texts)


def tfidf(texts):
    return hstack([wt.transform(texts), ct.transform(texts)], format="csr")


X_tfidf_tr = tfidf(train_df["text"])
X_tfidf_te = tfidf(test_df["text"])
y_all      = train_df["Rating"].to_numpy()

lr_tf  = LogisticRegression(C=5, max_iter=2000, solver="lbfgs", n_jobs=-1)
skf    = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
lr_oof = cross_val_predict(lr_tf, X_tfidf_tr, y_all, cv=skf, method="predict_proba")[:, 1]
print(f"TF-IDF OOF binary-F1: {f1_score(y_all, (lr_oof>=0.5).astype(int)):.6f}")

lr_tf.fit(X_tfidf_tr, y_all)
tfidf_test_p = lr_tf.predict_proba(X_tfidf_te)[:, 1]

# ── Tokenizer ─────────────────────────────────────────────────────────────────
print(f"\nLoading tokenizer: {MODEL_NAME}")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


# ── Dataset ───────────────────────────────────────────────────────────────────
class ReviewDataset(Dataset):
    def __init__(self, texts, labels=None):
        self.encodings = tokenizer(
            texts.tolist(),
            truncation=True, padding="max_length", max_length=MAX_LEN,
            return_tensors="pt",
        )
        self.labels = labels

    def __len__(self):
        return len(self.encodings["input_ids"])

    def __getitem__(self, idx):
        item = {k: v[idx] for k, v in self.encodings.items()}
        if self.labels is not None:
            item["labels"] = torch.tensor(int(self.labels[idx]), dtype=torch.long)
        return item


# ── Metrics ───────────────────────────────────────────────────────────────────
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    return {
        "f1_binary":   f1_score(labels, preds, average="binary",  zero_division=0),
        "f1_weighted": f1_score(labels, preds, average="weighted", zero_division=0),
        "accuracy":    accuracy_score(labels, preds),
    }



def tune_threshold(probs, labels):
    best_t, best_f = 0.5, 0.0
    for t in np.arange(0.05, 0.95, 0.005):
        s = f1_score(labels, (probs >= t).astype(int), average="binary", zero_division=0)
        if s > best_f: best_f, best_t = s, t
    return best_t, best_f


def get_probs(trainer_obj, dataset):
    out = trainer_obj.predict(dataset)
    return torch.softmax(torch.tensor(out.predictions, dtype=torch.float32), dim=-1)[:, 1].numpy()


def make_training_args(out_dir, lr_val, seed_val, save_limit=2):
    return TrainingArguments(
        output_dir                  = out_dir,
        num_train_epochs            = EPOCHS,
        per_device_train_batch_size = BATCH_TRAIN,
        per_device_eval_batch_size  = BATCH_EVAL,
        gradient_accumulation_steps = GRAD_ACCUM,
        learning_rate               = lr_val,
        warmup_ratio                = WARMUP_RATIO,
        weight_decay                = WEIGHT_DECAY,
        eval_strategy               = "epoch",
        save_strategy               = "epoch",
        load_best_model_at_end      = True,
        metric_for_best_model       = "f1_binary",
        greater_is_better           = True,
        fp16                        = USE_FP16,
        bf16                        = USE_BF16,
        dataloader_num_workers      = 0 if DEVICE == "mps" else 4,
        dataloader_pin_memory       = False,   # MPS uses unified memory
        save_total_limit            = save_limit,
        report_to                   = "none",
        seed                        = seed_val,
        logging_steps               = 50,
        max_grad_norm               = 1.0,
        torch_compile               = (DEVICE == "cuda"),
        torch_compile_backend       = "inductor",
    )


def load_fresh_model():
    m = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)
    try:
        m.config.use_cache = False
        m.gradient_checkpointing_enable()
        print("  Gradient checkpointing: ON")
    except Exception:
        pass
    return m


# ── Train / Val split ─────────────────────────────────────────────────────────
X_train, X_val, y_train, y_val = train_test_split(
    train_df["text"].to_numpy(), train_df["Rating"].to_numpy(),
    test_size=0.10, random_state=SEED, stratify=train_df["Rating"].to_numpy(),
)
print(f"\nTrain: {len(X_train):,}  |  Val: {len(X_val):,}")
print("Tokenizing...")
train_ds = ReviewDataset(pd.Series(X_train), y_train)
val_ds   = ReviewDataset(pd.Series(X_val),   y_val)
test_ds  = ReviewDataset(test_df["text"])
print("Done.\n")

# ── Base training ─────────────────────────────────────────────────────────────
print(f"Loading model: {MODEL_NAME}")
model = load_fresh_model()
n_params = sum(p.numel() for p in model.parameters()) / 1e6

print("=" * 60)
print(f"  Model  : {MODEL_NAME} ({n_params:.0f}M params)")
print(f"  Device : {DEVICE.upper()}")
print(f"  Batch  : {BATCH_TRAIN} × accum {GRAD_ACCUM} = {BATCH_TRAIN*GRAD_ACCUM} eff")
print(f"  MaxLen : {MAX_LEN}  |  LR: {LR}  |  bf16: {USE_BF16}  fp16: {USE_FP16}")
print("=" * 60)

trainer = Trainer(
    model           = model,
    args            = make_training_args(CKPT, LR, SEED),
    train_dataset   = train_ds,
    eval_dataset    = val_ds,
    compute_metrics = compute_metrics,
    callbacks       = [EarlyStoppingCallback(early_stopping_patience=PATIENCE)],
)
trainer.train()
print(f"\nBase val f1_binary: {trainer.state.best_metric:.6f}")

val_probs      = get_probs(trainer, val_ds)
best_t, best_f = tune_threshold(val_probs, y_val)
print(f"Threshold: {best_t:.3f}  →  F1: {best_f:.6f}")

# Initial blended test probs
test_probs_deb = get_probs(trainer, test_ds)
test_probs     = (1 - TFIDF_W) * test_probs_deb + TFIDF_W * tfidf_test_p

# ── Pseudo-labeling ───────────────────────────────────────────────────────────
print(f"\n── Pseudo-labeling: {PL_ROUNDS} rounds (conf={CONF}) ──")
for rnd in range(1, PL_ROUNDS + 1):
    mask      = (test_probs >= CONF) | (test_probs <= 1.0 - CONF)
    pl_texts  = test_df["text"].to_numpy()[mask]
    pl_labels = (test_probs[mask] >= CONF).astype(int)
    n_pos = pl_labels.sum(); n_neg = (~pl_labels.astype(bool)).sum()
    print(f"\nRound {rnd}: {mask.sum():,} pseudo-labels  (pos={n_pos:,}  neg={n_neg:,})")

    aug_ds  = ReviewDataset(pd.Series(np.concatenate([X_train, pl_texts])),
                             np.concatenate([y_train, pl_labels]))
    val_ds2 = ReviewDataset(pd.Series(X_val), y_val)

    del model; gc.collect()
    if DEVICE == "cuda": torch.cuda.empty_cache()
    elif DEVICE == "mps": torch.mps.empty_cache()

    model2   = load_fresh_model()
    trainer2 = Trainer(
        model           = model2,
        args            = make_training_args(os.path.join(CKPT, f"pl_{rnd}"), LR * 0.7, SEED + rnd, save_limit=1),
        train_dataset   = aug_ds,
        eval_dataset    = val_ds2,
        compute_metrics = compute_metrics,
        callbacks       = [EarlyStoppingCallback(early_stopping_patience=PATIENCE)],
    )
    trainer2.train()
    print(f"  PL round {rnd} best val f1_binary: {trainer2.state.best_metric:.6f}")

    # Update DeBERTa test probs
    test_probs_deb = get_probs(trainer2, test_ds)

    # Update TF-IDF on augmented data (skip if no pseudo-labels selected)
    if len(pl_texts) == 0:
        print(f"  No pseudo-labels at conf={CONF}, skipping TF-IDF update")
        tfidf_test_p2 = tfidf_test_p
    else:
        X_aug_tf  = vstack([X_tfidf_tr, tfidf(pd.Series(pl_texts))])
        y_aug_tf  = np.concatenate([y_all, pl_labels])
        lr_tf2    = LogisticRegression(C=5, max_iter=2000, solver="lbfgs", n_jobs=-1)
        lr_tf2.fit(X_aug_tf, y_aug_tf)
        tfidf_test_p2 = lr_tf2.predict_proba(X_tfidf_te)[:, 1]

    test_probs = (1 - TFIDF_W) * test_probs_deb + TFIDF_W * tfidf_test_p2

    # Re-tune threshold
    val_probs2     = get_probs(trainer2, val_ds2)
    best_t, best_f = tune_threshold(val_probs2, y_val)
    print(f"  Updated threshold: {best_t:.3f}  →  val F1: {best_f:.6f}")
    model = model2

# ── Final predictions ─────────────────────────────────────────────────────────
final_preds = (test_probs >= best_t).astype(int)
sub = pd.DataFrame({"ID": test_df["ID"], "Rating": final_preds})
out = os.path.join(OUTPUT, "submission.csv")
sub.to_csv(out, index=False)

print(f"\n{'='*60}")
print(f"  submission.csv → {out}")
print(f"  Rows: {len(sub):,}")
print("  Distribution:")
print(sub["Rating"].value_counts().to_string())
print(f"  Final val binary-F1: {best_f:.6f}")
print("="*60)
