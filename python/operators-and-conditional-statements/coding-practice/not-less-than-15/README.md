# 🔹 **Question: Not Less than 15**

Write a program that reads two integers **A** and **B**, and checks whether **at least one** of the numbers is **not less than 15**.

A number is **not less than 15** when:

```
number >= 15
```

### **Input**

- First line → integer A
- Second line → integer B

### **Output**

Print **True** if **any** of the given numbers is **not less than 15**,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

You must check two conditions:

### ✔ Condition 1: `A >= 15`

### ✔ Condition 2: `B >= 15`

If **at least one** of these is True → output **True**.

Final condition:

```
(A >= 15) OR (B >= 15)
```

---

# 🟩 **2. Approach**

1. Read A and B
2. Check if A is not less than 15 (A >= 15)
3. Check if B is not less than 15 (B >= 15)
4. Combine using `or`
5. Print the final result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
A = int(input())
B = int(input())
```

### **Step 2: Individual comparisons**

```python
is_A_not_less = A >= 15
is_B_not_less = B >= 15
```

### **Step 3: Combine using OR**

```python
result = is_A_not_less or is_B_not_less
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

is_A_not_less = A >= 15
is_B_not_less = B >= 15

result = is_A_not_less or is_B_not_less

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
921
6
```

### **Dry Run**

| Step | Code/Operation           | Explanation                             | Value/Result |
| ---- | ------------------------ | --------------------------------------- | ------------ |
| 1    | `A = int(input())`       | Read first number                       | 921          |
| 2    | `B = int(input())`       | Read second number                      | 6            |
| 3    | `A >= 15`                | Check if 921 is not less than 15        | True         |
| 4    | `B >= 15`                | Check if 6 is not less than 15          | False        |
| 5    | `result = True or False` | At least one number is not less than 15 | True         |
| 6    | `print(result)`          | Output result                           | True         |

### **Final Output**

```
True
```

---
