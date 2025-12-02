# 🧠 Logical Operators | Cheat Sheet

Logical operators are used to perform **logical operations** on Boolean values.
They return either **True** or **False** as the result.

---

## **Logical Operators in Python**

- **and**
- **or**
- **not**

---

## **Logical AND Operator**

Gives **True** only if **both** the booleans are True.
Otherwise, it returns **False**.

### Example:

```python
print(True and True)
```

**Output:**

```
True
```

### Example with Comparison:

```python
print((2 < 3) and (1 < 2))
```

**Step-by-Step:**

```
(2 < 3) and (1 < 2)
True and True
```

**Output:**

```
True
```

---

## **Logical OR Operator**

Gives **True** if **any one** of the booleans is True.
Only if both are False, it gives False.

### Example:

```python
print(False or False)
```

**Output:**

```
False
```

### Example with Comparison:

```python
print((2 < 3) or (2 < 1))
```

**Step-by-Step:**

```
(2 < 3) or (2 < 1)
True or False
```

**Output:**

```
True
```

---

## **Logical NOT Operator**

Gives the **opposite** of the Boolean value.

### Example:

```python
print(not(False))
```

**Output:**

```
True
```

### Example with Comparison:

```python
print(not(2 < 3))
```

**Step-by-Step:**

```
not(2 < 3)
not(True)
False
```

**Output:**

```
False
```

---

## **Summary**

- **AND** → True only if **all** conditions are True
- **OR** → True if **any one** condition is True
- **NOT** → Gives the **opposite** value

---
