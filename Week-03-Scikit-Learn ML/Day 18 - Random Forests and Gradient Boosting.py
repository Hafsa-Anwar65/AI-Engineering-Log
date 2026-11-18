"""
Day 18 · Ensembles: random forests (bagging) & gradient boosting (boosting)
One tree is weak and unstable. Many trees together are strong.
"""
import time

import numpy as np
from sklearn.datasets import load_breast_cancer, load_wine
from sklearn.ensemble import (
    GradientBoostingClassifier,
    HistGradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier

RANDOM = 42

data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM
)

# ------------------------------------------------------------
# 1. Why one tree isn't enough: it changes a lot with the data
# ------------------------------------------------------------
print("=== 1. One tree is unstable ===")
rng = np.random.default_rng(RANDOM)
for i in range(3):
    idx = rng.choice(len(X_train), size=len(X_train), replace=True)   # a bootstrap sample
    tree = DecisionTreeClassifier(random_state=RANDOM).fit(X_train[idx], y_train[idx])
    first_question = data.feature_names[tree.tree_.feature[0]]
    print(f"Tree {i + 1}: first question uses '{first_question}', "
          f"test accuracy {tree.score(X_test, y_test):.3f}")
print("Small changes in the data -> different trees and different scores")

# ------------------------------------------------------------
# 2. Bagging by hand: many trees on bootstrap samples, then vote
# ------------------------------------------------------------
print("\n=== 2. Bagging by hand (25 trees voting) ===")
votes = []
for _ in range(25):
    idx = rng.choice(len(X_train), size=len(X_train), replace=True)
    tree = DecisionTreeClassifier(max_features="sqrt", random_state=int(rng.integers(1e6)))
    votes.append(tree.fit(X_train[idx], y_train[idx]).predict(X_test))
majority = (np.mean(votes, axis=0) > 0.5).astype(int)
print(f"Average single tree: {np.mean([np.mean(v == y_test) for v in votes]):.3f}")
print(f"Majority vote:       {np.mean(majority == y_test):.3f}")

# ------------------------------------------------------------
# 3. Comparing models with 5-fold cross-validation
# ------------------------------------------------------------
print("\n=== 3. Model comparison (5-fold cross-validation) ===")
models = {
    "Decision tree": DecisionTreeClassifier(random_state=RANDOM),
    "Random forest": RandomForestClassifier(n_estimators=200, random_state=RANDOM, n_jobs=-1),
    "Gradient boosting": GradientBoostingClassifier(random_state=RANDOM),
    "Hist gradient boosting": HistGradientBoostingClassifier(random_state=RANDOM),
}
print(f"{'Model':<24}{'Mean acc':>9}{'Std':>8}{'Time':>8}")
for name, model in models.items():
    start = time.perf_counter()
    scores = cross_val_score(model, X, y, cv=5)
    print(f"{name:<24}{scores.mean():>9.3f}{scores.std():>8.3f}{time.perf_counter() - start:>7.1f}s")
print("Lower Std = more stable. Ensembles beat a single tree.")

# ------------------------------------------------------------
# 4. Random forest: number of trees and feature importance
# ------------------------------------------------------------
print("\n=== 4. Random forest ===")
for n in [1, 10, 50, 200]:
    rf = RandomForestClassifier(n_estimators=n, random_state=RANDOM, n_jobs=-1).fit(X_train, y_train)
    print(f"{n:>3} trees -> test accuracy {rf.score(X_test, y_test):.3f}")

rf = RandomForestClassifier(n_estimators=200, oob_score=True, random_state=RANDOM, n_jobs=-1)
rf.fit(X_train, y_train)
print(f"Out-of-bag score (free validation from unused samples): {rf.oob_score_:.3f}")

print("\nTop 5 important features:")
for i in np.argsort(rf.feature_importances_)[::-1][:5]:
    bar = "█" * int(rf.feature_importances_[i] * 100)
    print(f"  {data.feature_names[i]:<22} {rf.feature_importances_[i]:.3f} {bar}")

# ------------------------------------------------------------
# 5. Gradient boosting: each new tree fixes the last ones' mistakes
# ------------------------------------------------------------
print("\n=== 5. Gradient boosting: learning rate vs number of trees ===")
for lr in [0.01, 0.1, 1.0]:
    gb = GradientBoostingClassifier(learning_rate=lr, n_estimators=100, random_state=RANDOM)
    gb.fit(X_train, y_train)
    # staged_predict shows the accuracy after 1, 2, 3 ... trees
    staged = [np.mean(p == y_test) for p in gb.staged_predict(X_test)]
    print(f"learning_rate={lr:<5} after 10 trees {staged[9]:.3f} | after 100 trees {staged[-1]:.3f}")
print("Small learning rate = slow but careful; too big = can overshoot")

# ------------------------------------------------------------
# 6. A harder dataset: 3 classes of wine
# ------------------------------------------------------------
print("\n=== 6. Multi-class: wine (3 classes) ===")
Xw, yw = load_wine(return_X_y=True)
for name in ["Decision tree", "Random forest", "Hist gradient boosting"]:
    print(f"{name:<24}{cross_val_score(models[name], Xw, yw, cv=5).mean():.3f}")

# Optional: XGBoost works the same way (pip install xgboost)
# from xgboost import XGBClassifier
# XGBClassifier(n_estimators=200, learning_rate=0.1).fit(X_train, y_train)
