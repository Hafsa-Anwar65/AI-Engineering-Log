"""
Day 04 · Files, JSON & CSV, errors (try/except), custom exceptions, logging
"""
import csv
import json
import logging
from pathlib import Path

# All files from today go into a folder next to this script
DATA = Path(__file__).parent / "day04_data"
DATA.mkdir(exist_ok=True)

# ------------------------------------------------------------
# Logging setup: messages go to the screen AND to a file
# ------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-7s | %(message)s",
    handlers=[logging.FileHandler(DATA / "app.log", encoding="utf-8"), logging.StreamHandler()],
)
log = logging.getLogger("day04")


# ------------------------------------------------------------
# Part 0: concept practice
# ------------------------------------------------------------
print("--- Writing and reading a text file ---")
notes_file = DATA / "notes.txt"

with open(notes_file, "w", encoding="utf-8") as f:      # "w" = write (overwrites)
    f.write("Line 1: files are easy\n")
    f.write("Line 2: 'with' closes the file for me\n")

with open(notes_file, "a", encoding="utf-8") as f:      # "a" = append
    f.write("Line 3: added later\n")

with open(notes_file, "r", encoding="utf-8") as f:      # "r" = read
    for number, line in enumerate(f, start=1):
        print(number, line.strip())

print("\n--- pathlib ---")
print(notes_file.name, notes_file.suffix, notes_file.exists())
print(notes_file.read_text(encoding="utf-8").count("\n"), "lines")

print("\n--- JSON: Python dict <-> text file ---")
settings = {"theme": "dark", "font_size": 14, "languages": ["en", "ur"]}
(DATA / "settings.json").write_text(json.dumps(settings, indent=2), encoding="utf-8")
loaded = json.loads((DATA / "settings.json").read_text(encoding="utf-8"))
print(loaded["languages"], type(loaded))

print("\n--- try / except / else / finally ---")
for value in ["42", "abc", "0"]:
    try:
        number = int(value)
        result = 100 / number
    except ValueError:
        print(f"'{value}' is not a number")
    except ZeroDivisionError:
        print("Can't divide by zero")
    else:
        print(f"100 / {number} = {result}")       # runs only if no error
    finally:
        print("  (checked", value + ")")          # always runs

print("\n--- Raising an error myself ---")


def set_age(age: int) -> int:
    if age < 0:
        raise ValueError("Age can't be negative")
    return age


try:
    set_age(-5)
except ValueError as err:
    print("Caught:", err)


# ------------------------------------------------------------
# Script 1: Contact book saved in JSON
# ------------------------------------------------------------
print("\n--- Script 1: Contact book (JSON) ---")
CONTACTS = DATA / "contacts.json"


def load_contacts() -> dict:
    try:
        return json.loads(CONTACTS.read_text(encoding="utf-8"))
    except FileNotFoundError:
        log.info("No contacts file yet, starting empty")
        return {}
    except json.JSONDecodeError:
        log.warning("contacts.json was broken, starting empty")
        return {}


def save_contacts(contacts: dict) -> None:
    CONTACTS.write_text(json.dumps(contacts, indent=2), encoding="utf-8")
    log.info("Saved %d contact(s)", len(contacts))


contacts = load_contacts()
name = input("Contact name (leave empty to skip): ").strip().title()
if name:
    phone = input("Phone: ").strip()
    contacts[name] = phone
    save_contacts(contacts)

print("All contacts:")
for person, number in sorted(contacts.items()):
    print(f"  {person:<12} {number}")


# ------------------------------------------------------------
# Script 2: Expense report from a CSV file
# ------------------------------------------------------------
print("\n--- Script 2: Expense report (CSV) ---")
EXPENSES = DATA / "expenses.csv"

sample = [
    {"date": "2026-11-01", "category": "food", "amount": "850"},
    {"date": "2026-11-02", "category": "transport", "amount": "300"},
    {"date": "2026-11-03", "category": "food", "amount": "1200"},
    {"date": "2026-11-04", "category": "books", "amount": "1500"},
    {"date": "2026-11-05", "category": "transport", "amount": "abc"},   # bad row on purpose
]
with open(EXPENSES, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["date", "category", "amount"])
    writer.writeheader()
    writer.writerows(sample)

totals = {}
with open(EXPENSES, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        try:
            amount = float(row["amount"])
        except ValueError:
            log.warning("Skipping bad amount on %s: %r", row["date"], row["amount"])
            continue
        totals[row["category"]] = totals.get(row["category"], 0) + amount

for category, total in sorted(totals.items(), key=lambda kv: kv[1], reverse=True):
    print(f"  {category:<10} Rs {total:>8,.0f}")
print(f"  {'TOTAL':<10} Rs {sum(totals.values()):>8,.0f}")


# ------------------------------------------------------------
# Script 3: Bank account with a custom exception
# ------------------------------------------------------------
print("\n--- Script 3: Custom exception ---")


class InsufficientFundsError(Exception):
    """Raised when a withdrawal is bigger than the balance."""


def withdraw(balance: float, amount: float) -> float:
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise InsufficientFundsError(f"Balance Rs {balance:,.0f}, tried Rs {amount:,.0f}")
    return balance - amount


balance = 5000
for amount in [1200, -50, 10000, 800]:
    try:
        balance = withdraw(balance, amount)
        log.info("Withdrew Rs %s, balance Rs %s", amount, balance)
    except InsufficientFundsError as err:
        log.error("Not enough money: %s", err)
    except ValueError as err:
        log.error("Invalid amount: %s", err)

print(f"Final balance: Rs {balance:,.0f}")
print(f"\nAll log messages were also saved to {DATA / 'app.log'}")
