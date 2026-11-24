"""Tests for the banking intent classifier. Run with:  python -m pytest -v
Uses a tiny hand-made dataset, so the tests run fast and offline."""
from sklearn.svm import LinearSVC

from banking_intents import candidate_models, most_confused, tfidf
from sklearn.pipeline import make_pipeline

TEXTS = [
    "my card has not arrived", "when will my new card arrive", "card still not delivered",
    "my card was stolen", "i lost my card yesterday", "someone took my card",
    "what is the exchange rate", "how much is a dollar in euros", "currency conversion rate",
]
LABELS = ["card_arrival"] * 3 + ["lost_or_stolen_card"] * 3 + ["exchange_rate"] * 3


def test_all_models_fit_and_predict():
    for name, model in candidate_models().items():
        model.fit(TEXTS, LABELS)
        assert len(model.predict(["card not here yet"])) == 1, name


def test_svm_learns_obvious_intents():
    model = make_pipeline(tfidf(), LinearSVC()).fit(TEXTS, LABELS)
    assert model.predict(["my card got stolen"])[0] == "lost_or_stolen_card"
    assert model.predict(["dollar to euro rate"])[0] == "exchange_rate"


def test_tfidf_uses_word_pairs():
    vec = tfidf().fit(TEXTS)
    assert "not arrived" in vec.vocabulary_


def test_most_confused_ignores_correct_answers():
    y_true = ["a", "a", "b", "b", "b"]
    y_pred = ["a", "b", "a", "a", "b"]
    pairs = most_confused(y_true, y_pred, ["a", "b"], top=2)
    assert pairs[0] == ("b", "a", 2)
    assert all(t != p for t, p, _ in pairs)
