# Exercise 2 — Series Operations

# Given:
# scores = pd.Series([85, 92, 78, 90, 88])
# Find:
# Number of elements
# Sum
# Mean
# Maximum
# Minimum
# Standard deviation

import pandas as pd

scores = pd.Series([85, 92, 78, 90, 88])

print(f"Number of elements: {scores.count()}")
print(f"Sum: {scores.sum()}")
print(f"Mean: {scores.mean()}")
print(f"Max: {scores.max()}")
print(f"Min: {scores.min()}")
print(f"Standard deviation: {scores.std()}")


