# 🔹 **Question: Compare Numbers – 5**

Write a program that reads two integers **A** and **B**, and checks whether:

- **One of the numbers is negative**,
  **AND**
- **The product of A and B is greater than or equal to –46**

If _both_ conditions are true → print **True**,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

Two conditions must be checked:

### ✔ Condition 1: One number is negative

A number is negative if it is `< 0`.

So:

```
(A < 0) OR (B < 0)
```

### ✔ Condition 2: Product ≥ –46

Let `P = A * B`

Check:

```
P >= -46
```

### Final condition:

```
((A < 0) OR (B < 0))  AND  (A * B >= -46)
```

Both must be True to output **True**.

---

# 🟩 **2. Approach**

1. Read A and B
2. Compute product
3. Check if one number is negative
4. Check if product ≥ –46
5. Combine both using `and`
6. Print the result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
A = int(input())
B = int(input())
```

### **Step 2: Calculate product**

```python
product = A * B
```

### **Step 3: Check negative condition**

```python
is_negative = (A < 0) or (B < 0)
```

### **Step 4: Check product condition**

```python
is_product_valid = product >= -46
```

### **Step 5: Combine**

```python
result = is_negative and is_product_valid
```

### **Step 6: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
A = int(input())
B = int(input())

product = A * B
is_negative = (A < 0) or (B < 0)
is_product_valid = product >= -46

result = is_negative and is_product_valid

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
-10
1
```

### **Dry Run**

| Step | Code/Operation                | Explanation                                | Value/Result |
| ---- | ----------------------------- | ------------------------------------------ | ------------ |
| 1    | `A = int(input())`            | Read first number                          | -10          |
| 2    | `B = int(input())`            | Read second number                         | 1            |
| 3    | `product = A * B`             | Compute the product                        | -10          |
| 4    | `A < 0`                       | Check if -10 is negative                   | True         |
| 5    | `B < 0`                       | Check if 1 is negative                     | False        |
| 6    | `is_negative = True or False` | At least one number is negative            | True         |
| 7    | `product >= -46`              | Check if -10 ≥ -46                         | True         |
| 8    | `result = True and True`      | Both conditions True → final result = True | True         |
| 9    | `print(result)`               | Output                                     | True         |

### **Final Output**

```
True
```

---
