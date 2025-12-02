# 🔹 **Question: Less than 15**

Write a program that reads three integers **A, B, and C**, and checks if **any one** of the numbers is **less than 15**.

### **Input**

- Line 1 → integer A
- Line 2 → integer B
- Line 3 → integer C

### **Output**

Print **True** if **at least one** number is less than 15,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

A number is considered valid if:

```
number < 15
```

You must check this condition for **A**, **B**, and **C**.

If **any one** among them is less than 15 → output **True**.

This requires using the `or` operator.

---

# 🟩 **2. Approach**

1. Read A, B, C from input
2. Check if A < 15
3. Check if B < 15
4. Check if C < 15
5. Use `or` to combine the conditions
6. Print the final result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
A = int(input())
B = int(input())
C = int(input())
```

### **Step 2: Compare each number with 15**

```python
is_A_less = A < 15
is_B_less = B < 15
is_C_less = C < 15
```

### **Step 3: Combine using OR**

```python
result = is_A_less or is_B_less or is_C_less
```

### **Step 4: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
A = int(input())
B = int(input())
C = int(input())

is_A_less = A < 15
is_B_less = B < 15
is_C_less = C < 15

result = is_A_less or is_B_less or is_C_less

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
18
2
20
```

### **Dry Run**

| Step | Code/Operation                    | Explanation                  | Value/Result |
| ---- | --------------------------------- | ---------------------------- | ------------ |
| 1    | `A = int(input())`                | Read first number            | 18           |
| 2    | `B = int(input())`                | Read second number           | 2            |
| 3    | `C = int(input())`                | Read third number            | 20           |
| 4    | `A < 15`                          | Check if 18 < 15             | False        |
| 5    | `B < 15`                          | Check if 2 < 15              | True         |
| 6    | `C < 15`                          | Check if 20 < 15             | False        |
| 7    | `result = False or True or False` | At least one is less than 15 | True         |
| 8    | `print(result)`                   | Output result                | True         |

### **Final Output**

```
True
```

---
