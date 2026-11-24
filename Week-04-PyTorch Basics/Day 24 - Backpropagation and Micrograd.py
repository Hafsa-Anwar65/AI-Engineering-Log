"""
Day 24 · Backpropagation: my own micrograd (a tiny autograd engine) + a neural net trained with it
Based on Andrej Karpathy's micrograd.
"""
import math
import random
from pathlib import Path

HERE = Path(__file__).parent
random.seed(42)


# ------------------------------------------------------------
# 1. The engine: a Value that can backpropagate
# ------------------------------------------------------------
class Value:
    def __init__(self, data, _children=(), _op=""):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None     # how to push my gradient to my inputs
        self._prev = set(_children)
        self._op = _op

    def __repr__(self):
        return f"Value(data={self.data:.4f}, grad={self.grad:.4f})"

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), "+")

        def _backward():
            self.grad += out.grad          # += because a value can be used more than once
            other.grad += out.grad
        out._backward = _backward
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), "*")

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out

    def __pow__(self, k):
        out = Value(self.data**k, (self,), f"**{k}")

        def _backward():
            self.grad += k * self.data ** (k - 1) * out.grad
        out._backward = _backward
        return out

    def tanh(self):
        t = math.tanh(self.data)
        out = Value(t, (self,), "tanh")

        def _backward():
            self.grad += (1 - t**2) * out.grad
        out._backward = _backward
        return out

    def relu(self):
        out = Value(max(0.0, self.data), (self,), "relu")

        def _backward():
            self.grad += (out.data > 0) * out.grad
        out._backward = _backward
        return out

    def exp(self):
        out = Value(math.exp(self.data), (self,), "exp")

        def _backward():
            self.grad += out.data * out.grad
        out._backward = _backward
        return out

    def backward(self):
        # Topological order: every node comes after the nodes it depends on
        order, seen = [], set()

        def build(v):
            if v not in seen:
                seen.add(v)
                for child in v._prev:
                    build(child)
                order.append(v)
        build(self)

        self.grad = 1.0
        for v in reversed(order):          # from the output back to the inputs
            v._backward()

    # so that 2 * x, x - y, x / y, -x all work
    def __radd__(self, other): return self + other
    def __rmul__(self, other): return self * other
    def __neg__(self): return self * -1
    def __sub__(self, other): return self + (-other)
    def __rsub__(self, other): return other + (-self)
    def __truediv__(self, other): return self * other**-1


# ------------------------------------------------------------
# 2. Check the engine against numerical derivatives
# ------------------------------------------------------------
print("=== 1. Gradient check ===")


def expression(a, b, c):
    """Works with plain floats AND with Value objects."""
    if isinstance(a, Value):
        return ((a * b + c**2).tanh() * a + (b / c).exp()).relu()
    return max(0.0, math.tanh(a * b + c**2) * a + math.exp(b / c))


vals = {"a": 0.8, "b": -1.3, "c": 2.1}
va, vb, vc = (Value(v) for v in vals.values())
out = expression(va, vb, vc)
out.backward()

h = 1e-6
for name, v in zip(vals, (va, vb, vc)):
    bumped = dict(vals); bumped[name] += h
    numerical = (expression(*bumped.values()) - expression(*vals.values())) / h
    print(f"d out/d{name}: backprop {v.grad:+.6f} | numerical {numerical:+.6f}")

# The += matters: using a value twice
x = Value(3.0)
y = x + x
y.backward()
print(f"\ny = x + x -> dy/dx = {x.grad} (2.0 is right; with '=' instead of '+=' it would wrongly be 1.0)")


# ------------------------------------------------------------
# 3. Neuron, Layer, MLP built on Value
# ------------------------------------------------------------
class Neuron:
    def __init__(self, n_in, activation="tanh"):
        self.w = [Value(random.uniform(-1, 1)) for _ in range(n_in)]
        self.b = Value(0.0)
        self.activation = activation

    def __call__(self, x):
        act = sum((wi * xi for wi, xi in zip(self.w, x)), self.b)
        return {"tanh": act.tanh(), "relu": act.relu(), "linear": act}[self.activation]

    def parameters(self):
        return self.w + [self.b]


