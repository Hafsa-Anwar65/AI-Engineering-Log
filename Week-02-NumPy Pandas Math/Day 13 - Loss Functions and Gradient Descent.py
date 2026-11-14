
"""
DAY 13: LOSS FUNCTIONS & GRADIENT DESCENT
AI Engineering Learning Log

Topics:
1. Loss Functions
2. Mean Squared Error (MSE)
3. Mean Absolute Error (MAE)
4. Gradient Descent
5. Learning Rate
6. Weight and Bias Updates
7. Linear Regression from Scratch
8. Loss Visualization

Dependencies:
NumPy
Matplotlib

Install:
pip install numpy matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# 1. UNDERSTANDING LOSS FUNCTIONS
# ============================================================

print("\n========== 1. LOSS FUNCTIONS ==========")

"""
A loss function measures the difference between
actual values and model predictions.

Smaller loss generally means better predictions.
"""

actual = np.array([100, 200, 300, 400, 500])
predicted = np.array([90, 210, 280, 390, 520])

errors = actual - predicted

print("Actual values:", actual)
print("Predicted values:", predicted)
print("Errors:", errors)


# ============================================================
# 2. MEAN SQUARED ERROR (MSE)
# ============================================================

print("\n========== 2. MEAN SQUARED ERROR ==========")

"""
Formula:
MSE = mean((actual - predicted) ** 2)

MSE squares errors before averaging them.
Large errors receive a bigger penalty.
"""

def mean_squared_error(actual, predicted):
    return np.mean((actual - predicted) ** 2)


mse = mean_squared_error(actual, predicted)

print("Mean Squared Error:", mse)


# ============================================================
# 3. MEAN ABSOLUTE ERROR (MAE)
# ============================================================

print("\n========== 3. MEAN ABSOLUTE ERROR ==========")

"""
Formula:
MAE = mean(abs(actual - predicted))

MAE calculates the average absolute error.
"""

def mean_absolute_error(actual, predicted):
    return np.mean(np.abs(actual - predicted))


mae = mean_absolute_error(actual, predicted)

print("Mean Absolute Error:", mae)


# ============================================================
# 4. COMPARING MSE AND MAE
# ============================================================

print("\n========== 4. MSE VS MAE ==========")

actual_values = np.array([10, 20, 30, 40])
predicted_values = np.array([12, 18, 35, 50])

print("MSE:", mean_squared_error(actual_values, predicted_values))
print("MAE:", mean_absolute_error(actual_values, predicted_values))

"""
MSE:
- Squares errors.
- Penalizes large errors more heavily.
- Sensitive to outliers.

MAE:
- Uses absolute errors.
- Easier to interpret in the original unit.
- Less sensitive to outliers.
"""


# ============================================================
# 5. UNDERSTANDING GRADIENT DESCENT
# ============================================================

print("\n========== 5. GRADIENT DESCENT ==========")

"""
Gradient descent is an optimization algorithm.

It updates model parameters to reduce the loss.

Update formula:

new_weight = old_weight - learning_rate * gradient
"""

# Example loss function:
# Loss = (w - 5)^2
# Derivative = 2 * (w - 5)

def loss_function(w):
    return (w - 5) ** 2


def gradient_function(w):
    return 2 * (w - 5)


w = 0.0
learning_rate = 0.1
epochs = 20

for epoch in range(epochs):

    loss = loss_function(w)
    gradient = gradient_function(w)

    w = w - learning_rate * gradient

    print(
        f"Epoch {epoch + 1}: "
        f"Weight = {w:.4f}, "
        f"Loss = {loss:.4f}"
    )

print("Final weight:", w)
print("Target weight: 5")


# ============================================================
# 6. UNDERSTANDING LEARNING RATE
# ============================================================

print("\n========== 6. LEARNING RATE ==========")

"""
Learning rate controls the size of each update.

Small learning rate:
- Smaller updates.
- Usually slower learning.

