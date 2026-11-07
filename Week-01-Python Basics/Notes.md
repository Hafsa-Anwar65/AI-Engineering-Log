# 📝 Week 1 · Python from the Basics

> My notes, in my own words. One section per day.

**Days this week:**
[Day 1](#-day-1--variables-types-inputoutput-strings) ·
[Day 2](#-day-2--control-flow--data-structures) ·
[Day 3](#-day-3--functions-modules--virtual-environments) ·
[Day 4](#-day-4--files-json--csv-errors--logging) ·
[Day 5](#-day-5--object-oriented-programming-oop) ·
[Day 6](#-day-6--modern-python) ·
[Day 7](#-day-7--%EF%B8%8F-week-1-project-expense-tracker)

---

## 📅 Day 1 · Variables, Types, Input/Output, Strings

**Date:** Nov 1, 2026
**Code:** [`Day 01 - Python Basics.py`](./Day%2001%20-%20Python%20Basics.py)

### 1. Variables & Data Types

A variable is a name that stores a value. Python has 5 basic types:

| Type | What it holds | Example |
|---|---|---|
| `str` | Text | `city = "Karachi"` |
| `int` | Whole number | `year = 2026` |
| `float` | Decimal number | `temp = 31.5` |
| `bool` | True or False | `is_weekend = False` |
| `None` | No value yet | `plan = None` |

`type(x)` tells me which type a value is.

### 2. Input & Type Conversion

#### `input()` always returns text

```python
age = input("Age: ")   # "21" is a string, not a number
```

#### Convert before doing maths

```python
age = int(input("Age: "))       # whole number
price = float(input("Price: ")) # decimal
label = str(2026) + "!"         # number to text
```

> ⚠️ `"5" + 1` gives an error. Convert first.

### 3. Printing with f-strings

#### Basic f-string

```python
print(f"Hello {name}, you are {age}")
```

#### Formatting decimals

```python
print(f"Total: Rs {total:.2f}")   # 2 decimal places
```

### 4. Strings

#### Indexing & slicing

| Code | Result for `"Learning"` |
|---|---|
| `s[0]` | `L` (first character) |
| `s[-1]` | `g` (last character) |
| `s[0:5]` | `Learn` (first 5) |
| `s[-4:]` | `ning` (last 4) |
| `s[::-1]` | `gninraeL` (reversed) |

#### Useful methods

| Method | What it does |
|---|---|
| `strip()` | Removes spaces at both ends |
| `lower()` / `upper()` | Changes case |
| `title()` | Capitalises Every Word |
| `split()` | Breaks text into a list of words |
| `replace(a, b)` | Replaces `a` with `b` |
| `count(x)` | Counts how many times `x` appears |
| `len(s)` | Number of characters |

#### Checking if something is inside

```python
"python" in text.lower()   # True or False
```

### 5. Maths Operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `/` | Normal division | `17 / 5` | `3.4` |
| `//` | Whole-number division | `17 // 5` | `3` |
| `%` | Remainder | `17 % 5` | `2` |
| `**` | Power | `2 ** 10` | `1024` |

> 💡 `//` and `%` together turn minutes into hours + minutes: `75 // 60 = 1`, `75 % 60 = 15`.

### 🛠️ What I Built

| Script | What it does | Concepts used |
|---|---|---|
| **Profile card** | Asks name, birth year and hobby, prints a formatted card | `input()`, `int()`, `title()`, f-strings, indexing |
| **Bill splitter** | Splits a bill with tip between people | `float()`, maths, `:.2f` |
| **Text analyser** | Counts characters and words, reverses text, checks palindromes | `split()`, `len()`, slicing, `[::-1]` |

---

## 📅 Day 2 · Control Flow & Data Structures

**Date:** Nov 2, 2026
**Code:** [`Day 02 - Control Flow.py`](./Day%2002%20-%20Control%20Flow.py)

### 1. Conditions: if / elif / else

#### Basic structure

```python
if temperature >= 35:
    print("Very hot")
elif temperature >= 25:
    print("Warm")
else:
    print("Pleasant")
```

#### Combining conditions

| Keyword | Meaning | Example |
|---|---|---|
| `and` | Both must be true | `is_weekend and not has_work` |
| `or` | At least one is true | `day == "Sat" or day == "Sun"` |
| `not` | Flips True/False | `not has_work` |

> ⚠️ Indentation (4 spaces) decides what is inside the `if`.

### 2. Loops

#### `for` loop with `range()`

| Code | Gives |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(10, 0, -3)` | 10, 7, 4, 1 |

#### `while` loop

Runs as long as the condition is true. Good for menus and "keep asking" programs.

#### `break` and `continue`

| Keyword | What it does |
|---|---|
| `break` | Stops the loop completely |
| `continue` | Skips to the next round |

#### `enumerate()`

```python
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

### 3. Data Structures

#### Comparison

| Type | Syntax | Ordered | Changeable | Duplicates | Use it for |
|---|---|:-:|:-:|:-:|---|
| List | `[1, 2, 3]` | ✅ | ✅ | ✅ | A collection that changes |
| Tuple | `(1, 2)` | ✅ | ❌ | ✅ | Fixed groups, e.g. coordinates |
| Dict | `{"a": 1}` | ✅ | ✅ | Keys unique | Looking things up by name |
| Set | `{1, 2, 3}` | ❌ | ✅ | ❌ | Unique items, fast "is it in?" |

#### List methods

| Method | What it does |
|---|---|
| `append(x)` | Adds to the end |
| `insert(i, x)` | Adds at position `i` |
| `remove(x)` | Removes the first `x` |
| `pop()` | Removes and returns the last item |
| `sorted(lst)` | Returns a new sorted list |

#### Dictionary basics

```python
student["age"] = 22                 # add or update
student.get("email", "no email")   # safe lookup with a default
for key, value in student.items():  # loop over pairs
    ...
```

#### Set operations

| Operator | Meaning | `{1,2,3,4}` and `{3,4,5}` |
|---|---|---|
| `\|` | Union | `{1, 2, 3, 4, 5}` |
| `&` | Intersection | `{3, 4}` |
| `-` | Difference | `{1, 2}` |

### 4. Comprehensions

One-line way to build a list, dict or set:

```python
squares = [n ** 2 for n in range(1, 6)]              # list
evens   = [n for n in range(1, 11) if n % 2 == 0]    # list with a filter
lengths = {w: len(w) for w in ["python", "ai"]}      # dict
letters = {ch for ch in "banana"}                     # set
```

### 5. LeetCode

| # | Problem | Key idea | File |
|---|---|---|---|
| 1 | Two Sum | Dictionary of seen numbers, one pass, O(n) | [`0001 - Two Sum.py`](../LeetCode/0001%20-%20Two%20Sum.py) |
| 217 | Contains Duplicate | A set removes duplicates; compare lengths | [`0217 - Contains Duplicate.py`](../LeetCode/0217%20-%20Contains%20Duplicate.py) |

### 🛠️ What I Built

| Script | What it does | Concepts used |
|---|---|---|
| **Grade calculator** | Grades 5 subjects, finds the average and best subject | dict, `for`, `if/elif`, `max(key=...)` |
| **Shopping list manager** | Menu to add, remove and show items | `while True`, `break`, list methods, `enumerate` |
| **Word frequency counter** | Counts words in a paragraph, shows the top 5 | dict counting, `set`, `sorted(key=...)`, comprehension |

---

## 📅 Day 3 · Functions, Modules & Virtual Environments

**Date:** Nov 3, 2026
**Code:** [`Day 03 - Functions.py`](./Day%2003%20-%20Functions.py) · [`text_tools.py`](./text_tools.py)

### 1. Functions

#### Defining and calling

```python
def greet(name):
    """Docstring: explains what the function does."""
    return f"Hello, {name}!"

greet("Hafsa")
```

> 💡 `return` sends a value back. Without it, the function returns `None`.

#### Types of arguments

| Kind | Example | Meaning |
|---|---|---|
| Positional | `power(2, 10)` | Matched by order |
| Default | `def power(base, exponent=2)` | Used if I don't pass a value |
| Keyword | `describe(role="AI", name="Sara")` | Matched by name, order doesn't matter |
| `*args` | `def total(*args)` | Any number of values, arrives as a **tuple** |
| `**kwargs` | `def profile(**kwargs)` | Any number of named values, arrives as a **dict** |

#### Returning more than one value

```python
def min_max(nums):
    return min(nums), max(nums)   # a tuple

low, high = min_max([4, 9, 1])
```

#### Type hints

```python
def km_to_miles(km: float) -> float:
```

Hints don't change how the code runs; they make it easier to read and let the editor catch mistakes.

### 2. Scope

| Variable | Where it lives |
|---|---|
| Local | Created inside a function, gone when the function ends |
| Global | Created outside all functions, readable everywhere |

> ⚠️ Assigning inside a function creates a **new local** variable. Changing a global needs `global name`, which is best avoided.

### 3. Lambdas, map & filter

| Tool | What it does | Example |
|---|---|---|
| `lambda` | One-line nameless function | `lambda x: x ** 2` |
| `sorted(key=...)` | Sort by a rule | `sorted(students, key=lambda s: s[1])` |
| `map` | Transform every item | `map(lambda n: n * 10, nums)` |
| `filter` | Keep items that pass a test | `filter(lambda n: n % 2 == 0, nums)` |

Functions are values too: I can store them in a dict or pass them to another function.

### 4. Modules & Imports

#### Import styles

| Style | Example | Use |
|---|---|---|
| Whole module | `import math` → `math.sqrt(9)` | Clear where things come from |
| Some names | `from random import randint` | Shorter calls |
| Alias | `import datetime as dt` | Short name for long modules |

#### My own module

Any `.py` file is a module. `text_tools.py` sits next to my Day 3 file, so `import text_tools` works.

```python
if __name__ == "__main__":
    # runs only when I run this file directly, not when it's imported
```

> ⚠️ A module's file name can't have spaces, which is why it's `text_tools.py`.

### 5. Virtual Environments & Packages

#### Why

Each project gets its own isolated set of packages, so versions from one project never break another.

#### Commands (with uv)

| Task | Command |
|---|---|
| Create a venv | `uv venv` |
| Activate (Windows) | `.venv\Scripts\activate` |
| Install a package | `uv pip install requests` |
| Save the list | `uv pip freeze > requirements.txt` |
| Install from the list | `uv pip install -r requirements.txt` |

> 💡 `.venv/` goes in `.gitignore`; `requirements.txt` goes in git.

### 🛠️ What I Built

| Script | What it does | Concepts used |
|---|---|---|
| **Unit converter** | Menu that picks a conversion function from a dictionary | functions as values, type hints, return |
| **Password checker** | Scores a password with small single-job functions | `any()`, small functions, list indexing |
| **Text report** | Analyses a sentence using my own module | `import`, `**kwargs`, `.get()` defaults |
| **`text_tools.py`** | My first reusable module | docstrings, `if __name__ == "__main__"` |

---

## 📅 Day 4 · Files, JSON & CSV, Errors & Logging

**Date:** Nov 4, 2026
**Code:** [`Day 04 - Files and Errors.py`](./Day%2004%20-%20Files%20and%20Errors.py)

### 1. Reading & Writing Files

#### File modes

| Mode | Meaning |
|---|---|
| `"r"` | Read (default) |
| `"w"` | Write, **overwrites** the file |
| `"a"` | Append to the end |

#### Always use `with`

```python
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")
```

> 💡 `with` closes the file automatically, even if an error happens.

#### pathlib

```python
from pathlib import Path
p = Path("data") / "notes.txt"
p.exists(), p.name, p.suffix, p.read_text()
```

### 2. JSON & CSV

| Format | Looks like | Python tool |
|---|---|---|
| JSON | `{"name": "Ali", "age": 22}` | `json.dumps()` / `json.loads()` |
| CSV | `date,category,amount` rows | `csv.DictReader` / `csv.DictWriter` |

- JSON is for nested data (dicts and lists), like settings or API responses.
- CSV is for tables, like spreadsheets.

### 3. Handling Errors

#### try / except / else / finally

```python
try:
    number = int(value)
except ValueError:
    print("Not a number")
else:
    print("Worked!")         # only if no error
finally:
    print("Always runs")
```

#### Common errors

| Error | When it happens |
|---|---|
| `ValueError` | Right type, wrong value, e.g. `int("abc")` |
| `ZeroDivisionError` | Dividing by 0 |
| `FileNotFoundError` | File doesn't exist |
| `KeyError` | Dict key doesn't exist |
| `json.JSONDecodeError` | Broken JSON |

#### Raising errors & custom exceptions

```python
class InsufficientFundsError(Exception):
    pass

if amount > balance:
    raise InsufficientFundsError("Not enough money")
```

> ⚠️ Catch specific errors. A bare `except:` hides real bugs.

### 4. Logging

Better than `print()` for real programs: messages have a level and a time, and can go to a file.

| Level | Use for |
|---|---|
| `DEBUG` | Detailed info while developing |
| `INFO` | Normal events ("saved 3 contacts") |
| `WARNING` | Something odd but the program continues |
| `ERROR` | Something failed |

```python
import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("app")
log.info("Started")
```

### 🛠️ What I Built

| Script | What it does | Concepts used |
|---|---|---|
| **Contact book** | Saves contacts in JSON, survives a missing or broken file | `json`, `pathlib`, `FileNotFoundError` |
| **Expense report** | Totals expenses by category from a CSV, skips bad rows | `csv.DictReader`, `try/except`, `continue` |
| **Bank withdrawal** | Blocks overdrafts with my own exception, logs everything | custom exception, `raise`, logging to a file |

---

## 📅 Day 5 · Object-Oriented Programming (OOP)

**Date:** Nov 5, 2026
**Code:** [`Day 05 - OOP.py`](./Day%2005%20-%20OOP.py)

### 1. Classes & Objects

A **class** is a blueprint; an **object** is one thing made from it.

```python
class Dog:
    species = "Canis familiaris"     # class attribute (shared)

    def __init__(self, name, age):   # runs when an object is created
        self.name = name             # instance attributes (per object)
        self.age = age

    def bark(self):                  # method
        return f"{self.name} says Woof!"

tommy = Dog("Tommy", 3)
```

> 💡 `self` is the object itself: the "this one" the method is working on.

### 2. Dunder Methods

| Method | Makes this work |
|---|---|
| `__init__` | Creating an object |
| `__str__` | `print(obj)` |
| `__repr__` | How it shows in lists / the debugger |
| `__add__` | `a + b` |
| `__eq__` | `a == b` |
| `__lt__` | `a < b` and `sorted()` |
| `__len__` | `len(obj)` |

### 3. The 4 Pillars of OOP

| Pillar | Meaning | In my code |
|---|---|---|
| **Encapsulation** | Hide internal data, control access | `_balance` + `@property` |
| **Inheritance** | A child class reuses a parent class | `SavingsAccount(BankAccount)` |
| **Polymorphism** | Same method name, different behaviour | `speak()` for Cat vs Parrot, `area()` for shapes |
| **Abstraction** | Show what it does, hide how | `Shape.area()` that every shape must define |

#### Inheritance with `super()`

```python
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)   # parent sets owner & balance
        self.rate = rate
```

#### Inheritance vs composition

| | Inheritance | Composition |
|---|---|---|
| Relation | **IS A** (a Cat is an Animal) | **HAS A** (a Library has Books) |
| Example | `class Cat(Animal)` | `self.books = {}` inside `Library` |

### 4. Properties, Class & Static Methods

| Decorator | What it is | Example |
|---|---|---|
| `@property` | A method used like an attribute; can validate | `t.celsius = 30` |
| `@classmethod` | Gets the class (`cls`), often another way to create objects | `Temperature.from_fahrenheit(98.6)` |
| `@staticmethod` | Helper inside the class, no `self` | `Temperature.is_fever(38.5)` |

### 5. Dataclasses

Writes `__init__`, `__repr__` and `__eq__` for me:

```python
from dataclasses import dataclass, field

@dataclass
class Book:
    title: str
    pages: int
    tags: list = field(default_factory=list)   # safe mutable default
```

### 🛠️ What I Built

| Script | What it does | Concepts used |
|---|---|---|
| **Bank accounts** | Deposit, withdraw, history; savings account adds interest | encapsulation, `@property`, inheritance, `super()` |
| **Library system** | Lend and return books to members | composition, dataclasses, `__len__` |
| **Shapes** | Circle, rectangle, square sorted by area | polymorphism, `__lt__`, abstract `area()` |

---

## 📅 Day 6 · Modern Python

**Date:** Nov 6, 2026
**Code:** [`Day 06 - Modern Python.py`](./Day%2006%20-%20Modern%20Python.py)

### 1. Type Hints

```python
def average(numbers: list[float]) -> float: ...
def find_user(users: dict[str, int], name: str) -> Optional[int]: ...
def describe(value: int | str) -> str: ...
```

| Hint | Means |
|---|---|
| `list[float]` | A list of floats |
| `dict[str, int]` | Keys are str, values are int |
| `Optional[int]` | An int **or** `None` |
| `int \| str` | Either an int or a str |

> 💡 Python doesn't enforce hints at runtime. They help me, VS Code and tools like mypy catch mistakes.

### 2. Iterators

A `for` loop secretly calls `iter()` once and then `next()` again and again until `StopIteration`.

| Method | Job |
|---|---|
| `__iter__` | Returns the iterator |
| `__next__` | Returns the next value, or raises `StopIteration` |

### 3. Generators

```python
def countdown(start):
    while start > 0:
        yield start        # pause, hand back a value, continue next time
        start -= 1
```

| | List | Generator |
|---|---|---|
| Builds values | All at once | One at a time, when asked |
| Memory | Grows with size | Tiny, always |
| Syntax | `[n*n for n in x]` | `(n*n for n in x)` |
| Best for | Small data I reuse | Big files, streams, infinite sequences |

### 4. Decorators

A decorator is a function that **wraps** another function to add behaviour (timing, retrying, logging, checking).

```python
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

@timer              # same as: slow_sum = timer(slow_sum)
def slow_sum(n): ...
```

- **`@wraps(func)`** keeps the original function's name and docstring.
- **A decorator with an argument** (`@retry(times=3)`) is a function that **returns** a decorator: 3 levels.

### 5. Context Managers

Set something up, then **always** clean up, even if an error happens.

| Way | How |
|---|---|
| Class | `__enter__` (setup) and `__exit__` (cleanup) |
| Generator | `@contextmanager`: code before `yield` = setup, `finally` after it = cleanup |

```python
@contextmanager
def announce(task):
    print("start", task)
    try:
        yield
    finally:
        print("finished", task)
```

### 6. async / await

For tasks that spend most of their time **waiting** (web requests, APIs, files), run them together instead of one by one.

| Keyword | Meaning |
|---|---|
| `async def` | This function can pause |
| `await` | Pause here until this finishes; meanwhile others can run |
| `asyncio.gather()` | Run several at the same time |
| `asyncio.run()` | Start the async program |

> 💡 3 downloads of 1 second each took **1 second total**, not 3. This is how FastAPI and LLM apps handle many requests at once.

### 🛠️ What I Built

| Example | Concepts used |
|---|---|
| **Countdown** iterator class | `__iter__`, `__next__`, `StopIteration` |
| **Fibonacci** generator | infinite generator, `yield`, `next()` |
| **`@timer`** and **`@retry(times=3)`** | decorators, `*args/**kwargs`, `@wraps` |
| **Timer** and **announce()** | class and generator context managers |
| **Async downloads** | `async`, `await`, `asyncio.gather` |

---

## 📅 Day 7 · 🛠️ Week 1 Project: Expense Tracker

**Date:** Nov 7, 2026
**Code:** [`Day 07 - Expense Tracker Project/`](./Day%2007%20-%20Expense%20Tracker%20Project/)

### What it does

A command-line app to add, list and delete expenses, see a summary by category and this month's total. Data is saved to `expenses.json` automatically.

### How the code is organised

| Part | What it is | Week 1 concept |
|---|---|---|
| `ExpenseError` + 2 subclasses | My own errors | Day 4: custom exceptions |
| `Expense` | One expense, checks itself in `__post_init__` | Day 5: dataclasses |
| `ExpenseTracker` | Holds all expenses, saves and loads, makes reports | Day 5: classes, `__len__` |
| `@autosave` | Saves to disk after every change | Day 6: decorators |
| `safe_json_file()` | Returns `[]` if the file is missing or broken | Day 6: context managers |
| `in_month()` | Expenses from one month, one at a time | Day 6: generators |
| `main()` | Menu loop | Days 1–3: input, loops, functions |

### Testing with pytest

| Idea | Meaning |
|---|---|
| `def test_...()` | pytest finds and runs every function that starts with `test_` |
| `assert` | Fails the test if the condition is false |
| `pytest.raises(Error)` | Passes only if that error happens |
| `tmp_path` | A fresh temporary folder for each test, so my real data is never touched |

```bash
python -m pytest -v      # 9 passed ✅
```

### What I learned

- Splitting code into small classes and functions made it easy to test each piece.
- Validating data in one place (`Expense`) means bad data can't get in anywhere else.
- Tests caught problems faster than running the menu by hand.

---

# ✅ Week 1 complete
