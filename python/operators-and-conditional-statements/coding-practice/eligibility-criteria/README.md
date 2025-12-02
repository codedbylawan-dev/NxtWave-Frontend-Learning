# 🔹 **Question: Eligibility Criteria**

You are given marks in **Maths (M)**, **Physics (P)**, and **Chemistry (C)**.
A student is considered _eligible_ if **any one** of the following conditions is true:

### ✔ Condition 1

```
M >= 70 AND P >= 60 AND C >= 60
```

### ✔ Condition 2

```
M + P + C >= 180
```

If at least one condition is satisfied → print **True**,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

We need to evaluate two separate conditions:

### **Condition 1 (Individual subject requirement)**

- Maths ≥ 70
- Physics ≥ 60
- Chemistry ≥ 60

All three must be true.

### **Condition 2 (Total marks requirement)**

- Sum of marks ≥ 180

This means even if individual marks fail, the student may still be eligible by scoring well overall.

### Final condition:

```
(condition_1) OR (condition_2)
```

---

# 🟩 **2. Approach**

1. Read M, P, C
2. Check subject-wise condition
3. Compute total and check total condition
4. Combine conditions with OR
5. Print the result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Input**

```python
M = int(input())
P = int(input())
C = int(input())
```

### **Step 2: Check individual subject requirement**

```python
condition_1 = (M >= 70) and (P >= 60) and (C >= 60)
```

### **Step 3: Check total marks requirement**

```python
total = M + P + C
condition_2 = total >= 180
```

### **Step 4: Combine**

```python
result = condition_1 or condition_2
```

### **Step 5: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
M = int(input())
P = int(input())
C = int(input())

condition_1 = (M >= 70) and (P >= 60) and (C >= 60)

total = M + P + C
condition_2 = total >= 180

result = condition_1 or condition_2

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
0
100
100
```

### **Dry Run**

| Step | Code/Operation                          | Explanation                                 | Value/Result |
| ---- | --------------------------------------- | ------------------------------------------- | ------------ |
| 1    | `M = int(input())`                      | Read Maths mark                             | 0            |
| 2    | `P = int(input())`                      | Read Physics mark                           | 100          |
| 3    | `C = int(input())`                      | Read Chemistry mark                         | 100          |
| 4    | `M >= 70`                               | 0 ≥ 70 → False                              | False        |
| 5    | `P >= 60`                               | 100 ≥ 60 → True                             | True         |
| 6    | `C >= 60`                               | 100 ≥ 60 → True                             | True         |
| 7    | `condition_1 = False and True and True` | All must be True → condition_1 = False      | False        |
| 8    | `total = M + P + C`                     | 0 + 100 + 100                               | 200          |
| 9    | `condition_2 = total >= 180`            | 200 ≥ 180 → True                            | True         |
| 10   | `result = False or True`                | One condition is True → final result = True | True         |
| 11   | `print(result)`                         | Output                                      | True         |

### **Final Output**

```
True
```

---
