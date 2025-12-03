# 🔹 **Question: Compare Numbers – 10**

Write a program that reads two numbers **A** and **B** and checks if **both** of the below conditions are satisfied:

1️⃣ **One of A or B is less than 20**
2️⃣ **One of A or B is greater than 30**

If both conditions are true → print **True**
Otherwise → print **False**

---

# 🟦 **1. Question Explanation**

We need to verify **two separate conditions**:

### ✔ Condition 1:

At least one of the numbers should be **< 20**

### ✔ Condition 2:

At least one of the numbers should be **> 30**

**Both** conditions must be satisfied to print **True**.

This problem practices:

- Comparison operators
- Logical **and / or** usage
- Multi-condition checking

---

# 🟩 **2. Approach**

1. Read A and B
2. Check if one number is less than 20
3. Check if one number is greater than 30
4. Combine both using `and`
5. Print the result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
A = int(input())
B = int(input())
```

### **Step 2: Check if one number < 20**

```python
is_less_than_20 = (A < 20) or (B < 20)
```

### **Step 3: Check if one number > 30**

```python
is_greater_than_30 = (A > 30) or (B > 30)
```

### **Step 4: Combine the results**

```python
result = is_less_than_20 and is_greater_than_30
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

is_less_than_20 = (A < 20) or (B < 20)
is_greater_than_30 = (A > 30) or (B > 30)

result = is_less_than_20 and is_greater_than_30

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
15
32
```

### **Dry Run**

| Step | Operation                                   | Explanation               | Result |
| ---- | ------------------------------------------- | ------------------------- | ------ |
| 1    | A = 15, B = 32                              | Input values              | —      |
| 2    | is_less_than_20 = (15 < 20) or (32 < 20)    | True or False             | True   |
| 3    | is_greater_than_30 = (15 > 30) or (32 > 30) | False or True             | True   |
| 4    | result = True and True                      | Both conditions satisfied | True   |
| 5    | print(result)                               | Output                    | True   |

### **Final Output**

```
True
```

---
