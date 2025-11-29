# **Question: Sum of two numbers - 2**

Write a program that reads two float numbers and prints their sum in the format:

```
Sum: <value>
```

### **Input**

- First line: float
- Second line: float

### **Output**

A single line containing a string in the format:

```
Sum: <sum_of_numbers>
```

### **Explanation**

If inputs are 3.0 and 4.0:
Sum = 3.0 + 4.0 = **7.0**
Output should be:

```
Sum: 7.0
```

---

# **Approach**

### **Step 1: Read the input numbers**

```python
first_number = input()
second_number = input()
```

### **Step 2: Convert the inputs to float**

```python
first_number = float(first_number)
second_number = float(second_number)
```

### **Step 3: Calculate the sum**

```python
result = first_number + second_number
```

### **Step 4: Print the result in the given format**

```python
print("Sum: " + str(result))
```

---

# **Complete Code**

```python
first_number = input()
second_number = input()

first_number = float(first_number)
second_number = float(second_number)

result = first_number + second_number

print("Sum: " + str(result))
```

---

# 🟩 **DRY RUN (Tabular Form)**

| Step No. | Operation               | Value / Explanation |
| -------- | ----------------------- | ------------------- |
| 1        | Read input 1            | `"3.0"`             |
| 2        | Read input 2            | `"4.0"`             |
| 3        | Convert `"3.0"` → float | 3.0                 |
| 4        | Convert `"4.0"` → float | 4.0                 |
| 5        | Calculate sum           | `3.0 + 4.0 = 7.0`   |
| 6        | Prepare output string   | `"Sum: 7.0"`        |
| 7        | Print output            | Sum: 7.0            |

---

### **Final Output**

```
Sum: 7.0
```

---
