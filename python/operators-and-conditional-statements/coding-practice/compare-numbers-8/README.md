# 🔹 **Question: Compare Numbers – 8**

Write a program that reads a **three-digit number** and checks whether **all** the following conditions are satisfied:

1. The number **contains the digit 1**
2. The **sum of all digits** is **less than 12**
3. The **last digit is 5**

Only if **all three** are True → print **True**,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

Given a number like `"315"`:

- Contains **1** ✔
- Sum = 3 + 1 + 5 = **9 < 12** ✔
- Last digit = **5** ✔

All conditions True → Output **True**

We must ensure:

```
digit_1_present AND sum_of_digits < 12 AND last_digit == 5
```

---

# 🟩 **2. Approach**

1. Read the number as a string
2. Extract each digit
3. Convert to integers
4. Check if any digit is 1
5. Compute sum and check sum < 12
6. Check last digit == 5
7. Combine conditions using AND
8. Print result

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

### **Step 3: Condition — number contains 1**

```python
has_one = (first_digit == 1) or (second_digit == 1) or (third_digit == 1)
```

### **Step 4: Condition — sum < 12**

```python
sum_digits = first_digit + second_digit + third_digit
is_sum_small = sum_digits < 12
```

### **Step 5: Condition — last digit is 5**

```python
is_last_five = (third_digit == 5)
```

### **Step 6: Final combined result**

```python
result = has_one and is_sum_small and is_last_five
```

### **Step 7: Print**

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

has_one = (first_digit == 1) or (second_digit == 1) or (third_digit == 1)

sum_digits = first_digit + second_digit + third_digit
is_sum_small = sum_digits < 12

is_last_five = (third_digit == 5)

result = has_one and is_sum_small and is_last_five

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
315
```

### **Dry Run**

| Step | Operation                         | Explanation              | Value/Result |
| ---- | --------------------------------- | ------------------------ | ------------ |
| 1    | `number = "315"`                  | Read input               | "315"        |
| 2    | Extract digits                    |                          | 3, 1, 5      |
| 3    | `has_one = True`                  | One digit equals 1       | True         |
| 4    | `sum_digits = 3 + 1 + 5`          | Sum of digits            | 9            |
| 5    | `is_sum_small = 9 < 12`           | Sum less than 12         | True         |
| 6    | `is_last_five = 5 == 5`           | Last digit equals 5      | True         |
| 7    | `result = True and True and True` | All conditions satisfied | True         |
| 8    | `print(result)`                   | Output                   | True         |

### **Final Output**

```
True
```

---
