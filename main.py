import pandas as pd 


# print(pd.__version__)


# Series = A pandas 1- dimensional labeled array that can hold any data type 
# think of it like a single column in a spreadsheet (1-Dimensional)


# data = [100, 102, 104, 200, 202]

# series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

# # series.loc['a'] = 1000

# # print(series.iloc[1])

# print(series[series >= 200])


# calories = {"Day 1:": 1750,
#             "Day 2": 1500,
#             "Day 3": 1750}

# series = pd.Series(calories)

# # series.loc['Day 2'] += 500

# # print(series[series >= 1700])

# print(series)



# DataFrame = A tabular data structure with rows AND columns. (2 Dimensional)

# Simliar to an Excel spreadsheet

data = {"Name": ["John", "Jane", "Joe"],
        "Age": [20, 22, 23], 
        "job": ["Engineer", "Sales", "Engineer"] }

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

# print(df.loc["Employee 1"])
# print(df.iloc[0])

# Add a new column
# df["Salary"] = [1000, 1200, 1300]

# # Add a new rows
# new_rows = pd.DataFrame([{"Name": "Bob", "Age": 24, "Salary": 1500, "job": "Engineer"}, 
#                        {"Name": "Sandy", "Age": 35, "Salary": 2500, "job": "Engineer"}],
#                        index=["Employee 4", "Employee 5"])

# df = pd.concat([df, new_rows])



# print(df)


# Importing  

# df = pd.read_csv("data.csv")
# df = pd.read_json("data.json")
# print(df.to_string())

# Selection 

df = pd.read_csv("data.csv", index_col= "Name")

# Selcetion by column

# print(df["Name"].to_string())
# print(df["Height"].to_string())

# print(df[["Name", "Height", "Weight"]].to_string())


# Selcetion by rows
# print(df.loc["Pikachu"])
# print(df.loc["Charizard":"Blastoise"], ["Height", "Weight"])
# print(df.iloc[0:11:2, 0:3])


# pokemon  = input("Enter Pokemon Name: ")


# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} is not in the database")
    
# Filtering  = keeping the rows that match a condition 

 
# tall_pokemon = df[df["Height"] >= 2]
# heavy_pokemon = df[df["Weight"] > 100]

# print(heavy_pokemon)


# Aggregation = Reduces a set of values into a single summary value 
# used to summarize and analyze data 
# often used with the groupby() function 


# df = pd.read_csv("data.csv")

# Whole data frame
# print(df.mean(numeric_only= True))
# print(df.sum(numeric_only= True))
# print(df.min(numeric_only= True))
# print(df.max(numeric_only= True))
# print(df.count())


# Single column
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())


# Group by
# group = df.groupby("Type1")

# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].min())
# print(group["Height"].max())
# print(group["Height"].count())


# Data cleaning = the process of fixing/removing:
# incomplete, incorrect, or irrelevant data
# -75% of work with pandas is data cleaning 



df = pd.read_csv("data.csv") 

# drop a column
# df = df.drop(columns=["Legendary", "No"])

# Hanlde Missing data
# df = df.dropna(subset=["Type2"])
# df = df.fillna({ "Type2": "Unknown" })

# Fix inconsistent Values 

# df["Type1"] = df["Type1"].replace({"Normal": "Fighting"})

# Standardize Test 

# df["Name"] = df["Name"].str.lower()


# fix data types 

# df["Legendary"] = df["Legendary"].astype(bool)



# # Remove duplicate values 
# df = df.drop_duplicates()


# print(df.to_string())



g