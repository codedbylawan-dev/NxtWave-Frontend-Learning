## 🧱 **Problem 3: Numbers in Rectangle**

---

### **1️⃣ Question**

Given two numbers **M** and **N**, write a program to print a **rectangle of M rows and N columns** using numbers starting from **7**.

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Number Rectangle

---

### **2️⃣ Outline**

- Read **M** (rows)
- Read **N** (columns)
- For each row, print numbers from 7 to (7 + N − 1)

---

### **3️⃣ Objective**

To print a rectangle pattern of given dimensions using consecutive numbers starting from 7.

---

### **4️⃣ Purpose**

To practice:

- nested loops
- multi-input handling
- fixed-width pattern printing

---

### **5️⃣ Theory**

A rectangle pattern:

- Has **M rows**
- Each row contains **N numbers**
- Every row prints the **same sequence**

---

### **6️⃣ Step-by-Step Explanation**

1. Read input **M**
2. Read input **N**
3. Start outer loop from 1 to M
4. Inside it, run inner loop N times
5. Start printing from number 7 and increase by 1 for each column
6. Move to next line after finishing one row

---

### **7️⃣ Method**

- Outer loop → controls rows
- Inner loop → prints N numbers starting from 7

---

### **8️⃣ Constraints**

- M ≥ 1, N ≥ 1
- Only loops and printing allowed

---

### **9️⃣ Common Mistakes**

- Resetting starting number incorrectly
- Printing more or fewer than N numbers per row
- Forgetting new line after each row

---

### **🔟 Complexity**

- **Time:** O(M × N)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
m = int(input())
n = int(input())

for i in range(m):
    num = 7
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
7 8 9
7 8 9
```

---

### **1️⃣3️⃣ Dry Run**

If `m = 2`, `n = 3`

| Row | Printed |
| --- | ------- |
| 1   | 7 8 9   |
| 2   | 7 8 9   |

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output            |
| ----- | ----------------- |
| 1, 1  | 7                 |
| 3, 4  | 7 8 9 10 (3 rows) |
| 5, 2  | 7 8 (5 rows)      |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Reset number inside outer loop
- Rectangle uses independent row and column control

---

### **1️⃣6️⃣ Real-Life Application**

Tabular displays, reports, seating layouts, grid printing.

---

### **1️⃣7️⃣ Practice Questions**

1. Change starting number to 3
2. Print same rectangle but reverse numbers

---

### **1️⃣8️⃣ Result**

Successfully prints a rectangle with given rows and columns starting from 7.

---

### **1️⃣9️⃣ Conclusion**

This problem reinforces understanding of **two-dimensional loop control** and fixed-size pattern construction.

---
