# 🔹 **Question: Compare Numbers – 4**

Write a program that reads two integers **A** and **B**, and checks whether:

- **One number is less than 60**,
  **AND**
- **One number is greater than 80**

If both conditions are true → print **True**,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

To satisfy the condition, BOTH must be true:

### ✔ Condition 1:

At least one of A or B is **less than 60**
→ `(A < 60) or (B < 60)`

### ✔ Condition 2:

At least one of A or B is **greater than 80**
→ `(A > 80) or (B > 80)`

### Final condition:

```
(One number < 60) AND (One number > 80)
```

This means the two conditions must **both** be true, even if the same number is not used for both.

---

# 🟩 **2. Approach**

1. Read A and B
2. Check if at least one number is < 60
3. Check if at least one number is > 80
4. Combine using `and`
5. Print the result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
first_number = int(input())
second_number = int(input())
```

### **Step 2: Check < 60 condition**

```python
is_less_than = (first_number < 60) or (second_number < 60)
```

### **Step 3: Check > 80 condition**

```python
is_greater_than = (first_number > 80) or (second_number > 80)
```

### **Step 4: Final result**

```python
result = is_less_than and is_greater_than
```

### **Step 5: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
first_number = int(input())
second_number = int(input())

is_less_than = (first_number < 60) or (second_number < 60)
is_greater_than = (first_number > 80) or (second_number > 80)

result = is_less_than and is_greater_than

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
50
90
```

### **Dry Run**

| Step | Code/Operation                    | Explanation                                  | Value/Result |
| ---- | --------------------------------- | -------------------------------------------- | ------------ |
| 1    | `first_number = int(input())`     | Read first number                            | 50           |
| 2    | `second_number = int(input())`    | Read second number                           | 90           |
| 3    | `first_number < 60`               | 50 < 60 → True                               | True         |
| 4    | `second_number < 60`              | 90 < 60 → False                              | False        |
| 5    | `is_less_than = True or False`    | One number is less than 60                   | True         |
| 6    | `first_number > 80`               | 50 > 80 → False                              | False        |
| 7    | `second_number > 80`              | 90 > 80 → True                               | True         |
| 8    | `is_greater_than = False or True` | One number is greater than 80                | True         |
| 9    | `result = True and True`          | Both conditions must be true → result = True | True         |
| 10   | `print(result)`                   | Output result                                | True         |

### **Final Output**

```
True
```

---
