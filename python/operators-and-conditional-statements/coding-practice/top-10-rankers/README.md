# ✅ **Top 10 Rankers — Solved**

## **Question**

Write a program that reads the rank of a student (**R**) and checks whether the student belongs to the top 10 rankers.

- If **R < 10**, print **HONOR STUDENT**
- Otherwise, print **NORMAL STUDENT**

---

# 📘 **Outline**

### **Approach**

1. Read the rank of the student
2. Check if the rank is less than 10
3. Print the correct result

---

# 📘 **Step-by-Step Explanation**

### **Step 1: Read the student's rank**

Use `input()` to read the rank and convert it to an integer:

```python
rank = int(input())
```

---

### **Step 2: Check if the rank is less than 10**

A student is an **HONOR STUDENT** only if:

```
rank < 10
```

Use an if–else statement to check:

```python
if rank < 10:
    print("HONOR STUDENT")
else:
    print("NORMAL STUDENT")
```

---

# ✅ **Final Complete Program**

```python
rank = int(input())

if rank < 10:
    print("HONOR STUDENT")
else:
    print("NORMAL STUDENT")
```

---

# 📌 **Examples**

### **Input**

```
1
```

### **Output**

```
HONOR STUDENT
```

---

### **Input**

```
15
```

### **Output**

```
NORMAL STUDENT
```

---
