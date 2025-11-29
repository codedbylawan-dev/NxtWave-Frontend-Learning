# **Question: Percentage of a Number**

Write a program that reads a percentage `P` and prints `P` percent of the number 200.

**Formula:**
`Value = (P / 100) × 200`

### **Input**

- First line: an integer representing the percentage `P`

### **Output**

- First line: float representing `P` percent of 200

### **Explanation**

Example:
Input: 50
Calculation: (50 / 100) × 200 = 100.0
Output: 100.0

---

# **Approach**

### **Step 1: Read the input**

```python
percentage = input()
```

### **Step 2: Convert input to integer**

```python
percentage = int(percentage)
```

### **Step 3: Calculate percentage of 200**

```python
value = (percentage / 100) * 200
```

### **Step 4: Print the result**

```python
print(value)
```

---

# **Complete Code**

```python
percentage = input()
percentage = int(percentage)

value = (percentage / 100) * 200
print(value)
```

---

# 🟩 **DRY RUN (Tabular Form)**

| Step No. | Operation                   | Value / Explanation      |
| -------- | --------------------------- | ------------------------ |
| 1        | Read input                  | `"50"`                   |
| 2        | Convert to int              | 50                       |
| 3        | Calculate percentage of 200 | (50 / 100) × 200 = 100.0 |
| 4        | Print output                | 100.0                    |

---

### **Final Output**

```
100.0
```

---
