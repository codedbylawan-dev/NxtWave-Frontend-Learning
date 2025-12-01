# ✅ **Less than or Equal to — Solution**

Write a program to check whether **the first number is less than or equal to the second number** and print the result as a boolean.

---

# ✅ **Approach**

1. Read the first number as an integer.
2. Read the second number as a float.
3. Compare the two numbers using the `<=` operator.
4. Print the result as `True` or `False`.

---

# ✅ **Python Code**

```python
first_number = input()
first_number = int(first_number)

second_number = input()
second_number = float(second_number)

result = first_number <= second_number
print(result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

## **Example 1**

### Input:

```
2
5.3
```

| Step | Operation                             | Expression          | Result |
| ---- | ------------------------------------- | ------------------- | ------ |
| 1    | Read first number                     | first_number = 2    | 2      |
| 2    | Read second number                    | second_number = 5.3 | 5.3    |
| 3    | Compare first_number <= second_number | 2 <= 5.3            | True   |
| 4    | Print result                          | print(result)       | True   |

### Output:

```
True
```

---

## **Example 2**

### Input:

```
13
10.3
```

| Step | Operation                             | Expression           | Result |
| ---- | ------------------------------------- | -------------------- | ------ |
| 1    | Read first number                     | first_number = 13    | 13     |
| 2    | Read second number                    | second_number = 10.3 | 10.3   |
| 3    | Compare first_number <= second_number | 13 <= 10.3           | False  |
| 4    | Print result                          | print(result)        | False  |

### Output:

```
False
```

---
