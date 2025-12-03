# 🔹 **Question: Sum and Product Check – 2**

Write a program that reads two integers **A** and **B** and checks whether:

### ✔ The **sum** of A and B is **negative**,

**OR**

### ✔ The **product** of A and B is **negative**

If **any one** of these conditions is True → print **True**,
otherwise → print **False**.

---

# 🟦 **1. Question Explanation**

You must check two things:

### **Condition 1: Sum is negative**

```
A + B < 0
```

### **Condition 2: Product is negative**

```
A * B < 0
```

If **either** is True → result is **True**.

Example:
A = 5, B = -3

- Sum = 2 → Not negative
- Product = -15 → Negative ✔
  → Final output: **True**

---

# 🟩 **2. Approach**

1. Read A and B
2. Compute sum
3. Compute product
4. Check if sum < 0
5. Check if product < 0
6. Combine using OR
7. Print result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
A = int(input())
B = int(input())
```

### **Step 2: Compute sum and product**

```python
sum_val = A + B
product_val = A * B
```

### **Step 3: Check conditions**

```python
is_sum_negative = (sum_val < 0)
is_product_negative = (product_val < 0)
```

### **Step 4: Combine**

```python
result = is_sum_negative or is_product_negative
```

### **Step 5: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
A = int(input())
B = int(input())

sum_val = A + B
product_val = A * B

is_sum_negative = sum_val < 0
is_product_negative = product_val < 0

result = is_sum_negative or is_product_negative

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
5
-3
```

### **Dry Run**

| Step | Operation                     | Explanation         | Value/Result |
| ---- | ----------------------------- | ------------------- | ------------ |
| 1    | A = 5, B = -3                 | Read inputs         | 5, -3        |
| 2    | sum_val = 5 + (-3)            | Calculate sum       | 2            |
| 3    | product_val = 5 \* -3         | Calculate product   | -15          |
| 4    | is_sum_negative = 2 < 0       | Sum not negative    | False        |
| 5    | is_product_negative = -15 < 0 | Product is negative | True         |
| 6    | result = False or True        | One condition True  | True         |
| 7    | print(result)                 | Output              | True         |

### **Final Output**

```
True
```

---
