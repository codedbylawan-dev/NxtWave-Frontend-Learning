# ✅ **Question: Percentage – 2**

You are given a number **N**.

- X = **30% of N**
- Y = **remaining percentage of N**
  Remaining percentage = **100 − 30 = 70%**

Your task is to **print Y**, which is **70% of N**.

---

# ✅ **Approach**

### **Step 1: Read the Input**

Accept the input number **N**.

---

### **Step 2: Calculate Remaining Percentage**

Remaining percentage = **100 − 30 = 70**

---

### **Step 3: Compute Y**

Y = **70% of N**
Formula:

```
Y = (70 / 100) * N
```

---

### **Step 4: Print the Result**

Print the result as a **decimal number**.

---

# ✅ **Solution Code**

```python
N = int(input())
Y = (70 / 100) * N
print(Y)
```

---

# 🟩 **DRY RUN (Tabular Form)**

Assume Input:

```
50
```

| Step | Operation   | Expression    | Result   |
| ---- | ----------- | ------------- | -------- |
| 1    | Read N      | N = 50        | 50       |
| 2    | Remaining % | 100 − 30      | **70**   |
| 3    | Calculate Y | (70/100) × 50 | **35.0** |
| 4    | Print       | print(35.0)   | **35.0** |

---

### ✅ **Final Output**

```
35.0
```
