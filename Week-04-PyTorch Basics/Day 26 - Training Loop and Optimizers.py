"""
Day 26 · The PyTorch training loop + optimizers (SGD, momentum, Adam) + learning-rate schedules
"""
from pathlib import Path

import torch
from sklearn.datasets import load_breast_cancer, make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

HERE = Path(__file__).parent
torch.manual_seed(42)

# ------------------------------------------------------------
# 1. The model: nn.Module (my Day 24 MLP class, PyTorch style)
# ------------------------------------------------------------
print("=== 1. A model with nn.Module ===")


class MLP(nn.Module):
    def __init__(self, n_in: int, hidden: int = 16):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_in, hidden), nn.ReLU(),
            nn.Linear(hidden, hidden), nn.ReLU(),
            nn.Linear(hidden, 1),                 # 1 raw score (logit)
        )

    def forward(self, x):
        return self.net(x).squeeze(-1)


model = MLP(2)
print(model)
print("Parameters:", sum(p.numel() for p in model.parameters()))   # 337, same size as Day 24!

# ------------------------------------------------------------
# 2. Data: two moons (like Day 24)
# ------------------------------------------------------------
X, y = make_moons(n_samples=1000, noise=0.2, random_state=1)
X_tr, X_val, y_tr, y_val = train_test_split(X, y, test_size=0.2, random_state=0)
to_t = lambda a: torch.tensor(a, dtype=torch.float32)
train_loader = DataLoader(TensorDataset(to_t(X_tr), to_t(y_tr)), batch_size=32, shuffle=True)
X_val_t, y_val_t = to_t(X_val), to_t(y_val)

# ------------------------------------------------------------
# 3. The training loop: the same 5 steps as micrograd
# ------------------------------------------------------------
print("\n=== 2. The training loop ===")


def accuracy(model, X, y):
    model.eval()                                    # evaluation mode
    with torch.no_grad():                           # no gradients needed
        return ((model(X) > 0).float() == y).float().mean().item()


def train(model, optimizer, epochs=30, scheduler=None, verbose=False):
    loss_fn = nn.BCEWithLogitsLoss()                # sigmoid + binary cross-entropy in one, numerically safe
    history = []
    for epoch in range(epochs):
        model.train()                               # training mode
        total = 0.0
        for xb, yb in train_loader:
            logits = model(xb)                      # 1. forward
            loss = loss_fn(logits, yb)              # 2. loss
            optimizer.zero_grad()                   # 3. reset gradients
            loss.backward()                         # 4. backprop
            optimizer.step()                        # 5. update weights
            total += loss.item() * len(xb)
        if scheduler:
            scheduler.step()
        history.append(total / len(train_loader.dataset))
        if verbose and (epoch % 5 == 0 or epoch == epochs - 1):
            lr = optimizer.param_groups[0]["lr"]
            print(f"epoch {epoch:>2} loss {history[-1]:.4f} val acc {accuracy(model, X_val_t, y_val_t):.3f} lr {lr:.4f}")
    return history


torch.manual_seed(0)
model = MLP(2)
train(model, torch.optim.Adam(model.parameters(), lr=0.01), epochs=30, verbose=True)

# ------------------------------------------------------------
# 4. Comparing optimizers
# ------------------------------------------------------------
print("\n=== 3. Optimizers compared (same model, same data, same seed) ===")
optimizers = {
    "SGD lr=0.01": lambda p: torch.optim.SGD(p, lr=0.01),
    "SGD lr=0.1": lambda p: torch.optim.SGD(p, lr=0.1),
    "SGD + momentum": lambda p: torch.optim.SGD(p, lr=0.1, momentum=0.9),
    "Adam lr=0.01": lambda p: torch.optim.Adam(p, lr=0.01),
    "AdamW lr=0.01": lambda p: torch.optim.AdamW(p, lr=0.01, weight_decay=0.01),
}
curves = {}
print(f"{'Optimizer':<18}{'loss after 5 ep':>16}{'final loss':>12}{'val acc':>9}")
for name, make in optimizers.items():
    torch.manual_seed(0)
    m = MLP(2)
    hist = train(m, make(m.parameters()), epochs=30)
    curves[name] = hist
    print(f"{name:<18}{hist[4]:>16.4f}{hist[-1]:>12.4f}{accuracy(m, X_val_t, y_val_t):>9.3f}")
print("Plain SGD with a small LR crawls; momentum and Adam get there much faster.")

# ------------------------------------------------------------
# 5. Learning-rate schedules
# ------------------------------------------------------------
print("\n=== 4. Learning-rate schedules ===")
for name, make_sched in {
    "constant": None,
    "StepLR (x0.5 every 10)": lambda opt: torch.optim.lr_scheduler.StepLR(opt, step_size=10, gamma=0.5),
    "CosineAnnealing": lambda opt: torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=30),
}.items():
    torch.manual_seed(0)
    m = MLP(2)
    opt = torch.optim.SGD(m.parameters(), lr=0.2, momentum=0.9)
    sched = make_sched(opt) if make_sched else None
    hist = train(m, opt, epochs=30, scheduler=sched)
    print(f"{name:<24} final lr {opt.param_groups[0]['lr']:.4f} | final loss {hist[-1]:.4f} | val acc {accuracy(m, X_val_t, y_val_t):.3f}")

# ------------------------------------------------------------
# 6. A real dataset: breast cancer with a PyTorch model
# ------------------------------------------------------------
print("\n=== 5. Breast cancer with PyTorch (vs 98.2% from scikit-learn on Day 17) ===")
Xc, yc = load_breast_cancer(return_X_y=True)
Xc_tr, Xc_te, yc_tr, yc_te = train_test_split(Xc, yc, test_size=0.2, stratify=yc, random_state=42)
scaler = StandardScaler().fit(Xc_tr)                     # fit on train only (no leakage!)
Xc_tr, Xc_te = scaler.transform(Xc_tr), scaler.transform(Xc_te)
train_loader = DataLoader(TensorDataset(to_t(Xc_tr), to_t(yc_tr)), batch_size=32, shuffle=True)
torch.manual_seed(0)
cancer_model = MLP(30, hidden=32)
train(cancer_model, torch.optim.Adam(cancer_model.parameters(), lr=1e-3), epochs=40)
print(f"Test accuracy: {accuracy(cancer_model, to_t(Xc_te), to_t(yc_te)):.3f}")

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(7, 4))
    colors = ["#A3A3A3", "#5EEAD4", "#14B8A6", "#0F766E", "#111111"]
    for (name, hist), color in zip(curves.items(), colors):
        ax.plot(hist, label=name, color=color, linewidth=2)
    ax.set(xlabel="Epoch", ylabel="Training loss", title="Optimizers on two moons", yscale="log")
    ax.legend()
    fig.tight_layout()
    fig.savefig(HERE / "day26_optimizers.png", dpi=110)
    print("\nSaved plot: day26_optimizers.png")
except ImportError:
    pass
