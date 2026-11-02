"""
Day 02 · Control flow & data structures
if/elif/else, loops, lists, tuples, dicts, sets, comprehensions
"""

# ------------------------------------------------------------
# Part 0: concept practice
# ------------------------------------------------------------
print("--- if / elif / else ---")
temperature = 34
if temperature >= 35:
    print("Very hot, stay inside")
elif temperature >= 25:
    print("Warm day")
else:
    print("Pleasant weather")

# and / or / not
is_weekend = True
has_work = False
if is_weekend and not has_work:
    print("Free day!")

print("\n--- for loops ---")
for i in range(1, 6):          # 1, 2, 3, 4, 5
    print(i, end=" ")
print()

for i in range(10, 0, -3):     # start, stop, step: 10, 7, 4, 1
    print(i, end=" ")
print()

print("\n--- while loop, break, continue ---")
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue               # skip even numbers
    if count > 7:
        break                  # stop the loop completely
    print(count, end=" ")      # 1 3 5 7
print()

print("\n--- Lists (ordered, changeable) ---")
fruits = ["mango", "apple", "banana"]
fruits.append("orange")        # add to the end
fruits.insert(0, "grapes")     # add at a position
fruits.remove("apple")         # remove by value
last = fruits.pop()            # remove and return the last item
print(fruits, "| popped:", last)
print(fruits[0], fruits[-1], fruits[1:3])
print(len(fruits), "mango" in fruits)
print(sorted(fruits))          # new sorted list, original unchanged

for index, fruit in enumerate(fruits):
    print(index, fruit)

print("\n--- Tuples (ordered, NOT changeable) ---")
point = (24.86, 67.01)         # e.g. latitude, longitude of Karachi
lat, lon = point               # unpacking
print(f"lat={lat}, lon={lon}")

print("\n--- Dictionaries (key -> value) ---")
student = {"name": "Ali", "age": 21, "city": "Lahore"}
student["age"] = 22                     # update
student["course"] = "AI"                # add
print(student["name"])
print(student.get("email", "no email")) # safe lookup with default
for key, value in student.items():
    print(f"{key}: {value}")

print("\n--- Sets (unique, unordered) ---")
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(a | b)   # union        {1, 2, 3, 4, 5}
print(a & b)   # intersection {3, 4}
print(a - b)   # difference   {1, 2}
print(set([1, 1, 2, 2, 3]))   # removes duplicates -> {1, 2, 3}

print("\n--- Comprehensions ---")
squares = [n ** 2 for n in range(1, 6)]
evens = [n for n in range(1, 11) if n % 2 == 0]
word_lengths = {w: len(w) for w in ["python", "ai", "code"]}
unique_letters = {ch for ch in "banana"}
print(squares, evens, word_lengths, unique_letters)


# ------------------------------------------------------------
# Script 1: Grade calculator
# ------------------------------------------------------------
print("\n--- Script 1: Grade calculator ---")

marks = {"Maths": 88, "Physics": 72, "English": 91, "Programming": 95, "Chemistry": 64}

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"

for subject, score in marks.items():
    print(f"{subject:<12} {score:>3}  {grade(score)}")

average = sum(marks.values()) / len(marks)
best = max(marks, key=marks.get)
print(f"Average: {average:.1f} ({grade(average)}) | Best subject: {best}")


# ------------------------------------------------------------
# Script 2: Shopping list manager (menu loop)
# ------------------------------------------------------------
print("\n--- Script 2: Shopping list ---")

shopping = []
while True:
    choice = input("\n[a]dd  [r]emove  [s]how  [q]uit: ").strip().lower()
    if choice == "a":
        item = input("Item: ").strip().lower()
        if item in shopping:
            print(f"'{item}' is already on the list")
        else:
            shopping.append(item)
            print(f"Added '{item}'")
    elif choice == "r":
        item = input("Item to remove: ").strip().lower()
        if item in shopping:
            shopping.remove(item)
            print(f"Removed '{item}'")
        else:
            print("Not on the list")
    elif choice == "s":
        if not shopping:
            print("List is empty")
        for i, item in enumerate(sorted(shopping), start=1):
            print(f"{i}. {item}")
    elif choice == "q":
        print(f"Bye! {len(shopping)} item(s) on your list.")
        break
    else:
        print("Please choose a, r, s or q")


# ------------------------------------------------------------
# Script 3: Word frequency counter
# ------------------------------------------------------------
print("\n--- Script 3: Word frequency ---")

text = input("Paste a paragraph: ").lower()

# keep only letters and spaces
clean = "".join(ch for ch in text if ch.isalpha() or ch == " ")
words = clean.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

top = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)[:5]

print(f"Total words: {len(words)} | Unique words: {len(set(words))}")
print("Top 5 words:")
for word, n in top:
    print(f"  {word:<10} {'*' * n} ({n})")