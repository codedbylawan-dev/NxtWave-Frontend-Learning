## 🧱 **Problem 10: Numbers in Rectangle – 2**

---

### **1️⃣ Question**

Given two numbers **M** and **N**, write a program to print a **Rectangle of M rows and N columns** using **continuous numbers starting from 1**.

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Number Rectangle (Continuous)

---

### **2️⃣ Outline**

- Read **M** (rows)
- Read **N** (columns)
- Start number at 1
- Print numbers continuously across rows

---

### **3️⃣ Objective**

To construct a rectangle with continuous numbers across rows.

---

### **4️⃣ Purpose**

To practice:

- nested loops
- number tracking
- structured output control

---

### **5️⃣ Theory**

Unlike previous rectangles:

- Numbers do **not reset** per row
- They increase continuously from left to right, top to bottom

---

### **6️⃣ Step-by-Step Explanation**

1. Read **M** and **N**
2. Initialize `num = 1`
3. Outer loop controls rows
4. Inner loop prints N numbers and increments `num`
5. Move to next line after each row

---

### **7️⃣ Method**

Use:

- Outer loop → rows
- Inner loop → columns
- One number variable that never resets

---

### **8️⃣ Constraints**

- M ≥ 1, N ≥ 1
- Only loops, arithmetic, printing

---

### **9️⃣ Common Mistakes**

- Resetting number at each row
- Printing incorrect count of numbers
- Missing line breaks

---

### **🔟 Complexity**

- **Time:** O(M × N)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
m = int(input())
n = int(input())

num = 1

for i in range(m):
    for j in range(n):
        print(num, end=" ")
        num = num + 1
    print()
```

---

### **1️⃣2️⃣ Example**

**Input:**

```
2
3
```

**Output:**

```
1 2 3
4 5 6
```

---

### **1️⃣3️⃣ Dry Run**

If `m = 2`, `n = 3`

| Step  | Printed | num |
| ----- | ------- | --- |
| Start | —       | 1   |
| Row 1 | 1 2 3   | 4   |
| Row 2 | 4 5 6   | 7   |

---

### **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output          |
| --- | --- | --------------- |
| 1   | 5   | 1 2 3 4 5       |
| 3   | 2   | 1 2 / 3 4 / 5 6 |
| 4   | 4   | 1–16 grid       |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Continuous counting is controlled by single variable
- Never reset the counter inside outer loop

---

### **1️⃣6️⃣ Real-Life Application**

Seat numbering, report tables, grid-based data printing.

---

### **1️⃣7️⃣ Practice Questions**

1. Start from 10 instead of 1
2. Print only even numbers continuously

---

### **1️⃣8️⃣ Result**

Correctly prints a continuous-number rectangle.

---

### **1️⃣9️⃣ Conclusion**

This problem enforces number flow control across nested loops.

---
