# 📝 Week 1 · Python from the Basics

> My notes, in my own words. One section per day.

**Days this week:**
[Day 1](#-day-1--variables-types-inputoutput-strings) ·
Day 2 · Day 3 · Day 4 · Day 5 · Day 6 · Day 7

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
