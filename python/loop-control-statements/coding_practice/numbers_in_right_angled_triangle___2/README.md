## 🔻 **Problem 6: Numbers in Right Angled Triangle – 2**

---

### **1️⃣ Question**

Given a number **N**, write a program to print a **Right Angled Triangle of N rows** using numbers starting from **1**, **decreasing in each row**.

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Number Triangle (Reverse per row)

---

### **2️⃣ Outline**

- Read integer **N**
- For each row from 1 to N
- Print numbers from current row down to 1

---

### **3️⃣ Objective**

To generate a right angled triangle where numbers decrease from left to right in each row.

---

### **4️⃣ Purpose**

To practice:

- nested loops
- reverse counting
- row-dependent logic

---

### **5️⃣ Theory**

In this triangle:

- Row 1 prints: `1`
- Row 2 prints: `2 1`
- Row 3 prints: `3 2 1`
- Row N prints: `N ... 2 1`

---

### **6️⃣ Step-by-Step Explanation**

1. Read **N**
2. Start outer loop from 1 to N → controls rows
3. Inner loop runs from current row down to 1
4. Print each number with a space
5. After inner loop, move to next line

---

### **7️⃣ Method**

Use nested loops:

- Outer loop → row count
- Inner loop → descending numbers

---

### **8️⃣ Constraints**

- N ≥ 1
- Only loops and printing allowed

---

### **9️⃣ Common Mistakes**

- Printing in ascending order
- Wrong inner loop range
- Forgetting to go to new line

---

### **🔟 Complexity**

- **Time:** O(N²)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
n = int(input())

for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
```

---

### **1️⃣2️⃣ Example**

**Input:**

```
4
```

**Output:**

```
1
2 1
3 2 1
4 3 2 1
```

---

### **1️⃣3️⃣ Dry Run**

If `n = 4`

| Row | Printed |
| --- | ------- |
| 1   | 1       |
| 2   | 2 1     |
| 3   | 3 2 1   |
| 4   | 4 3 2 1 |

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output                                |
| ----- | ------------------------------------- |
| 1     | 1                                     |
| 3     | 1 / 2 1 / 3 2 1                       |
| 5     | 1 / 2 1 / 3 2 1 / 4 3 2 1 / 5 4 3 2 1 |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Inner loop controls reverse order
- Row number determines max value

---

### **1️⃣6️⃣ Real-Life Application**

Reverse ordering in reports, countdown group displays.

---

### **1️⃣7️⃣ Practice Questions**

1. Start from 10 instead of N
2. Print only even numbers in the triangle

---

### **1️⃣8️⃣ Result**

Successfully prints a reverse-number right angled triangle.

---

### **1️⃣9️⃣ Conclusion**

This problem completes the core triangle family and cements descending loop logic.

---
