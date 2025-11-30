# ✅ **Question: Basic Arithmetic**

Write a program that reads **two integers A and B**, and prints:

1. **A + B**
2. **A - B**
3. **A × B**

Each on a new line.

---

# ✅ **Approach**

### **Step 1: Read the Inputs**

- Read first integer → A
- Read second integer → B

---

### **Step 2: Perform Operations**

- Addition → `A + B`
- Subtraction → `A - B`
- Multiplication → `A * B`

---

### **Step 3: Print Results**

Print each result on a **new line**, in order.

---

# ✅ **Solution Code**

```python
A = int(input())
B = int(input())

print(A + B)
print(A - B)
print(A * B)
```

---

# 🟩 **DRY RUN (Tabular Form)**

Assume Input:

```
4
3
```

| Step             | Operation      | Expression | Result       |
| ---------------- | -------------- | ---------- | ------------ |
| 1                | Read A         | A = 4      | 4            |
| 2                | Read B         | B = 3      | 3            |
| 3                | Addition       | 4 + 3      | **7**        |
| 4                | Subtraction    | 4 - 3      | **1**        |
| 5                | Multiplication | 4 × 3      | **12**       |
| **Final Output** | Combined       | —          | 7<br>1<br>12 |

---
