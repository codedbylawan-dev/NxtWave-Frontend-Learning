# ✅ **Sum of Two Numbers (Solved)**

Write a program to print the **sum** of two integer inputs **A** and **B**.

---

## **Sample Input 1**

```
2
3
```

## **Sample Output 1**

```
5
```

---

## **Sample Input 2**

```
20
1
```

## **Sample Output 2**

```
21
```

---

# 🧭 **Outline**

**Question:** Sum of Two Numbers
**Approach:**

1. Read the first input (A).
2. Read the second input (B).
3. Convert both inputs to integers.
4. Add A and B.
5. Print the result.

---

# 📝 **Step-by-Step Explanation**

### **Step 1: Read the two inputs**

```python
a = input()
b = input()
```

These inputs come as **strings**, not numbers.

---

### **Step 2: Convert the inputs to integers**

```python
a = int(a)
b = int(b)
```

We convert because we need numeric addition, not string addition.

---

### **Step 3: Calculate the sum**

```python
result = a + b
```

---

### **Step 4: Print the result**

```python
print(result)
```

---

# ✅ **Final Solution**

```python
a = input()
b = input()
a = int(a)
b = int(b)
result = a + b
print(result)
```

---
