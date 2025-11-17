
# 📊 Seaborn Cheat Sheet  
Clean, Visual & Beginner‑Friendly

---

## 📌 1. Basic Plots
```python
sns.histplot(df["age"])
sns.boxplot(data=df, x="category", y="price")
sns.scatterplot(data=df, x="weight", y="height")
sns.lineplot(data=df, x="time", y="sales")
```

---

## 📌 2. Categorical
```python
sns.countplot(df["city"])
sns.barplot(data=df, x="city", y="income")
```

---

## 📌 3. Heatmaps
```python
sns.heatmap(df.corr(), annot=True)
```

---

## 📌 4. Pairplot
```python
sns.pairplot(df)
```

---

