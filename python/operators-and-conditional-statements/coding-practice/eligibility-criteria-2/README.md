# 🔹 **Question: Eligibility Criteria – 2**

You are given three marks:

- **M** → Maths
- **P** → Physics
- **C** → Chemistry

You must check whether **both** of these conditions are satisfied:

### ✔ Condition 1:

At least one pair of subjects has a combined score **≥ 100**

Pairs:

- M + P ≥ 100
- P + C ≥ 100
- M + C ≥ 100

### ✔ Condition 2:

Total score **M + P + C ≥ 180**

Only if **both** conditions are True → print **True**,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

Example:
M = 82, P = 55, C = 45

- 82 + 55 = 137 ≥ 100 ✔
- Total = 82 + 55 + 45 = 182 ≥ 180 ✔

Both conditions satisfied → **True**

Final logic:

```
(pair_sum ≥ 100) AND (total ≥ 180)
```

---

# 🟩 **2. Approach**

1. Read marks M, P, C
2. Compute pairwise sums
3. Check if **any** pair sum ≥ 100
4. Compute total M + P + C
5. Check if total ≥ 180
6. Combine both conditions using AND
7. Print result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read marks**

```python
M = int(input())
P = int(input())
C = int(input())
```

### **Step 2: Compute pairwise sums**

```python
sum_MP = M + P
sum_PC = P + C
sum_CM = C + M
```

### **Step 3: Condition — any pair sum ≥ 100**

```python
pair_condition = (sum_MP >= 100) or (sum_PC >= 100) or (sum_CM >= 100)
```

### **Step 4: Compute total**

```python
total = M + P + C
```

### **Step 5: Condition — total ≥ 180**

```python
total_condition = total >= 180
```

### **Step 6: Final combined result**

```python
result = pair_condition and total_condition
```

### **Step 7: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
M = int(input())
P = int(input())
C = int(input())

sum_MP = M + P
sum_PC = P + C
sum_CM = C + M

pair_condition = (sum_MP >= 100) or (sum_PC >= 100) or (sum_CM >= 100)

total = M + P + C
total_condition = total >= 180

result = pair_condition and total_condition

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
82
55
45
```

### **Dry Run**

| Step | Operation                   | Explanation              | Value/Result |
| ---- | --------------------------- | ------------------------ | ------------ |
| 1    | M=82, P=55, C=45            | Read marks               | 82, 55, 45   |
| 2    | sum_MP = 82+55              | Pair 1 sum               | 137          |
| 3    | sum_PC = 55+45              | Pair 2 sum               | 100          |
| 4    | sum_CM = 45+82              | Pair 3 sum               | 127          |
| 5    | pair_condition = True       | At least one pair ≥ 100  | True         |
| 6    | total = 82+55+45            | Total marks              | 182          |
| 7    | total_condition = 182 ≥ 180 | Total meets condition    | True         |
| 8    | result = True and True      | All conditions satisfied | True         |
| 9    | print(result)               | Output                   | True         |

### **Final Output**

```
True
```

---
