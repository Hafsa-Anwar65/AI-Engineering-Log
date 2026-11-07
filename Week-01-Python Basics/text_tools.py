"""
text_tools.py · my first Python module (Day 03)
Any .py file is a module: other files can import its functions.
"""

VOWELS = "aeiou"


def word_count(text: str) -> int:
    """Return the number of words in text."""
    return len(text.split())


def count_vowels(text: str) -> int:
    """Return how many vowels are in text."""
    return sum(1 for ch in text.lower() if ch in VOWELS)


def is_palindrome(text: str) -> bool:
    """True if text reads the same backwards (ignores spaces and case)."""
    clean = "".join(ch for ch in text.lower() if ch.isalnum())
    return clean == clean[::-1]


def slugify(text: str) -> str:
    """Turn 'Hello World!' into 'hello-world'."""
    words = "".join(ch if ch.isalnum() else " " for ch in text.lower()).split()
    return "-".join(words)


# This block only runs when I run this file directly,
# not when another file imports it.
if __name__ == "__main__":
    print(word_count("one two three"))      # 3
    print(is_palindrome("Never odd or even"))  # True
    print(slugify("Hello World! Day 3"))    # hello-world-day-3
