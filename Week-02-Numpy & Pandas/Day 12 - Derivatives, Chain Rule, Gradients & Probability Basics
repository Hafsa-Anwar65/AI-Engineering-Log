
"""
DAY 12: DERIVATIVES, CHAIN RULE, GRADIENTS & PROBABILITY BASICS
AI Engineering Learning Log

Topics:
1. Derivatives and rate of change
2. Power rule
3. Numerical derivatives
4. Chain rule
5. Partial derivatives
6. Gradients
7. Probability basics
8. Empirical probability
9. Conditional probability

Dependency: NumPy
Install: pip install numpy
"""

import numpy as np


# ============================================================
# 1. DERIVATIVES: UNDERSTANDING RATE OF CHANGE
# ============================================================

print("\n========== 1. DERIVATIVES ==========")

# Function: f(x) = x^2
def f(x):
    return x ** 2


# Derivative of x^2 = 2x
def derivative_f(x):
    return 2 * x


x = 3

print("Function: f(x) = x^2")
print("Value of f(3):", f(x))
print("Derivative at x=3:", derivative_f(x))


# ============================================================
# 2. POWER RULE
# ============================================================

print("\n========== 2. POWER RULE ==========")

# Power rule:
# If f(x) = x^n
# Then f'(x) = n * x^(n-1)

def power_rule(x, n):
    return n * (x ** (n - 1))


x = 2
n = 3

print("Function: f(x) = x^3")
print("Derivative: 3x^2")
print("Derivative at x=2:", power_rule(x, n))


# Example: f(x) = 4x^2 + 3x + 5
# Derivative: f'(x) = 8x + 3

def polynomial_derivative(x):
    return 8 * x + 3


print("\nPolynomial: f(x) = 4x^2 + 3x + 5")
print("Derivative at x=2:", polynomial_derivative(2))


# ============================================================
# 3. NUMERICAL DERIVATIVE
# ============================================================

print("\n========== 3. NUMERICAL DERIVATIVE ==========")

# Sometimes we don't know the exact derivative.
# We can approximate it using a small value of h.

# Formula:
# f'(x) = (f(x+h) - f(x)) / h

def numerical_derivative(function, x, h=0.0001):
    return (function(x + h) - function(x)) / h


def square_function(x):
    return x ** 2


x = 3

print("Numerical derivative:", numerical_derivative(square_function, x))
print("Exact derivative:", 2 * x)


# ============================================================
# 4. CHAIN RULE
# ============================================================

print("\n========== 4. CHAIN RULE ==========")

# Chain rule is used when one function is inside another.
#
# Example:
# y = (3x + 2)^2
#
# Outer function: u^2
# Inner function: 3x + 2
#
# dy/dx = 2(3x + 2) * 3

def chain_rule(x):
    return 6 * (3 * x + 2)


x = 2

print("Function: y = (3x + 2)^2")
print("Derivative at x=2:", chain_rule(x))


# ============================================================
# 5. PARTIAL DERIVATIVES
# ============================================================

print("\n========== 5. PARTIAL DERIVATIVES ==========")

# A function can have multiple variables.
#
# Example:
# f(x, y) = x^2 + 3y^2
#
# Partial derivative with respect to x = 2x
# Partial derivative with respect to y = 6y

def partial_x(x, y):
    return 2 * x


def partial_y(x, y):
    return 6 * y


x = 2
y = 1

print("Function: f(x,y) = x^2 + 3y^2")
print("Partial derivative with respect to x:", partial_x(x, y))
print("Partial derivative with respect to y:", partial_y(x, y))


# ============================================================
# 6. GRADIENTS USING NUMPY
# ============================================================

print("\n========== 6. GRADIENTS ==========")

# Gradient is a collection of partial derivatives.
#
# For f(x,y) = x^2 + 3y^2
# Gradient = [2x, 6y]

def gradient(x, y):
    return np.array([2 * x, 6 * y])


result = gradient(2, 1)

print("Gradient at (2,1):", result)


# Numerical gradient using NumPy
# This approach is useful when calculating gradients
# for more complicated functions.

