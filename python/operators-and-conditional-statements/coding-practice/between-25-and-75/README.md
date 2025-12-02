# 🔹 **Question: Between 25 and 75**

Write a program that reads a number and checks whether the number is **strictly between 25 and 75**.

### **Input**

- A single integer.

### **Output**

Print **True** if the number is between 25 and 75 (exclusive).
Otherwise print **False**.

### **Important Note**

- 25 is **not** included
- 75 is **not** included
- So the condition is:

  ```
  number > 25 AND number < 75
  ```

---

# 🟦 **1. Question Explanation**

You must verify **two conditions**:

### ✔ Condition 1:

Number is greater than 25 → `num > 25`

### ✔ Condition 2:

Number is less than 75 → `num < 75`

### Final Condition:

```
num > 25 AND num < 75
```

If both are true → output **True**.

---

# 🟩 **2. Approach**

1. Read the number
2. Check if it is > 25
3. Check if it is < 75
4. Combine using `and`
5. Print the result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read input**

```python
number = int(input())
```

### **Step 2: Compare with 25**

```python
is_greater_than_25 = number > 25
```

### **Step 3: Compare with 75**

```python
is_less_than_75 = number < 75
```

### **Step 4: Final condition**

```python
result = is_greater_than_25 and is_less_than_75
```

### **Step 5: Print result**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
number = int(input())

is_greater_than_25 = number > 25
is_less_than_75 = number < 75

result = is_greater_than_25 and is_less_than_75

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
35
```

### **Dry Run**

| Step | Code/Operation           | Explanation                    | Value/Result |
| ---- | ------------------------ | ------------------------------ | ------------ |
| 1    | `number = int(input())`  | Read the number                | 35           |
| 2    | `number > 25`            | Check if 35 is greater than 25 | True         |
| 3    | `number < 75`            | Check if 35 is less than 75    | True         |
| 4    | `result = True and True` | Both conditions must be True   | True         |
| 5    | `print(result)`          | Output result                  | True         |

### **Final Output**

```
True
```

---
