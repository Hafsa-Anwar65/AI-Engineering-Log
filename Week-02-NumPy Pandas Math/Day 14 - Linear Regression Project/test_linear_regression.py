"""Tests for my linear regression. Run with:  python -m pytest -v"""
import numpy as np
import pytest

from linear_regression import LinearRegressionGD, mse, r2_score, train_test_split


def test_learns_a_perfect_line():
    x = np.arange(0, 10, dtype=float)
    y = 3 * x + 2
    model = LinearRegressionGD(learning_rate=0.1, epochs=5000).fit(x, y)
    w, b = model.original_scale_params()
    assert w[0] == pytest.approx(3, abs=1e-3)
    assert b == pytest.approx(2, abs=1e-3)


def test_matches_numpy_least_squares():
    rng = np.random.default_rng(0)
    x = rng.uniform(0, 5, 100)
    y = 4 - 2 * x + rng.normal(0, 0.5, 100)
    w, b = LinearRegressionGD(learning_rate=0.1, epochs=5000).fit(x, y).original_scale_params()
    slope, intercept = np.polyfit(x, y, 1)
    assert w[0] == pytest.approx(slope, abs=1e-3)
    assert b == pytest.approx(intercept, abs=1e-3)


def test_multiple_features():
    rng = np.random.default_rng(1)
    X = rng.normal(size=(200, 3))
    y = X @ np.array([1.5, -2.0, 0.5]) + 4
    model = LinearRegressionGD(learning_rate=0.1, epochs=5000).fit(X, y)
    assert r2_score(y, model.predict(X)) > 0.999


def test_loss_goes_down():
    x = np.linspace(0, 1, 50)
    model = LinearRegressionGD().fit(x, 5 * x + 1)
    assert model.loss_history[-1] < model.loss_history[0]


def test_predict_before_fit_raises():
    with pytest.raises(RuntimeError):
        LinearRegressionGD().predict([1, 2, 3])


def test_metrics():
    assert mse([1, 2, 3], [1, 2, 3]) == 0
    assert r2_score([1, 2, 3], [1, 2, 3]) == 1
    assert mse([0, 0], [1, 3]) == 5


def test_train_test_split_sizes():
    X = np.arange(100)
    X_tr, X_te, y_tr, y_te = train_test_split(X, X, test_size=0.2)
    assert len(X_tr) == 80 and len(X_te) == 20
    assert set(X_tr) | set(X_te) == set(range(100))
