"""
Day 03 · Functions, scope, lambdas, modules & imports
"""

# ------------------------------------------------------------
# Part 0: concept practice
# ------------------------------------------------------------
print("--- Defining and calling functions ---")


def greet(name):
    """A docstring explains what the function does."""
    return f"Hello, {name}!"


print(greet("Hafsa"))
print(greet.__doc__)


print("\n--- Default arguments ---")


def power(base, exponent=2):
    return base ** exponent


print(power(5))       # 25, uses the default exponent
print(power(2, 10))   # 1024


print("\n--- Keyword arguments (order doesn't matter) ---")


def describe(name, city, role):
    return f"{name} from {city} works as {role}"


print(describe(role="AI Engineer", name="Sara", city="Karachi"))


print("\n--- Returning more than one value ---")


def min_max(numbers):
    return min(numbers), max(numbers)   # returns a tuple


low, high = min_max([4, 9, 1, 7])
print(f"min={low}, max={high}")


print("\n--- *args: any number of positional arguments ---")


def total(*args):
    print("args is a tuple:", args)
    return sum(args)


print(total(1, 2, 3, 4))


print("\n--- **kwargs: any number of keyword arguments ---")


def profile(**kwargs):
    print("kwargs is a dict:", kwargs)
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


profile(name="Ali", age=22, skill="Python")


print("\n--- Scope: local vs global ---")
counter = 0            # global variable


def show_scope():
    counter = 100      # local: a new variable that only exists inside
    print("inside:", counter)


show_scope()
print("outside:", counter)   # still 0


def increase():
    global counter     # now we change the global one (use rarely)
    counter += 1


increase()
print("after increase():", counter)


print("\n--- Functions are values ---")


def shout(text):
    return text.upper() + "!"


def apply(func, value):
    return func(value)


print(apply(shout, "python"))


print("\n--- Lambdas: tiny one-line functions ---")
square = lambda x: x ** 2
print(square(6))

students = [("Ali", 72), ("Sara", 91), ("Omar", 85)]
by_marks = sorted(students, key=lambda s: s[1], reverse=True)
print(by_marks)

numbers = [1, 2, 3, 4, 5, 6]
print(list(map(lambda n: n * 10, numbers)))        # transform each
print(list(filter(lambda n: n % 2 == 0, numbers)))  # keep some


print("\n--- Importing modules ---")
import math                      # whole module
from random import randint, choice   # only some names
import datetime as dt            # with a short alias

print(math.sqrt(144), math.pi)
print(randint(1, 6), choice(["red", "green", "blue"]))
print(dt.date.today())

# My own module (text_tools.py in the same folder)
import text_tools

print(text_tools.word_count("Functions make code reusable"))
print(text_tools.slugify("Day 3: Functions & Modules"))


# ------------------------------------------------------------
# Script 1: Unit converter (functions + a dictionary of functions)
# ------------------------------------------------------------
print("\n--- Script 1: Unit converter ---")


def km_to_miles(km: float) -> float:
    return km * 0.621371


def celsius_to_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32


def kg_to_pounds(kg: float) -> float:
    return kg * 2.20462


converters = {
    "1": ("km -> miles", km_to_miles),
    "2": ("°C -> °F", celsius_to_fahrenheit),
    "3": ("kg -> lb", kg_to_pounds),
}

for key, (label, _) in converters.items():
    print(f"{key}. {label}")

choice_key = input("Choose 1, 2 or 3: ").strip()
if choice_key in converters:
    label, func = converters[choice_key]
    value = float(input("Value: "))
    print(f"{label}: {value} -> {func(value):.2f}")
else:
    print("Unknown choice")


# ------------------------------------------------------------
# Script 2: Password checker (small functions that each do one job)
# ------------------------------------------------------------
print("\n--- Script 2: Password checker ---")


def has_upper(pw: str) -> bool:
    return any(ch.isupper() for ch in pw)


def has_digit(pw: str) -> bool:
    return any(ch.isdigit() for ch in pw)


def has_symbol(pw: str) -> bool:
    return any(not ch.isalnum() for ch in pw)


def password_strength(pw: str) -> str:
    score = sum([len(pw) >= 8, has_upper(pw), has_digit(pw), has_symbol(pw)])
    return ["Very weak", "Weak", "Okay", "Good", "Strong"][score]


password = input("Enter a test password: ")
print(f"Strength: {password_strength(password)}")


# ------------------------------------------------------------
# Script 3: Text report using my own module
# ------------------------------------------------------------
print("\n--- Script 3: Text report (uses text_tools.py) ---")


def text_report(text: str, **options) -> None:
    """Print a report. Options: show_slug=True, show_vowels=True"""
    print(f"Words: {text_tools.word_count(text)}")
    print(f"Palindrome: {text_tools.is_palindrome(text)}")
    if options.get("show_vowels", True):
        print(f"Vowels: {text_tools.count_vowels(text)}")
    if options.get("show_slug", False):
        print(f"Slug: {text_tools.slugify(text)}")


sentence = input("Type a sentence: ")
text_report(sentence, show_slug=True)
