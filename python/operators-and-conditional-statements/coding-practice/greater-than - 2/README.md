# ✅ **Greater than – 2**

Write a program to check whether **A is greater than B**, and print the result in the format:

```
A > B is True
```

or

```
A > B is False
```

---

# ✅ **Approach**

1. Read input `A` (integer).
2. Read input `B` (integer).
3. Compare the numbers using the `>` operator.
4. Convert the result to string.
5. Print final output in the required format.

---

# ✅ **Python Code**

```python
a = input()
a = int(a)

b = input()
b = int(b)

result = a > b
result = str(result)

print("A > B is " + result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

---

## **Example 1**

### **Input**

```
8
5
```

| Step | Operation                | Expression    | Result |
| ---- | ------------------------ | ------------- | ------ |
| 1    | Read A                   | A = 8         | 8      |
| 2    | Read B                   | B = 5         | 5      |
| 3    | Compare A > B            | 8 > 5         | True   |
| 4    | Convert result to string | str(True)     | "True" |
| 5    | Print output             | A > B is True | Output |

### **Output**

```
A > B is True
```

---

## **Example 2**

### **Input**

```
12
32
```

| Step | Operation                | Expression     | Result  |
| ---- | ------------------------ | -------------- | ------- |
| 1    | Read A                   | A = 12         | 12      |
| 2    | Read B                   | B = 32         | 32      |
| 3    | Compare A > B            | 12 > 32        | False   |
| 4    | Convert result to string | str(False)     | "False" |
| 5    | Print output             | A > B is False | Output  |

### **Output**

```
A > B is False
```

---
