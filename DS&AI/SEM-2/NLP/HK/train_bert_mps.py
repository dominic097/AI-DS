"""
DistilBERT fine-tuning on Apple M4 MPS GPU
- Up to 50 epochs with early stopping (patience=5)
- Best model checkpoint auto-loaded at end
- Generates submission.csv
"""

import os, re, warnings
os.environ['TOKENIZERS_PARALLELISM']        = 'false'
os.environ['PYTORCH_MPS_HIGH_WATERMARK_RATIO'] = '0.0'   # unlock full unified memory for MPS
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']   = '1'        # fallback to CPU for unsupported ops
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset
from transformers import (
    DistilBertTokenizerFast,
    DistilBertForSequenceClassification,
    TrainingArguments,
    Trainer,
    EarlyStoppingCallback,
)
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import f1_score, accuracy_score, classification_report, confusion_matrix

# ── Device ────────────────────────────────────────────────────────────────────
device = "mps" if torch.backends.mps.is_available() else "cpu"
print(f"Device : {device}")
print(f"PyTorch: {torch.__version__}\n")

BASE = os.path.dirname(os.path.abspath(__file__))

# ── 1. Load data ──────────────────────────────────────────────────────────────
train_full = pd.read_csv(f"{BASE}/train (1).csv")
test_df    = pd.read_csv(f"{BASE}/test.csv")
print(f"Train: {train_full.shape}  |  Test: {test_df.shape}")
print(f"Class distribution:\n{train_full['Rating'].value_counts().to_string()}\n")

# ── 2. Text preprocessing ─────────────────────────────────────────────────────
def clean(t):
    if not isinstance(t, str): return ''
    t = re.sub(r'\s+', ' ', t.lower())
    return t.strip()

def make_text(df):
    # Title × 3 weighting — same as TF-IDF pipeline
    return ((df['Review_Title'].fillna('') + ' ') * 3 + df['Review'].fillna('')).apply(clean)

train_full['text'] = make_text(train_full)
test_df['text']    = make_text(test_df)

# ── 3. Train / val split (90/10 stratified) ───────────────────────────────────
sss = StratifiedShuffleSplit(n_splits=1, test_size=0.10, random_state=42)
idx_tr, idx_val = next(sss.split(train_full, train_full['Rating']))
tr  = train_full.iloc[idx_tr].reset_index(drop=True)
val = train_full.iloc[idx_val].reset_index(drop=True)
print(f"Train split : {len(tr):,}  |  Val split: {len(val):,}")
print(f"Val class 1 : {val['Rating'].mean():.3f}\n")

# ── 4. Tokenizer & Dataset ────────────────────────────────────────────────────
MODEL_NAME = "distilbert-base-uncased"
MAX_LEN    = 128

print(f"Loading tokenizer: {MODEL_NAME}")
tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_NAME)

class ReviewDataset(Dataset):
    def __init__(self, texts, labels=None):
        self.encodings = tokenizer(
            texts,
            truncation=True,
            padding='max_length',
            max_length=MAX_LEN,
        )
        self.labels = labels

    def __len__(self):
        return len(self.encodings['input_ids'])

    def __getitem__(self, idx):
        item = {k: torch.tensor(v[idx]) for k, v in self.encodings.items()}
        if self.labels is not None:
            item['labels'] = torch.tensor(self.labels[idx], dtype=torch.long)
        return item

print("Tokenizing datasets...")
train_ds = ReviewDataset(tr['text'].tolist(),       tr['Rating'].tolist())
val_ds   = ReviewDataset(val['text'].tolist(),      val['Rating'].tolist())
test_ds  = ReviewDataset(test_df['text'].tolist())   # no labels
print(f"Datasets ready. Train={len(train_ds):,}  Val={len(val_ds):,}  Test={len(test_ds):,}\n")

# ── 5. Metrics ────────────────────────────────────────────────────────────────
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=1)
    return {
        'f1_binary':   f1_score(labels, preds, average='binary'),
        'f1_weighted': f1_score(labels, preds, average='weighted'),
        'accuracy':    accuracy_score(labels, preds),
    }

# ── 6. Model ──────────────────────────────────────────────────────────────────
print(f"Loading model: {MODEL_NAME}")
model = DistilBertForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=2,
)

# ── torch.compile: graph fusion + kernel optimization (PyTorch 2.x) ──────────
try:
    model = torch.compile(model)
    print("torch.compile: enabled (faster MPS kernels)\n")
except Exception as e:
    print(f"torch.compile: skipped ({e})\n")

CKPT_DIR = os.path.join(BASE, "bert_checkpoints")

