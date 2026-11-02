"""
Day 001 · Python basics: variables, types, input/output, strings
"""

# ------------------------------------------------------------
# Part 0: concept practice
# ------------------------------------------------------------
print("--- Concept practice ---")

city = "Karachi"        # str: text
year = 2026             # int: whole number
temperature = 31.5      # float: decimal number
is_weekend = False      # bool: True or False
plan = None             # None: no value yet

print(type(city), type(year), type(temperature), type(is_weekend), type(plan))
print(f"It's {temperature}°C in {city} in {year}. Weekend: {is_weekend}")

# Type conversion: input() always gives text
age_text = "21"
age = int(age_text)
print(age + 1)            # 22
print(str(year) + "!")    # "2026!": joining text needs str()
print(float("3.5") * 2)   # 7.0

# Strings
quote = "   Learning Python one day at a time   "
print(quote.strip())             # removes outer spaces
print(quote.upper())             # UPPERCASE
print(quote.lower())             # lowercase
print(quote.strip().title())     # Every Word Capitalised
print(quote.split())             # list of words
print(len(quote.strip()))        # character count
print(quote.strip()[0:8])        # slicing: "Learning"
print(quote.strip()[-4:])        # last 4 characters: "time"
print("python" in quote.lower()) # True
print(quote.strip().replace("Python", "AI"))
print(quote.count("e"))          # how many times "e" appears

# Maths operators
print(17 / 5)    # 3.4  normal division
print(17 // 5)   # 3    whole-number division
print(17 % 5)    # 2    remainder
print(2 ** 10)   # 1024 power
print(round(22 / 7, 3))  # 3.143


# ------------------------------------------------------------
# Script 1: Personal profile card
# ------------------------------------------------------------
print("\n--- Script 1: Profile card ---")

name = input("Your name: ").strip().title()
birth_year = int(input("Birth year: "))
hobby = input("Favourite hobby: ").strip().lower()

age = 2026 - birth_year

print("+" + "-" * 30 + "+")
print(f"  Name : {name}")
print(f"  Age  : {age}")
print(f"  Loves: {hobby}")
print(f"  Initials: {name[0]}")
print("+" + "-" * 30 + "+")


# ------------------------------------------------------------
# Script 2: Bill splitter with tip
# ------------------------------------------------------------
print("\n--- Script 2: Bill splitter ---")

bill = float(input("Total bill (Rs): "))
tip_percent = float(input("Tip % (e.g. 10): "))
people = int(input("Number of people: "))

tip = bill * tip_percent / 100
total = bill + tip
per_person = total / people

print(f"Tip: Rs {tip:.2f}")
print(f"Total with tip: Rs {total:.2f}")
print(f"Each person pays: Rs {per_person:.2f}")


# ------------------------------------------------------------
# Script 3: Text analyser
# ------------------------------------------------------------
print("\n--- Script 3: Text analyser ---")

text = input("Type a sentence: ")
clean = text.strip()
words = clean.split()

print(f"Characters (with spaces): {len(clean)}")
print(f"Characters (no spaces):   {len(clean.replace(' ', ''))}")
print(f"Words: {len(words)}")
print(f"First word: {words[0]}")
print(f"Last word:  {words[-1]}")
print(f"Shouting:   {clean.upper()}")
print(f"Reversed:   {clean[::-1]}")

if clean.lower() == clean.lower()[::-1]:
    print("Fun fact: that's a palindrome!")