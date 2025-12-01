# ✅ **Compare Sum of the Digits — Full Solution (Your Format)**

## **🔹 Question: Compare Sum of the Digits**

Write a program that reads a **two-digit number N**
and checks whether the **sum of its digits** is **greater than 7**.

---

# ✅ **Approach**

### **Step 1:** Read the input

### **Step 2:** Extract the digits

### **Step 3:** Calculate the sum

### **Step 4:** Compare sum with 7

### **Step 5:** Print the boolean result

---

# ✅ **Step-by-Step Explanation**

### **Step 1: Read the input**

```python
number = input()
```

### **Step 2: Extract digits**

```python
first_digit = int(number[0])
second_digit = int(number[1])
```

### **Step 3: Calculate sum**

```python
sum_of_digits = first_digit + second_digit
```

### **Step 4: Compare**

```python
result = sum_of_digits > 7
```

### **Step 5: Print**

```python
print(result)
```

---

# ✅ **Final Code**

```python
number = input()
first_digit = int(number[0])
second_digit = int(number[1])
sum_of_digits = first_digit + second_digit
result = sum_of_digits > 7
print(result)
```

---

# ✅ **Dry Run (Tabular Form)**

### **Dry Run 1 — Input: 45**

| Step | Variable / Action       | Value  |
| ---- | ----------------------- | ------ |
| 1    | number                  | `"45"` |
| 2    | first_digit = int('4')  | `4`    |
| 2    | second_digit = int('5') | `5`    |
| 3    | sum_of_digits = 4 + 5   | `9`    |
| 4    | Compare 9 > 7           | `True` |
| 5    | Output                  | `True` |

---

### **Dry Run 2 — Input: 12**

| Step | Variable / Action | Value   |
| ---- | ----------------- | ------- |
| 1    | number            | `"12"`  |
| 2    | first_digit       | `1`     |
| 2    | second_digit      | `2`     |
| 3    | sum_of_digits     | `3`     |
| 4    | Compare 3 > 7     | `False` |
| 5    | Output            | `False` |

---
