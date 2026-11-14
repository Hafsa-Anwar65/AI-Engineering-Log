"""
Linear Regression from scratch · Week 2 project
Only NumPy, no scikit-learn. Trained with gradient descent.

Run:   python linear_regression.py
Test:  python -m pytest
"""
from __future__ import annotations

from pathlib import Path

import numpy as np

HERE = Path(__file__).parent


class LinearRegressionGD:
    """y = X @ w + b, learned with batch gradient descent on MSE loss."""

    def __init__(self, learning_rate: float = 0.05, epochs: int = 2000, tol: float = 1e-10):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.tol = tol                    # stop early when the loss stops improving
        self.w: np.ndarray | None = None
        self.b: float = 0.0
        self.loss_history: list[float] = []
        self._mean: np.ndarray | None = None
        self._std: np.ndarray | None = None

    # --- feature scaling: makes gradient descent converge much faster ---
    def _scale(self, X: np.ndarray) -> np.ndarray:
        return (X - self._mean) / self._std

    @staticmethod
    def _as_2d(X) -> np.ndarray:
        X = np.asarray(X, dtype=float)
        return X.reshape(-1, 1) if X.ndim == 1 else X

    def fit(self, X, y) -> "LinearRegressionGD":
        X = self._as_2d(X)
        y = np.asarray(y, dtype=float)
        n_samples, n_features = X.shape

        self._mean = X.mean(axis=0)
        self._std = X.std(axis=0)
        self._std[self._std == 0] = 1.0
        Xs = self._scale(X)

        self.w = np.zeros(n_features)
        self.b = 0.0
        self.loss_history = []

        for _ in range(self.epochs):
            y_pred = Xs @ self.w + self.b                 # 1. predict
            error = y_pred - y
            loss = np.mean(error ** 2)                    # 2. MSE loss
            self.loss_history.append(loss)

            dw = (2 / n_samples) * (Xs.T @ error)         # 3. gradients
            db = (2 / n_samples) * error.sum()

            self.w -= self.learning_rate * dw             # 4. step downhill
            self.b -= self.learning_rate * db

            if len(self.loss_history) > 1 and abs(self.loss_history[-2] - loss) < self.tol:
                break
        return self

    def predict(self, X) -> np.ndarray:
        if self.w is None:
            raise RuntimeError("Call fit() before predict()")
        return self._scale(self._as_2d(X)) @ self.w + self.b

    def original_scale_params(self) -> tuple[np.ndarray, float]:
        """Weights and bias for the UNscaled features, easier to read."""
        w = self.w / self._std
        b = self.b - np.sum(self.w * self._mean / self._std)
        return w, b


# --- metrics ---
def mse(y_true, y_pred) -> float:
    return float(np.mean((np.asarray(y_true) - np.asarray(y_pred)) ** 2))


def r2_score(y_true, y_pred) -> float:
    """1.0 = perfect, 0 = no better than predicting the mean."""
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - y_true.mean()) ** 2)
    return float(1 - ss_res / ss_tot)


def train_test_split(X, y, test_size: float = 0.2, seed: int = 42):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(y))
    cut = int(len(y) * (1 - test_size))
    return X[idx[:cut]], X[idx[cut:]], y[idx[:cut]], y[idx[cut:]]


def main() -> None:
    rng = np.random.default_rng(7)

    # ---------- Demo 1: study hours -> exam marks (1 feature) ----------
    print("=== Demo 1: study hours -> exam marks ===")
    hours = rng.uniform(1, 10, 120)
    marks = 35 + 6 * hours + rng.normal(0, 4, 120)        # true rule: 35 + 6 * hours

    X_tr, X_te, y_tr, y_te = train_test_split(hours, marks)
    model = LinearRegressionGD(learning_rate=0.05).fit(X_tr, y_tr)
    w, b = model.original_scale_params()

    print(f"Learned:  marks = {b:.2f} + {w[0]:.2f} * hours   (true: 35 + 6 * hours)")
    print(f"Epochs:   {len(model.loss_history)}")
    print(f"Test MSE: {mse(y_te, model.predict(X_te)):.2f}")
    print(f"Test R²:  {r2_score(y_te, model.predict(X_te)):.3f}")
    print(f"7.5 hours of study -> {model.predict([7.5])[0]:.1f} marks")

    # Check against NumPy's exact least-squares answer
    slope, intercept = np.polyfit(X_tr, y_tr, 1)
    print(f"np.polyfit check: marks = {intercept:.2f} + {slope:.2f} * hours")

    # ---------- Demo 2: house price from 3 features ----------
    print("\n=== Demo 2: house price (3 features) ===")
    n = 300
    size = rng.uniform(500, 3000, n)            # square feet
    rooms = rng.integers(1, 6, n)
    age = rng.uniform(0, 40, n)                 # years
    price = 20 + 0.05 * size + 8 * rooms - 0.6 * age + rng.normal(0, 6, n)   # lakh Rs
    X = np.column_stack([size, rooms, age])

    X_tr, X_te, y_tr, y_te = train_test_split(X, price)
    house = LinearRegressionGD(learning_rate=0.1).fit(X_tr, y_tr)
    w, b = house.original_scale_params()
    print(f"Learned weights: size {w[0]:.3f}, rooms {w[1]:.2f}, age {w[2]:.2f}, bias {b:.1f}")
    print("True weights:    size 0.050, rooms 8.00, age -0.60, bias 20.0")
    print(f"Test R²: {r2_score(y_te, house.predict(X_te)):.3f}")

    # ---------- Plots ----------
    try:
        import matplotlib
        matplotlib.use("Agg")                   # save to files, no window needed
        import matplotlib.pyplot as plt
    except ImportError:
        print("\n(Install matplotlib to save the plots: pip install matplotlib)")
        return

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
    ax1.scatter(hours, marks, s=12, alpha=0.6, label="students")
    line_x = np.linspace(1, 10, 50)
    ax1.plot(line_x, model.predict(line_x), color="crimson", linewidth=2, label="my model")
    ax1.set(xlabel="Study hours", ylabel="Marks", title="Fitted line")
    ax1.legend()

    ax2.plot(model.loss_history)
    ax2.set(xlabel="Epoch", ylabel="MSE loss", title="Loss going down", yscale="log")

    fig.tight_layout()
    out = HERE / "results.png"
    fig.savefig(out, dpi=120)
    print(f"\nSaved plots to {out.name}")


if __name__ == "__main__":
    main()
