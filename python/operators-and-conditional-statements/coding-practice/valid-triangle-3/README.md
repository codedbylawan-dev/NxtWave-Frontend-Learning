# ✅ **Valid Triangle – 3 (Solved)**

---

# 🔹 **Question Summary**

You are given three sides of a triangle: **A, B, C**.
A valid triangle must satisfy the **Triangle Inequality Rule**:

### ✔ The sum of any two sides must be **greater than** the third side:

- A + B > C
- B + C > A
- C + A > B

If **all three** conditions are true → **It's a Triangle**
Otherwise → **It's not a Triangle**

---

# 🔹 **Step-by-Step Outline**

### **Step 1: Read the input sides**

Use `input()` and convert to integers:

```python
first_side = int(input())
second_side = int(input())
third_side = int(input())
```

### **Step 2: Check triangle conditions**

```python
is_greater_than_third_side = (first_side + second_side) > third_side
is_greater_than_first_side = (second_side + third_side) > first_side
is_greater_than_second_side = (third_side + first_side) > second_side
```

### **Step 3: Print results**

If **all** conditions are true → print `"It's a Triangle"`
Otherwise → print `"It's not a Triangle"`

---

# 🔹 **Final Code Solution**

```python
first_side = int(input())
second_side = int(input())
third_side = int(input())

is_greater_than_third_side = (first_side + second_side) > third_side
is_greater_than_first_side = (second_side + third_side) > first_side
is_greater_than_second_side = (third_side + first_side) > second_side

if is_greater_than_first_side and is_greater_than_second_side and is_greater_than_third_side:
    print("It's a Triangle")
else:
    print("It's not a Triangle")
```

---

# 🔹 **Example Walkthrough**

### **Input:**

```
4
5
3
```

### **Checks:**

- 4 + 5 = 9 > 3 ✔
- 5 + 3 = 8 > 4 ✔
- 3 + 4 = 7 > 5 ✔

✅ All conditions true →
**Output:**

```
It's a Triangle
```

---
