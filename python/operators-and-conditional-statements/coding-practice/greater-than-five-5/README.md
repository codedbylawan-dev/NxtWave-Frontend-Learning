# 🔹 **Question: Greater than Five – 2**

Write a program that reads three numbers **A**, **B**, and **C**, and checks if **each** of the given numbers is **greater than 5**.

### **Input**

- First line → integer A
- Second line → integer B
- Third line → integer C

### **Output**

Print **True** if **all three** numbers are greater than 5,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

A number is considered valid if:

```
number > 5
```

We must check this condition for:

- A
- B
- C

Final condition:

```
(A > 5) AND (B > 5) AND (C > 5)
```

If **all** are True → output True
If **any** is False → output False

---

# 🟩 **2. Approach**

1. Read the three numbers
2. Check if A > 5
3. Check if B > 5
4. Check if C > 5
5. Combine using `and`
6. Print the final result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
A = int(input())
B = int(input())
C = int(input())
```

### **Step 2: Compare each number**

```python
is_A_valid = A > 5
is_B_valid = B > 5
is_C_valid = C > 5
```

### **Step 3: Combine using AND**

```python
result = is_A_valid and is_B_valid and is_C_valid
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

is_A_valid = A > 5
is_B_valid = B > 5
is_C_valid = C > 5

result = is_A_valid and is_B_valid and is_C_valid

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
7
18
239
```

### **Dry Run**

| Step | Code/Operation                    | Explanation                             | Value/Result |
| ---- | --------------------------------- | --------------------------------------- | ------------ |
| 1    | `A = int(input())`                | Read first number                       | 7            |
| 2    | `B = int(input())`                | Read second number                      | 18           |
| 3    | `C = int(input())`                | Read third number                       | 239          |
| 4    | `A > 5`                           | Check if 7 > 5                          | True         |
| 5    | `B > 5`                           | Check if 18 > 5                         | True         |
| 6    | `C > 5`                           | Check if 239 > 5                        | True         |
| 7    | `result = True and True and True` | All conditions are True → result = True | True         |
| 8    | `print(result)`                   | Output result                           | True         |

### **Final Output**

```
True
```

---
