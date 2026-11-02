# 📝 Week 1 · Python from the Basics

> My notes, in my own words. One section per day.

**Days this week:**
[Day 1](#-day-1--variables-types-inputoutput-strings) ·
Day 2 · Day 3 · Day 4 · Day 5 · Day 6 · Day 7

---

## 📅 Day 1 · Variables, Types, Input/Output, Strings

**Date:** Nov 2, 2026
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

_Coming next: if/elif/else, loops, lists, tuples, dicts, sets, comprehensions._