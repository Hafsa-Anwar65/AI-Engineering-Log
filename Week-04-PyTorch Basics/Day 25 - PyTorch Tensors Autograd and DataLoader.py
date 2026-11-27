"""
Day 25 · PyTorch basics: tensors, devices, autograd, Dataset & DataLoader
Everything I built by hand in micrograd, now with PyTorch.
"""
import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset, TensorDataset, random_split

torch.manual_seed(42)

# ------------------------------------------------------------
# 1. Tensors: NumPy arrays that can run on a GPU and track gradients
# ------------------------------------------------------------
print("=== 1. Tensors ===")
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.ones(2, 2)
print("a =\n", a)
print("shape:", a.shape, "| dtype:", a.dtype, "| device:", a.device)

print("a + b =\n", a + b)
print("a * b (element-wise) =\n", a * b)
print("a @ b (matrix multiply) =\n", a @ b)
print("mean of each column:", a.mean(dim=0))       # dim works like NumPy's axis

# Creating tensors
print("zeros:", torch.zeros(3), "| arange:", torch.arange(0, 10, 3), "| rand:", torch.rand(2).round(decimals=3))

# Reshaping
x = torch.arange(12)
print("reshape(3, 4):\n", x.reshape(3, 4))
print("view(2, -1) shape:", x.view(2, -1).shape, "  (-1 = work it out)")
print("unsqueeze(0) shape:", x.unsqueeze(0).shape, "  (adds a batch dimension)")

# NumPy <-> PyTorch
arr = np.array([1.5, 2.5, 3.5])
t = torch.from_numpy(arr)
print("from NumPy:", t, "| back to NumPy:", t.numpy())

# ------------------------------------------------------------
# 2. Devices: CPU or GPU
# ------------------------------------------------------------
print("\n=== 2. Devices ===")
device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
print("Using device:", device)
big = torch.rand(1000, 1000).to(device)        # move data to the device
result = big @ big
print("Result lives on:", result.device)
# Rule: the model and its data must be on the SAME device.

# ------------------------------------------------------------
# 3. Autograd: PyTorch's micrograd
# ------------------------------------------------------------
print("\n=== 3. Autograd (same example as Day 22) ===")
a = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(-3.0, requires_grad=True)
c = torch.tensor(10.0, requires_grad=True)
f = torch.tensor(-2.0, requires_grad=True)
L = (a * b + c) * f
L.backward()
print(f"L = {L.item()}")
print(f"dL/da = {a.grad.item()}, dL/db = {b.grad.item()}, dL/dc = {c.grad.item()}, dL/df = {f.grad.item()}")
print("Same as my hand-made backprop on Day 22: 6, -4, -2, 4 ✅")

# The tricky expression from Day 24, checked against my micrograd answer
a = torch.tensor(0.8, requires_grad=True)
b = torch.tensor(-1.3, requires_grad=True)
c = torch.tensor(2.1, requires_grad=True)
out = torch.relu(torch.tanh(a * b + c**2) * a + torch.exp(b / c))
out.backward()
print(f"Day 24 expression -> grads a {a.grad.item():+.6f}, b {b.grad.item():+.6f}, c {c.grad.item():+.6f}")

# Gradients ADD UP unless I reset them
w = torch.tensor(3.0, requires_grad=True)
for i in range(3):
    (w * 2).backward()
    print(f"after backward #{i + 1}: w.grad = {w.grad.item()}")
w.grad.zero_()
print("after w.grad.zero_():", w.grad.item(), " <- this is why training loops call zero_grad()")

# Turning gradients off (faster, for predictions)
with torch.no_grad():
    y = w * 2
print("inside no_grad, requires_grad =", y.requires_grad)

# ------------------------------------------------------------
# 4. Dataset & DataLoader: feeding data in batches
# ------------------------------------------------------------
print("\n=== 4. Custom Dataset ===")


class SquaresDataset(Dataset):
    """x -> x² with a bit of noise. A Dataset only needs __len__ and __getitem__."""

    def __init__(self, n: int = 100):
        self.x = torch.linspace(-2, 2, n).unsqueeze(1)          # shape (n, 1)
        self.y = self.x**2 + 0.1 * torch.randn_like(self.x)

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]


ds = SquaresDataset(100)
print("len(ds):", len(ds), "| ds[0]:", tuple(round(v.item(), 3) for v in ds[0]))

train_ds, val_ds = random_split(ds, [80, 20], generator=torch.Generator().manual_seed(0))
train_loader = DataLoader(train_ds, batch_size=16, shuffle=True)
val_loader = DataLoader(val_ds, batch_size=16)

print(f"train batches: {len(train_loader)} | val batches: {len(val_loader)}")
xb, yb = next(iter(train_loader))
print("one batch -> x", tuple(xb.shape), "y", tuple(yb.shape))
print("shuffle=True gives a new order every epoch; validation is not shuffled")

print("\n=== 5. TensorDataset: the quick way for data already in tensors ===")
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)
X_t = torch.tensor(X, dtype=torch.float32)
y_t = torch.tensor(y, dtype=torch.float32)
loader = DataLoader(TensorDataset(X_t, y_t), batch_size=64, shuffle=True)
xb, yb = next(iter(loader))
print(f"{len(loader)} batches of up to 64 rows | features per row: {xb.shape[1]}")
print("Tomorrow: a training loop that uses these batches.")
