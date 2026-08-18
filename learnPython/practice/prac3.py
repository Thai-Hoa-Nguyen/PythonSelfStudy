# Part 2 — DataFrame
# Create this DataFrame:
# Name       Age    Major          GPA
# Alice      20     Computer       3.8
# Bob        22     Business       3.2
# Charlie    21     Computer       3.9
# David      23     Engineering    3.5
# Emma       20     Business       3.7
# Exercise 3 — Create the DataFrame
# Create the DataFrame using a Python dictionary.
# Then:
# Display the DataFrame.
text =  "the first 3 rows."
text2 = "the last 2 rows."
# Display the column names.
# Display the number of rows and columns.
# Display the DataFrame information using info().

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [20, 22, 21, 23, 20],
    "Major": ["Computer", "Bussiness", "Computer", "Engineering", "Bussiness"],
    "GPA": [3.8, 3.2, 3.9, 3.5, 3.7]
}

df = pd.DataFrame(data, index = ["Student 1","Student 2","Student 3","Student 4","Student 5" ])

print("===DATA FRAME===")
print(df)
print(f"==={text.upper()}===")
#There are 2 ways to do
# head() or use slicing
# tail() or use slicing
print(df[:3])
print(f"==={text2.upper()}====")
print(df.tail(2))

print(df.info())