class Layer:
    def __init__(self, n_in, n_out, activation="tanh"):
        self.neurons = [Neuron(n_in, activation) for _ in range(n_out)]

    def __call__(self, x):
        outs = [n(x) for n in self.neurons]
        return outs[0] if len(outs) == 1 else outs

    def parameters(self):
        return [p for n in self.neurons for p in n.parameters()]


class MLP:
    def __init__(self, n_in, sizes, hidden_act="tanh", out_act="tanh"):
        dims = [n_in] + sizes
        self.layers = [
            Layer(dims[i], dims[i + 1], hidden_act if i < len(sizes) - 1 else out_act)
            for i in range(len(sizes))
        ]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]


# ------------------------------------------------------------
# 4. Train on Karpathy's tiny dataset
# ------------------------------------------------------------
print("\n=== 2. Training a 3-4-4-1 network on 4 examples ===")
xs = [[2.0, 3.0, -1.0], [3.0, -1.0, 0.5], [0.5, 1.0, 1.0], [1.0, 1.0, -1.0]]
ys = [1.0, -1.0, -1.0, 1.0]
net = MLP(3, [4, 4, 1])
print(f"Parameters: {len(net.parameters())}")

for step in range(60):
    preds = [net(x) for x in xs]                                    # 1. forward
    loss = sum((p - y) ** 2 for p, y in zip(preds, ys))             # 2. loss
    for p in net.parameters():                                      # 3. zero grads
        p.grad = 0.0
    loss.backward()                                                 # 4. backward
    for p in net.parameters():                                      # 5. update
        p.data -= 0.05 * p.grad
    if step % 10 == 0 or step == 59:
        print(f"step {step:>2} loss {loss.data:.4f}")

print("Targets:    ", ys)
print("Predictions:", [round(net(x).data, 3) for x in xs])

# ------------------------------------------------------------
# 5. A real classification task: two moons
# ------------------------------------------------------------
print("\n=== 3. Two moons with a 2-16-16-1 ReLU network (max-margin loss) ===")
from sklearn.datasets import make_moons

X, y = make_moons(n_samples=100, noise=0.1, random_state=1)
y = y * 2 - 1                                   # labels -1 / +1
model = MLP(2, [16, 16, 1], hidden_act="relu", out_act="linear")
print(f"Parameters: {len(model.parameters())}")


def loss_and_accuracy():
    scores = [model([Value(a), Value(b)]) for a, b in X]
    data_loss = sum((1 + -yi * s).relu() for yi, s in zip(y, scores)) * (1.0 / len(y))   # SVM hinge loss
    reg_loss = 1e-4 * sum(p * p for p in model.parameters())                              # L2 (Day 19!)
    acc = sum((yi > 0) == (s.data > 0) for yi, s in zip(y, scores)) / len(y)
    return data_loss + reg_loss, acc


for step in range(40):
    loss, acc = loss_and_accuracy()
    for p in model.parameters():
        p.grad = 0.0
    loss.backward()
    lr = 1.0 - 0.9 * step / 40                  # learning-rate decay
    for p in model.parameters():
        p.data -= lr * p.grad
    if step % 5 == 0 or step == 39:
        print(f"step {step:>2} loss {loss.data:.4f} accuracy {acc:.0%}")

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    xx, yy = np.meshgrid(np.linspace(-1.5, 2.5, 60), np.linspace(-1, 1.5, 60))
    Z = np.array([model([Value(a), Value(b)]).data > 0 for a, b in zip(xx.ravel(), yy.ravel())]).reshape(xx.shape)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.contourf(xx, yy, Z, alpha=0.35, cmap="BrBG")
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap="BrBG", edgecolors="black", s=25)
    ax.set_title("Decision boundary learned by my micrograd MLP")
    fig.tight_layout()
    fig.savefig(HERE / "day24_moons_boundary.png", dpi=110)
    print("Saved plot: day24_moons_boundary.png")
except ImportError:
    pass
