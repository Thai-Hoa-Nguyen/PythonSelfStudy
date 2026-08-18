# Part 1 — Series
# Exercise 1 — Create a Series
# Create a pandas Series containing:
# 85, 92, 78, 90, 88
# with the index:
# Math, English, History, Science, Programming
# Tasks:
# Create the Series.
# Print it.
# Find the Programming grade.
# Find the average grade.
# Find the highest grade.

import pandas as pd

subjects = {"Math": 85, "English": 92, "History": 78, "Science": 90, "Programming": 88}
series = pd.Series(subjects)

# subjects_score = [85, 92, 78, 90, 88]
# series = pd.Series(subjects_score, index = ["Math", "English", "History", "Science", "Programming"])

print(f"Programing grade: {series.iloc[4]}")
print(f"Avarege grade: {series.mean()}")
print(f"Highest grade: {series.max()} -> {series.idxmax()}")

