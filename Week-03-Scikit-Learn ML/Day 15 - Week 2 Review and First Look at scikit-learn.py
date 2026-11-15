"""
Day 15 · Week 2 review + first look at a real dataset and scikit-learn
1. Self-check: Week 2 ideas as small asserts (if it runs, I remember them)
2. Explore a real dataset with pandas (EDA)
3. The scikit-learn pattern: fit -> predict -> score
"""
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer, load_diabetes
from sklearn.linear_model import LinearRegression

HERE = Path(__file__).parent

# ------------------------------------------------------------
# 1. Week 2 self-check
# ------------------------------------------------------------
print("=== 1. Week 2 self-check ===")

# NumPy: shapes and broadcasting
a = np.arange(12).reshape(3, 4)
assert a.shape == (3, 4)
assert (a + np.array([1, 0, 0, 0]))[0, 0] == 1          # row vector broadcast to every row
assert a.mean(axis=0).shape == (4,)                      # axis=0 -> one value per column

# Linear algebra: a layer is W @ x + b
W = np.array([[1, 2], [3, 4]])
x = np.array([1, 1])
assert np.array_equal(W @ x + 1, np.array([4, 8]))

# pandas: groupby
df = pd.DataFrame({"city": ["KHI", "LHE", "KHI"], "sales": [10, 20, 30]})
assert df.groupby("city")["sales"].sum()["KHI"] == 40

# Gradient descent on f(w) = (w - 3)^2: the minimum is at w = 3
w = 0.0
for _ in range(100):
    w -= 0.1 * 2 * (w - 3)                               # derivative of (w-3)^2 is 2(w-3)
assert abs(w - 3) < 1e-6

print("All Week 2 checks passed ✅")

# ------------------------------------------------------------
# 2. Explore a real dataset (EDA)
# ------------------------------------------------------------
print("\n=== 2. Exploring the breast cancer dataset ===")
data = load_breast_cancer(as_frame=True)
df = data.frame                                          # features + 'target' column
df["diagnosis"] = df["target"].map({0: "malignant", 1: "benign"})

print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")
print(f"Missing values: {df.isna().sum().sum()}")
print("\nClass balance:")
print(df["diagnosis"].value_counts(normalize=True).round(3))

print("\nFirst 5 features, summary:")
print(df.iloc[:, :5].describe().round(2))

# Which features differ most between the two classes?
means = df.groupby("diagnosis").mean(numeric_only=True).drop(columns="target").T
means["ratio"] = means["malignant"] / means["benign"]
print("\nTop 5 features where malignant is much bigger than benign:")
print(means.sort_values("ratio", ascending=False).head(5).round(2))

# Correlation with the target
corr = df.drop(columns=["diagnosis"]).corr()["target"].drop("target")
print("\nMost correlated features with the target:")
print(corr.abs().sort_values(ascending=False).head(5).round(3))

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(7, 4))
    for label, group in df.groupby("diagnosis"):
        ax.hist(group["mean radius"], bins=30, alpha=0.6, label=label)
    ax.set(xlabel="Mean radius", ylabel="Count", title="Mean radius by diagnosis")
    ax.legend()
    fig.tight_layout()
    fig.savefig(HERE / "day15_radius_hist.png", dpi=110)
    print("\nSaved plot: day15_radius_hist.png")
except ImportError:
    print("\n(pip install matplotlib to save the plot)")

# ------------------------------------------------------------
# 3. The scikit-learn pattern
# ------------------------------------------------------------
print("\n=== 3. scikit-learn: fit -> predict -> score ===")
X, y = load_diabetes(return_X_y=True)

model = LinearRegression()          # 1. create
model.fit(X, y)                     # 2. learn from data
preds = model.predict(X[:3])        # 3. predict
r2 = model.score(X, y)              # 4. evaluate (R² for regressors)

print("First 3 predictions:", preds.round(1))
print("True values:        ", y[:3])
print(f"R² on training data: {r2:.3f}")

# Same answer as solving it with plain NumPy least squares (Week 2 maths)
X_b = np.c_[np.ones(len(X)), X]                       # add a column of 1s for the bias
theta, *_ = np.linalg.lstsq(X_b, y, rcond=None)
print(f"Bias  sklearn: {model.intercept_:.3f} | NumPy: {theta[0]:.3f}")
print("Same weights as NumPy:", np.allclose(model.coef_, theta[1:]))
