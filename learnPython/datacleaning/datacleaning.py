import pandas as pd

df = pd.read_csv("data.csv")

#drop columns
# df = df.drop(columns=["Legendary",  "No"])

#handle missing data
# df = df.dropna(subset=["Type2"])

# df = df.fillna({"Type2": "None"})

#fix inconsistent value
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS",
#                                   "Fire" : "FIRE",
#                                   "Water": "WATER"})

#stadnardize text
# df["Name"] = df["Name"].str.lower()

#fix datatype
# df["Legendary"] = df["Legendary"].astype(bool)

#remove duplicate value
df = df.drop_duplicates()

print(df.to_string())