Large learning rate:
- Larger updates.
- May overshoot the minimum.
- Can make training unstable.
"""

def run_gradient_descent(start, learning_rate, epochs):

    weight = start
    losses = []

    for _ in range(epochs):

        loss = loss_function(weight)
        gradient = gradient_function(weight)

        losses.append(loss)

        weight = weight - learning_rate * gradient

    return weight, losses


for rate in [0.01, 0.1, 0.5]:

    final_weight, losses = run_gradient_descent(
        start=0,
        learning_rate=rate,
        epochs=20
    )

    print(
        f"Learning Rate: {rate} | "
        f"Final Weight: {final_weight:.4f} | "
        f"Final Loss: {losses[-1]:.4f}"
    )


# ============================================================
# 7. LINEAR REGRESSION FROM SCRATCH
# ============================================================

print("\n========== 7. LINEAR REGRESSION ==========")

"""
Linear regression model:

y = wx + b

w = weight
b = bias
x = input
y = prediction

Goal:
Find the best weight and bias to minimize MSE.
"""

# Training data
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([3, 5, 7, 9, 11], dtype=float)

# Initialize parameters
w = 0.0
b = 0.0

learning_rate = 0.01
epochs = 1000
n = len(X)

loss_history = []

for epoch in range(epochs):

    # Step 1: Make predictions
    predictions = w * X + b

    # Step 2: Calculate MSE
    loss = np.mean((predictions - y) ** 2)
    loss_history.append(loss)

    # Step 3: Calculate gradients
    dw = (2 / n) * np.sum((predictions - y) * X)
    db = (2 / n) * np.sum(predictions - y)

    # Step 4: Update parameters
    w = w - learning_rate * dw
    b = b - learning_rate * db

print("Final Weight:", w)
print("Final Bias:", b)
print("Final Training Loss:", loss_history[-1])

# Make a prediction
new_input = 6
prediction = w * new_input + b

print("Prediction for x=6:", prediction)


# ============================================================
# 8. VISUALIZING LOSS REDUCTION
# ============================================================

print("\n========== 8. LOSS VISUALIZATION ==========")

plt.figure(figsize=(8, 5))

plt.plot(loss_history)

plt.title("Gradient Descent: Loss Reduction")
plt.xlabel("Epochs")
plt.ylabel("Mean Squared Error")

plt.grid(True)
plt.show()


# ============================================================
# 9. ACTUAL VS PREDICTED VALUES
# ============================================================

print("\n========== 9. ACTUAL VS PREDICTED ==========")

predictions = w * X + b

plt.figure(figsize=(8, 5))

plt.scatter(X, y, label="Actual Values")
plt.plot(X, predictions, label="Predicted Values")

plt.title("Actual vs Predicted Values")
plt.xlabel("Input X")
plt.ylabel("Output Y")

plt.legend()
plt.grid(True)
plt.show()


# ============================================================
# 10. LEARNING LOG
# ============================================================

"""
KEY LEARNINGS:

1. Loss functions measure prediction errors.
2. MSE squares errors and calculates their average.
3. MAE calculates average absolute errors.
4. Gradient descent minimizes loss by updating parameters.
5. Learning rate controls the size of parameter updates.
6. Weight and bias are trainable model parameters.
7. An epoch is one complete training iteration.
8. Loss reduction shows improvement on training data.

WHY THIS MATTERS IN AI/ML:

- Loss functions measure model performance.
- Gradient descent helps models learn.
- Neural networks use gradients to update weights.
- Learning rate affects training speed and stability.
- Optimization is fundamental to machine learning.


PRACTICE TASKS:

1. Calculate MSE for:
   Actual = [10, 20, 30]
   Predicted = [12, 18, 28]

2. Calculate MAE for the same values.

3. Change learning rate to 0.001.
   Observe how training changes.

4. Try a learning rate of 1.0.
   Does the loss decrease or become unstable?

5. Change the training data:
   X = [1, 2, 3, 4, 5]
   y = [5, 10, 15, 20, 25]

6. Train the model and check whether it learns y = 5x.

7. Experiment with different epoch values.

8. Explain why gradient descent subtracts the gradient.


RUN THIS FILE:

python day_13_loss_functions_gradient_descent.py

DAY 13 STATUS: COMPLETED
"""

print("\n========== DAY 13 COMPLETED ==========")
print("Next: Day 14 - Linear Regression from Scratch!")
