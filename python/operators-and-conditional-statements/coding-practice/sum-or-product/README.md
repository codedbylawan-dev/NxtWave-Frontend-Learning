# ✅ **Sum or Product — Solved**

## **Question**

Write a program that reads two numbers **A** and **B** and checks whether:

- The **sum** of A and B is **less than 10**

### **If the condition is true:**

Print **A + B**

### **Otherwise:**

Print **A × B**

---

# 📘 **Outline**

### **Approach**

1. Read the two input numbers
2. Calculate their sum
3. Check if the sum is less than 10
4. Print either the sum or the product based on the condition

---

# 📘 **Step-by-Step Explanation**

### **Step 1: Read the two numbers**

```python
a = int(input())
b = int(input())
```

---

### **Step 2: Calculate the sum**

```python
sum_of_numbers = a + b
```

---

### **Step 3: Check if the sum is less than 10**

If the sum is < 10 → print the sum
Else → print the product

```python
if sum_of_numbers < 10:
    print(sum_of_numbers)
else:
    print(a * b)
```

---

# ✅ **Final Complete Program**

```python
a = int(input())
b = int(input())

sum_of_numbers = a + b

if sum_of_numbers < 10:
    print(sum_of_numbers)
else:
    print(a * b)
```

---

# 📌 **Examples**

### **Input**

```
1
2
```

### **Output**

```
3
```

---

### **Input**

```
42
10
```

### **Output**

```
420
```

---
