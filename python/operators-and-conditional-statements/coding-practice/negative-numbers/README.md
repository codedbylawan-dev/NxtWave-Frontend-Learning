# 🔹 **Question: Negative Numbers**

Write a program that reads two integers **A** and **B**, and checks whether **both** numbers are **negative**.

### **Input**

- First line → integer **A**
- Second line → integer **B**

### **Output**

Print **True** if both numbers are negative,
else print **False**.

### **Example**

- A = -1, B = -2 → True
- A = 3, B = -1 → False

---

# 🟦 **1. Question Explanation**

A number is **negative** if it is **less than 0**.

So you must check:

- Is **A < 0**?
- Is **B < 0**?

If both are True → print **True**
Else → print **False**

This uses:

- Comparison operator `<`
- Boolean `and`

---

# 🟩 **2. Approach**

1. Read A and B from input.
2. Convert them into integers.
3. Check if A < 0
4. Check if B < 0
5. Combine the results using `and`
6. Print the final boolean result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Accept input**

```python
first_number = int(input())
second_number = int(input())
```

### **Step 2: Compare both with 0**

```python
result = (first_number < 0) and (second_number < 0)
```

### **Step 3: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
first_number = int(input())
second_number = int(input())

result = (first_number < 0) and (second_number < 0)

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
-1
-2
```

### **Dry Run**

| Step | Code/Operation                 | Explanation                               | Value/Result |
| ---- | ------------------------------ | ----------------------------------------- | ------------ |
| 1    | `first_number = int(input())`  | Read first number and convert to integer  | -1           |
| 2    | `second_number = int(input())` | Read second number and convert to integer | -2           |
| 3    | `first_number < 0`             | Check if -1 is negative                   | True         |
| 4    | `second_number < 0`            | Check if -2 is negative                   | True         |
| 5    | `(True) and (True)`            | Combine conditions using AND              | True         |
| 6    | `print(result)`                | Print the result                          | True         |

### **Final Output**

```
True
```

---
