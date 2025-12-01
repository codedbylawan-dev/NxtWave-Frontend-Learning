# ✅ **Check One Greater — Solution**

Write a program to check whether **B is greater than A by exactly 1**.

That means:

```
B == A + 1
```

---

# ✅ **Approach**

1. Read A (integer).
2. Read B (integer).
3. Check if `B == A + 1`.
4. Print `True` or `False`.

---

# ✅ **Python Code**

```python
A = input()
A = int(A)

B = input()
B = int(B)

result = (B == A + 1)
print(result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

---

## **Example 1**

### **Input**

```
2
3
```

| Step | Operation        | Expression  | Result |
| ---- | ---------------- | ----------- | ------ |
| 1    | Read A           | A = 2       | 2      |
| 2    | Read B           | B = 3       | 3      |
| 3    | Check B == A + 1 | 3 == 2 + 1  | True   |
| 4    | Print result     | print(True) | True   |

### **Output**

```
True
```

---

## **Example 2**

### **Input**

```
2
5
```

| Step | Operation        | Expression   | Result |
| ---- | ---------------- | ------------ | ------ |
| 1    | Read A           | A = 2        | 2      |
| 2    | Read B           | B = 5        | 5      |
| 3    | Check B == A + 1 | 5 == 2 + 1   | False  |
| 4    | Print result     | print(False) | False  |

### **Output**

```
False
```

---

## **Example 3**

### **Input**

```
7
6
```

| Step | Operation        | Expression   | Result |
| ---- | ---------------- | ------------ | ------ |
| 1    | Read A           | A = 7        | 7      |
| 2    | Read B           | B = 6        | 6      |
| 3    | Check B == A + 1 | 6 == 7 + 1   | False  |
| 4    | Print result     | print(False) | False  |

### **Output**

```
False
```

---
