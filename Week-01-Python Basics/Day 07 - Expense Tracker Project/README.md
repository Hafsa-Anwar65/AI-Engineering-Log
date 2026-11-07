# 💰 Expense Tracker · Week 1 Project

A command-line expense tracker that brings together everything from Week 1 of my [AI Engineering Log](../../README.md).

## ✨ Features

- Add, list and delete expenses with a category and an optional note
- Summary by category with a small bar chart in the terminal
- This month's total
- Data saved automatically to `expenses.json`
- Handles bad input, broken files and wrong categories without crashing

## 🧠 Week 1 concepts used

| Day | Concept | Where |
|:-:|---|---|
| 1 | Strings, f-strings, input | menu, formatted rows |
| 2 | Lists, dicts, loops, comprehensions | `by_category()`, menu loop |
| 3 | Functions, modules, type hints | `ask_float()`, imports in the tests |
| 4 | JSON, custom exceptions, logging | `save()` / `load()`, `ExpenseError` |
| 5 | Classes, dataclasses, dunder methods | `Expense`, `ExpenseTracker`, `__len__`, `__str__` |
| 6 | Generators, decorators, context managers | `in_month()`, `@autosave`, `safe_json_file()` |

## ▶️ Run it

```bash
python expense_tracker.py
```

```
💰 Expense Tracker · 0 expense(s) loaded

1. Add expense
2. List expenses
3. Summary by category
4. This month's total
5. Delete expense
6. Quit
```

## ✅ Tests

9 tests with **pytest**: adding, totals, validation, saving and loading, broken files, sorting, monthly filter and deleting.

```bash
pip install pytest
python -m pytest -v
```

## 📁 Files

| File | What it is |
|---|---|
| `expense_tracker.py` | The app |
| `test_expense_tracker.py` | Tests |
| `expenses.json` | Created when I add my first expense |
