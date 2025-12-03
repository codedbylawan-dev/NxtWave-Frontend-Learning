# 🔹 **Question: Same Digits**

Write a program that reads a **three-digit number** and checks whether **all three digits are the same**.

### **Input**

A single three-digit integer.

### **Output**

Print **True** if all digits are the same,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

A three-digit number like `"222"` has:

- first digit → 2
- second digit → 2
- third digit → 2

All are equal → **True**

But for `"989"`:

- 9 ≠ 8
- 8 ≠ 9
  So → **False**

We simply check:

```
(first_digit == second_digit) AND (second_digit == third_digit)
```

---

# 🟩 **2. Approach**

1. Read the number as a string
2. Extract each digit
3. Convert digits to integers
4. Compare all digits with each other
5. Print the result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read input**

```python
number = input()
```

### **Step 2: Extract digits**

```python
d1 = int(number[0])
d2 = int(number[1])
d3 = int(number[2])
```

### **Step 3: Check if all digits are the same**

```python
result = (d1 == d2) and (d2 == d3)
```

### **Step 4: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
number = input()

d1 = int(number[0])
d2 = int(number[1])
d3 = int(number[2])

result = (d1 == d2) and (d2 == d3)

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
222
```

### **Dry Run**

| Step | Operation                | Explanation        | Value/Result |
| ---- | ------------------------ | ------------------ | ------------ |
| 1    | Read number `"222"`      | Input              | "222"        |
| 2    | Extract digits → 2, 2, 2 | Convert each digit | 2, 2, 2      |
| 3    | Check: 2 == 2            | First equal second | True         |
| 4    | Check: 2 == 2            | Second equal third | True         |
| 5    | `result = True and True` | All equal          | True         |
| 6    | Print result             | Output             | True         |

### **Final Output**

```
True
```

---
