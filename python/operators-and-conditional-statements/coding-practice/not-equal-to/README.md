# ✅ **Not Equal to — Solution**

Write a program to check whether **two given numbers are not equal**.

---

# ✅ **Approach**

1. Read the two numbers from the user.
2. Convert them to integers.
3. Compare the numbers using the `!=` operator.
4. Print `True` if they are not equal, otherwise `False`.

---

# ✅ **Python Code**

```python
first_number = int(input())
second_number = int(input())
result = first_number != second_number
print(result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

## **Example 1**

### Input:

```
2
3
```

| Step | Operation          | Expression        | Result |
| ---- | ------------------ | ----------------- | ------ |
| 1    | Read first number  | first_number = 2  | 2      |
| 2    | Read second number | second_number = 3 | 3      |
| 3    | Compare numbers    | 2 != 3            | True   |
| 4    | Print result       | print(True)       | True   |

### Output:

```
True
```

---

## **Example 2**

### Input:

```
10
10
```

| Step | Operation          | Expression         | Result |
| ---- | ------------------ | ------------------ | ------ |
| 1    | Read first number  | first_number = 10  | 10     |
| 2    | Read second number | second_number = 10 | 10     |
| 3    | Compare numbers    | 10 != 10           | False  |
| 4    | Print result       | print(False)       | False  |

### Output:

```
False
```

---
