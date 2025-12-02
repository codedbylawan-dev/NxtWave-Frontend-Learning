# 🔹 **Question: Compare Numbers – 3**

Write a program that reads two integers **A** and **B**, and checks if:

- **Both A and B are positive numbers**
  **OR**
- **Both A and B are less than 70**

If either condition is true → print **True**,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

You must check **two separate conditions**:

### ✔ Condition 1:

Both numbers are **positive**
→ `(A > 0) and (B > 0)`

### ✔ Condition 2:

Both numbers are **less than 70**
→ `(A < 70) and (B < 70)`

### Final condition:

```
Condition 1 OR Condition 2
```

If either one is true → output **True**.

---

# 🟩 **2. Approach**

1. Read A and B
2. Check if both are positive
3. Check if both are less than 70
4. Combine using `or`
5. Print the result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
first_number = int(input())
second_number = int(input())
```

### **Step 2: Check positivity**

```python
are_positive = (first_number > 0) and (second_number > 0)
```

### **Step 3: Check less-than-70 condition**

```python
are_less_than = (first_number < 70) and (second_number < 70)
```

### **Step 4: Combine using OR**

```python
result = are_positive or are_less_than
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

are_positive = (first_number > 0) and (second_number > 0)
are_less_than = (first_number < 70) and (second_number < 70)

result = are_positive or are_less_than

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
200
50
```

### **Dry Run**

| Step | Code/Operation                   | Explanation                           | Value/Result |
| ---- | -------------------------------- | ------------------------------------- | ------------ |
| 1    | `first_number = int(input())`    | Read first number                     | 200          |
| 2    | `second_number = int(input())`   | Read second number                    | 50           |
| 3    | `first_number > 0`               | Check if 200 is positive              | True         |
| 4    | `second_number > 0`              | Check if 50 is positive               | True         |
| 5    | `are_positive = True and True`   | Both numbers are positive             | True         |
| 6    | `first_number < 70`              | Check if 200 < 70                     | False        |
| 7    | `second_number < 70`             | Check if 50 < 70                      | True         |
| 8    | `are_less_than = False and True` | Both must be < 70 → False             | False        |
| 9    | `result = True or False`         | One condition is True → result = True | True         |
| 10   | `print(result)`                  | Output the result                     | True         |

### **Final Output**

```
True
```

---
