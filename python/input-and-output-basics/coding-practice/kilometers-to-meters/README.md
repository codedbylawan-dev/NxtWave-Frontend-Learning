# **Question: Kilometers to Meters**

Write a program to take the number of kilometers as input and convert it into meters.

**Conversion formula:**
1 Kilometer = 1000 Meters

### **Input**

- First line: number of kilometers (can have a decimal part)

### **Output**

- First line: number of meters (integer)

### **Explanation**

Example:
Input: 1.2 kilometers
Conversion: 1.2 × 1000 = **1200 meters**
Output: 1200

---

# **Approach**

### **Step 1: Read the input**

```python
kilometers = input()
```

### **Step 2: Convert input to float**

```python
kilometers = float(kilometers)
```

### **Step 3: Convert kilometers to meters**

```python
meters = kilometers * 1000
```

### **Step 4: Convert result to integer**

```python
meters = int(meters)
```

### **Step 5: Print the result**

```python
print(meters)
```

---

# **Complete Code**

```python
kilometers = input()
kilometers = float(kilometers)

meters = kilometers * 1000
meters = int(meters)

print(meters)
```

---

# 🟩 **DRY RUN (Tabular Form)**

| Step No. | Operation        | Value / Explanation |
| -------- | ---------------- | ------------------- |
| 1        | Read input       | `"1.2"`             |
| 2        | Convert to float | 1.2                 |
| 3        | Multiply by 1000 | 1.2 × 1000 = 1200.0 |
| 4        | Convert to int   | 1200                |
| 5        | Print output     | 1200                |

---

### **Final Output**

```
1200
```

---
