# 🔹 **Question: Compare Numbers – 9**

Write a program that reads a **three-digit number** and checks if **any one** of the following conditions is satisfied:

### ✔ Condition 1:

Each digit of the number is **greater than 7**

### ✔ Condition 2:

The **product of every pair of digits** is **less than or equal to 30**

If **either** of these conditions is True → print **True**,
otherwise → print **False**.

---

# 🟦 **1. Question Explanation**

For a 3-digit number like `"832"`:

- Digits: 8, 3, 2
- Check if:

  - **All digits > 7**? → 8 ✔, 3 ✖, 2 ✖ → False
  - **Products**:

    - 8×3 = 24 ≤ 30 ✔
    - 3×2 = 6 ≤ 30 ✔
    - 2×8 = 16 ≤ 30 ✔
      Condition 2 True → Output **True**

Final condition:

```
(all digits > 7) OR (all pairwise products ≤ 30)
```

---

# 🟩 **2. Approach**

1. Read the number as a string
2. Extract each digit
3. Convert digits to integers
4. Check if all digits > 7
5. Check product of each pair ≤ 30
6. Combine using OR
7. Print result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read input**

```python
number = input()
```

### **Step 2: Extract digits**

```python
first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])
```

### **Step 3: Check Condition 1 (all digits > 7)**

```python
is_greater = (first_digit > 7) and (second_digit > 7) and (third_digit > 7)
```

### **Step 4: Check Condition 2 (pairwise products ≤ 30)**

```python
p1 = (first_digit * second_digit) <= 30
p2 = (second_digit * third_digit) <= 30
p3 = (third_digit * first_digit) <= 30

is_product_small = p1 and p2 and p3
```

### **Step 5: Final combined result**

```python
result = is_greater or is_product_small
```

### **Step 6: Print result**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
number = input()

first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])

is_greater = (first_digit > 7) and (second_digit > 7) and (third_digit > 7)

p1 = (first_digit * second_digit) <= 30
p2 = (second_digit * third_digit) <= 30
p3 = (third_digit * first_digit) <= 30

is_product_small = p1 and p2 and p3

result = is_greater or is_product_small

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
832
```

### **Dry Run**

| Step | Operation                                   | Explanation             | Value/Result |
| ---- | ------------------------------------------- | ----------------------- | ------------ |
| 1    | Digits extracted → 8, 3, 2                  | Read and convert        | 8, 3, 2      |
| 2    | `is_greater = (8>7 and 3>7 and 2>7)`        | 3 and 2 fail            | False        |
| 3    | `p1 = 8*3 <= 30`                            | 24 ≤ 30                 | True         |
| 4    | `p2 = 3*2 <= 30`                            | 6 ≤ 30                  | True         |
| 5    | `p3 = 2*8 <= 30`                            | 16 ≤ 30                 | True         |
| 6    | `is_product_small = True and True and True` | All products ≤ 30       | True         |
| 7    | `result = False or True`                    | One condition satisfied | True         |
| 8    | Print                                       | Output                  | True         |

### **Final Output**

```
True
```

---
