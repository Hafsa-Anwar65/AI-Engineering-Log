# 📝 Week 2 · NumPy, Pandas & the Math You Actually Use

> My notes, in my own words. One section per day.

**Days this week:**  
[Day 8](#-day-8--review-week-1--numpy-arrays) ·  
[Day 9](#-day-9--numpy-broadcasting--vectorisation) ·  
[Day 10](#-day-10--pandas-csvs-filtering--data-cleaning) ·  
[Day 11](#-day-11--linear-algebra) ·  
[Day 12](#-day-12--derivatives-chain-rule-gradients--probability) ·  
[Day 13](#-day-13--loss-functions-mse--gradient-descent) ·  
[Day 14](#-day-14--week-2-project-linear-regression-from-scratch)

---

## 📅 Day 8 · Review Week 1 + NumPy Arrays

**Date:** Nov 8, 2026  
**Code:** [`Day 08 - NumPy Arrays.py`](./Day%2008%20-%20NumPy%20Arrays.py)

### 1. What is NumPy?

**NumPy** stands for **Numerical Python**.

It helps me work efficiently with:

- Numbers
- Large arrays
- Matrices
- Mathematical operations
- Data used in Machine Learning

```python
import numpy as np
```

The `np` name is just a short alias for NumPy.

---

### 2. NumPy Arrays

A NumPy array is similar to a Python list, but it is designed for fast numerical operations.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
```

### Python list vs NumPy array

| Python List | NumPy Array |
|---|---|
| General-purpose | Mainly numerical data |
| Slower for large calculations | Faster for numerical calculations |
| Cannot directly multiply every item easily | Supports vectorized operations |
| `[1, 2] * 2` repeats the list | `array * 2` multiplies values |

Example:

```python
numbers = np.array([1, 2, 3])

print(numbers * 2)
```

Output:

```text
[2 4 6]
```

---

### 3. `dtype`

`dtype` tells me what type of data the NumPy array contains.

```python
arr = np.array([1, 2, 3])

print(arr.dtype)
```

Usually this will show an integer type.

With decimal values:

```python
arr = np.array([1.5, 2.5, 3.5])

print(arr.dtype)
```

---

### 4. `shape`

`shape` tells me the dimensions of an array.

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.shape)
```

Output:

```text
(2, 3)
```

This means:

- 2 rows
- 3 columns

---

### 5. `reshape()`

`reshape()` changes the structure of an array without changing its values.

```python
arr = np.array([1, 2, 3, 4, 5, 6])

matrix = arr.reshape(2, 3)

print(matrix)
```

Output:

```text
[[1 2 3]
 [4 5 6]]
```

The total number of elements must stay the same.

For example:

- 6 elements → `(2, 3)` ✅
- 6 elements → `(3, 2)` ✅
- 6 elements → `(2, 4)` ❌

---

### 6. Indexing

NumPy indexing works similarly to Python lists.

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])   # First element
print(arr[-1])  # Last element
```

---

### 7. 2D Array Indexing

For a matrix:

```python
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

I can access values using:

```python
print(matrix[0, 1])
```

Output:

```text
20
```

The format is:

```text
matrix[row, column]
```

---

### 🛠️ What I Practised

| Concept | What I did |
|---|---|
| Arrays | Created 1D and 2D arrays |
| `dtype` | Checked data types |
| `shape` | Checked rows and columns |
| `reshape()` | Converted a 1D array into a matrix |
| Indexing | Accessed individual values |

---

## 📅 Day 9 · NumPy Broadcasting & Vectorisation

**Date:** Nov 9, 2026  
**Code:** [`Day 09 - Broadcasting and Vectorization.py`](./Day%2009%20-%20Broadcasting%20and%20Vectorization.py)

### 1. Vectorisation

**Vectorisation** means performing an operation on an entire array at once instead of manually looping through every value.

### Using a Python loop

```python
numbers = [1, 2, 3, 4, 5]

result = []

for num in numbers:
    result.append(num * 2)

print(result)
```

### Using NumPy

```python
numbers = np.array([1, 2, 3, 4, 5])

result = numbers * 2

print(result)
```

Both give:

```text
[2 4 6 8 10]
```

But NumPy is generally much more efficient for large numerical datasets.

---

### 2. Element-wise Operations

NumPy applies operations to every element.

```python
arr = np.array([1, 2, 3, 4])

print(arr + 10)
print(arr * 2)
print(arr ** 2)
```

Output:

```text
[11 12 13 14]

[2 4 6 8]

[ 1  4  9 16]
```

This is useful in Machine Learning because datasets often contain thousands or millions of values.

---

### 3. Broadcasting

**Broadcasting** allows NumPy to perform operations between arrays of different shapes when their dimensions are compatible.

Example:

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([10, 20, 30])

print(matrix + vector)
```

Output:

```text
[[11 22 33]
 [14 25 36]]
```

NumPy applies the vector to each row.

---

### 4. Why Vectorisation Matters in AI

Instead of calculating:

```text
one value → then another → then another
```

I can perform:

```text
an operation on the whole dataset at once
```

This is important for:

- Machine Learning datasets
- Image processing
- Neural networks
- Matrix operations
- Large-scale calculations

---

### 🛠️ What I Practised

| Concept | What I did |
|---|---|
| Vectorisation | Multiplied an entire array at once |
| Element-wise operations | Added, multiplied and squared arrays |
| Broadcasting | Added a vector to every matrix row |
| Loops vs NumPy | Compared manual loops with vectorised operations |

---

## 📅 Day 10 · Pandas: CSVs, Filtering & Data Cleaning

**Date:** Nov 10, 2026  
**Code:** [`Day 10 - Pandas.py`](./Day%2010%20-%20Pandas.py)

### 1. What is Pandas?

**Pandas** is a Python library used for working with structured data.

It is useful for:

- CSV files
- Tables
- Data cleaning
- Filtering
- Grouping
- Data analysis

```python
import pandas as pd
```

---

### 2. DataFrame

A **DataFrame** is like a table with rows and columns.

```python
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Hafsa"],
    "Age": [20, 22, 21, 23],
    "Score": [85, 90, 78, 95]
}

df = pd.DataFrame(data)

print(df)
```

---

### 3. Reading a CSV

```python
df = pd.read_csv("data.csv")

print(df.head())
```

`head()` shows the first 5 rows by default.

Useful commands:

| Command | What it does |
|---|---|
| `df.head()` | Shows first rows |
| `df.tail()` | Shows last rows |
| `df.shape` | Shows rows and columns |
| `df.columns` | Shows column names |
| `df.info()` | Shows data information |

---

### 4. Filtering Data

I can select rows based on a condition.

```python
filtered = df[df["Score"] > 85]

print(filtered)
```

Multiple conditions:

```python
filtered = df[
    (df["Score"] > 80) &
    (df["Age"] > 20)
]
```

---

### 5. Missing Values

Missing values are often represented as:

```text
NaN
```

I can check them using:

```python
df.isnull()
```

To count missing values:

```python
df.isnull().sum()
```

---

### 6. Filling Missing Values

```python
df["Score"] = df["Score"].fillna(0)
```

This replaces missing values with `0`.

---

### 7. GroupBy

`groupby()` allows me to group data and perform calculations.

```python
data = {
    "Department": ["AI", "AI", "Web", "Web"],
    "Salary": [50000, 60000, 40000, 45000]
}

df = pd.DataFrame(data)

result = df.groupby("Department")["Salary"].mean()

print(result)
```

This calculates the average salary for each department.

---

### 8. Merging Data

Pandas can combine tables using common columns.

Conceptually:

```python
pd.merge(table1, table2, on="id")
```

This is useful when related information is stored in different datasets.

---

### 🛠️ What I Practised

| Concept | What I did |
|---|---|
| DataFrames | Created tabular data |
| CSVs | Learned how to load CSV files |
| Filtering | Selected rows based on conditions |
| Missing values | Detected and filled missing data |
| `groupby()` | Calculated grouped averages |

---

## 📅 Day 11 · Linear Algebra

**Date:** Nov 11, 2026  
**Code:** [`Day 11 - Linear Algebra.py`](./Day%2011%20-%20Linear%20Algebra.py)

### 1. Vectors

A **vector** is an ordered collection of numbers.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

I can add vectors:

```python
print(a + b)
```

Output:

```text
[5 7 9]
```

---

### 2. Dot Product

The dot product multiplies corresponding values and then adds them.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.dot(a, b)

print(result)
```

Calculation:

```text
(1 × 4) + (2 × 5) + (3 × 6)

= 4 + 10 + 18

= 32
```

The dot product is important in:

- Machine Learning
- Neural networks
- Linear regression
- Similarity calculations

---

### 3. Matrices

A **matrix** is a rectangular arrangement of numbers.

```python
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])
```

---

### 4. Matrix Multiplication

```python
result = A @ B

print(result)
```

I can also use:

```python
np.dot(A, B)
```

> ⚠️ Matrix multiplication is different from normal element-by-element multiplication.

Matrix multiplication is one of the core mathematical operations behind Machine Learning models and neural networks.

---

### 🛠️ What I Practised

| Concept | What I did |
|---|---|
| Vectors | Created and added vectors |
| Dot product | Calculated weighted multiplication |
| Matrices | Created 2D numerical structures |
| Matrix multiplication | Used `@` and `np.dot()` |

---

## 📅 Day 12 · Derivatives, Chain Rule, Gradients & Probability

**Date:** Nov 12, 2026  
**Code:** [`Day 12 - Derivatives Gradients and Probability.py`](./Day%2012%20-%20Derivatives%20Gradients%20and%20Probability.py)

### 1. What is a Derivative?

A derivative tells me how quickly a function changes.

For:

```text
y = x²
```

The derivative is:

```text
dy/dx = 2x
```

At:

```text
x = 5
```

The derivative is:

```text
2 × 5 = 10
```

---

### 2. Numerical Derivative

I can approximately calculate a derivative using:

```python
def f(x):
    return x ** 2

x = 5
h = 0.0001

derivative = (f(x + h) - f(x)) / h

print(derivative)
```

This measures how much the function changes when `x` changes by a very small amount.

---

### 3. Gradients

For functions with multiple variables, I use a **gradient**.

Example:

```text
f(x, y) = x² + y²
```

The gradient is:

```text
[2x, 2y]
```

In Python:

```python
x = 3
y = 4

gradient = np.array([
    2 * x,
    2 * y
])
```

A gradient points in the direction of the greatest increase.

To minimise a loss function, Machine Learning algorithms move in the **opposite direction**.

---

### 4. Chain Rule

The chain rule is used when one function is inside another function.

Conceptually:

```text
If:

y = f(g(x))

Then:

dy/dx = f'(g(x)) × g'(x)
```

This becomes especially important in neural networks, where multiple mathematical operations are connected together.

---

### 5. Probability Basics

Probability tells me how likely something is to happen.

```text
Probability = Favorable Outcomes / Total Outcomes
```

Example:

```python
favorable = 3
total = 10

probability = favorable / total

print(probability)
```

Output:

```text
0.3
```

This means a probability of **30%**.

---

### 🛠️ What I Practised

| Concept | What I learned |
|---|---|
| Derivatives | How quickly a function changes |
| Numerical derivatives | Approximation using small changes |
| Gradients | Direction of change for multiple variables |
| Chain rule | Derivatives of connected functions |
| Probability | Calculating likelihood |

---

## 📅 Day 13 · Loss Functions (MSE) & Gradient Descent

**Date:** Nov 13, 2026  
**Code:** [`Day 13 - Loss Functions and Gradient Descent.py`](./Day%2013%20-%20Loss%20Functions%20and%20Gradient%20Descent.py)

### 1. What is a Loss Function?

A Machine Learning model makes predictions.

A **loss function** tells me how wrong those predictions are.

```text
Actual Value → What really happened

Predicted Value → What the model guessed

Loss → How wrong the prediction is
```

The goal of training is to **reduce the loss**.

---

### 2. Mean Squared Error (MSE)

MSE is a common loss function for regression.

```text
MSE = Average of (Actual - Predicted)²
```

In NumPy:

```python
actual = np.array([10, 20, 30])
predicted = np.array([12, 18, 29])

mse = np.mean((actual - predicted) ** 2)

print(mse)
```

### Why square the errors?

Squaring:

- Makes negative errors positive
- Gives bigger mistakes more importance
- Makes the result easier to optimise mathematically

---

### 3. Gradient Descent

**Gradient Descent** is an optimisation algorithm.

The basic idea:

```text
1. Start with a guess
        ↓
2. Calculate how wrong it is
        ↓
3. Calculate the gradient
        ↓
4. Move in the direction that reduces the loss
        ↓
5. Repeat
```

---

### 4. Simple Gradient Descent Example

For:

```text
f(x) = x²
```

The derivative is:

```text
2x
```

Python:

```python
x = 10
learning_rate = 0.1

for i in range(10):

    gradient = 2 * x

    x = x - learning_rate * gradient

    print("Step:", i + 1, "x:", x)
```

The value gradually moves closer to:

```text
x = 0
```

which is where `x²` is minimised.

---

### 5. Learning Rate

The learning rate controls the size of each step.

```text
Too small → Learning is slow

Too large → May overshoot the minimum

Good value → Learns efficiently
```

The update rule is:

```text
new_value = old_value - learning_rate × gradient
```

---

### 🛠️ What I Practised

| Concept | What I did |
|---|---|
| MSE | Calculated prediction error |
| Loss function | Measured how wrong predictions are |
| Gradient | Found the direction of change |
| Gradient descent | Updated values repeatedly |
| Learning rate | Controlled the step size |

---

## 📅 Day 14 · 🛠️ Week 2 Project: Linear Regression from Scratch

**Date:** Nov 14, 2026
**Code:** [`Day 14 - Linear Regression Project/`](./Day%2014%20-%20Linear%20Regression%20Project/)

### What I Built

A **Linear Regression model from scratch using only NumPy** (no scikit-learn), trained with **gradient descent**, plus 7 pytest tests.

| Demo | Predicts | Features | Test R² |
|---|---|---|:-:|
| Study hours → marks | Exam marks | 1 (hours) | **0.95** |
| House price | Price in lakh Rs | 3 (size, rooms, age) | **0.98** |

![Results](./Day%2014%20-%20Linear%20Regression%20Project/results.png)

### 1. The Model

```text
prediction = X @ w + b
```

| Symbol | Meaning |
|---|---|
| `X` | Input features (one row per example) |
| `w` | Weights: how much each feature matters |
| `b` | Bias: the starting value |

### 2. The Training Loop

Every epoch does 4 steps:

```python
y_pred = X @ w + b                       # 1. predict
loss = np.mean((y_pred - y) ** 2)        # 2. measure the error (MSE)
dw = (2 / n) * X.T @ (y_pred - y)        # 3. gradients: which way is uphill
db = (2 / n) * (y_pred - y).sum()
w -= learning_rate * dw                  # 4. take a step downhill
b -= learning_rate * db
```

### 3. Feature Scaling

House size is in the thousands while rooms are 1 to 5. Without scaling, one learning rate can't suit both, and training is slow or explodes.

```python
X_scaled = (X - mean) / std    # every feature ends up around 0 with similar spread
```

> 💡 With scaling, the study-hours model converged in **144 epochs**.

### 4. Measuring the Model

| Metric | Meaning | Good value |
|---|---|---|
| **MSE** | Average squared error | As low as possible |
| **R²** | How much of the variation the model explains | Close to 1.0 |

I split the data **80% train / 20% test** and report test scores, so the numbers show how the model does on data it hasn't seen.

### 5. Checking My Work

My gradient descent answer matched NumPy's exact least-squares answer (`np.polyfit`):

```text
My model:   marks = 34.06 + 6.11 * hours
np.polyfit: marks = 34.06 + 6.11 * hours
```

### 6. Tests (7 passed ✅)

| Test | Checks |
|---|---|
| Perfect line | Learns `y = 3x + 2` exactly |
| Matches NumPy | Same answer as `np.polyfit` |
| Multiple features | R² > 0.999 on 3 features |
| Loss goes down | Training actually improves |
| Predict before fit | Raises a clear error |
| Metrics | MSE and R² formulas |
| Train/test split | 80/20 sizes, no data lost |

---

## 📁 Week 2 Structure

```text
Week-02-NumPy Pandas Math/
├── Day 08 - NumPy Arrays.py
├── Day 09 - Broadcasting and Vectorization.py
├── Day 10 - Pandas.py
├── Day 11 - Linear Algebra.py
├── Day 12 - Derivatives Gradients and Probability.py
├── Day 13 - Loss Functions and Gradient Descent.py
├── Notes.md
└── Day 14 - Linear Regression Project/
    ├── linear_regression.py
    ├── test_linear_regression.py
    ├── results.png
    └── README.md
```

---

# 🎯 What I Learned This Week

This week connected **Python programming with the mathematical foundation of Machine Learning**.

I learned:

- How NumPy arrays work
- Why vectorisation is important
- How broadcasting works
- How to work with tabular data using Pandas
- How vectors and matrices are used in ML
- What derivatives and gradients mean
- How probability connects to data
- How loss functions measure prediction errors
- How Gradient Descent improves a model
- How to build Linear Regression from scratch using NumPy

### The biggest connection I learned:

```text
NumPy
   ↓
Mathematical Operations
   ↓
Vectors & Matrices
   ↓
Derivatives & Gradients
   ↓
Loss Function
   ↓
Gradient Descent
   ↓
Machine Learning Model
```

# ✅ Week 2 complete
