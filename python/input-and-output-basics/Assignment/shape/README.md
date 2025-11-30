# ✅ **Question: Shape**

Write a program that reads a number **N** and prints **three lines**, each containing **N space-separated pluses (`+`)**.

---

# ✅ **Approach**

### **Step 1: Understand the Task**

You must print **three lines**.
Each line must have **N plus signs**, each separated by a space.

Example for N = 3:

```
+ + +
+ + +
+ + +
```

---

### **Step 2: Read the Input**

- Use `input()` to read the value of N
- Convert it to an integer using `int()`

---

### **Step 3: Print the Lines**

- Use string multiplication → `"+ " * N`
- Print the same line **three times**

---

# ✅ **Final Code**

```python
count = int(input())
print("+ " * count)
print("+ " * count)
print("+ " * count)
```

---

# 🟩 **DRY RUN (Tabular Form)**

Assume input:

```
4
```

| Step No.         | Operation        | Result / Explanation            |
| ---------------- | ---------------- | ------------------------------- |
| 1                | Read input `"4"` | count = 4                       |
| 2                | Print `"+ " * 4` | `+ + + + `                      |
| 3                | Print `"+ " * 4` | `+ + + + `                      |
| 4                | Print `"+ " * 4` | `+ + + + `                      |
| **Final Output** | Combined result  | + + + + <br>+ + + + <br>+ + + + |

---
