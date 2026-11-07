"""
Tests for the expense tracker. Run with:  python -m pytest
tmp_path is a pytest fixture: a fresh temporary folder for every test,
so tests never touch my real expenses.json.
"""
import pytest

from expense_tracker import (
    Expense,
    ExpenseError,
    ExpenseTracker,
    InvalidAmountError,
    InvalidCategoryError,
)


def make_tracker(tmp_path) -> ExpenseTracker:
    return ExpenseTracker(path=tmp_path / "expenses.json")


def test_add_and_total(tmp_path):
    tracker = make_tracker(tmp_path)
    tracker.add(500, "food")
    tracker.add(250.5, "transport")
    assert len(tracker) == 2
    assert tracker.total() == 750.5


def test_negative_amount_is_rejected():
    with pytest.raises(InvalidAmountError):
        Expense(-10, "food")


def test_unknown_category_is_rejected():
    with pytest.raises(InvalidCategoryError):
        Expense(100, "games")


def test_category_is_cleaned():
    assert Expense(100, "  FOOD ").category == "food"


def test_saves_and_loads_from_json(tmp_path):
    path = tmp_path / "expenses.json"
    ExpenseTracker(path).add(1200, "bills", "electricity", "2026-11-05")
    reloaded = ExpenseTracker(path)                 # a brand-new tracker reads the file
    assert len(reloaded) == 1
    assert reloaded.expenses[0].note == "electricity"


def test_broken_json_starts_empty(tmp_path):
    path = tmp_path / "expenses.json"
    path.write_text("{ this is not json", encoding="utf-8")
    assert len(ExpenseTracker(path)) == 0


def test_by_category_sorted_biggest_first(tmp_path):
    tracker = make_tracker(tmp_path)
    tracker.add(100, "food")
    tracker.add(900, "bills")
    tracker.add(300, "food")
    assert list(tracker.by_category().items()) == [("bills", 900), ("food", 400)]


def test_in_month_filters_by_date(tmp_path):
    tracker = make_tracker(tmp_path)
    tracker.add(100, "food", day="2026-10-30")
    tracker.add(200, "food", day="2026-11-02")
    tracker.add(300, "food", day="2026-11-07")
    assert sum(e.amount for e in tracker.in_month("2026-11")) == 500


def test_delete_bad_index_raises(tmp_path):
    tracker = make_tracker(tmp_path)
    with pytest.raises(ExpenseError):
        tracker.delete(5)
