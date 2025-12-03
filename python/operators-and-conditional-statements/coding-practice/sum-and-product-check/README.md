# 🔹 **Question: Sum and Product Check**

Write a program that reads two integers **A** and **B** and checks whether:

- The **sum** of A and B has **less than 3 digits**,
  **AND**
- The **product** of A and B has **less than 3 digits**

If both conditions are true → print **True**,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

A number has **less than 3 digits** if it is between:

```
0 to 99   → 2 digits
Or
-99 to -1 → 2 digits (negative also counted by length)
```

But easiest check:
Convert to string → count characters → ignore minus sign.

We check:

### ✔ Condition 1:

```
length of sum < 3
```

### ✔ Condition 2:

```
length of product < 3
```

Final condition:

```
(sum < 3 digits) AND (product < 3 digits)
```

---

# 🟩 **2. Approach**

1. Read A and B
2. Compute sum
3. Convert sum to string and check length
4. Compute product
5. Convert product to string and check length
6. Combine checks with AND
7. Print the result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read input numbers**

```python
A = int(input())
B = int(input())
```

### **Step 2: Compute sum**

```python
sum_val = A + B
```

### **Step 3: Check sum length**

```python
sum_digits = len(str(sum_val))
is_sum_valid = sum_digits < 3
```

### **Step 4: Compute product**

```python
product_val = A * B
```

### **Step 5: Check product length**

```python
product_digits = len(str(product_val))
is_product_valid = product_digits < 3
```

### **Step 6: Combine**

```python
result = is_sum_valid and is_product_valid
```

### **Step 7: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
A = int(input())
B = int(input())

sum_val = A + B
sum_digits = len(str(sum_val))
is_sum_valid = sum_digits < 3

product_val = A * B
product_digits = len(str(product_val))
is_product_valid = product_digits < 3

result = is_sum_valid and is_product_valid

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
17
4
```

### **Dry Run**

| Step | Code/Operation             | Explanation                    | Value/Result |
| ---- | -------------------------- | ------------------------------ | ------------ |
| 1    | `A = int(input())`         | Read first number              | 17           |
| 2    | `B = int(input())`         | Read second number             | 4            |
| 3    | `sum_val = A + B`          | Compute sum (17+4)             | 21           |
| 4    | `len(str(sum_val))`        | "21" has 2 digits              | 2            |
| 5    | `is_sum_valid = 2 < 3`     | Sum has less than 3 digits     | True         |
| 6    | `product_val = A * B`      | Compute product (17×4)         | 68           |
| 7    | `len(str(product_val))`    | "68" has 2 digits              | 2            |
| 8    | `is_product_valid = 2 < 3` | Product has less than 3 digits | True         |
| 9    | `result = True and True`   | Both conditions true           | True         |
| 10   | `print(result)`            | Output result                  | True         |

### **Final Output**

```
True
```

---
