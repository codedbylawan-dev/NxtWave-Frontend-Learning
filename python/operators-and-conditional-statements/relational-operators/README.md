# 🧠 Relational Operators | Cheat Sheet

## **What Are Relational Operators?**

Relational operators are used to **compare values**.
They give either **True** or **False** as the result.

---

## **List of Relational Operators**

| Operator | Meaning                     |
| -------- | --------------------------- |
| >        | Is greater than             |
| <        | Is less than                |
| ==       | Is equal to                 |
| <=       | Is less than or equal to    |
| >=       | Is greater than or equal to |
| !=       | Is not equal to             |

---

## **Examples**

```python
print(5 < 10)
print(2 > 1)
```

**Output:**

```
True
True
```

---

## **Possible Mistakes**

### **Mistake 1: Using = instead of ==**

```python
print(3 = 3)
```

**Output:**

```
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
```

---

### **Mistake 2: Adding space inside the operator**

```python
print(2 < = 3)
```

**Output:**

```
SyntaxError: invalid syntax
```

❗ Spaces inside relational operators (`==`, `<=`, `>=`, `!=`) are **not allowed**.

---

## **Comparing Numbers**

```python
print(2 <= 3)
print(2.53 >= 2.55)
```

**Output:**

```
True
False
```

---

## **Comparing Integers and Floats**

```python
print(12 == 12.0)
print(12 == 12.1)
```

**Output:**

```
True
False
```

---

## **Comparing Strings**

```python
print("ABC" == "ABC")
print("CBA" != "ABC")
```

**Output:**

```
True
True
```

---

## **Case Sensitivity**

```python
print("ABC" == "abc")
```

**Output:**

```
False
```

Python is **case-sensitive**, meaning capital letters and small letters are **not the same**.

---

## **Strings and Equality Operator**

```python
print(True == "True")
print(123 == "123")
print(1.1 == "1.1")
```

**Output:**

```
False
False
False
```

Different data types are **not equal**, even if they look similar.

---
