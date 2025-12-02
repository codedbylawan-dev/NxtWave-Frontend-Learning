# 🔹 **Question: Positive Number**

Write a program that reads two integers **A** and **B**, and checks whether **one** of the given numbers is **positive**.

### **Input**

- First line → integer **A**
- Second line → integer **B**

### **Output**

Print **True** if **at least one** number is positive,
otherwise print **False**.

### **Example**

- A = 4, B = -6 → True
- A = -12, B = -22 → False

---

# 🟦 **1. Question Explanation**

A number is **positive** if it is **greater than 0**.

You need to check:

- Is A > 0?
- Is B > 0?

If **any one** of them is positive → output **True**.
If **both are NOT positive** → output **False**.

This problem practices:

- Boolean logic
- Using the `or` operator
- Comparison operators

---

# 🟩 **2. Approach**

1. Read A and B from input.
2. Convert the values to integers.
3. Check if A is positive.
4. Check if B is positive.
5. Combine conditions using `or`.
6. Print the result.

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
first_number = int(input())
second_number = int(input())
```

### **Step 2: Check positivity**

A number is positive if it's **greater than 0**.

```python
result = (first_number > 0) or (second_number > 0)
```

### **Step 3: Print the result**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
first_number = int(input())
second_number = int(input())

result = (first_number > 0) or (second_number > 0)

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
4
-6
```

### **Dry Run**

| Step | Code/Operation                 | Explanation                               | Value/Result |
| ---- | ------------------------------ | ----------------------------------------- | ------------ |
| 1    | `first_number = int(input())`  | Read first number and convert to integer  | 4            |
| 2    | `second_number = int(input())` | Read second number and convert to integer | -6           |
| 3    | `first_number > 0`             | Check if 4 is positive                    | True         |
| 4    | `second_number > 0`            | Check if -6 is positive                   | False        |
| 5    | `(True) or (False)`            | Check if **either** number is positive    | True         |
| 6    | `print(result)`                | Print output                              | True         |

### **Final Output**

```
True
```

---
