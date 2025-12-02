# 🔹 **Question: Greater than Five**

Write a program that reads two integers and checks whether:

- **Both numbers are positive**,
  **AND**
- **At least one of them is greater than 5**

If both conditions are satisfied → print **True**,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

You must check two separate conditions:

### ✔ Condition 1: Both numbers are positive

```
A > 0  AND  B > 0
```

### ✔ Condition 2: At least one number is greater than 5

```
A > 5  OR  B > 5
```

### Final condition:

```
(A > 0 AND B > 0)  AND  (A > 5 OR B > 5)
```

Only if **both** conditions are True → output **True**.

---

# 🟩 **2. Approach**

1. Read A and B
2. Check if both A and B are positive
3. Check if at least one of them is greater than 5
4. Use `and` to combine conditions
5. Print the final result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
A = int(input())
B = int(input())
```

### **Step 2: Check positivity**

```python
are_positive = (A > 0) and (B > 0)
```

### **Step 3: Check if at least one is greater than 5**

```python
is_greater_than_5 = (A > 5) or (B > 5)
```

### **Step 4: Combine**

```python
result = are_positive and is_greater_than_5
```

### **Step 5: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
A = int(input())
B = int(input())

are_positive = (A > 0) and (B > 0)
is_greater_than_5 = (A > 5) or (B > 5)

result = are_positive and is_greater_than_5

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
10
1
```

### **Dry Run**

| Step | Code/Operation                      | Explanation               | Value/Result |
| ---- | ----------------------------------- | ------------------------- | ------------ |
| 1    | `A = int(input())`                  | Read first number         | 10           |
| 2    | `B = int(input())`                  | Read second number        | 1            |
| 3    | `A > 0`                             | Check if 10 is positive   | True         |
| 4    | `B > 0`                             | Check if 1 is positive    | True         |
| 5    | `are_positive = True and True`      | Both numbers are positive | True         |
| 6    | `A > 5`                             | Check if 10 > 5           | True         |
| 7    | `B > 5`                             | Check if 1 > 5            | False        |
| 8    | `is_greater_than_5 = True or False` | At least one number > 5   | True         |
| 9    | `result = True and True`            | Both conditions satisfied | True         |
| 10   | `print(result)`                     | Output                    | True         |

### **Final Output**

```
True
```

---
