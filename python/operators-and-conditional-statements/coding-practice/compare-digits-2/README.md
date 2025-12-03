# 🔹 **Question: Compare Digits – 2**

Write a program to check whether a given **two-digit number** satisfies both conditions:

1. The number is **greater than 25**
2. Its **first digit** is greater than its **second digit**

If both conditions are true → print **True**,
otherwise → print **False**.

---

# 🟦 **1. Question Explanation**

For a two-digit number (like 42, 57, 91):

### ✔ Condition 1:

```
number > 25
```

### ✔ Condition 2:

Extract digits from the number:

- First digit → number_str[0]
- Second digit → number_str[1]

Then check:

```
first_digit > second_digit
```

### Final condition:

```
(number > 25) AND (first_digit > second_digit)
```

Only if **both** are True → output **True**.

---

# 🟩 **2. Approach**

1. Read the number as a string
2. Convert it to integer
3. Extract first and second digits
4. Compare number with 25
5. Compare digits
6. Combine the two conditions
7. Print the final result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read input**

```python
a = input()
```

### **Step 2: Check number > 25**

```python
is_above = int(a) > 25
```

### **Step 3: Extract digits**

```python
first_digit = int(a[0])
second_digit = int(a[1])
```

### **Step 4: Compare digits**

```python
is_greater = first_digit > second_digit
```

### **Step 5: Final result**

```python
result = is_above and is_greater
```

### **Step 6: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
a = input()

is_above = int(a) > 25

first_digit = int(a[0])
second_digit = int(a[1])

is_greater = first_digit > second_digit

result = is_above and is_greater

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
42
```

### **Dry Run**

| Step | Code/Operation               | Explanation                                | Value/Result |
| ---- | ---------------------------- | ------------------------------------------ | ------------ |
| 1    | `a = input()`                | Read the two-digit number                  | "42"         |
| 2    | `int(a) > 25`                | Check if 42 > 25                           | True         |
| 3    | `first_digit = int(a[0])`    | Extract first digit                        | 4            |
| 4    | `second_digit = int(a[1])`   | Extract second digit                       | 2            |
| 5    | `first_digit > second_digit` | Check if 4 > 2                             | True         |
| 6    | `result = True and True`     | Both conditions True → final result = True | True         |
| 7    | `print(result)`              | Output                                     | True         |

### **Final Output**

```
True
```

---
