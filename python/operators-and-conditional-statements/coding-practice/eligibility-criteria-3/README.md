# 🔹 **Question: Eligibility Criteria – 3**

Write a program that reads marks in **Maths (M)**, **Physics (P)**, and **Chemistry (C)** and checks whether **both** of the following conditions are satisfied:

1️⃣ **All three marks are ≥ 35**
2️⃣ **At least one of these is true:**

- M + P ≥ 90
- P + C ≥ 90
- M + C ≥ 90

If BOTH conditions are true → print **True**
Else → print **False**

---

# 🟦 **1. Question Explanation**

This question checks **minimum subject qualification** _and_ **minimum combined score qualification**.

### ✔ Condition 1: Pass all subjects

M ≥ 35
P ≥ 35
C ≥ 35

### ✔ Condition 2: At least one strong combination

- M+P ≥ 90
- P+C ≥ 90
- M+C ≥ 90

The final output is **True only if BOTH condition groups are satisfied**.

---

# 🟩 **2. Approach**

1. Read marks M, P, C
2. Check if each mark ≥ 35
3. Check all three pair-sums
4. Combine conditions with `and`
5. Print result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
M = int(input())
P = int(input())
C = int(input())
```

### **Step 2: Check if all subjects have marks ≥ 35**

```python
all_pass = (M >= 35) and (P >= 35) and (C >= 35)
```

### **Step 3: Check if any pair-sum ≥ 90**

```python
pair_sum_ok = (M + P >= 90) or (P + C >= 90) or (M + C >= 90)
```

### **Step 4: Combine the two conditions**

```python
result = all_pass and pair_sum_ok
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

all_pass = (M >= 35) and (P >= 35) and (C >= 35)

pair_sum_ok = (M + P >= 90) or (P + C >= 90) or (M + C >= 90)

result = all_pass and pair_sum_ok

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
50
35
40
```

### **Dry Run**

| Step | Operation                                  | Explanation               | Result |
| ---- | ------------------------------------------ | ------------------------- | ------ |
| 1    | M=50, P=35, C=40                           | Inputs                    | —      |
| 2    | all_pass = (50≥35) and (35≥35) and (40≥35) | All subjects passed       | True   |
| 3    | pair_sum_ok:                               |                           |        |
|      | 50+35 = 85 ≥ 90 → False                    | First pair                | False  |
|      | 35+40 = 75 ≥ 90 → False                    | Second pair               | False  |
|      | 50+40 = 90 ≥ 90 → True                     | Third pair                | True   |
|      | pair_sum_ok = False or False or True       | At least one satisfies    | True   |
| 4    | result = True and True                     | Both conditions satisfied | True   |
| 5    | print(result)                              | Output                    | True   |

### **Final Output**

```
True
```

---
