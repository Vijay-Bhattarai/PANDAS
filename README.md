# PANDAS

# 🐼 Pandas Basics Guide 

This repository covers the essential topics of Pandas required for data analysis and preparing data for Machine Learning.

---

## 📌 What is Pandas?

Pandas is a powerful Python library used for:

* Data manipulation
* Data cleaning
* Data analysis

It works mainly with structured data like CSV, Excel, etc.

---

## 📚 Topics Covered

### 1️⃣ Introduction to Pandas

Pandas is a Python library used for working with data sets.

It has functions for analyzing, cleaning, exploring, and manipulating data.

The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

Why Use Pandas?
Pandas allows us to analyze big data and make conclusions based on statistical theories.

Pandas can clean messy data sets, and make them readable and relevant.

Relevant data is very important in data science.

:}
Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.

What Can Pandas Do?
Pandas gives you answers about the data. Like:

Is there a correlation between two or more columns?
What is average value?
Max value?
Min value?
Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data.

Where is the Pandas Codebase?
The source code for Pandas is located at this github repository https://github.com/pandas-dev/pandas

{:
github: enables many people to work on the same codebase.

```python
import pandas as pd
```

---

### 2️⃣ Series

* One-dimensional data structure
* Similar to a single column

```python
s = pd.Series([10, 20, 30])
print(s)
```

---

### 3️⃣ DataFrames

* Two-dimensional table (rows & columns)
* Most used structure in Pandas

```python
df = pd.DataFrame({
    "Name": ["Ram", "Shyam"],
    "Age": [20, 22]
})
print(df)
```

---

### 4️⃣ Importing Data

* Load data from files

```python
df = pd.read_csv("data.csv")
```

---

### 5️⃣ Selection

* Selecting columns and rows

```python
df["Name"]        # column
df.loc[0]         # row
df.iloc[0:2]      # slicing
```

---

### 6️⃣ Filtering

* Select data based on conditions

```python
df[df["Age"] > 20]
```

---

### 7️⃣ Aggregation

* Summary operations

```python
df["Age"].mean()
df.groupby("Name").count()
```

---

### 8️⃣ Data Cleaning

* Handling missing and duplicate data

```python
df.dropna()
df.fillna(0)
df.drop_duplicates()
```

---

