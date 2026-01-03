## 🧮 **13B – Problem 1: Numbers in Square – 3**

---

### **1️⃣ Question**

Given a number **N**, write a program to print a **Square of N rows** using **continuous numbers starting from 1**.

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Continuous Number Square

---

### **2️⃣ Outline**

- Read integer **N**
- Print an **N × N square**
- Numbers must be **continuous** from 1 across all rows

---

### **3️⃣ Objective**

To construct a square pattern where numbers continue increasing across rows.

---

### **4️⃣ Purpose**

To practice:

- nested loops
- continuous number tracking
- structured output control

---

### **5️⃣ Theory**

Unlike a normal square:

- Numbers **do not reset** each row
- They flow continuously from 1 to N²

---

### **6️⃣ Step-by-Step Explanation**

1. Read **N**
2. Initialize `num = 1`
3. Outer loop runs **N** times (rows)
4. Inner loop runs **N** times (columns)
5. Print `num`, then increment
6. Move to next line after each row

---

### **7️⃣ Method**

- Outer loop → row control
- Inner loop → column printing
- Single variable maintains number flow

---

### **8️⃣ Constraints**

- N ≥ 1
- Use only loops, arithmetic, and printing

---

### **9️⃣ Common Mistakes**

- Resetting the number every row
- Printing wrong number of columns
- Forgetting line breaks

---

### **🔟 Complexity**

- **Time:** O(N²)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
n = int(input())

num = 1

for i in range(n):
    for j in range(n):
        print(num, end=" ")
        num = num + 1
    print()
```

---

### **1️⃣2️⃣ Example**

**Input:**

```
3
```

**Output:**

```
1 2 3
4 5 6
7 8 9
```

---

### **1️⃣3️⃣ Dry Run**

If `n = 3`

| Step  | Printed | num |
| ----- | ------- | --- |
| Start | —       | 1   |
| Row 1 | 1 2 3   | 4   |
| Row 2 | 4 5 6   | 7   |
| Row 3 | 7 8 9   | 10  |

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output                      |
| ----- | --------------------------- |
| 1     | 1                           |
| 2     | 1 2 / 3 4                   |
| 5     | Square with numbers 1 to 25 |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Continuous patterns require a single shared counter
- Never reset the counter inside outer loop

---

### **1️⃣6️⃣ Real-Life Application**

Serial number grids, seating layouts, table indexing.

---

### **1️⃣7️⃣ Practice Questions**

1. Start from 10 instead of 1
2. Print only even numbers in the square

---

### **1️⃣8️⃣ Result**

Successfully prints a square of continuous numbers.

---

### **1️⃣9️⃣ Conclusion**

This problem establishes the foundation for all continuous-number patterns in 13B.

---
