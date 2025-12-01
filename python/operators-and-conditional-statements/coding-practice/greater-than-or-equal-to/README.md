# ✅ **Greater than or Equal to — Solution**

Write a program to check whether **A is greater than or equal to B** and print the result in the required format.

---

# ✅ **Approach**

1. Read the two numbers from the user.
2. Convert them to floats.
3. Compare the numbers using the `>=` operator.
4. Print the result as `"A >= B is True"` or `"A >= B is False"`.

---

# ✅ **Python Code**

```python
a = input()
a = float(a)
b = input()
b = float(b)
result = a >= b
print("A >= B is " + str(result))
```

---

# 🟩 **DRY RUN (Tabular Form)**

## **Example 1**

### Input:

```
4.3
3.2
```

| Step | Operation          | Expression              | Result         |
| ---- | ------------------ | ----------------------- | -------------- |
| 1    | Read first number  | a = 4.3                 | 4.3            |
| 2    | Read second number | b = 3.2                 | 3.2            |
| 3    | Compare a >= b     | 4.3 >= 3.2              | True           |
| 4    | Print result       | print("A >= B is True") | A >= B is True |

### Output:

```
A >= B is True
```

---

## **Example 2**

### Input:

```
9.9
10.0
```

| Step | Operation          | Expression               | Result          |
| ---- | ------------------ | ------------------------ | --------------- |
| 1    | Read first number  | a = 9.9                  | 9.9             |
| 2    | Read second number | b = 10.0                 | 10.0            |
| 3    | Compare a >= b     | 9.9 >= 10.0              | False           |
| 4    | Print result       | print("A >= B is False") | A >= B is False |

### Output:

```
A >= B is False
```

---
