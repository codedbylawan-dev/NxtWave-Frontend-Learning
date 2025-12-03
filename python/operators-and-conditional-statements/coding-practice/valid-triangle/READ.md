# 🔹 **Question: Valid Triangle**

Write a program that reads the three sides **A**, **B**, and **C** of a triangle and checks whether:

### ✔ The sum of **any two** sides is **always greater** than the third side.

If **all** three triangle conditions are satisfied → print **True**,
otherwise → print **False**.

---

# 🟦 **1. Question Explanation**

To form a valid triangle, **all** three rules must be True:

1. **A + B > C**
2. **B + C > A**
3. **C + A > B**

If **any** one of these fails → it is **NOT** a triangle.

Example:
A = 3, B = 4, C = 5
All three conditions are True → Valid triangle.

---

# 🟩 **2. Approach**

1. Read A, B, C
2. Compute three conditions:

   - A + B > C
   - B + C > A
   - C + A > B

3. Combine all using **and**
4. Print result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
A = int(input())
B = int(input())
C = int(input())
```

### **Step 2: Check triangle inequalities**

```python
cond1 = (A + B) > C
cond2 = (B + C) > A
cond3 = (C + A) > B
```

### **Step 3: Combine**

```python
result = cond1 and cond2 and cond3
```

### **Step 4: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
A = int(input())
B = int(input())
C = int(input())

cond1 = (A + B) > C
cond2 = (B + C) > A
cond3 = (C + A) > B

result = cond1 and cond2 and cond3

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
3
4
5
```

### **Dry Run**

| Step | Operation                       | Explanation         | Result |
| ---- | ------------------------------- | ------------------- | ------ |
| 1    | A = 3, B = 4, C = 5             | Read inputs         | 3,4,5  |
| 2    | cond1: 3 + 4 > 5                | 7 > 5 → True        | True   |
| 3    | cond2: 4 + 5 > 3                | 9 > 3 → True        | True   |
| 4    | cond3: 5 + 3 > 4                | 8 > 4 → True        | True   |
| 5    | result = True and True and True | All conditions hold | True   |
| 6    | print(result)                   | Output              | True   |

### **Final Output**

```
True
```

---
