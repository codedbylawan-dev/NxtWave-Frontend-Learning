# ✅ **Valid Number — Solved**

## **Question**

You are given a **three-digit number N**.
You must check **both** conditions:

### ✔ Condition 1

**At least one digit** of N is **not equal to 5**
(Meaning: Not all digits should be 5)

### ✔ Condition 2

N is **between 300 and 700** (exclusive or inclusive?)
→ According to question examples, "between" means:
**300 < N < 700**

If **both** conditions are satisfied → print **Valid Number**
Else → print **Not a Valid Number**

---

# 📘 **Outline**

### **Approach**

1. Read the three-digit number N
2. Extract its digits
3. Check if any digit is not equal to 5
4. Check if N is between 300 and 700
5. Print result

---

# 📘 **Step-by-Step Explanation**

### **Step 1: Read the number**

```python
number = int(input())
```

---

### **Step 2: Extract digits**

Convert the number to a string and take individual digits.

```python
n_str = str(number)

digit1 = int(n_str[0])
digit2 = int(n_str[1])
digit3 = int(n_str[2])
```

---

### **Step 3: Check if any digit is NOT equal to 5**

This condition must be **true** if even one digit ≠ 5.

```python
is_any_digit_not_five = (digit1 != 5) or (digit2 != 5) or (digit3 != 5)
```

(As long as at least one digit is not 5 → condition satisfied)

---

### **Step 4: Check if N is between 300 and 700**

```python
is_between = (number > 300) and (number < 700)
```

---

### **Step 5: Print the result**

```python
if is_any_digit_not_five and is_between:
    print("Valid Number")
else:
    print("Not a Valid Number")
```

---

# ✅ **Final Complete Program**

```python
number = int(input())

n_str = str(number)
digit1 = int(n_str[0])
digit2 = int(n_str[1])
digit3 = int(n_str[2])

is_any_digit_not_five = (digit1 != 5) or (digit2 != 5) or (digit3 != 5)
is_between = (number > 300) and (number < 700)

if is_any_digit_not_five and is_between:
    print("Valid Number")
else:
    print("Not a Valid Number")
```

---

# 📌 **Example Walkthroughs**

### **Example 1**

Input:

```
653
```

Check digits → 6, 5, 3 → at least one digit ≠ 5 ✔
Check range → 653 is between 300 and 700 ✔

Output:

```
Valid Number
```

---

### **Example 2**

Input:

```
947
```

Check range → 947 is NOT between 300 and 700 ✖
No need to check further → fails

Output:

```
Not a Valid Number
```

---
