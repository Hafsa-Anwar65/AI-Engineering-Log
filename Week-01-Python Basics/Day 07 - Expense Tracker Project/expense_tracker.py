"""
Expense Tracker · Week 1 project
A command-line app that uses everything from Week 1:
classes, dataclasses, JSON storage, error handling, logging,
type hints, generators, a decorator and a context manager.

Run:   python expense_tracker.py
Test:  python -m pytest
"""
from __future__ import annotations

import json
import logging
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from datetime import date
from functools import wraps
from pathlib import Path
from typing import Iterator

DATA_FILE = Path(__file__).parent / "expenses.json"
CATEGORIES = ["food", "transport", "bills", "shopping", "education", "health", "other"]

logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")
log = logging.getLogger("expense_tracker")


# ------------------------------------------------------------
# Errors
# ------------------------------------------------------------
class ExpenseError(Exception):
    """Base error for this app."""


class InvalidAmountError(ExpenseError):
    pass


class InvalidCategoryError(ExpenseError):
    pass


# ------------------------------------------------------------
# Data
# ------------------------------------------------------------
@dataclass
class Expense:
    amount: float
    category: str
    note: str = ""
    day: str = ""            # ISO date "2026-11-07"

    def __post_init__(self) -> None:
        if self.amount <= 0:
            raise InvalidAmountError("Amount must be more than 0")
        self.category = self.category.strip().lower()
        if self.category not in CATEGORIES:
            raise InvalidCategoryError(f"Category must be one of: {', '.join(CATEGORIES)}")
        if not self.day:
            self.day = date.today().isoformat()

    def __str__(self) -> str:
        return f"{self.day}  {self.category:<10} Rs {self.amount:>9,.0f}  {self.note}"


# ------------------------------------------------------------
# Helpers: a decorator and a context manager
# ------------------------------------------------------------
def autosave(method):
    """After a method changes the expenses, save them to disk."""
    @wraps(method)
    def wrapper(self: "ExpenseTracker", *args, **kwargs):
        result = method(self, *args, **kwargs)
        self.save()
        return result
    return wrapper


@contextmanager
def safe_json_file(path: Path) -> Iterator[list]:
    """Yields the list stored in a JSON file, or [] if it's missing or broken."""
    try:
        yield json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        yield []
    except json.JSONDecodeError:
        log.warning("%s is broken, starting with an empty list", path.name)
        yield []


# ------------------------------------------------------------
# The tracker
# ------------------------------------------------------------
class ExpenseTracker:
    def __init__(self, path: Path = DATA_FILE):
        self.path = path
        self.expenses: list[Expense] = []
        self.load()

    # storage
    def load(self) -> None:
        with safe_json_file(self.path) as rows:
            loaded = []
            for row in rows:
                try:
                    loaded.append(Expense(**row))
                except (ExpenseError, TypeError) as err:
                    log.warning("Skipping bad row %s: %s", row, err)
            self.expenses = loaded

    def save(self) -> None:
        data = [asdict(e) for e in self.expenses]
        self.path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    # actions
    @autosave
    def add(self, amount: float, category: str, note: str = "", day: str = "") -> Expense:
        expense = Expense(amount, category, note, day)
        self.expenses.append(expense)
        return expense

    @autosave
    def delete(self, index: int) -> Expense:
        if not 0 <= index < len(self.expenses):
            raise ExpenseError(f"No expense number {index + 1}")
        return self.expenses.pop(index)

    # reports
    def total(self) -> float:
        return sum(e.amount for e in self.expenses)

    def by_category(self) -> dict[str, float]:
        totals: dict[str, float] = {}
        for e in self.expenses:
            totals[e.category] = totals.get(e.category, 0) + e.amount
        return dict(sorted(totals.items(), key=lambda kv: kv[1], reverse=True))

    def in_month(self, year_month: str) -> Iterator[Expense]:
        """Generator: expenses from one month, e.g. '2026-11'."""
        return (e for e in self.expenses if e.day.startswith(year_month))

    def __len__(self) -> int:
        return len(self.expenses)


# ------------------------------------------------------------
# Command-line menu
# ------------------------------------------------------------
MENU = """
1. Add expense
2. List expenses
3. Summary by category
4. This month's total
5. Delete expense
6. Quit"""


def ask_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please type a number, e.g. 450 or 99.5")


def main() -> None:
    tracker = ExpenseTracker()
    print(f"💰 Expense Tracker · {len(tracker)} expense(s) loaded")

    while True:
        print(MENU)
        choice = input("Choose 1-6: ").strip()

        if choice == "1":
            amount = ask_float("Amount (Rs): ")
            print("Categories:", ", ".join(CATEGORIES))
            category = input("Category: ")
            note = input("Note (optional): ").strip()
            try:
                expense = tracker.add(amount, category, note)
                print(f"✅ Added: {expense}")
            except ExpenseError as err:
                print(f"❌ {err}")

        elif choice == "2":
            if not tracker.expenses:
                print("No expenses yet")
            for i, e in enumerate(tracker.expenses, start=1):
                print(f"{i:>3}. {e}")

        elif choice == "3":
            for category, amount in tracker.by_category().items():
                share = amount / tracker.total() * 100
                print(f"{category:<10} Rs {amount:>9,.0f}  {'█' * round(share / 5)} {share:.0f}%")
            print(f"{'TOTAL':<10} Rs {tracker.total():>9,.0f}")

        elif choice == "4":
            month = date.today().strftime("%Y-%m")
            print(f"{month}: Rs {sum(e.amount for e in tracker.in_month(month)):,.0f}")

        elif choice == "5":
            try:
                removed = tracker.delete(int(input("Number to delete: ")) - 1)
                print(f"🗑️ Deleted: {removed}")
            except (ValueError, ExpenseError) as err:
                print(f"❌ {err}")

        elif choice == "6":
            print("Bye! Your expenses are saved.")
            break

        else:
            print("Please choose 1-6")


if __name__ == "__main__":
    main()
