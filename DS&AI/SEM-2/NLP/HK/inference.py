"""
NLP Hackathon — Inference Script
RA2512044015131_Dominic

Binary classification of product reviews (Sentiment Analysis)
Approach: TF-IDF (word + char n-grams) + LR/SVC Ensemble + Pseudo-labeling
Best OOF binary F1: ~0.9934  |  Kaggle eval_f1_binary: 0.9936
"""

import os
import re
import warnings
import numpy as np
import pandas as pd
from scipy.sparse import hstack, vstack
from sklearn.calibration import CalibratedClassifierCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, classification_report
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.svm import LinearSVC

warnings.filterwarnings("ignore")

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE  = os.path.dirname(os.path.abspath(__file__))
TRAIN = os.path.join(BASE, "train (1).csv")
TEST  = os.path.join(BASE, "test.csv")
OUT   = os.path.join(BASE, "submission.csv")

# ── 1. Load Data ───────────────────────────────────────────────────────────────
print("Loading data...")
train = pd.read_csv(TRAIN)
test  = pd.read_csv(TEST)
print(f"Train: {train.shape}  |  Test: {test.shape}")
print("Rating distribution:\n", train["Rating"].value_counts().to_string(), "\n")


# ── 2. Text Preprocessing ──────────────────────────────────────────────────────
def clean(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# Title × 3 for higher weighting (titles are very informative)
train["text"] = (
    (train["Review_Title"].fillna("") + " ") * 3 + train["Review"].fillna("")
).apply(clean)
test["text"] = (
    (test["Review_Title"].fillna("") + " ") * 3 + test["Review"].fillna("")
).apply(clean)

print("Sample cleaned text:", train["text"].iloc[0][:120])


# ── 3. TF-IDF Features ────────────────────────────────────────────────────────
print("\nFitting TF-IDF vectorizers (word + char n-grams)...")
all_texts = pd.concat([train["text"], test["text"]], ignore_index=True)

word_tfidf = TfidfVectorizer(
    analyzer="word",
    ngram_range=(1, 3),
    sublinear_tf=True,
    max_features=200_000,
    min_df=1,
    token_pattern=r"(?u)\b\w+\b",
)
char_tfidf = TfidfVectorizer(
    analyzer="char_wb",
    ngram_range=(2, 5),
    sublinear_tf=True,
    max_features=150_000,
    min_df=2,
)
word_tfidf.fit(all_texts)
char_tfidf.fit(all_texts)
print(f"Word vocab: {len(word_tfidf.vocabulary_):,}  |  Char vocab: {len(char_tfidf.vocabulary_):,}")


def make_features(texts):
    return hstack(
        [word_tfidf.transform(texts), char_tfidf.transform(texts)], format="csr"
    )


X_tr = make_features(train["text"])
X_te = make_features(test["text"])
y    = train["Rating"].values


# ── 4. Cross-validated OOF predictions (threshold tuning) ─────────────────────
print("\nRunning 5-fold OOF cross-validation...")
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

lr  = LogisticRegression(C=5, max_iter=2000, solver="lbfgs", n_jobs=-1)
svc = CalibratedClassifierCV(LinearSVC(C=0.3, max_iter=2000), cv=3)

lr_oof  = cross_val_predict(lr,  X_tr, y, cv=skf, method="predict_proba")[:, 1]
svc_oof = cross_val_predict(svc, X_tr, y, cv=skf, method="predict_proba")[:, 1]
ens_oof = (lr_oof + svc_oof) / 2.0

# Find best threshold on OOF (optimising weighted F1 to handle class imbalance)
best_t, best_f = 0.5, 0.0
for t in np.arange(0.05, 0.95, 0.005):
    score = f1_score(y, (ens_oof >= t).astype(int), average="weighted")
    if score > best_f:
        best_f, best_t = score, t

print(f"OOF weighted-F1 = {best_f:.6f} @ threshold = {best_t:.3f}")
print(f"OOF binary-F1   = {f1_score(y, (ens_oof >= best_t).astype(int)):.6f}")
print("\nClassification Report (OOF):")
print(classification_report(y, (ens_oof >= best_t).astype(int)))


# ── 5. Train on full data & predict test ──────────────────────────────────────
print("Training on full dataset...")
lr.fit(X_tr, y)
svc.fit(X_tr, y)
p_te = (lr.predict_proba(X_te)[:, 1] + svc.predict_proba(X_te)[:, 1]) / 2


# ── 6. Iterative Pseudo-labeling ──────────────────────────────────────────────
CONF       = 0.90
PL_ROUNDS  = 3
print(f"\nPseudo-labeling: {PL_ROUNDS} rounds, confidence threshold = {CONF}")

for rd in range(1, PL_ROUNDS + 1):
    mask  = (p_te >= CONF) | (p_te <= 1 - CONF)
    y_pl  = (p_te[mask] >= CONF).astype(int)

    if mask.sum() == 0:
        print(f"  Round {rd}: no confident pseudo-labels found, stopping.")
        break

    X_aug = vstack([X_tr, X_te[mask]])
    y_aug = np.concatenate([y, y_pl])

    lr2  = LogisticRegression(C=5, max_iter=2000, solver="lbfgs", n_jobs=-1)
    svc2 = CalibratedClassifierCV(LinearSVC(C=0.3, max_iter=2000), cv=3)
    lr2.fit(X_aug, y_aug)
    svc2.fit(X_aug, y_aug)
    p_te = (lr2.predict_proba(X_te)[:, 1] + svc2.predict_proba(X_te)[:, 1]) / 2

    p_tr = (lr2.predict_proba(X_tr)[:, 1] + svc2.predict_proba(X_tr)[:, 1]) / 2
    bf1  = f1_score(y, (p_tr >= best_t).astype(int), average="binary")
    wf1  = f1_score(y, (p_tr >= best_t).astype(int), average="weighted")
    print(
        f"  Round {rd}: pseudo-labels = {mask.sum():5d} "
        f"| train binary-F1 = {bf1:.6f} | train weighted-F1 = {wf1:.6f}"
    )


# ── 7. Save Submission ────────────────────────────────────────────────────────
final_preds = (p_te >= best_t).astype(int)
sub = pd.DataFrame({"ID": test["ID"], "Rating": final_preds})
sub.to_csv(OUT, index=False)

print(f"\nSaved: {OUT}")
print("Prediction distribution:")
print(sub["Rating"].value_counts().to_string())
