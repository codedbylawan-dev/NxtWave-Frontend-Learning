# 🔹 **Question: Entrance**

Write a program that reads:

- an age **A** (integer)
- a guardian status **S** (string)

and checks whether:

- **Age is between 12 and 60 (exclusive)**
  **OR**
- **Guardian status S is equal to "yes"**

If either condition is true → print **True**, else print **False**.

---

# 🟦 **1. Question Explanation**

Two conditions must be checked:

### ✔ Condition 1:

Age **A is between 12 and 60**
Since boundaries are not included:

```
A > 12  AND  A < 60
```

### ✔ Condition 2:

Guardian status is `"yes"`:

```
S == "yes"
```

### Final condition:

```
(A > 12 AND A < 60)  OR  (S == "yes")
```

If any one is true → output **True**.

---

# 🟩 **2. Approach**

1. Read age A and guardian status S
2. Check if A is between 12 and 60
3. Check if S equals `"yes"`
4. Combine with OR
5. Print the final result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
A = int(input())
S = input()
```

### **Step 2: Check age condition**

```python
is_age_valid = (A > 12) and (A < 60)
```

### **Step 3: Check guardian status**

```python
is_guardian_yes = (S == "yes")
```

### **Step 4: Combine**

```python
result = is_age_valid or is_guardian_yes
```

### **Step 5: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
A = int(input())
S = input()

is_age_valid = (A > 12) and (A < 60)
is_guardian_yes = (S == "yes")

result = is_age_valid or is_guardian_yes

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
15
no
```

### **Dry Run**

| Step | Code/Operation                 | Explanation                     | Value/Result |
| ---- | ------------------------------ | ------------------------------- | ------------ |
| 1    | `A = int(input())`             | Read age                        | 15           |
| 2    | `S = input()`                  | Read guardian status            | "no"         |
| 3    | `A > 12`                       | Check if age is greater than 12 | True         |
| 4    | `A < 60`                       | Check if age is less than 60    | True         |
| 5    | `is_age_valid = True and True` | Age is between 12 and 60        | True         |
| 6    | `S == "yes"`                   | Check if guardian status is yes | False        |
| 7    | `result = True or False`       | Age valid → result = True       | True         |
| 8    | `print(result)`                | Output result                   | True         |

### **Final Output**

```
True
```

---
