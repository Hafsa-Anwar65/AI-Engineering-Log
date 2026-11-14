# ============================================================
# DAY 9: Broadcasting & Vectorization vs Loops
# ============================================================

import time

import numpy as np

print("\n========== DAY 9 ==========")

numbers = np.array([1, 2, 3, 4, 5])

# Vectorization
print("Original:", numbers)
print("Multiply by 2:", numbers * 2)
print("Add 10:", numbers + 10)
print("Square:", numbers ** 2)

# Broadcasting
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([10, 20, 30])

print("\nBroadcasting:")
print(matrix + vector)

# Loop comparison
result_loop = []

for num in numbers:
    result_loop.append(num * 2)

print("\nUsing Loop:", result_loop)
print("Using NumPy:", numbers * 2)

# Speed test: loop vs vectorised on 1 million numbers
big = np.arange(1_000_000)

start = time.perf_counter()
loop_result = [n * 2 for n in big]
loop_time = time.perf_counter() - start

start = time.perf_counter()
vector_result = big * 2
vector_time = time.perf_counter() - start

print(f"\nLoop on 1M numbers:       {loop_time:.4f}s")
print(f"Vectorised on 1M numbers: {vector_time:.4f}s")
print(f"NumPy was about {loop_time / vector_time:.0f}x faster")
