# 🔹 **Question: Compare with Ten**

Write a program that reads two integers **A** and **B**, and checks if **any one** of the following conditions is true:

1. The **sum** of A and B is **less than 10**
2. The **difference** between A and B is **less than 10**
3. A is **between 5 and 30** (exclusive)

If **any** condition is satisfied → print **True**
Else → print **False**

---

# 🟦 **1. Question Explanation**

We must evaluate **three conditions**:

### ✔ Condition 1

```
A + B < 10
```

### ✔ Condition 2

```
abs(A - B) < 10
```

(Difference means A − B, but both A−B and B−A should be considered → use absolute value.)

### ✔ Condition 3

```
A > 5 AND A < 30
```

Final output should be:

```
condition_1 OR condition_2 OR condition_3
```

---

# 🟩 **2. Approach**

1. Read A and B
2. Compute sum
3. Compute difference
4. Check if sum < 10
5. Check if difference < 10
6. Check if A is between 5 and 30
7. Combine using OR
8. Print result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
A = int(input())
B = int(input())
```

### **Step 2: Compute sum**

```python
sum_val = A + B
```

### **Step 3: Compute difference**

```python
diff_val = abs(A - B)
```

### **Step 4: Check all conditions**

```python
condition_1 = sum_val < 10
condition_2 = diff_val < 10
condition_3 = (A > 5) and (A < 30)
```

### **Step 5: Combine**

```python
result = condition_1 or condition_2 or condition_3
```

### **Step 6: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
A = int(input())
B = int(input())

sum_val = A + B
diff_val = abs(A - B)

condition_1 = sum_val < 10
condition_2 = diff_val < 10
condition_3 = (A > 5) and (A < 30)

result = condition_1 or condition_2 or condition_3

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
12
8
```

### **Dry Run**

| Step | Code/Operation                   | Explanation                                    | Value/Result |     |     |
| ---- | -------------------------------- | ---------------------------------------------- | ------------ | --- | --- |
| 1    | `A = int(input())`               | Read first number                              | 12           |     |     |
| 2    | `B = int(input())`               | Read second number                             | 8            |     |     |
| 3    | `sum_val = A + B`                | Sum = 12 + 8                                   | 20           |     |     |
| 4    | `sum_val < 10`                   | 20 < 10 → False                                | False        |     |     |
| 5    | `diff_val = abs(A - B)`          | Difference =                                   | 12 − 8       | = 4 | 4   |
| 6    | `diff_val < 10`                  | 4 < 10 → True                                  | True         |     |     |
| 7    | `A > 5` and `A < 30`             | 12 is between 5 and 30 → True                  | True         |     |     |
| 8    | `result = False or True or True` | At least one condition is True → result = True | True         |     |     |
| 9    | `print(result)`                  | Output result                                  | True         |     |     |

### **Final Output**

```
True
```

---
