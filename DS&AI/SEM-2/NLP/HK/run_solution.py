"""
NLP Hackathon Solution — RA2512044015131_Dominic
Binary classification of product reviews to maximize F1-Score
"""

import pandas as pd
import numpy as np
import re
import warnings
warnings.filterwarnings('ignore')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.metrics import f1_score, classification_report
from sklearn.calibration import CalibratedClassifierCV
from scipy.sparse import hstack

# ── 1. Load Data ──────────────────────────────────────────────────────────────
import os
BASE = "/Users/damirdarasu/workspace/workbooks/AI-DS/DS&AI/SEM-2/NLP/HK"
train = pd.read_csv(f"{BASE}/train (1).csv")
test  = pd.read_csv(f"{BASE}/test.csv")
print(f"Train: {train.shape}  |  Test: {test.shape}")
print("Rating distribution:\n", train['Rating'].value_counts(), "\n")

# ── 2. Text Preprocessing ─────────────────────────────────────────────────────
def clean_text(text):
    if not isinstance(text, str):
        return ''
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s!?.,]', ' ', text)
    return text.strip()

# Duplicate title for higher weighting (title is very informative)
train['text'] = (train['Review_Title'].fillna('') + ' ' +
                 train['Review_Title'].fillna('') + ' ' +
                 train['Review'].fillna('')).apply(clean_text)

test['text']  = (test['Review_Title'].fillna('')  + ' ' +
                 test['Review_Title'].fillna('')   + ' ' +
                 test['Review'].fillna('')).apply(clean_text)

# ── 3. TF-IDF Features (word + char n-grams) ─────────────────────────────────
all_texts = pd.concat([train['text'], test['text']], ignore_index=True)

print("Fitting TF-IDF vectorizers...")
word_tfidf = TfidfVectorizer(
    analyzer='word', ngram_range=(1, 3), sublinear_tf=True,
    max_features=150_000, min_df=1, strip_accents='unicode',
    token_pattern=r'(?u)\b\w+\b'
)
char_tfidf = TfidfVectorizer(
    analyzer='char_wb', ngram_range=(2, 5), sublinear_tf=True,
    max_features=100_000, min_df=2, strip_accents='unicode'
)

word_tfidf.fit(all_texts)
char_tfidf.fit(all_texts)

X_train = hstack([word_tfidf.transform(train['text']),
                  char_tfidf.transform(train['text'])], format='csr')
X_test  = hstack([word_tfidf.transform(test['text']),
                  char_tfidf.transform(test['text'])],  format='csr')
y_train = train['Rating'].values
print(f"X_train: {X_train.shape}  |  X_test: {X_test.shape}\n")

# ── 4. Cross-Validation & Threshold Tuning ───────────────────────────────────
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

def best_threshold(proba, y, average='weighted'):
    best_t, best_f = 0.5, 0.0
    for t in np.arange(0.05, 0.95, 0.01):
        score = f1_score(y, (proba >= t).astype(int), average=average)
        if score > best_f:
            best_f, best_t = score, t
    return best_t, best_f

# Model A: Logistic Regression (class_weight=balanced)
print("Cross-validating Logistic Regression...")
lr = LogisticRegression(C=5.0, max_iter=1000, class_weight='balanced',
                        solver='lbfgs', n_jobs=-1)
lr_oof = cross_val_predict(lr, X_train, y_train, cv=skf, method='predict_proba')[:, 1]
t_lr, f_lr = best_threshold(lr_oof, y_train)
print(f"LR  OOF weighted-F1: {f_lr:.6f}  (threshold={t_lr:.2f})")

# Model B: LinearSVC (calibrated)
print("Cross-validating LinearSVC...")
svc = CalibratedClassifierCV(LinearSVC(C=0.5, class_weight='balanced', max_iter=2000), cv=3)
svc_oof = cross_val_predict(svc, X_train, y_train, cv=skf, method='predict_proba')[:, 1]
t_svc, f_svc = best_threshold(svc_oof, y_train)
print(f"SVC OOF weighted-F1: {f_svc:.6f}  (threshold={t_svc:.2f})")

# Model C: LR without class balancing (good when majority-class F1 matters)
print("Cross-validating LR (unbalanced)...")
lr2 = LogisticRegression(C=5.0, max_iter=1000, solver='lbfgs', n_jobs=-1)
lr2_oof = cross_val_predict(lr2, X_train, y_train, cv=skf, method='predict_proba')[:, 1]
t_lr2, f_lr2 = best_threshold(lr2_oof, y_train)
print(f"LR2 OOF weighted-F1: {f_lr2:.6f}  (threshold={t_lr2:.2f})")

# Ensemble all three
ens_oof = (lr_oof + svc_oof + lr2_oof) / 3.0
t_ens, f_ens = best_threshold(ens_oof, y_train)
print(f"\nENSEMBLE OOF weighted-F1: {f_ens:.6f}  (threshold={t_ens:.2f})")
print()
print(classification_report(y_train, (ens_oof >= t_ens).astype(int)))

# ── 5. Train Final Models on All Training Data ────────────────────────────────
print("Training final models on full training data...")
lr.fit(X_train, y_train)
svc.fit(X_train, y_train)
lr2.fit(X_train, y_train)

test_proba = (lr.predict_proba(X_test)[:, 1] +
              svc.predict_proba(X_test)[:, 1] +
              lr2.predict_proba(X_test)[:, 1]) / 3.0

test_preds = (test_proba >= t_ens).astype(int)

print("Test prediction distribution:")
for v, c in zip(*np.unique(test_preds, return_counts=True)):
    print(f"  Rating {v}: {c} ({c/len(test_preds)*100:.1f}%)")

# ── 6. Save Submission ────────────────────────────────────────────────────────
submission = pd.DataFrame({'ID': test['ID'], 'Rating': test_preds})
submission.to_csv(f"{BASE}/submission.csv", index=False)
print(f"\nSaved submission.csv  ({len(submission)} rows)")
print(submission.head(10))
