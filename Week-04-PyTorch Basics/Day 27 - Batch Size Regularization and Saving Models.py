"""
Day 27 · Batch size & epochs, early stopping, dropout, batchnorm, saving/loading, seeds
"""
import copy
import random
from pathlib import Path

import numpy as np
import torch
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch import nn
from torch.utils.data import DataLoader, TensorDataset

HERE = Path(__file__).parent


# ------------------------------------------------------------
# 1. Seeds: same code -> same results
# ------------------------------------------------------------
def set_seed(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)          # also seeds CUDA when there is a GPU


print("=== 1. Seeds ===")
set_seed(1); a = torch.rand(3)
set_seed(1); b = torch.rand(3)
set_seed(2); c = torch.rand(3)
print("same seed -> same numbers:", torch.equal(a, b), "| different seed:", torch.equal(a, c))

# ------------------------------------------------------------
# Data: a small, noisy problem where a big network can overfit
# ------------------------------------------------------------
X, y = make_classification(n_samples=600, n_features=20, n_informative=5, n_redundant=5,
                           flip_y=0.08, random_state=7)
X_tr, X_tmp, y_tr, y_tmp = train_test_split(X, y, test_size=0.4, stratify=y, random_state=0)
X_val, X_te, y_val, y_te = train_test_split(X_tmp, y_tmp, test_size=0.5, stratify=y_tmp, random_state=0)
scaler = StandardScaler().fit(X_tr)
to_t = lambda a: torch.tensor(a, dtype=torch.float32)
X_tr, X_val, X_te = (to_t(scaler.transform(a)) for a in (X_tr, X_val, X_te))
y_tr, y_val, y_te = to_t(y_tr), to_t(y_val), to_t(y_te)
print(f"\nTrain {len(y_tr)} | Val {len(y_val)} | Test {len(y_te)}")


def make_model(dropout: float = 0.0, batchnorm: bool = False, hidden: int = 256) -> nn.Module:
    layers, n_in = [], 20
    for _ in range(3):
        layers.append(nn.Linear(n_in, hidden))
        if batchnorm:
            layers.append(nn.BatchNorm1d(hidden))
        layers.append(nn.ReLU())
        if dropout:
            layers.append(nn.Dropout(dropout))
        n_in = hidden
    layers.append(nn.Linear(hidden, 1))
    return nn.Sequential(*layers)


loss_fn = nn.BCEWithLogitsLoss()


def evaluate(model, X, y):
    model.eval()
    with torch.no_grad():
        logits = model(X).squeeze(-1)
        return loss_fn(logits, y).item(), ((logits > 0).float() == y).float().mean().item()


def train(model, epochs=150, batch_size=32, lr=1e-3, patience=None):
    loader = DataLoader(TensorDataset(X_tr, y_tr), batch_size=batch_size, shuffle=True)
    opt = torch.optim.Adam(model.parameters(), lr=lr)
    best_val, best_state, bad_epochs, history = float("inf"), None, 0, []
    for epoch in range(epochs):
        model.train()
        for xb, yb in loader:
            loss = loss_fn(model(xb).squeeze(-1), yb)
            opt.zero_grad()
            loss.backward()
            opt.step()
        tr_loss, _ = evaluate(model, X_tr, y_tr)
        val_loss, _ = evaluate(model, X_val, y_val)
        history.append((tr_loss, val_loss))
        # early stopping: keep the best weights, stop when val loss stops improving
        if val_loss < best_val - 1e-4:
            best_val, best_state, bad_epochs = val_loss, copy.deepcopy(model.state_dict()), 0
        else:
            bad_epochs += 1
        if patience is not None and bad_epochs >= patience:
            break
    if patience is not None and best_state is not None:
        model.load_state_dict(best_state)
    return history, epoch + 1