def function_for_gradient(values):
    x, y = values
    return x**2 + 3*y**2


def numerical_gradient(function, values, h=0.0001):
    grad = np.zeros_like(values, dtype=float)

    for i in range(len(values)):
        values_plus = values.copy()
        values_minus = values.copy()

        values_plus[i] += h
        values_minus[i] -= h

        grad[i] = (
            function(values_plus) - function(values_minus)
        ) / (2 * h)

    return grad


point = np.array([2.0, 1.0])

print("Numerical gradient:", numerical_gradient(
    function_for_gradient, point
))


# ============================================================
# 7. BASIC PROBABILITY
# ============================================================

print("\n========== 7. BASIC PROBABILITY ==========")

# Probability formula:
#
# Probability = Favorable outcomes / Total outcomes

# Example: Rolling a dice
# Probability of getting a number greater than 3:
# Favorable outcomes = 4, 5, 6
# Total outcomes = 6

favorable_outcomes = 3
total_outcomes = 6

probability = favorable_outcomes / total_outcomes

print("Probability of rolling a number greater than 3:")
print(probability)


# ============================================================
# 8. EMPIRICAL PROBABILITY
# ============================================================

print("\n========== 8. EMPIRICAL PROBABILITY ==========")

# Empirical probability is calculated using actual experiments.
#
# Example: Tossing a coin 1000 times.

coin_tosses = np.random.choice(
    ["Heads", "Tails"],
    size=1000
)

heads_count = np.sum(coin_tosses == "Heads")
tails_count = np.sum(coin_tosses == "Tails")

heads_probability = heads_count / len(coin_tosses)
tails_probability = tails_count / len(coin_tosses)

print("Total tosses:", len(coin_tosses))
print("Heads count:", heads_count)
print("Tails count:", tails_count)
print("Empirical probability of Heads:", heads_probability)
print("Empirical probability of Tails:", tails_probability)


# ============================================================
# 9. CONDITIONAL PROBABILITY
# ============================================================

print("\n========== 9. CONDITIONAL PROBABILITY ==========")

# Conditional probability:
#
# P(A | B) = P(A and B) / P(B)
#
# Example:
# Out of 100 students:
# 60 know Python.
# 30 know both Python and AI.
#
# Find the probability that a student knows AI
# given that they know Python.

students_python = 60
students_both = 30

conditional_probability = students_both / students_python

print("Probability of knowing AI given Python:")
print(conditional_probability)


# ============================================================
# 10. LEARNING LOG
# ============================================================

"""
KEY LEARNINGS:

1. Derivative measures how quickly a function changes.
2. Power rule helps calculate derivatives of powers.
3. Numerical derivatives approximate derivatives using small changes.
4. Chain rule helps differentiate nested functions.
5. Partial derivatives measure change with respect to one variable.
6. Gradient combines partial derivatives into a vector.
7. Probability measures how likely an event is.
8. Empirical probability comes from actual experiments.
9. Conditional probability calculates probability under a condition.

WHY THIS MATTERS IN AI/ML:

- Gradients help machine learning models learn.
- Gradient descent uses gradients to minimize loss.
- Derivatives help update model parameters.
- Probability is important in classification and prediction.
- Conditional probability is used in Bayesian reasoning.


PRACTICE TASKS:

1. Calculate the derivative of f(x) = x^4.
2. Find the derivative of f(x) = 5x^2 + 4x + 7.
3. Calculate the derivative of x^2 at x = 5 using the numerical method.
4. Apply the chain rule to y = (2x + 5)^3.
5. Find the gradient of f(x,y) = 2x^2 + 4y^2.
6. Simulate rolling a dice 10,000 times using NumPy.
7. Calculate the probability of getting an even number.
8. Simulate 5,000 coin tosses and calculate Heads probability.


RUN THIS FILE:

python day_12_derivatives_gradients_probability.py

DAY 12 STATUS: COMPLETED
"""

print("\n========== DAY 12 COMPLETED ==========")
print("Keep learning. Keep building. Keep experimenting!")
