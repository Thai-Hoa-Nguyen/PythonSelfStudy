import pandas as pd

#pokename = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard"]
pokename = {1: "Bulbasaur", 2: "Ivysaur", 3:"Venusaur", 4:"Charmander",5: "Charmeleon", 6:"Charizard"}

series = pd.Series(pokename)

print(series)