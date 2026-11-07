"""
Day 05 · Object-oriented programming
classes, __init__, methods, inheritance, composition, dataclasses, dunder methods
"""
from dataclasses import dataclass, field

# ------------------------------------------------------------
# Part 0: concept practice
# ------------------------------------------------------------
print("--- A class and its objects ---")


class Dog:
    species = "Canis familiaris"        # class attribute: shared by all dogs

    def __init__(self, name: str, age: int):
        self.name = name                # instance attributes: each dog has its own
        self.age = age

    def bark(self) -> str:              # method: a function that belongs to the class
        return f"{self.name} says Woof!"

    def birthday(self) -> None:
        self.age += 1


tommy = Dog("Tommy", 3)
bruno = Dog("Bruno", 5)
print(tommy.bark(), "|", bruno.bark())
tommy.birthday()
print(tommy.name, tommy.age, tommy.species)


print("\n--- Dunder (double underscore) methods ---")


class Money:
    def __init__(self, amount: float):
        self.amount = amount

    def __str__(self) -> str:           # used by print()
        return f"Rs {self.amount:,.0f}"

    def __repr__(self) -> str:          # used in lists / the debugger
        return f"Money({self.amount})"

    def __add__(self, other: "Money") -> "Money":   # makes + work
        return Money(self.amount + other.amount)

    def __eq__(self, other: object) -> bool:        # makes == work
        return isinstance(other, Money) and self.amount == other.amount

    def __lt__(self, other: "Money") -> bool:       # makes < and sorted() work
        return self.amount < other.amount


a, b = Money(1500), Money(2500)
print(a + b, a == Money(1500), a < b)
print(sorted([b, a]))


print("\n--- Inheritance ---")


class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "..."

    def introduce(self) -> str:
        return f"I'm {self.name} and I say {self.speak()}"


class Cat(Animal):                      # Cat IS AN Animal
    def speak(self) -> str:             # override the parent method
        return "Meow"


class Parrot(Animal):
    def __init__(self, name: str, words: list):
        super().__init__(name)          # run the parent's __init__ first
        self.words = words

    def speak(self) -> str:
        return ", ".join(self.words)


for pet in [Cat("Mano"), Parrot("Mithu", ["Hello", "Salam"])]:
    print(pet.introduce())              # same call, different behaviour (polymorphism)

print(isinstance(Cat("x"), Animal))     # True


print("\n--- Encapsulation: properties ---")


class Thermostat:
    def __init__(self, celsius: float):
        self._celsius = celsius         # _ means "internal, don't touch directly"

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32


t = Thermostat(25)
t.celsius = 30                          # goes through the setter (validated)
print(t.celsius, t.fahrenheit)


print("\n--- Class methods and static methods ---")


class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f: float) -> "Temperature":   # another way to create one
        return cls((f - 32) * 5 / 9)

    @staticmethod
    def is_fever(celsius: float) -> bool:                   # related helper, no self needed
        return celsius >= 38


print(round(Temperature.from_fahrenheit(98.6).celsius, 1), Temperature.is_fever(38.5))


print("\n--- Dataclasses: less typing for data-holding classes ---")


@dataclass
class Book:
    title: str
    author: str
    pages: int
    tags: list = field(default_factory=list)   # mutable default done safely

    def is_long(self) -> bool:
        return self.pages > 400


book = Book("Atomic Habits", "James Clear", 320, ["habits"])
print(book)                                    # __repr__ is generated for me
print(book == Book("Atomic Habits", "James Clear", 320, ["habits"]))  # __eq__ too
print(book.is_long())


# ------------------------------------------------------------
# Script 1: Bank account system (encapsulation + inheritance)
# ------------------------------------------------------------
print("\n--- Script 1: Bank accounts ---")


class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self._balance = balance
        self.history = []

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self.history.append(("withdraw", amount))

    def __str__(self) -> str:
        return f"{self.owner}: Rs {self._balance:,.0f}"


class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: float = 0, rate: float = 0.05):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self) -> None:
        interest = self._balance * self.rate
        self.deposit(interest)


acc = BankAccount("Hafsa", 10000)
acc.deposit(2500)
try:
    acc.withdraw(50000)
except ValueError as err:
    print("Error:", err)
acc.withdraw(3000)

savings = SavingsAccount("Sara", 20000, rate=0.1)
savings.add_interest()

print(acc, "| history:", acc.history)
print(savings)


# ------------------------------------------------------------
# Script 2: Library (composition: a Library HAS Books)
# ------------------------------------------------------------
print("\n--- Script 2: Library ---")


@dataclass
class Member:
    name: str
    borrowed: list = field(default_factory=list)


class Library:
    def __init__(self):
        self.books = {}                 # title -> Book
        self.available = set()

    def add(self, book: Book) -> None:
        self.books[book.title] = book
        self.available.add(book.title)

    def lend(self, title: str, member: Member) -> str:
        if title not in self.books:
            return f"'{title}' is not in the library"
        if title not in self.available:
            return f"'{title}' is already borrowed"
        self.available.remove(title)
        member.borrowed.append(title)
        return f"{member.name} borrowed '{title}'"

    def give_back(self, title: str, member: Member) -> str:
        member.borrowed.remove(title)
        self.available.add(title)
        return f"{member.name} returned '{title}'"

    def __len__(self) -> int:           # makes len(library) work
        return len(self.books)


lib = Library()
lib.add(Book("Atomic Habits", "James Clear", 320))
lib.add(Book("Deep Work", "Cal Newport", 304))
lib.add(Book("Clean Code", "Robert Martin", 464))

ali = Member("Ali")
print(lib.lend("Deep Work", ali))
print(lib.lend("Deep Work", Member("Sara")))
print(lib.lend("Dune", ali))
print(lib.give_back("Deep Work", ali))
print(f"{len(lib)} books, available: {sorted(lib.available)}")


# ------------------------------------------------------------
# Script 3: Shapes (polymorphism + sorting with dunder methods)
# ------------------------------------------------------------
print("\n--- Script 3: Shapes ---")
import math


class Shape:
    def area(self) -> float:
        raise NotImplementedError("Every shape must define area()")

    def __lt__(self, other: "Shape") -> bool:
        return self.area() < other.area()

    def __str__(self) -> str:
        return f"{type(self).__name__:<9} area = {self.area():7.2f}"


class Circle(Shape):
    def __init__(self, r: float):
        self.r = r

    def area(self) -> float:
        return math.pi * self.r ** 2


class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w, self.h = w, h

    def area(self) -> float:
        return self.w * self.h


class Square(Rectangle):                # a Square IS A Rectangle with equal sides
    def __init__(self, side: float):
        super().__init__(side, side)


shapes = [Circle(3), Rectangle(4, 6), Square(5), Circle(1.5)]
for s in sorted(shapes, reverse=True):
    print(s)
print("Total area:", round(sum(s.area() for s in shapes), 2))
