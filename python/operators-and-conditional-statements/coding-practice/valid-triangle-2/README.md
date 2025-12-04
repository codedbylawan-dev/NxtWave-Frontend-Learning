# 🔹 **Question: Valid Triangle – 2**

Write a program that reads three angles **A, B, C** of a triangle and checks whether their sum is **equal to 180**.

- If **A + B + C == 180**, print this triangle pattern:

```
*
**
***
```

- Otherwise, print:

```
Not a Valid Triangle
```

---

# 🟦 **1. Question Explanation**

A set of three angles forms a **valid triangle** only when:

### ✅ **A + B + C = 180**

If the angles form a valid triangle, you must print:

- Line 1 → `*`
- Line 2 → `**`
- Line 3 → `***`

If invalid → print `"Not a Valid Triangle"`.

---

# 🟩 **2. Approach**

1. Read angles A, B, and C
2. Calculate the sum
3. Compare sum with **180**
4. If valid → print star pattern
5. Else → print the error message

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read three angles**

```python
first_angle = int(input())
second_angle = int(input())
third_angle = int(input())
```

### **Step 2: Calculate the sum**

```python
sum_of_three_angles = first_angle + second_angle + third_angle
```

### **Step 3: Check if valid**

```python
if sum_of_three_angles == 180:
```

### **Step 4: Print triangle pattern**

```python
print("*")
print("*" * 2)
print("*" * 3)
```

### **Else: Print invalid message**

```python
print("Not a Valid Triangle")
```

---

# 🟧 **4. Final Code**

```python
first_angle = int(input())
second_angle = int(input())
third_angle = int(input())

sum_of_three_angles = first_angle + second_angle + third_angle

if sum_of_three_angles == 180:
    print("*")
    print("*" * 2)
    print("*" * 3)
else:
    print("Not a Valid Triangle")
```

---

# 🟥 **5. Dry Run (Preview Table)**

### For input:

```
60
45
75
```

| Step | Operation        | Value              |
| ---- | ---------------- | ------------------ |
| 1    | Read angles      | 60, 45, 75         |
| 2    | Compute sum      | 60 + 45 + 75 = 180 |
| 3    | Check sum == 180 | True               |
| 4    | Print pattern    | `*` → `**` → `***` |

**Final Output:**

```
*
**
***
```

---
