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

* What is Pandas?
* Why it is important for AI and Data Science

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

