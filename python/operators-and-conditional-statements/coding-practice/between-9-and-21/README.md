# ✅ **Between 9 and 21 — Solved**

## **Question**

You are given **three numbers**: A, B, and C.
You must check if **any** of these numbers is **between 9 and 21** (exclusive).

If **at least one** number is between 9 and 21 → print **True**
Otherwise → print **False**

---

# 📘 **Outline**

### **Approach**

1. Read the three input numbers
2. Check if A is between 9 and 21
3. Check if B is between 9 and 21
4. Check if C is between 9 and 21
5. If any condition is true → print True, else False

---

# 📘 **Step-by-Step Explanation**

### **Step 1: Read the three numbers**

```python
a = int(input())
b = int(input())
c = int(input())
```

---

### **Step 2: Check if each number is between 9 and 21**

A number is **between 9 and 21** if:

```
number > 9 and number < 21
```

So:

```python
is_a_between = (a > 9) and (a < 21)
is_b_between = (b > 9) and (b < 21)
is_c_between = (c > 9) and (c < 21)
```

---

### **Step 3: Check if any of them is true**

```python
result = is_a_between or is_b_between or is_c_between
```

---

### **Step 4: Print the result**

```python
print(result)
```

---

# ✅ **Final Complete Program**

```python
a = int(input())
b = int(input())
c = int(input())

is_a_between = (a > 9) and (a < 21)
is_b_between = (b > 9) and (b < 21)
is_c_between = (c > 9) and (c < 21)

result = is_a_between or is_b_between or is_c_between

print(result)
```

---

# 📌 **Example Walkthroughs**

### **Example 1**

Input:

```
2
4
16
```

- 2 → not between
- 4 → not between
- 16 → between ✔

Output:

```
True
```

---

### **Example 2**

Input:

```
2
4
6
```

None are between 9 and 21.

Output:

```
False
```

---
