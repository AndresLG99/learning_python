
# 🤖 Scikit‑Learn Cheat Sheet  
Clean, Visual & Beginner‑Friendly

---

## 📌 1. Train/Test Split
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

---

## 📌 2. Scaling
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## 📌 3. Common Models
```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

model = LogisticRegression()
model.fit(X_train, y_train)
```

---

## 📌 4. Predictions
```python
pred = model.predict(X_test)
probs = model.predict_proba(X_test)
```

---

## 📌 5. Metrics
```python
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report
)

accuracy_score(y_test, pred)
confusion_matrix(y_test, pred)
print(classification_report(y_test, pred))
```

---

## 📌 6. Cross Validation
```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
scores.mean()
```

---

