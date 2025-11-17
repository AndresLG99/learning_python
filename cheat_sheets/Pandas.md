
# 🐼 Pandas Cheat Sheet  
Clean, Visual & Beginner‑Friendly

---

## 📌 1. Importing Data
```python
df = pd.read_csv("data.csv")
df = pd.read_excel("file.xlsx")
df = pd.read_json("file.json")
```

---

## 📌 2. Basic Exploration
```python
df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns
```

---

## 📌 3. Selecting Data
### Columns
```python
df["col"]
df[["col1","col2"]]
```

### Rows
```python
df.loc[0:5]
df.iloc[0:5]
```

---

## 📌 4. Filtering
```python
df[df["age"] > 30]
df[(df["age"] > 30) & (df["city"] == "Vancouver")]
```

---

## 📌 5. Missing Values
```python
df.isna().sum()
df.dropna()
df.fillna(0)
df.fillna(df.mean())
```

---

## 📌 6. Grouping
```python
df.groupby("category")["sales"].mean()
df.groupby("type").agg({"sales":"sum", "profit":"mean"})
```

---

## 📌 7. Merging & Joining
```python
pd.merge(df1, df2, on="id", how="inner")
df1.join(df2, lsuffix="_left", rsuffix="_right")
```

---

## 📌 8. Sorting
```python
df.sort_values("age")
df.sort_values(["age","salary"], ascending=[True, False])
```

---

## 📌 9. Apply Functions
```python
df["new"] = df["col"].apply(lambda x: x*2)
```

---

## 📌 10. Exporting
```python
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx")
```

---

