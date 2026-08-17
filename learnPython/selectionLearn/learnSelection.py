import pandas as pd

df = pd.read_csv("data.csv", index_col = "Name")

#SELECTION By column
# print(df["Weight"].to_string())

#Select multiple columns
# print(df[["Name", "Height", "Weight"]])

#Selection by row/s
# print(df.loc["Charizard": "Blastoise", ["Height", "Weight"]])

# print(df.iloc[0:11:2, 0:3])

