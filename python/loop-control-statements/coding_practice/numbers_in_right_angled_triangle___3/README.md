## 🔺 **13B – Problem 2: Numbers in Right Angled Triangle – 3**

---

### **1️⃣ Question**

Given two numbers **S** and **N**, write a program to print a **Right Angled Triangle of N rows** using **continuous numbers starting from S**.

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Continuous Number Triangle

---

### **2️⃣ Outline**

- Read **S** (starting number)
- Read **N** (number of rows)
- Print N rows with increasing numbers per row continuously

---

### **3️⃣ Objective**

To build a right angled triangle using continuous numbers starting from S.

---

### **4️⃣ Purpose**

To practice:

- nested loops
- continuous number tracking
- row-based pattern construction

---

### **5️⃣ Theory**

In this pattern:

- Row 1 prints 1 number
- Row 2 prints 2 numbers
- …
- Row N prints N numbers
- All numbers increase continuously without reset

---

### **6️⃣ Step-by-Step Explanation**

1. Read **S**
2. Read **N**
3. Set `num = S`
4. Outer loop runs from 1 to N
5. Inner loop prints current row count of numbers
6. Increase `num` after each print
7. Move to next line

---

### **7️⃣ Method**

- Outer loop → controls rows
- Inner loop → prints row values
- One variable maintains continuous counting

---

### **8️⃣ Constraints**

- N ≥ 1
- Use only loops, arithmetic, and printing

---

### **9️⃣ Common Mistakes**

- Resetting number inside outer loop
- Printing wrong number of values per row
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
    for j in range(i):
        print(num, end=" ")
        num = num + 1
    print()
```

---

### **1️⃣2️⃣ Example**

**Input:**

```
10
5
```

**Output:**

```
10
11 12
13 14 15
16 17 18 19
20 21 22 23 24
```

---

### **1️⃣3️⃣ Dry Run**

If `s = 9`, `n = 3`

| Row | Printed  | num after |
| --- | -------- | --------- |
| 1   | 9        | 10        |
| 2   | 10 11    | 12        |
| 3   | 12 13 14 | 15        |

---

### **1️⃣4️⃣ Test Cases Table**

| S   | N   | Output                     |
| --- | --- | -------------------------- |
| 1   | 4   | 1 / 2 3 / 4 5 6 / 7 8 9 10 |
| 5   | 1   | 5                          |
| 9   | 3   | 9 / 10 11 / 12 13 14       |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Continuous patterns use one counter
- Inner loop length depends on row number

---

### **1️⃣6️⃣ Real-Life Application**

Ticket numbering, ordered listings, triangular data structures.

---

### **1️⃣7️⃣ Practice Questions**

1. Start from 100 instead of S
2. Print triangle with only odd numbers

---

### **1️⃣8️⃣ Result**

Successfully prints a continuous-number right angled triangle.

---

### **1️⃣9️⃣ Conclusion**

This problem builds confidence in managing continuous number flow inside nested loops.

---
