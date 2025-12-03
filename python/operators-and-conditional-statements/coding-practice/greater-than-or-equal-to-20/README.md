# 🔹 **Question: Greater than or Equal to 20**

Write a program that reads three integers **A**, **B**, and **C**, and checks whether **each** of the numbers is **greater than or equal to 20**.

### **Input**

- Line 1 → A
- Line 2 → B
- Line 3 → C

### **Output**

Print **True** if **all three** numbers are ≥ 20,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

A number is valid if:

```
number >= 20
```

We must check this condition for:

- A
- B
- C

Final condition:

```
(A >= 20) AND (B >= 20) AND (C >= 20)
```

Only if **all** are True → output **True**.

---

# 🟩 **2. Approach**

1. Read A, B, C
2. Check if A ≥ 20
3. Check if B ≥ 20
4. Check if C ≥ 20
5. Combine all using `and`
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
is_A_valid = A >= 20
is_B_valid = B >= 20
is_C_valid = C >= 20
```

### **Step 3: Combine using AND**

```python
result = is_A_valid and is_B_valid and is_C_valid
```

### **Step 4: Print result**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
A = int(input())
B = int(input())
C = int(input())

is_A_valid = A >= 20
is_B_valid = B >= 20
is_C_valid = C >= 20

result = is_A_valid and is_B_valid and is_C_valid

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
10
20
30
```

### **Dry Run**

| Step | Code/Operation                     | Explanation                   | Value/Result |
| ---- | ---------------------------------- | ----------------------------- | ------------ |
| 1    | `A = int(input())`                 | Read first number             | 10           |
| 2    | `B = int(input())`                 | Read second number            | 20           |
| 3    | `C = int(input())`                 | Read third number             | 30           |
| 4    | `A >= 20`                          | Check if 10 ≥ 20              | False        |
| 5    | `B >= 20`                          | Check if 20 ≥ 20              | True         |
| 6    | `C >= 20`                          | Check if 30 ≥ 20              | True         |
| 7    | `result = False and True and True` | One is False → result = False | False        |
| 8    | `print(result)`                    | Output                        | False        |

### **Final Output**

```
False
```

---
