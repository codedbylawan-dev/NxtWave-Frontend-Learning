# ✅ **Discount — Solved**

## **Question**

Write a program that reads two coupon codes **A** and **B** and checks:

### ✔ Condition

If the **first three characters** of **either** coupon code is `"DIS"` → print **Discount**

### ✖ Otherwise

Print **No Discount**

---

# 📘 **Outline**

### **Approach**

1. Read coupon codes A and B
2. Extract first three characters from both
3. Compare them with the string `"DIS"`
4. If A or B starts with `"DIS"`, print **Discount**, else **No Discount**

---

# 📘 **Step-by-Step Explanation**

### **Step 1: Read the coupon codes**

```python
coupon_1 = input()
coupon_2 = input()
```

---

### **Step 2: Extract the first three characters**

We use slicing `[0:3]` to get the first three characters:

```python
first_three_A = coupon_1[0:3]
first_three_B = coupon_2[0:3]
```

---

### **Step 3: Check if any one of them equals "DIS"**

```python
is_discount = (first_three_A == "DIS") or (first_three_B == "DIS")
```

---

### **Step 4: Print the correct result**

```python
if is_discount:
    print("Discount")
else:
    print("No Discount")
```

---

# ✅ **Final Complete Program**

```python
coupon_1 = input()
coupon_2 = input()

first_three_A = coupon_1[0:3]
first_three_B = coupon_2[0:3]

is_discount = (first_three_A == "DIS") or (first_three_B == "DIS")

if is_discount:
    print("Discount")
else:
    print("No Discount")
```

---

# 📌 **Examples**

### **Input**

```
DISA9#5
6BY@X
```

### **Output**

```
Discount
```

---

### **Input**

```
17F
DVC&SN
```

### **Output**

```
No Discount
```

---
