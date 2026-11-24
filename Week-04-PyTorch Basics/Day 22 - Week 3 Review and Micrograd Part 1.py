"""
Day 22 · Week 3 review + micrograd part 1 (derivatives and the computation graph)
Following Karpathy's "The spelled-out intro to neural networks and backpropagation".
"""
import math

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

# ------------------------------------------------------------
# 1. Week 3 self-check
# ------------------------------------------------------------
print("=== 1. Week 3 self-check ===")
X, y = load_breast_cancer(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, stratify=y, random_state=0)

# stratify keeps the class share the same
assert abs(y_tr.mean() - y_te.mean()) < 0.01

# a Pipeline scales inside each CV fold (no leakage)
pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
assert cross_val_score(pipe, X_tr, y_tr, cv=5).mean() > 0.95

# precision / recall / F1 by hand match scikit-learn
pred = pipe.fit(X_tr, y_tr).predict(X_te)
tn, fp, fn, tp = confusion_matrix(y_te, pred).ravel()
p, r = tp / (tp + fp), tp / (tp + fn)
assert math.isclose(p, precision_score(y_te, pred))
assert math.isclose(r, recall_score(y_te, pred))
assert math.isclose(2 * p * r / (p + r), f1_score(y_te, pred))
print("All Week 3 checks passed ✅")

# ------------------------------------------------------------
# 2. What a derivative really is
# ------------------------------------------------------------
print("\n=== 2. Derivative = how much the output moves when I nudge the input ===")


def f(x):
    return 3 * x**2 - 4 * x + 5


x = 3.0
for h in [0.1, 0.001, 0.00001]:
    print(f"h={h:<8} slope ≈ {(f(x + h) - f(x)) / h:.5f}")
print("Exact derivative 6x - 4 at x=3 is 14.0")

# With several inputs: nudge one, keep the others fixed
a, b, c = 2.0, -3.0, 10.0
d = a * b + c
h = 0.0001
print(f"d = a*b + c = {d}")
print(f"dd/da ≈ {((a + h) * b + c - d) / h:.3f}  (should be b = {b})")
print(f"dd/db ≈ {(a * (b + h) + c - d) / h:.3f}  (should be a = {a})")
print(f"dd/dc ≈ {(a * b + (c + h) - d) / h:.3f}  (should be 1)")

# ------------------------------------------------------------
# 3. A Value object that remembers how it was made
# ------------------------------------------------------------
print("\n=== 3. Building a computation graph ===")


class Value:
    def __init__(self, data, _children=(), _op="", label=""):
        self.data = data
        self.grad = 0.0                 # dL/d(this value), filled in later
        self._prev = set(_children)     # the values that produced this one
        self._op = _op                  # the operation that produced it
        self.label = label

    def __repr__(self):
        return f"Value({self.label}={self.data:.4f}, grad={self.grad:.4f})"

    def __add__(self, other):
        return Value(self.data + other.data, (self, other), "+")

    def __mul__(self, other):
        return Value(self.data * other.data, (self, other), "*")


def show(node, indent=0):
    """Print the graph as a tree, from the output back to the inputs."""
    op = f" (made by {node._op})" if node._op else ""
    print("  " * indent + f"{node.label} = {node.data:.2f}, grad {node.grad:.2f}{op}")
    for child in node._prev:
        show(child, indent + 1)


a = Value(2.0, label="a")
b = Value(-3.0, label="b")
c = Value(10.0, label="c")
e = a * b; e.label = "e"
d = e + c; d.label = "d"
f_ = Value(-2.0, label="f")
L = d * f_; L.label = "L"
show(L)

# ------------------------------------------------------------
# 4. Backpropagation BY HAND with the chain rule
# ------------------------------------------------------------
print("\n=== 4. Manual backprop: L = (a*b + c) * f ===")
# Start at the end: dL/dL = 1
L.grad = 1.0
# L = d * f  ->  dL/dd = f,  dL/df = d
d.grad = f_.data
f_.grad = d.data
# d = e + c  ->  '+' passes the gradient through unchanged
e.grad = d.grad * 1.0
c.grad = d.grad * 1.0
# e = a * b  ->  chain rule: dL/da = dL/de * de/da = e.grad * b
a.grad = e.grad * b.data
b.grad = e.grad * a.data
show(L)


def L_of(a_, b_, c_, f__):
    return (a_ * b_ + c_) * f__


print("\nNumerical check (nudge each input by h):")
base = L_of(2.0, -3.0, 10.0, -2.0)
for name, args, mine in [
    ("a", (2.0 + h, -3.0, 10.0, -2.0), a.grad),
    ("b", (2.0, -3.0 + h, 10.0, -2.0), b.grad),
    ("c", (2.0, -3.0, 10.0 + h, -2.0), c.grad),
    ("f", (2.0, -3.0, 10.0, -2.0 + h), f_.grad),
]:
    print(f"  dL/d{name}: by hand {mine:>6.2f} | numerical {(L_of(*args) - base) / h:>6.2f}")

# ------------------------------------------------------------
# 5. One step of "learning": move inputs against the gradient
# ------------------------------------------------------------
print("\n=== 5. Nudging inputs to increase L ===")
step = 0.01
new_L = L_of(a.data + step * a.grad, b.data + step * b.grad, c.data + step * c.grad, f_.data + step * f_.grad)
print(f"L before: {L.data:.4f} | after one small step along the gradient: {new_L:.4f}")
print("Training a neural net is this, repeated millions of times (but going DOWN the loss).")
