# ✅ **Sunday — Solution**

Write a program to check whether a given **day number corresponds to Sunday**.

Day Number Table:

| Day       | Day Number |
| --------- | ---------- |
| Monday    | 1          |
| Tuesday   | 2          |
| Wednesday | 3          |
| Thursday  | 4          |
| Friday    | 5          |
| Saturday  | 6          |
| Sunday    | 7          |

---

# ✅ **Approach**

1. Read the day number from the user.
2. Convert the input to an integer.
3. Compare the number with 7 (Sunday).
4. Print `True` if it matches, otherwise `False`.

---

# ✅ **Python Code**

```python
day_number = input()
day_number = int(day_number)
result = day_number == 7
print(result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

## **Example 1**

### Input:

```
7
```

| Step | Operation          | Expression       | Result |
| ---- | ------------------ | ---------------- | ------ |
| 1    | Read day number    | day_number = "7" | "7"    |
| 2    | Convert to integer | int("7")         | 7      |
| 3    | Check if Sunday    | 7 == 7           | True   |
| 4    | Print result       | print(True)      | True   |

### Output:

```
True
```

---

## **Example 2**

### Input:

```
1
```

| Step | Operation          | Expression       | Result |
| ---- | ------------------ | ---------------- | ------ |
| 1    | Read day number    | day_number = "1" | "1"    |
| 2    | Convert to integer | int("1")         | 1      |
| 3    | Check if Sunday    | 1 == 7           | False  |
| 4    | Print result       | print(False)     | False  |

### Output:

```
False
```

---
