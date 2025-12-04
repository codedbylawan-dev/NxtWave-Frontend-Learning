# ✅ **Qualified or Not Qualified — Solved**

## **Question**

You need to read two marks:

- **M** → Maths
- **P** → Physics

Then check **either** of these conditions:

### ✔ Condition 1

Both **M > 35** and **P > 35**

### ✔ Condition 2

The **sum** of M and P is **≥ 100**

If **any one** of the above conditions is true → print **Qualified**
Else → print **Not Qualified**

---

# 📘 **Outline**

### **Approach**

1. Read marks M and P
2. Check if both marks are greater than 35
3. Check if sum of M and P is ≥ 100
4. If any condition is true → print “Qualified”
5. Else → print “Not Qualified”

---

# 📘 **Step-by-Step Explanation**

### **Step 1: Read the input marks**

```python
maths = int(input())
physics = int(input())
```

---

### **Step 2: Check if both marks are greater than 35**

```python
is_both_greater = (maths > 35) and (physics > 35)
```

---

### **Step 3: Check if sum is ≥ 100**

```python
sum_of_marks = maths + physics
is_sum_greater = (sum_of_marks >= 100)
```

---

### **Step 4: Decide Qualification**

```python
if is_both_greater or is_sum_greater:
    print("Qualified")
else:
    print("Not Qualified")
```

---

# ✅ **Final Complete Program**

```python
maths = int(input())
physics = int(input())

is_both_greater = (maths > 35) and (physics > 35)
sum_of_marks = maths + physics
is_sum_greater = (sum_of_marks >= 100)

if is_both_greater or is_sum_greater:
    print("Qualified")
else:
    print("Not Qualified")
```

---

# 📌 **Examples**

### **Input**

```
50
40
```

### **Output**

```
Qualified
```

---

### **Input**

```
30
49
```

### **Output**

```
Not Qualified
```

---
