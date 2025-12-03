# 🔹 **Question: Eligibility Criteria – 4**

Write a program that reads marks in **Maths (M)**, **Physics (P)**, and **Chemistry (C)** and checks whether **any ONE** of the following conditions is satisfied:

### ✔ Condition 1:

- M ≥ 60
- P ≥ 50
- C ≥ 45
- M + P + C ≥ 180

### ✔ Condition 2:

- M + P ≥ 120
  **OR**
- C + P ≥ 110

If **any** of these two major conditions is satisfied → print **True**, otherwise print **False**.

---

# 🟦 **1. Question Explanation**

You must check **two different eligibility paths**:

### **Path 1 (Strict subject-wise + total):**

All these must be true:

- Maths ≥ 60
- Physics ≥ 50
- Chemistry ≥ 45
- Total marks ≥ 180

### **Path 2 (High scoring combinations):**

Either:

- M + P ≥ 120
  or
- C + P ≥ 110

If **any one** of the two paths satisfies → result is **True**.

---

# 🟩 **2. Approach**

1. Read M, P, C
2. Check condition group 1
3. Check condition group 2
4. Combine using `or`
5. Print result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read marks**

```python
M = int(input())
P = int(input())
C = int(input())
```

### **Step 2: Check strict subject & total condition**

```python
cond1 = (M >= 60) and (P >= 50) and (C >= 45) and (M + P + C >= 180)
```

### **Step 3: Check high-scoring pair condition**

```python
cond2 = (M + P >= 120) or (C + P >= 110)
```

### **Step 4: Combine using OR**

```python
result = cond1 or cond2
```

### **Step 5: Print result**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
M = int(input())
P = int(input())
C = int(input())

cond1 = (M >= 60) and (P >= 50) and (C >= 45) and (M + P + C >= 180)

cond2 = (M + P >= 120) or (C + P >= 110)

result = cond1 or cond2

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Sample Input**

```
72
65
51
```

### **Dry Run Table**

| Step | Operation                              | Explanation                  | Result |
| ---- | -------------------------------------- | ---------------------------- | ------ |
| 1    | M=72, P=65, C=51                       | Inputs                       | —      |
| 2    | cond1: (72≥60) and (65≥50) and (51≥45) | All subjects meet criteria   | True   |
|      | Total = 72+65+51 = 188 ≥ 180           | Total meets condition        | True   |
|      | cond1 = True and True                  | Full condition satisfied     | True   |
| 3    | cond2: (72+65 = 137 ≥ 120)             | One pair sufficient          | True   |
|      | No need to check C+P                   | Already True                 | True   |
| 4    | result = True or True                  | At least one condition works | True   |
| 5    | print(result)                          | Final output                 | True   |

### **Final Output**

```
True
```

---
