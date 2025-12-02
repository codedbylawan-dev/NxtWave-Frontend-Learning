# 🔹 **Question: Compare Numbers – 2**

Write a program that reads two integers **A** and **B**, and checks whether:

- **At least one** of the numbers is **negative**,
  **AND**
- The **sum** of the numbers is **greater than 7**

If both conditions are true → print **True**,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

This problem requires checking **two conditions** at the same time:

### ✔ Condition 1:

One of the numbers must be **negative**
→ `(A < 0) or (B < 0)`

### ✔ Condition 2:

The sum must be **greater than 7**
→ `A + B > 7`

### Final Condition:

```
(One number is negative) AND (Sum > 7)
```

If **both** are True → output **True**.

---

# 🟩 **2. Approach**

1. Read A and B from input
2. Compute the sum of A and B
3. Check if one number is negative
4. Check if the sum is greater than 7
5. Combine using `and`
6. Print the result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
first_number = int(input())
second_number = int(input())
```

### **Step 2: Calculate sum**

```python
sum_of_numbers = first_number + second_number
```

### **Step 3: Check for negative number**

```python
is_negative = (first_number < 0) or (second_number < 0)
```

### **Step 4: Check if sum > 7**

```python
is_greater_than = sum_of_numbers > 7
```

### **Step 5: Final result**

```python
result = is_negative and is_greater_than
```

### **Step 6: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
first_number = int(input())
second_number = int(input())

sum_of_numbers = first_number + second_number
is_negative = (first_number < 0) or (second_number < 0)
is_greater_than = sum_of_numbers > 7

result = is_negative and is_greater_than

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
13
-3
```

### **Dry Run**

| Step | Code/Operation                                  | Explanation             | Value/Result |
| ---- | ----------------------------------------------- | ----------------------- | ------------ |
| 1    | `first_number = int(input())`                   | Read first number       | 13           |
| 2    | `second_number = int(input())`                  | Read second number      | -3           |
| 3    | `sum_of_numbers = first_number + second_number` | Calculate sum           | 10           |
| 4    | `first_number < 0`                              | Check if 13 is negative | False        |
| 5    | `second_number < 0`                             | Check if -3 is negative | True         |
| 6    | `is_negative = False or True`                   | One number is negative  | True         |
| 7    | `sum_of_numbers > 7`                            | Check if 10 > 7         | True         |
| 8    | `is_negative and is_greater_than`               | True and True → result  | True         |
| 9    | `print(result)`                                 | Output the result       | True         |

### **Final Output**

```
True
```

---
