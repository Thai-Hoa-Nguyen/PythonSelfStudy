import pandas as pd

data = {"Name": ["Thai Nguyen", "Martin Nguyen", "Yuma Kawai", "Judd Niemi"],
        "Age": [21, 20, 22, 20]
        }

df = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3", "Employee 4"])

# Add new column
df["Job"] = ["SDE", "SWE", "Student", "Intern"]

#Add new rows
new_rows = pd.DataFrame([{"Name": "Sandy Ng", "Age": 28, "Job": "Enginner"},
                         {"Name": "Simon Nguyen", "Age": 23, "Job": "Student"},
                         {"Name": "Cyrus Hui", "Age": 32, "Job": "Intern"},
                         {"Name": "Yoon Park", "Age": 19, "Job": "Student"}],
                         index = ["Employee 5", "Employee 6", "Employee 7", "Employee 8"])

df = pd.concat([df, new_rows])

print(df)