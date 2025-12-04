# 🔹 **Question: Greater than 100**

Write a program that reads three numbers **A, B, and C**, and checks if **each number is greater than 100**.

### ✔ If all three numbers are greater than 100 → print

**All are greater than 100**

### ✖ Otherwise → print

**Not all are greater than 100**

---

# 🟦 **1. Explanation**

You must check these three conditions:

- A > 100
- B > 100
- C > 100

If **all** are true → print the success message.
If **any one** fails → print the failure message.

---

# 🟩 **2. Approach**

1. Read A, B, C
2. Check if all three are greater than 100
3. Print the required output

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read three inputs**

```python
first_number = int(input())
second_number = int(input())
third_number = int(input())
```

### **Step 2: Check all numbers**

```python
is_all_greater = (first_number > 100) and (second_number > 100) and (third_number > 100)
```

### **Step 3: Print the result**

```python
if is_all_greater:
    print("All are greater than 100")
else:
    print("Not all are greater than 100")
```

---

# 🟧 **4. Final Code**

```python
first_number = int(input())
second_number = int(input())
third_number = int(input())

if (first_number > 100 and second_number > 100 and third_number > 100):
    print("All are greater than 100")
else:
    print("Not all are greater than 100")
```

---

# 🟥 **5. Dry Run Example**

### Input:

```
110
256
6350
```

| Number     | Check |
| ---------- | ----- |
| 110 > 100  | ✔     |
| 256 > 100  | ✔     |
| 6350 > 100 | ✔     |

All conditions are satisfied → **Print:**

```
All are greater than 100
```

---
