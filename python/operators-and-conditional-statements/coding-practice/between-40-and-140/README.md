# ✅ **Between 40 and 140 — Solved**

## **Question**

Write a program that reads two numbers **A** and **B** and checks if **any one** of them is between **40 and 140** (exclusive).

- If **A** or **B** is between 40 and 140 → print
  **Between 40 and 140: Yes**
- Otherwise → print
  **Between 40 and 140: No**

---

# 📘 **Outline**

### **Approach**

1. Read the two input numbers
2. Check if **either** number lies between 40 and 140
3. Print the correct message

---

# 📘 **Step-by-Step Explanation**

### **Step 1: Read the input numbers**

```python
first_number = int(input())
second_number = int(input())
```

---

### **Step 2: Check if the numbers are between 40 and 140**

A number is **between 40 and 140** if:

```
number > 40 AND number < 140
```

```python
is_first_between = (first_number > 40) and (first_number < 140)
is_second_between = (second_number > 40) and (second_number < 140)
```

---

### **Step 3: Print the result**

If **any one** of the conditions is true, print **Yes**.

```python
if is_first_between or is_second_between:
    print("Between 40 and 140: Yes")
else:
    print("Between 40 and 140: No")
```

---

# ✅ **Final Solution Code**

```python
first_number = int(input())
second_number = int(input())

is_first_between = (first_number > 40) and (first_number < 140)
is_second_between = (second_number > 40) and (second_number < 140)

if is_first_between or is_second_between:
    print("Between 40 and 140: Yes")
else:
    print("Between 40 and 140: No")
```

---

# 📌 **Examples**

### **Input**

```
12
100
```

A = 12 → not between
B = 100 → ✔ between
**Output:**

```
Between 40 and 140: Yes
```

---

### **Input**

```
33
4
```

Neither value is between 40 and 140.
**Output:**

```
Between 40 and 140: No
```

---
