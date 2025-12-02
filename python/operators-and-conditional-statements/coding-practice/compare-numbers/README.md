# 🔹 **Question: Compare Numbers**

Write a program that reads two integers **A** and **B**, and checks whether:

- **Both A and B are greater than 35**
  **OR**
- **A is greater than B**

If any one of these conditions is true → print **True**
Else → print **False**

---

# 🟦 **1. Question Explanation**

This problem involves **two conditions**:

### ✔ Condition 1:

`A > 35 AND B > 35`

### ✔ Condition 2:

`A > B`

You must check:

```
Condition 1 OR Condition 2
```

If **either one** is true, output should be **True**.

---

# 🟩 **2. Approach**

1. Read A and B from input.
2. Check if both A and B are greater than 35.
3. Check if A is greater than B.
4. Combine conditions using the `or` operator.
5. Print the final result.

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
first_number = int(input())
second_number = int(input())
```

### **Step 2: Condition 1 → Both numbers > 35**

```python
are_greater_than = (first_number > 35) and (second_number > 35)
```

### **Step 3: Condition 2 → A > B**

```python
is_first_number_greater = first_number > second_number
```

### **Step 4: Combine conditions**

```python
result = are_greater_than or is_first_number_greater
```

### **Step 5: Print result**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
first_number = int(input())
second_number = int(input())

are_greater_than = (first_number > 35) and (second_number > 35)
is_first_number_greater = first_number > second_number

result = are_greater_than or is_first_number_greater

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
45
25
```

### **Dry Run**

| Step | Code/Operation                                 | Explanation                           | Value/Result |
| ---- | ---------------------------------------------- | ------------------------------------- | ------------ |
| 1    | `first_number = int(input())`                  | Read first number                     | 45           |
| 2    | `second_number = int(input())`                 | Read second number                    | 25           |
| 3    | `first_number > 35`                            | 45 > 35 → True                        | True         |
| 4    | `second_number > 35`                           | 25 > 35 → False                       | False        |
| 5    | `(first_number > 35) and (second_number > 35)` | True and False → False                | False        |
| 6    | `first_number > second_number`                 | 45 > 25 → True                        | True         |
| 7    | `False or True`                                | One condition is True → result = True | True         |
| 8    | `print(result)`                                | Output result                         | True         |

### **Final Output**

```
True
```

---

s
