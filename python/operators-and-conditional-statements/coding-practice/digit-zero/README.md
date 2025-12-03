# 🔹 **Question: Digit Zero**

Write a program that reads a **three-digit number** and checks whether it contains the digit **0**.

### **Input**

A single three-digit integer.

### **Output**

Print **True** if _any_ digit is 0.
Otherwise print **False**.

---

# 🟦 **1. Question Explanation**

A three-digit number has **three digits**:

- first digit
- second digit
- third digit

We simply need to check:

```
(first_digit == 0)
OR (second_digit == 0)
OR (third_digit == 0)
```

If any is **0**, answer → **True**.

---

# 🟩 **2. Approach**

1. Read the number as a string
2. Extract each digit
3. Convert digits to integers
4. Compare each digit with 0
5. Combine using OR
6. Print the final result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read number**

```python
number = input()
```

### **Step 2: Extract digits**

```python
first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])
```

### **Step 3: Check for zero**

```python
result = (first_digit == 0) or (second_digit == 0) or (third_digit == 0)
```

### **Step 4: Print**

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

result = (first_digit == 0) or (second_digit == 0) or (third_digit == 0)

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
120
```

### **Dry Run**

| Step | Code/Operation                    | Explanation                | Value/Result |
| ---- | --------------------------------- | -------------------------- | ------------ |
| 1    | `number = input()`                | Read number                | "120"        |
| 2    | `first_digit = int(number[0])`    | Extract first digit        | 1            |
| 3    | `second_digit = int(number[1])`   | Extract second digit       | 2            |
| 4    | `third_digit = int(number[2])`    | Extract third digit        | 0            |
| 5    | `first_digit == 0`                | 1 == 0                     | False        |
| 6    | `second_digit == 0`               | 2 == 0                     | False        |
| 7    | `third_digit == 0`                | 0 == 0                     | True         |
| 8    | `result = False or False or True` | At least one digit is zero | True         |
| 9    | `print(result)`                   | Output                     | True         |

### **Final Output**

```
True
```

---
