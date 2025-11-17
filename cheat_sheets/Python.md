
# 🐍 Python Cheat Sheet  
Clean, Visual & Beginner‑Friendly

---

## 📌 1. Variables & Data Types
```python
x = 5               # int
pi = 3.14           # float
name = "Alice"      # str
flag = True         # bool
nums = [1,2,3]      # list
items = (1,2,3)     # tuple
person = {"name":"Bob", "age":30}  # dict
```

---

## 📌 2. Basic Operators
```python
a + b      # addition
a - b      # subtraction
a * b      # multiplication
a / b      # division
a // b     # floor division
a ** b     # exponent
```

---

## 📌 3. Conditionals
```python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

---

## 📌 4. Loops
### For loop
```python
for i in range(5):
    print(i)
```

### While loop
```python
while x < 10:
    x += 1
```

---

## 📌 5. Functions
```python
def greet(name, age=18):
    return f"Hello {name}, age {age}"
```

---

## 📌 6. Useful Built‑ins
```python
len(list)
type(obj)
sorted(list)
sum(list)
```

---

## 📌 7. List Comprehensions
```python
squares = [x*x for x in range(10)]
```

---

## 📌 8. File Handling
```python
with open("file.txt", "r") as f:
    data = f.read()
```

---

## 📌 9. Exceptions
```python
try:
    result = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")
```

---

## 📌 10. Classes
```python
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
```

---
