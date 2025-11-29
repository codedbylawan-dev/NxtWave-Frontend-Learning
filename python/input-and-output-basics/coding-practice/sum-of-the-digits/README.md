# **Question: Sum of the Digits**

Write a program that prints the sum of the digits of a given three-digit number.

### **Input**

- Single line: a three-digit number

### **Output**

- Single line: sum of the digits of the number

### **Explanation**

Example:
Number = 326
Sum of digits = 3 + 2 + 6 = 11
Output: 11

---

# **Approach**

### **Step 1: Read the number**

```python
number = input()
```

### **Step 2: Extract individual digits**

```python
first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])
```

### **Step 3: Add the digits**

```python
sum_of_digits = first_digit + second_digit + third_digit
```

### **Step 4: Print the sum**

```python
print(sum_of_digits)
```

---

# **Complete Code**

```python
number = input()

first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])

sum_of_digits = first_digit + second_digit + third_digit

print(sum_of_digits)
```

---

# 🟩 **DRY RUN (Tabular Form)**

| Step No. | Operation                   | Value / Explanation |
| -------- | --------------------------- | ------------------- |
| 1        | Read number                 | "326"               |
| 2        | Convert first digit to int  | 3                   |
| 3        | Convert second digit to int | 2                   |
| 4        | Convert third digit to int  | 6                   |
| 5        | Add digits                  | 3 + 2 + 6 = 11      |
| 6        | Print sum                   | 11                  |

---

### **Final Output**

```
11
```

---
