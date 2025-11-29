# **Question: Remainder of Two Numbers**

Write a program that reads a dividend and a divisor and prints the remainder.

**Formula:**
`remainder = dividend % divisor`
or equivalently:
`quotient = dividend // divisor`
`remainder = dividend - (divisor * quotient)`

### **Input**

- First line: dividend (integer)
- Second line: divisor (integer)

### **Output**

- Single line: integer remainder

### **Explanation**

Example:
Dividend = 7, Divisor = 2
Quotient = 7 // 2 = 3
Remainder = 7 - (2 × 3) = 1
Output: 1

---

# **Approach**

### **Step 1: Read the input**

```python
dividend = int(input())
divisor = int(input())
```

### **Step 2: Calculate quotient and remainder**

```python
quotient = dividend // divisor
remainder = dividend % divisor
```

### **Step 3: Print the remainder**

```python
print(remainder)
```

---

# **Complete Code**

```python
dividend = int(input())
divisor = int(input())

quotient = dividend // divisor
remainder = dividend % divisor

print(remainder)
```

---

# 🟩 **DRY RUN (Tabular Form)**

| Step No. | Operation           | Value / Explanation |
| -------- | ------------------- | ------------------- |
| 1        | Read dividend       | 7                   |
| 2        | Read divisor        | 2                   |
| 3        | Calculate quotient  | 7 // 2 = 3          |
| 4        | Calculate remainder | 7 % 2 = 1           |
| 5        | Print remainder     | 1                   |

---

### **Final Output**

```
1
```

---
