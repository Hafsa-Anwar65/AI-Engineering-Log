"""
Banking Intent Classifier · Week 3 project
Reads a customer's message and predicts which of 77 banking intents it is
(card_arrival, lost_or_stolen_card, exchange_rate ...).

Dataset: Banking77 (PolyAI, CC-BY-4.0), downloaded on first run.

Run:   python banking_intents.py
Test:  python -m pytest -v
"""
from __future__ import annotations

import csv
import time
import urllib.request
from pathlib import Path

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.model_selection import GridSearchCV
from sklearn.naive_bayes import ComplementNB
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.svm import LinearSVC

HERE = Path(__file__).parent
DATA_DIR = HERE / "data"
BASE_URL = "https://raw.githubusercontent.com/PolyAI-LDN/task-specific-datasets/master/banking_data/"


# ------------------------------------------------------------
# Data
# ------------------------------------------------------------
def download(split: str) -> Path:
    """Download train.csv / test.csv once and reuse the local copy."""
    DATA_DIR.mkdir(exist_ok=True)
    path = DATA_DIR / f"{split}.csv"
    if not path.exists():
        print(f"Downloading {split}.csv ...")
        urllib.request.urlretrieve(BASE_URL + f"{split}.csv", path)
    return path


def load(split: str) -> tuple[list[str], list[str]]:
    with open(download(split), newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return [r["text"] for r in rows], [r["category"] for r in rows]


# ------------------------------------------------------------
# Models
# ------------------------------------------------------------
def tfidf() -> TfidfVectorizer:
    # word 1-2 grams catch phrases like "not arrived", "top up"
    return TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, min_df=1)


def candidate_models() -> dict[str, Pipeline]:
    return {
        "Naive Bayes": make_pipeline(tfidf(), ComplementNB()),
        "Logistic Regression": make_pipeline(tfidf(), LogisticRegression(max_iter=2000, C=10)),
        "Linear SVM": make_pipeline(tfidf(), LinearSVC(C=1)),
        "Random Forest": make_pipeline(tfidf(), RandomForestClassifier(n_estimators=200, n_jobs=-1, random_state=42)),
    }


def tune_svm(X_train, y_train) -> Pipeline:
    """GridSearch the best SVM settings with 5-fold CV on the training data only."""
    pipe = Pipeline([("tfidf", tfidf()), ("clf", LinearSVC())])
    grid = GridSearchCV(
        pipe,
        {"tfidf__ngram_range": [(1, 1), (1, 2)], "clf__C": [0.3, 1, 3]},
        cv=5, scoring="f1_macro", n_jobs=-1,
    )
    grid.fit(X_train, y_train)
    print(f"Best settings: {grid.best_params_} (CV macro-F1 {grid.best_score_:.3f})")
    return grid.best_estimator_


def most_confused(y_true, y_pred, labels, top: int = 5) -> list[tuple[str, str, int]]:
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    np.fill_diagonal(cm, 0)
    pairs = []
    for i, j in zip(*np.unravel_index(np.argsort(cm, axis=None)[::-1][:top], cm.shape)):
        pairs.append((labels[i], labels[j], int(cm[i, j])))
    return pairs


# ------------------------------------------------------------
# Main
# ------------------------------------------------------------
def main() -> None:
    X_train, y_train = load("train")
    X_test, y_test = load("test")
    labels = sorted(set(y_train))
    print(f"Train {len(X_train)} | Test {len(X_test)} | Intents {len(labels)}")

    # 1. Compare 4 models
    print(f"\n{'Model':<22}{'Accuracy':>10}{'Macro-F1':>10}{'Train time':>12}")
    results = {}
    for name, model in candidate_models().items():
        start = time.perf_counter()
        model.fit(X_train, y_train)
        seconds = time.perf_counter() - start
        pred = model.predict(X_test)
        results[name] = (accuracy_score(y_test, pred), f1_score(y_test, pred, average="macro"), seconds)
        print(f"{name:<22}{results[name][0]:>10.3f}{results[name][1]:>10.3f}{seconds:>11.1f}s")

    # 2. Tune the best family
    print("\nTuning Linear SVM with GridSearchCV ...")
    best = tune_svm(X_train, y_train)
    pred = best.predict(X_test)
    acc, f1 = accuracy_score(y_test, pred), f1_score(y_test, pred, average="macro")
    print(f"Tuned Linear SVM on test: accuracy {acc:.3f} | macro-F1 {f1:.3f}")

    # 3. Where does it struggle?
    report = classification_report(y_test, pred, output_dict=True, zero_division=0)
    per_class = sorted(((report[c]["f1-score"], c) for c in labels))
    print("\nHardest 5 intents:")
    for score, c in per_class[:5]:
        print(f"  {c:<45} F1 {score:.2f}")
    print("Easiest 5 intents:")
    for score, c in per_class[-5:][::-1]:
        print(f"  {c:<45} F1 {score:.2f}")

    print("\nMost confused pairs (true -> predicted):")
    for true, guess, n in most_confused(y_test, pred, labels):
        print(f"  {true} -> {guess}: {n} times")

    # 4. Try it on new messages
    print("\nNew messages:")
    for msg in [
        "my card still hasn't come in the post",
        "someone stole my wallet with my debit card",
        "what rate do you use to convert dollars to euros?",
        "I was charged twice for the same coffee",
        "how do I top up using apple pay",
    ]:
        print(f"  {msg!r:<55} -> {best.predict([msg])[0]}")

    # 5. Plot
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
        names = list(results) + ["Tuned Linear SVM"]
        f1s = [results[n][1] for n in results] + [f1]
        colors = ["#99F6E4"] * len(results) + ["#0F766E"]
        ax1.barh(names, f1s, color=colors)
        ax1.set(xlim=(0.5, 1), xlabel="Macro-F1 on test", title="Model comparison")
        for y, v in enumerate(f1s):
            ax1.text(v + 0.005, y, f"{v:.3f}", va="center")

        worst = per_class[:10]
        ax2.barh([c for _, c in worst][::-1], [s for s, _ in worst][::-1], color="#14B8A6")
        ax2.set(xlim=(0, 1), xlabel="F1", title="10 hardest intents")
        ax2.tick_params(axis="y", labelsize=8)
        fig.tight_layout()
        fig.savefig(HERE / "results.png", dpi=110)
        print("\nSaved plot: results.png")
    except ImportError:
        print("\n(pip install matplotlib to save the plot)")


if __name__ == "__main__":
    main()
