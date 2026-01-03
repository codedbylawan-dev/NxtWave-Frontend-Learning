## 🔺 **13B – Problem 3: Numbers in Right Angled Triangle – 4**

---

### **1️⃣ Question**

Given two numbers **S** and **N**, write a program to print a **Right Angled Triangle of N rows** using numbers starting from **S**, where **each row prints 2 × row numbers**.

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Advanced Number Triangle

---

### **2️⃣ Outline**

- Read **S**
- Read **N**
- Print N rows
- Each row prints **2 × row number** values continuously starting from S

---

### **3️⃣ Objective**

To construct a triangle with controlled growth using continuous numbers.

---

### **4️⃣ Purpose**

To strengthen:

- nested loops
- dynamic row sizing
- continuous number tracking

---

### **5️⃣ Theory**

For row `i`:

- Total numbers printed = `2 × i`
- All numbers increase continuously from S

---

### **6️⃣ Step-by-Step Explanation**

1. Read **S** and **N**
2. Initialize `num = S`
3. For each row from 1 to N:

   - Inner loop runs `2 × row` times
   - Print `num`, then increment

4. Move to next line

---

### **7️⃣ Method**

Use:

- Outer loop → rows
- Inner loop → controls count per row
- One variable for continuous numbers

---

### **8️⃣ Constraints**

- N ≥ 1
- Only loops, arithmetic, printing

---

### **9️⃣ Common Mistakes**

- Using row count instead of `2 × row`
- Resetting number each row
- Forgetting line breaks

---

### **🔟 Complexity**

- **Time:** O(N²)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
s = int(input())
n = int(input())

num = s

for i in range(1, n + 1):
    for j in range(2 * i):
        print(num, end=" ")
        num = num + 1
    print()
```

---

### **1️⃣2️⃣ Example**

**Input:**

```
2
4
```

**Output:**

```
2 3
4 5 6 7
8 9 10 11 12 13
14 15 16 17 18 19 20 21
```

---

### **1️⃣3️⃣ Dry Run**

If `s = 2`, `n = 3`

| Row | Printed         | num after |
| --- | --------------- | --------- |
| 1   | 2 3             | 4         |
| 2   | 4 5 6 7         | 8         |
| 3   | 8 9 10 11 12 13 | 14        |

---

### **1️⃣4️⃣ Test Cases Table**

| S   | N   | Output                              |
| --- | --- | ----------------------------------- |
| 2   | 2   | 2 3 / 4 5 6 7                       |
| 6   | 1   | 6 7                                 |
| 6   | 3   | 6 7 / 8 9 10 11 / 12 13 14 15 16 17 |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Row width depends on formula: `2 × row`
- Continuous counter should never reset

---

### **1️⃣6️⃣ Real-Life Application**

Batch ID generation, grouped data printing.

---

### **1️⃣7️⃣ Practice Questions**

1. Change growth rule to `3 × row`
2. Start from 100 instead of S

---

### **1️⃣8️⃣ Result**

Correctly prints a right angled triangle where each row contains double the previous row count.

---

### **1️⃣9️⃣ Conclusion**

This problem teaches formula-based loop control and disciplined number flow.

---
