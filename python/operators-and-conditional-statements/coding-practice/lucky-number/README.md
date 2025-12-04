# ✅ **Lucky Number — Solved**

## **Question**

Write a program that reads two numbers **A** and **B** and checks if _any_ of these conditions is satisfied:

1️⃣ One of A or B is **equal to 6**
2️⃣ The **sum** of A and B is **6**
3️⃣ The **difference** between A and B is **6**

- (difference means **A - B** or **B - A**, whichever equals 6)

### **Output**

- If **any condition** is satisfied → print **Lucky**
- Otherwise → print **Not Lucky**

---

# 📘 **Outline**

### **Approach**

1. Read A and B
2. Check all three conditions
3. Print the appropriate result

---

# 📘 **Step-by-Step Explanation**

### **Step 1: Read the input numbers**

```python
a = int(input())
b = int(input())
```

---

### **Step 2: Check the conditions**

#### ✔ Condition 1: One of the numbers is 6

```python
is_any_number_has = (a == 6) or (b == 6)
```

#### ✔ Condition 2: Sum equals 6

```python
is_sum_equal_to_6 = (a + b) == 6
```

#### ✔ Condition 3: Difference equals 6

Either **a - b = 6** or **b - a = 6**

```python
is_diff_equal_to_6 = (a - b == 6) or (b - a == 6)
```

---

### **Step 3: Print the result**

If **any** of the three conditions is TRUE → print **Lucky**

```python
if is_any_number_has or is_sum_equal_to_6 or is_diff_equal_to_6:
    print("Lucky")
else:
    print("Not Lucky")
```

---

# ✅ **Final Complete Solution**

```python
a = int(input())
b = int(input())

is_any_number_has = (a == 6) or (b == 6)
is_sum_equal_to_6 = (a + b) == 6
is_diff_equal_to_6 = (a - b == 6) or (b - a == 6)

if is_any_number_has or is_sum_equal_to_6 or is_diff_equal_to_6:
    print("Lucky")
else:
    print("Not Lucky")
```

---

# 📌 **Examples**

### **Input**

```
4
10
```

Check difference: |4 – 10| = 6 → ✔
Output:

```
Lucky
```

---

### **Input**

```
3
2
```

None of the conditions are satisfied → ✖
Output:

```
Not Lucky
```

---

### **Input**

```
15
9
```

Difference: 15 – 9 = 6 → ✔
Output:

```
Lucky
```

---
