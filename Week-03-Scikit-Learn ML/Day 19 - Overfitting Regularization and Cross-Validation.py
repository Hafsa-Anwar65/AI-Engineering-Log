"""
Day 19 · Overfitting, bias-variance, L1/L2 regularisation, cross-validation & tuning
"""
from pathlib import Path

import numpy as np
from sklearn.datasets import load_breast_cancer, load_diabetes
from sklearn.linear_model import Lasso, LinearRegression, LogisticRegression, Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import (
    GridSearchCV,
    KFold,
    RandomizedSearchCV,
    cross_val_score,
    train_test_split,
)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.tree import DecisionTreeClassifier

HERE = Path(__file__).parent
RANDOM = 42
rng = np.random.default_rng(RANDOM)

# ------------------------------------------------------------
# 1. Underfitting vs overfitting with polynomials
# ------------------------------------------------------------
print("=== 1. Bias vs variance: fitting a curve ===")
x = np.sort(rng.uniform(0, 1, 30))
y = np.sin(2 * np.pi * x) + rng.normal(0, 0.2, 30)          # the true pattern is a sine wave
x_new = np.linspace(0, 1, 200)
y_new = np.sin(2 * np.pi * x_new) + rng.normal(0, 0.2, 200)

print(f"{'Degree':<8}{'Train MSE':>11}{'New-data MSE':>14}   Verdict")
curves = {}
for degree in [1, 4, 15]:
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(x.reshape(-1, 1), y)
    train_mse = mean_squared_error(y, model.predict(x.reshape(-1, 1)))
    new_mse = mean_squared_error(y_new, model.predict(x_new.reshape(-1, 1)))
    verdict = {1: "underfit (high bias)", 4: "just right", 15: "overfit (high variance)"}[degree]
    print(f"{degree:<8}{train_mse:>11.3f}{new_mse:>14.3f}   {verdict}")
    curves[degree] = model.predict(x_new.reshape(-1, 1))

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 3, figsize=(13, 3.6), sharey=True)
    for ax, (degree, pred) in zip(axes, curves.items()):
        ax.scatter(x, y, s=15, color="gray", label="training points")
        ax.plot(x_new, np.sin(2 * np.pi * x_new), "g--", label="true pattern")
        ax.plot(x_new, pred, color="crimson", label=f"degree {degree}")
        ax.set_ylim(-2, 2)
        ax.set_title(["Underfit", "Good fit", "Overfit"][list(curves).index(degree)])
        ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(HERE / "day19_bias_variance.png", dpi=110)
    print("Saved plot: day19_bias_variance.png")
except ImportError:
    pass

# ------------------------------------------------------------
# 2. Regularisation: L2 (Ridge) and L1 (Lasso)
# ------------------------------------------------------------
print("\n=== 2. Ridge (L2) shrinks weights, Lasso (L1) can zero them out ===")
X, y = load_diabetes(return_X_y=True)
names = load_diabetes().feature_names
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=RANDOM)

print(f"{'Model':<20}{'Test MSE':>10}{'Weights = 0':>13}{'Size of weights':>17}")
for name, model in [
    ("Linear (none)", LinearRegression()),
    ("Ridge alpha=1", Ridge(alpha=1)),
    ("Ridge alpha=10", Ridge(alpha=10)),
    ("Lasso alpha=0.1", Lasso(alpha=0.1)),
    ("Lasso alpha=1", Lasso(alpha=1)),
]:
    pipe = make_pipeline(StandardScaler(), model).fit(X_train, y_train)
    coef = pipe[-1].coef_
    mse = mean_squared_error(y_test, pipe.predict(X_test))
    print(f"{name:<20}{mse:>10.0f}{int(np.sum(np.abs(coef) < 1e-6)):>13}{np.abs(coef).sum():>17.1f}")

lasso = make_pipeline(StandardScaler(), Lasso(alpha=1)).fit(X_train, y_train)
kept = [n for n, c in zip(names, lasso[-1].coef_) if abs(c) > 1e-6]
print("Lasso alpha=1 kept only these features:", ", ".join(kept))

# Overfitting example where regularisation clearly helps
Xp = PolynomialFeatures(degree=3).fit_transform(X)             # 220 features from 10
Xp_train, Xp_test, yp_train, yp_test = train_test_split(Xp, y, test_size=0.2, random_state=RANDOM)
plain = make_pipeline(StandardScaler(), LinearRegression()).fit(Xp_train, yp_train)
ridge = make_pipeline(StandardScaler(), Ridge(alpha=100)).fit(Xp_train, yp_train)
print(f"\nWith 220 polynomial features:  plain R² {plain.score(Xp_test, yp_test):.2f} | "
      f"Ridge R² {ridge.score(Xp_test, yp_test):.2f}")

# ------------------------------------------------------------
# 3. Cross-validation: a fairer score than one split
# ------------------------------------------------------------
print("\n=== 3. Cross-validation ===")
Xc, yc = load_breast_cancer(return_X_y=True)
one_split_scores = []
for seed in range(5):
    a, b, c, d = train_test_split(Xc, yc, test_size=0.2, random_state=seed)
    one_split_scores.append(DecisionTreeClassifier(random_state=0).fit(a, c).score(b, d))
print("Single splits with different seeds:", np.round(one_split_scores, 3), "<- it depends on luck")

cv = KFold(n_splits=5, shuffle=True, random_state=RANDOM)
scores = cross_val_score(DecisionTreeClassifier(random_state=0), Xc, yc, cv=cv)
print(f"5-fold CV: {np.round(scores, 3)} -> mean {scores.mean():.3f} ± {scores.std():.3f}")

# ------------------------------------------------------------
# 4. Hyperparameter tuning: GridSearch and RandomizedSearch
# ------------------------------------------------------------
print("\n=== 4. Tuning with GridSearchCV ===")
Xc_train, Xc_test, yc_train, yc_test = train_test_split(
    Xc, yc, test_size=0.2, stratify=yc, random_state=RANDOM
)
grid = GridSearchCV(
    DecisionTreeClassifier(random_state=RANDOM),
    param_grid={"max_depth": [2, 3, 4, 5, 8, None], "min_samples_leaf": [1, 5, 10]},
    cv=5,
)
grid.fit(Xc_train, yc_train)                      # tries 6 x 3 = 18 combinations x 5 folds
print(f"Tried {len(grid.cv_results_['params'])} combinations")
print(f"Best settings: {grid.best_params_}")
print(f"Best CV score: {grid.best_score_:.3f} | Test score: {grid.score(Xc_test, yc_test):.3f}")

print("\n=== 4b. RandomizedSearchCV (faster when there are many options) ===")
pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=5000))
rand = RandomizedSearchCV(
    pipe,
    param_distributions={"logisticregression__C": np.logspace(-3, 3, 50)},
    n_iter=10,
    cv=5,
    random_state=RANDOM,
)
rand.fit(Xc_train, yc_train)
print(f"Best C: {rand.best_params_['logisticregression__C']:.3f} | "
      f"CV {rand.best_score_:.3f} | Test {rand.score(Xc_test, yc_test):.3f}")
