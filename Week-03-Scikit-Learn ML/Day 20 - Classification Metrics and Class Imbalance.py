"""
Day 20 · Classification metrics & class imbalance
Accuracy, confusion matrix, precision, recall, F1, ROC-AUC, PR-AUC, thresholds,
and what to do when one class is rare.
"""
from pathlib import Path

import numpy as np
from sklearn.datasets import make_classification
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    average_precision_score,
    confusion_matrix,
    f1_score,
    precision_recall_curve,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

HERE = Path(__file__).parent
RANDOM = 42

# A fraud-like problem: only 3% of transactions are fraud (class 1)
X, y = make_classification(
    n_samples=10_000, n_features=20, n_informative=6,
    weights=[0.97, 0.03], class_sep=0.8, random_state=RANDOM,
)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=RANDOM
)
print(f"Fraud share: {y.mean():.1%} ({y_test.sum()} fraud cases in the test set)")


def report(name, y_true, y_pred, y_score=None):
    line = (f"{name:<28} acc {accuracy_score(y_true, y_pred):.3f} | "
            f"prec {precision_score(y_true, y_pred, zero_division=0):.3f} | "
            f"rec {recall_score(y_true, y_pred):.3f} | "
            f"F1 {f1_score(y_true, y_pred):.3f}")
    if y_score is not None:
        line += f" | ROC-AUC {roc_auc_score(y_true, y_score):.3f} | PR-AUC {average_precision_score(y_true, y_score):.3f}"
    print(line)


# ------------------------------------------------------------
# 1. Why accuracy lies on imbalanced data
# ------------------------------------------------------------
print("\n=== 1. The accuracy trap ===")
dummy = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
report("Always says 'not fraud'", y_test, dummy.predict(X_test))
print(f"{accuracy_score(y_test, dummy.predict(X_test)):.1%} accuracy while catching ZERO fraud. Accuracy alone is misleading here.")

# ------------------------------------------------------------
# 2. Confusion matrix -> precision, recall, F1
# ------------------------------------------------------------
print("\n=== 2. Confusion matrix of a real model ===")
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(X_train, y_train)
pred = model.predict(X_test)
scores = model.predict_proba(X_test)[:, 1]

tn, fp, fn, tp = confusion_matrix(y_test, pred).ravel()
print("                 predicted OK   predicted FRAUD")
print(f"actually OK      {tn:>11}   {fp:>15}")
print(f"actually FRAUD   {fn:>11}   {tp:>15}")
print(f"Precision = TP / (TP + FP) = {tp} / {tp + fp} = {tp / (tp + fp):.3f}")
print(f"Recall    = TP / (TP + FN) = {tp} / {tp + fn} = {tp / (tp + fn):.3f}")
report("Logistic regression", y_test, pred, scores)

# ------------------------------------------------------------
# 3. Changing the threshold: trade precision for recall
# ------------------------------------------------------------
print("\n=== 3. Threshold: when do we call it fraud? ===")
for t in [0.5, 0.3, 0.15, 0.05]:
    p = (scores >= t).astype(int)
    print(f"threshold {t:<5} -> caught {recall_score(y_test, p):.0%} of fraud, "
          f"{precision_score(y_test, p, zero_division=0):.0%} of alerts were real, "
          f"{p.sum():>4} alerts")
print("Lower threshold = catch more fraud, but more false alarms")

# Best F1 threshold, chosen on the TRAINING data (never tune on test)
train_scores = model.predict_proba(X_train)[:, 1]
prec, rec, thr = precision_recall_curve(y_train, train_scores)
f1s = 2 * prec[:-1] * rec[:-1] / (prec[:-1] + rec[:-1] + 1e-12)
best_t = thr[np.argmax(f1s)]
report(f"Logistic, threshold {best_t:.2f}", y_test, (scores >= best_t).astype(int), scores)

# ------------------------------------------------------------
# 4. Fixing imbalance: class weights
# ------------------------------------------------------------
print("\n=== 4. Handling imbalance ===")
balanced = make_pipeline(
    StandardScaler(), LogisticRegression(class_weight="balanced", max_iter=1000)
).fit(X_train, y_train)
report("Logistic, class_weight=balanced", y_test, balanced.predict(X_test),
       balanced.predict_proba(X_test)[:, 1])

rf = RandomForestClassifier(n_estimators=300, class_weight="balanced_subsample",
                            random_state=RANDOM, n_jobs=-1).fit(X_train, y_train)
rf_scores = rf.predict_proba(X_test)[:, 1]
report("Random forest, balanced", y_test, rf.predict(X_test), rf_scores)
report("Random forest, threshold 0.3", y_test, (rf_scores >= 0.3).astype(int), rf_scores)

# Random oversampling by hand: copy fraud rows until classes are equal (TRAIN only)
rng = np.random.default_rng(RANDOM)
fraud_idx = np.where(y_train == 1)[0]
extra = rng.choice(fraud_idx, size=(y_train == 0).sum() - len(fraud_idx), replace=True)
X_over = np.vstack([X_train, X_train[extra]])
y_over = np.concatenate([y_train, y_train[extra]])
over = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(X_over, y_over)
report("Logistic, oversampled", y_test, over.predict(X_test), over.predict_proba(X_test)[:, 1])
print("(SMOTE from the imbalanced-learn library creates NEW synthetic fraud rows instead of copies)")

# ------------------------------------------------------------
# 5. Curves
# ------------------------------------------------------------
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from sklearn.metrics import roc_curve

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
    for name, s in [("Logistic", scores), ("Random forest", rf_scores)]:
        fpr, tpr, _ = roc_curve(y_test, s)
        ax1.plot(fpr, tpr, label=f"{name} (AUC {roc_auc_score(y_test, s):.2f})")
        p_, r_, _ = precision_recall_curve(y_test, s)
        ax2.plot(r_, p_, label=f"{name} (AP {average_precision_score(y_test, s):.2f})")
    ax1.plot([0, 1], [0, 1], "k--", label="random guess")
    ax1.set(xlabel="False positive rate", ylabel="Recall (true positive rate)", title="ROC curve")
    ax2.axhline(y_test.mean(), color="k", linestyle="--", label="random guess")
    ax2.set(xlabel="Recall", ylabel="Precision", title="Precision-Recall curve")
    ax1.legend(); ax2.legend()
    fig.tight_layout()
    fig.savefig(HERE / "day20_roc_pr_curves.png", dpi=110)
    print("\nSaved plot: day20_roc_pr_curves.png")
except ImportError:
    pass

print("\nWhich metric when?")
print("  Missing a positive is costly (fraud, cancer) -> watch RECALL")
print("  False alarms are costly (spam filter)         -> watch PRECISION")
print("  Rare positive class                            -> PR-AUC and F1, not accuracy")
