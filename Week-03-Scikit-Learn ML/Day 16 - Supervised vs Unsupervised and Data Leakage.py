"""
Day 16 · Supervised vs unsupervised learning, train/val/test splits, data leakage
"""
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_breast_cancer, load_diabetes, load_iris
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, adjusted_rand_score, mean_absolute_error
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

RANDOM = 42

# ------------------------------------------------------------
# 1. Supervised: we have the answers (labels)
# ------------------------------------------------------------
print("=== 1a. Supervised · CLASSIFICATION (predict a category) ===")
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM
)
clf = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
clf.fit(X_train, y_train)
print(f"Benign or malignant? Test accuracy: {accuracy_score(y_test, clf.predict(X_test)):.3f}")

print("\n=== 1b. Supervised · REGRESSION (predict a number) ===")
X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM)
reg = LinearRegression().fit(X_train, y_train)
print(f"Disease progression score. Test MAE: {mean_absolute_error(y_test, reg.predict(X_test)):.1f} points")

# ------------------------------------------------------------
# 2. Unsupervised: no answers, find structure
# ------------------------------------------------------------
print("\n=== 2. Unsupervised · CLUSTERING ===")
X, species = load_iris(return_X_y=True)
kmeans = KMeans(n_clusters=3, n_init=10, random_state=RANDOM).fit(X)   # never sees `species`
print("Cluster sizes:", np.bincount(kmeans.labels_))
print(f"How well clusters match the real species (1 = perfect): "
      f"{adjusted_rand_score(species, kmeans.labels_):.2f}")

# ------------------------------------------------------------
# 3. Train / validation / test
# ------------------------------------------------------------
print("\n=== 3. Train / validation / test split (60 / 20 / 20) ===")
X, y = load_breast_cancer(return_X_y=True)

# First cut off the test set, then split the rest into train and validation
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=RANDOM)
X_train, X_val, y_train, y_val = train_test_split(
    X_temp, y_temp, test_size=0.25, stratify=y_temp, random_state=RANDOM   # 0.25 of 80% = 20%
)
print(f"Train {len(X_train)} | Validation {len(X_val)} | Test {len(X_test)}")
print(f"Benign share  train {y_train.mean():.2f} | val {y_val.mean():.2f} | test {y_test.mean():.2f}  (stratify keeps them equal)")

# Use validation to CHOOSE a setting, test only ONCE at the end
best_C, best_val = None, 0
for C in [0.001, 0.01, 0.1, 1, 10]:
    model = make_pipeline(StandardScaler(), LogisticRegression(C=C, max_iter=1000))
    val_acc = model.fit(X_train, y_train).score(X_val, y_val)
    print(f"  C={C:<6} validation accuracy {val_acc:.3f}")
    if val_acc > best_val:
        best_C, best_val = C, val_acc

final = make_pipeline(StandardScaler(), LogisticRegression(C=best_C, max_iter=1000))
final.fit(X_temp, y_temp)                         # retrain on train + validation
print(f"Chose C={best_C}. Final TEST accuracy (looked at once): {final.score(X_test, y_test):.3f}")

# ------------------------------------------------------------
# 4. Data leakage
# ------------------------------------------------------------
print("\n=== 4a. Leakage: choosing features BEFORE splitting ===")
# Pure noise: 100 people, 10,000 random features, random labels.
# The honest best possible accuracy is about 50% (a coin flip).
rng = np.random.default_rng(0)
X_noise = rng.normal(size=(100, 10_000))
y_noise = rng.integers(0, 2, size=100)

# ❌ WRONG: pick the 20 "best" features using ALL the data, then cross-validate
X_selected = SelectKBest(f_classif, k=20).fit_transform(X_noise, y_noise)
leaky = cross_val_score(LogisticRegression(max_iter=1000), X_selected, y_noise, cv=5).mean()

# ✅ RIGHT: feature selection inside a pipeline, so it only ever sees training folds
honest_model = make_pipeline(SelectKBest(f_classif, k=20), LogisticRegression(max_iter=1000))
honest = cross_val_score(honest_model, X_noise, y_noise, cv=5).mean()

print(f"Leaky accuracy on pure noise:  {leaky:.2f}  <- looks amazing, is a lie")
print(f"Honest accuracy on pure noise: {honest:.2f}  <- about a coin flip, the truth")

print("\n=== 4b. Leakage: a feature that secretly contains the answer ===")
X, y = load_breast_cancer(return_X_y=True)
# Imagine a column "second_opinion_result" that is only known AFTER diagnosis
leak_column = y + rng.normal(0, 0.1, size=len(y))
X_leak = np.column_stack([X, leak_column])

for name, features in [("with the leaky column", X_leak), ("without it", X)]:
    Xtr, Xte, ytr, yte = train_test_split(features, y, test_size=0.2, stratify=y, random_state=RANDOM)
    acc = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(Xtr, ytr).score(Xte, yte)
    print(f"Accuracy {name:<22} {acc:.3f}")
print("A near-perfect score is a warning sign: check that no feature is known only after the answer.")
