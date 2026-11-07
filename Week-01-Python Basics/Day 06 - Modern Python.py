"""
Day 06 · Modern Python
type hints, iterators & generators, decorators, context managers, async/await
"""
import asyncio
import time
from contextlib import contextmanager
from functools import wraps
from typing import Iterator, Optional

# ------------------------------------------------------------
# 1. Type hints
# ------------------------------------------------------------
print("--- Type hints ---")


def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)


def find_user(users: dict[str, int], name: str) -> Optional[int]:
    """Returns the age, or None if the user isn't there."""
    return users.get(name)


def describe(value: int | str) -> str:          # either an int or a str
    return f"{value!r} is a {type(value).__name__}"


print(average([3.5, 4.0, 5.5]))
print(find_user({"ali": 22}, "sara"))
print(describe(7), "|", describe("seven"))
# Hints don't stop wrong types at runtime; tools like mypy and VS Code use them to warn me.


# ------------------------------------------------------------
# 2. Iterators
# ------------------------------------------------------------
print("\n--- Iterators: what a for loop really does ---")
letters = iter(["a", "b", "c"])
print(next(letters), next(letters), next(letters))
try:
    next(letters)
except StopIteration:
    print("StopIteration: nothing left")


class Countdown:
    """My own iterable: for n in Countdown(3) gives 3, 2, 1."""

    def __init__(self, start: int):
        self.current = start

    def __iter__(self) -> "Countdown":
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


print(list(Countdown(5)))


# ------------------------------------------------------------
# 3. Generators: iterators the easy way, with yield
# ------------------------------------------------------------
print("\n--- Generators ---")


def countdown(start: int) -> Iterator[int]:
    while start > 0:
        yield start          # pause here, hand back a value, continue next time
        start -= 1


print(list(countdown(5)))


def fibonacci() -> Iterator[int]:
    a, b = 0, 1
    while True:              # infinite, but only computes what I ask for
        yield a
        a, b = b, a + b


fib = fibonacci()
print([next(fib) for _ in range(10)])

# Generator expression: like a list comprehension, but lazy
squares_list = [n * n for n in range(1_000_000)]   # builds all 1M now
squares_gen = (n * n for n in range(1_000_000))    # builds one at a time
print(sum(squares_gen))
import sys
print("list size:", sys.getsizeof(squares_list), "bytes | generator:", sys.getsizeof((n for n in range(10))), "bytes")


def read_big_file(lines: list[str]) -> Iterator[str]:
    """Pipeline step: only keep non-empty lines, one at a time."""
    for line in lines:
        if line.strip():
            yield line.strip().upper()


for row in read_big_file(["first", "", "second", "  ", "third"]):
    print(row)


# ------------------------------------------------------------
# 4. Decorators: wrap a function to add behaviour
# ------------------------------------------------------------
print("\n--- Decorators ---")


def timer(func):
    @wraps(func)                         # keeps the original name and docstring
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"[timer] {func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper


def retry(times: int):
    """Decorator WITH an argument: a function that returns a decorator."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except ValueError as err:
                    print(f"[retry] attempt {attempt} failed: {err}")
            raise RuntimeError(f"{func.__name__} failed {times} times")
        return wrapper
    return decorator


@timer
def slow_sum(n: int) -> int:
    return sum(range(n))


print(slow_sum(2_000_000))

calls = {"count": 0}


@retry(times=3)
def flaky_api() -> str:
    calls["count"] += 1
    if calls["count"] < 3:
        raise ValueError("server busy")
    return "success on call 3"


print(flaky_api())
print(slow_sum.__name__)      # still "slow_sum" thanks to @wraps


# ------------------------------------------------------------
# 5. Context managers: set up, then always clean up
# ------------------------------------------------------------
print("\n--- Context managers ---")


class Timer:
    """Class-based: __enter__ runs at the start, __exit__ always runs at the end."""

    def __enter__(self) -> "Timer":
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        self.elapsed = time.perf_counter() - self.start
        print(f"[Timer] block took {self.elapsed:.4f}s")
        return False          # False = don't hide errors


with Timer():
    sum(range(1_000_000))


@contextmanager
def announce(task: str):
    """Generator-based: code before yield = setup, after yield = cleanup."""
    print(f"▶ starting {task}")
    try:
        yield
    finally:
        print(f"■ finished {task}")


with announce("backup"):
    print("  copying files...")

try:
    with announce("risky job"):
        raise ValueError("something broke")
except ValueError:
    print("  (error was caught, but cleanup still ran)")


# ------------------------------------------------------------
# 6. async / await: doing many waiting tasks at the same time
# ------------------------------------------------------------
print("\n--- async / await ---")


async def download(name: str, seconds: float) -> str:
    print(f"  start {name}")
    await asyncio.sleep(seconds)      # waiting (like a network call), not blocking
    print(f"  done  {name}")
    return f"{name} ({seconds}s)"


async def main() -> None:
    start = time.perf_counter()
    results = await asyncio.gather(
        download("page A", 1.0),
        download("page B", 1.0),
        download("page C", 1.0),
    )
    print(results)
    print(f"3 downloads of 1s each took {time.perf_counter() - start:.1f}s total (not 3s!)")


asyncio.run(main())