# ── 7. Training arguments ─────────────────────────────────────────────────────
training_args = TrainingArguments(
    output_dir              = CKPT_DIR,
    num_train_epochs        = 50,            # up to 50; early stopping kicks in
    per_device_train_batch_size = 128,       # 64→128: keeps GPU fuller each step
    per_device_eval_batch_size  = 256,
    gradient_accumulation_steps = 2,         # effective batch = 256, less fragmentation
    learning_rate           = 2e-5,
    warmup_ratio            = 0.06,
    weight_decay            = 0.01,
    eval_strategy           = "epoch",
    save_strategy           = "epoch",
    load_best_model_at_end  = True,
    metric_for_best_model   = "f1_binary",
    greater_is_better       = True,
    save_total_limit        = 2,
    logging_steps           = 50,
    dataloader_num_workers  = 4,             # parallel CPU data loading (PyTorch 2.x MPS safe)
    dataloader_prefetch_factor = 2,          # pre-fetch next batch while GPU trains
    dataloader_pin_memory   = False,         # MPS uses unified memory — pin_memory not needed
    report_to               = "none",
    bf16                    = True,          # M-series natively supports bfloat16
    fp16                    = False,
)

# ── 8. Trainer ────────────────────────────────────────────────────────────────
trainer = Trainer(
    model           = model,
    args            = training_args,
    train_dataset   = train_ds,
    eval_dataset    = val_ds,
    compute_metrics = compute_metrics,
    callbacks       = [EarlyStoppingCallback(early_stopping_patience=5)],
)

print("=" * 60)
print("  Starting fine-tuning on MPS (Apple M4 GPU)")
print("  Max epochs : 50  |  Early stopping patience : 5")
print("  Batch size : 128 x grad_accum 2 = eff. batch 256")
print("  Max seq len: 128  |  Workers: 4 + prefetch 2")
print("  Model      : distilbert-base-uncased (66M params)")
print("=" * 60)
trainer.train()

# ── 9. Evaluate best model on validation set ──────────────────────────────────
print("\nEvaluating best checkpoint on validation set...")
metrics = trainer.evaluate()
print(f"\n  Val binary-F1  : {metrics['eval_f1_binary']:.6f}")
print(f"  Val weighted-F1: {metrics['eval_f1_weighted']:.6f}")
print(f"  Val accuracy   : {metrics['eval_accuracy']:.6f}")

# ── 10. Full evaluation with confusion matrix ─────────────────────────────────
val_preds_out = trainer.predict(val_ds)
val_proba     = torch.softmax(torch.tensor(val_preds_out.predictions, dtype=torch.float32), dim=1)[:, 1].numpy()
val_labels    = val['Rating'].values

# Tune threshold on val set
best_t, best_f = 0.5, 0.0
for t in np.arange(0.05, 0.95, 0.005):
    s = f1_score(val_labels, (val_proba >= t).astype(int), average='binary')
    if s > best_f:
        best_f, best_t = s, t
print(f"\n  Best threshold on val : {best_t:.3f}  (binary-F1 = {best_f:.6f})")

val_preds_final = (val_proba >= best_t).astype(int)
cm = confusion_matrix(val_labels, val_preds_final)
print(f"\nConfusion Matrix (val):")
print(f"  TN={cm[0,0]:5d}  FP={cm[0,1]:5d}")
print(f"  FN={cm[1,0]:5d}  TP={cm[1,1]:5d}")
print(f"\n{classification_report(val_labels, val_preds_final, target_names=['Neg(0)', 'Pos(1)'])}")

# ── 11. Predict test set ──────────────────────────────────────────────────────
print("Predicting test set...")
test_preds_out = trainer.predict(test_ds)
test_proba     = torch.softmax(torch.tensor(test_preds_out.predictions, dtype=torch.float32), dim=1)[:, 1].numpy()
test_preds     = (test_proba >= best_t).astype(int)

sub = pd.DataFrame({'ID': test_df['ID'], 'Rating': test_preds})
sub.to_csv(f"{BASE}/submission.csv", index=False)

print(f"\nSaved submission.csv  ({len(sub):,} rows)")
print(sub['Rating'].value_counts().to_string())

# ── 12. Verify against sample_submission ─────────────────────────────────────
sample = pd.read_csv(f"{BASE}/sample_submission.csv")
print(f"\nVerification:")
print(f"  Columns match : {sample.columns.tolist() == sub.columns.tolist()}")
print(f"  Row count     : {len(sub)} (expected {len(sample)})")
print(f"  IDs match     : {sorted(sub['ID'].tolist()) == sorted(sample['ID'].tolist())}")
print(f"  Valid labels  : {set(sub['Rating'].unique()).issubset({0, 1})}")
print(f"\nDone!")
