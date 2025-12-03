# 🔹 **Question: Compare Numbers – 7**

Write a program that reads a **four-digit number** and checks whether:

### ✔ The **first two digits are 19**

### ✔ The **last two digits are between 30 and 60 (exclusive)**

(i.e., > 30 AND < 60)

Only if **both** conditions are satisfied → print **True**,
else print **False**.

---

# 🟦 **1. Question Explanation**

For a four-digit number like `"1947"`:

- First two digits → `"19"`
- Last two digits → `"47"`

We check two conditions:

### **Condition 1:**

```
first_two_digits == 19
```

### **Condition 2:**

```
30 < last_two_digits < 60
```

### **Final Condition:**

```
(first_two_digits == 19) AND (last_two_digits between 30 and 60)
```

---

# 🟩 **2. Approach**

1. Read the 4-digit number as a string
2. Extract first two digits
3. Extract last two digits
4. Convert both to integers
5. Check if first two digits == 19
6. Check if last two digits are > 30 and < 60
7. Combine using AND
8. Print final result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read input**

```python
number = input()
```

### **Step 2: Extract digits**

```python
first_two = int(number[:2])
last_two = int(number[-2:])
```

### **Step 3: Check conditions**

```python
check_first = (first_two == 19)
check_last = (last_two > 30) and (last_two < 60)
```

### **Step 4: Final result**

```python
result = check_first and check_last
```

### **Step 5: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
number = input()

first_two = int(number[:2])
last_two = int(number[-2:])

check_first = (first_two == 19)
check_last = (last_two > 30) and (last_two < 60)

result = check_first and check_last

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
1947
```

### **Dry Run**

| Step | Operation                              | Explanation                       | Value/Result |
| ---- | -------------------------------------- | --------------------------------- | ------------ |
| 1    | `number = "1947"`                      | Read input                        | "1947"       |
| 2    | `first_two = int(number[:2])`          | Extract first two digits          | 19           |
| 3    | `last_two = int(number[-2:])`          | Extract last two digits           | 47           |
| 4    | `check_first = (19 == 19)`             | First two digits check            | True         |
| 5    | `check_last = (47 > 30) and (47 < 60)` | Last two digits between 30 and 60 | True         |
| 6    | `result = True and True`               | Both conditions satisfied         | True         |
| 7    | `print(result)`                        | Output                            | True         |

### **Final Output**

```
True
```

---
