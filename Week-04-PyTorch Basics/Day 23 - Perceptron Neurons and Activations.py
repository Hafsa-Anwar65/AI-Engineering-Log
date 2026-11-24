"""
Day 23 · Perceptron, neurons, layers and activation functions (NumPy only)
"""
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent

# ------------------------------------------------------------
# 1. A perceptron: weighted sum + step function
# ------------------------------------------------------------
print("=== 1. Perceptron learning AND, OR and XOR ===")
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets = {
    "AND": np.array([0, 0, 0, 1]),
    "OR": np.array([0, 1, 1, 1]),
    "XOR": np.array([0, 1, 1, 0]),
}


def train_perceptron(X, y, epochs=20, lr=0.1):
    w, b = np.zeros(X.shape[1]), 0.0
    for _ in range(epochs):
        for xi, target in zip(X, y):
            pred = int(xi @ w + b > 0)            # step function
            w += lr * (target - pred) * xi        # perceptron learning rule
            b += lr * (target - pred)
    return w, b


for name, y in targets.items():
    w, b = train_perceptron(X, y)
    preds = (X @ w + b > 0).astype(int)
    ok = "✅ learned" if np.array_equal(preds, y) else "❌ can't learn it"
    print(f"{name:<4} predictions {preds}  target {y}  {ok}")
print("XOR isn't linearly separable: one straight line can't split it. We need layers.")

# ------------------------------------------------------------
# 2. Activation functions and their derivatives
# ------------------------------------------------------------
print("\n=== 2. Activation functions ===")


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def tanh(z):
    return np.tanh(z)


def relu(z):
    return np.maximum(0, z)


def softmax(z):
    e = np.exp(z - z.max())          # subtract max for numerical stability
    return e / e.sum()


derivatives = {
    "sigmoid": lambda z: sigmoid(z) * (1 - sigmoid(z)),
    "tanh": lambda z: 1 - np.tanh(z) ** 2,
    "relu": lambda z: (z > 0).astype(float),
}

z = np.array([-3.0, -1.0, 0.0, 1.0, 3.0])
print(f"z        {z}")
print(f"sigmoid  {np.round(sigmoid(z), 3)}   range (0, 1)")
print(f"tanh     {np.round(tanh(z), 3)}   range (-1, 1)")
print(f"relu     {relu(z)}   range [0, inf)")
print(f"softmax([2, 1, 0.1]) = {np.round(softmax(np.array([2.0, 1.0, 0.1])), 3)}  (sums to 1)")

print("\nGradient at z = 5 (big input):")
for name, d in derivatives.items():
    print(f"  {name:<8} {d(np.array([5.0]))[0]:.4f}")
print("Sigmoid/tanh gradients almost vanish for big inputs; ReLU keeps gradient 1.")

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    zz = np.linspace(-5, 5, 200)
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))
    for name, fn, color in [("sigmoid", sigmoid, "#0F766E"), ("tanh", tanh, "#14B8A6"), ("ReLU", relu, "#111111")]:
        axes[0].plot(zz, fn(zz), label=name, color=color, linewidth=2)
        axes[1].plot(zz, derivatives[name.lower()](zz), label=name, color=color, linewidth=2)
    axes[0].set(title="Activation", ylim=(-1.2, 2.5)); axes[1].set(title="Derivative", ylim=(-0.1, 1.2))
    for ax in axes:
        ax.axhline(0, color="gray", linewidth=0.5); ax.legend()
    fig.tight_layout()
    fig.savefig(HERE / "day23_activations.png", dpi=110)
    print("Saved plot: day23_activations.png")
except ImportError:
    pass

# ------------------------------------------------------------
# 3. A neuron, a layer, a network
# ------------------------------------------------------------
print("\n=== 3. Neuron -> layer -> network ===")
rng = np.random.default_rng(0)

# One neuron: 3 inputs -> 1 output
x = np.array([0.5, -1.2, 2.0])
w = rng.normal(size=3)
b = 0.1
print(f"Neuron: tanh(w·x + b) = {np.tanh(x @ w + b):.4f}")

# A layer of 4 neurons is a matrix: each ROW is one neuron's weights
W1 = rng.normal(size=(4, 3))
b1 = np.zeros(4)
h = np.tanh(W1 @ x + b1)
print(f"Layer of 4 neurons -> {h.shape} output: {np.round(h, 3)}")

# A batch of 5 examples at once (rows = examples)
batch = rng.normal(size=(5, 3))
out = np.tanh(batch @ W1.T + b1)
print(f"Batch of 5 through the layer -> shape {out.shape}")

# ------------------------------------------------------------
# 4. Two layers solve XOR (weights chosen by hand)
# ------------------------------------------------------------
print("\n=== 4. A 2-layer network solves XOR ===")
# Hidden neuron 1 acts like OR, hidden neuron 2 like AND
W_hidden = np.array([[20.0, 20.0], [20.0, 20.0]])
b_hidden = np.array([-10.0, -30.0])
# Output: OR and NOT AND  ->  XOR
w_out = np.array([20.0, -20.0])
b_out = -10.0

hidden = sigmoid(X @ W_hidden.T + b_hidden)
output = sigmoid(hidden @ w_out + b_out)
print("input  hidden(OR, AND)  output")
for xi, hi, oi in zip(X, hidden, output):
    print(f"{xi}   {np.round(hi, 2)}         {oi:.3f} -> {int(oi > 0.5)}")
print("Stacking layers with a non-linear activation lets the network draw curved boundaries.")
print("Tomorrow: learn these weights automatically with backpropagation.")
