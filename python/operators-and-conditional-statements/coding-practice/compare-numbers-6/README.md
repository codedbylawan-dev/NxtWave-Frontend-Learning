# 🔹 **Question: Compare Numbers – 6**

Write a program that reads a **three-digit number** and checks whether:

### ✔ **All three digits are greater than 4**

**OR**

### ✔ **The first digit is equal to 6**

If **either** condition is True → print **True**,
otherwise → print **False**.

---

# 🟦 **1. Question Explanation**

A three-digit number has:

- first digit → number[0]
- second digit → number[1]
- third digit → number[2]

We must check **two conditions**:

### **Condition 1: Each digit > 4**

```
(first_digit > 4)
AND (second_digit > 4)
AND (third_digit > 4)
```

### **Condition 2: First digit == 6**

```
first_digit == 6
```

### **Final condition**

```
(all digits > 4) OR (first digit == 6)
```

---

# 🟩 **2. Approach**

1. Read the number as a string
2. Extract the three digits
3. Convert to integers
4. Check if all digits > 4
5. Check if first digit is 6
6. Combine using OR
7. Print the result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read input**

```python
number = input()
```

### **Step 2: Extract and convert digits**

```python
first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])
```

### **Step 3: Check conditions**

```python
all_digits_greater = (first_digit > 4) and (second_digit > 4) and (third_digit > 4)
first_digit_is_six = (first_digit == 6)
```

### **Step 4: Combine**

```python
result = all_digits_greater or first_digit_is_six
```

### **Step 5: Print**

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

all_digits_greater = (first_digit > 4) and (second_digit > 4) and (third_digit > 4)
first_digit_is_six = (first_digit == 6)

result = all_digits_greater or first_digit_is_six

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
612
```

### **Dry Run**

| Step | Operation                       | Explanation                 | Value/Result |
| ---- | ------------------------------- | --------------------------- | ------------ |
| 1    | `number = "612"`                | Read input                  | "612"        |
| 2    | `first_digit = int(number[0])`  | First digit                 | 6            |
| 3    | `second_digit = int(number[1])` | Second digit                | 1            |
| 4    | `third_digit = int(number[2])`  | Third digit                 | 2            |
| 5    | `all_digits_greater`            | Check 6>4, 1>4, 2>4 → False | False        |
| 6    | `first_digit_is_six`            | Check 6 == 6                | True         |
| 7    | `result = False or True`        | One condition True          | True         |
| 8    | `print(result)`                 | Output                      | True         |

### **Final Output**

```
True
```

---
