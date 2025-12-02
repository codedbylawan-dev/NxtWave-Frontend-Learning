# 🔹 **Question: Greater than Nine**

Write a program that reads two integers **A** and **B**, and checks whether **both** numbers are **greater than 9**.

### **Input**

- First line → integer **A**
- Second line → integer **B**

### **Output**

Print **True** if both A and B are greater than 9,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

You must check:

- Is **A > 9**?
- Is **B > 9**?

If **both** are True → output **True**.
If **any one is False** → output **False**.

This problem helps you practice:

- Boolean logic
- Comparison operators
- Using `and` in Python

---

# 🟩 **2. Approach**

1. Read A and B.
2. Convert them to integers.
3. Check `A > 9`.
4. Check `B > 9`.
5. Combine both using `and`.
6. Print the result.

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read input values**

Use `input()` and `int()` to get numbers.

```python
first_number = int(input())
second_number = int(input())
```

### **Step 2: Compare with 9**

Check if both values are greater than 9.

```python
result = (first_number > 9) and (second_number > 9)
```

### **Step 3: Print**

Print the final boolean result.

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
first_number = int(input())
second_number = int(input())

result = (first_number > 9) and (second_number > 9)

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
11
20
```

### **Dry Run**

| Step | Code/Operation                 | Explanation                              | Value/Result |
| ---- | ------------------------------ | ---------------------------------------- | ------------ |
| 1    | `first_number = int(input())`  | Read first value and convert to integer  | 11           |
| 2    | `second_number = int(input())` | Read second value and convert to integer | 20           |
| 3    | `first_number > 9`             | Check if first number is greater than 9  | True         |
| 4    | `second_number > 9`            | Check if second number is greater than 9 | True         |
| 5    | `(True) and (True)`            | Combine both conditions using AND        | True         |
| 6    | `print(result)`                | Print the final result                   | True         |

### **Final Output**

```
True
```

---