# ------------------------------------------------------------
# 2. Batch size and epochs
# ------------------------------------------------------------
print("\n=== 2. Batch size ===")
print(f"{'batch':>6}{'updates/epoch':>15}{'val acc':>9}")
for bs in [8, 32, 128, 360]:
    set_seed(0)
    m = make_model(hidden=64)
    train(m, epochs=40, batch_size=bs)
    print(f"{bs:>6}{-(-len(y_tr) // bs):>15}{evaluate(m, X_val, y_val)[1]:>9.3f}")
print("Small batches = more (noisier) updates; one giant batch = few updates per epoch.")

# ------------------------------------------------------------
# 3. Overfitting, early stopping, dropout, batchnorm
# ------------------------------------------------------------
print("\n=== 3. Fighting overfitting (3 x 256 network, 150 epochs) ===")
print(f"{'Setup':<32}{'epochs':>7}{'train acc':>10}{'val acc':>9}{'test acc':>9}")
results = {}
for name, kwargs, patience in [
    ("Plain (no regularisation)", {}, None),
    ("Early stopping (patience 10)", {}, 10),
    ("Dropout 0.5", {"dropout": 0.5}, None),
    ("BatchNorm", {"batchnorm": True}, None),
    ("Dropout + early stopping", {"dropout": 0.5}, 10),
]:
    set_seed(0)
    m = make_model(**kwargs)
    hist, ran = train(m, patience=patience)
    results[name] = (hist, m)
    print(f"{name:<32}{ran:>7}{evaluate(m, X_tr, y_tr)[1]:>10.3f}"
          f"{evaluate(m, X_val, y_val)[1]:>9.3f}{evaluate(m, X_te, y_te)[1]:>9.3f}")
print("Plain memorises the training set (100% train) and does worse on new data.")

# train() vs eval() really matters for dropout and batchnorm
m = results["Dropout 0.5"][1]
m.train()
with torch.no_grad():
    o1, o2 = m(X_val[:1]).item(), m(X_val[:1]).item()
m.eval()
with torch.no_grad():
    e1, e2 = m(X_val[:1]).item(), m(X_val[:1]).item()
print(f"\nSame input twice in train() mode: {o1:.3f} vs {o2:.3f} (dropout is random)")
print(f"Same input twice in eval() mode:  {e1:.3f} vs {e2:.3f} (stable)")

# ------------------------------------------------------------
# 4. Saving and loading
# ------------------------------------------------------------
print("\n=== 4. Save and load ===")
best = results["Dropout + early stopping"][1]
path = HERE / "day27_best_model.pt"
torch.save({"model_state": best.state_dict(), "config": {"dropout": 0.5}}, path)   # save weights + config
print(f"Saved {path.name} ({path.stat().st_size // 1024} KB)")

checkpoint = torch.load(path, weights_only=True)
restored = make_model(**checkpoint["config"])      # 1. rebuild the same architecture
restored.load_state_dict(checkpoint["model_state"]) # 2. load the weights
restored.eval()                                     # 3. eval mode before predicting
with torch.no_grad():
    same = torch.allclose(best(X_te), restored(X_te))
print("Restored model gives identical predictions:", same)
path.unlink()                                       # keep the repo clean (*.pt is git-ignored anyway)

# ------------------------------------------------------------
# 5. Plot: train vs validation loss
# ------------------------------------------------------------
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(11, 4), sharey=True)
    for ax, name in zip(axes, ["Plain (no regularisation)", "Dropout 0.5"]):
        hist = np.array(results[name][0])
        ax.plot(hist[:, 0], label="train loss", color="#0F766E", linewidth=2)
        ax.plot(hist[:, 1], label="validation loss", color="#111111", linewidth=2)
        best_epoch = int(hist[:, 1].argmin())
        ax.axvline(best_epoch, color="#14B8A6", linestyle="--", label=f"best val (epoch {best_epoch})")
        ax.set(title=name, xlabel="Epoch", ylim=(0, 1.5))
        ax.legend()
    axes[0].set_ylabel("Loss")
    fig.tight_layout()
    fig.savefig(HERE / "day27_overfitting.png", dpi=110)
    print("Saved plot: day27_overfitting.png")
except ImportError:
    pass
