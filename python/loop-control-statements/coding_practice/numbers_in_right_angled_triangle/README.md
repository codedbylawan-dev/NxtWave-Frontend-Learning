## 🔺 **Problem 2: Numbers in Right Angled Triangle**

---

### **1️⃣ Question**

Given a number **N**, write a program to print a **Right Angled Triangle** of **N rows** using numbers starting from **1**.

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Number Triangle

---

### **2️⃣ Outline**

- Read integer **N**
- For each row from 1 to N
- Print numbers from 1 to row count

---

### **3️⃣ Objective**

To construct a right angled triangle using numbers.

---

### **4️⃣ Purpose**

To practice:

- nested loops
- increasing patterns
- row-based logic

---

### **5️⃣ Theory**

In a right angled triangle:

- Row 1 prints 1 number
- Row 2 prints 2 numbers
- …
- Row N prints N numbers

---

### **6️⃣ Step-by-Step Explanation**

1. Read input **N**
2. Start outer loop from 1 to N → controls rows
3. Inner loop runs from 1 to current row number
4. Print each number with a space
5. After inner loop, move to next line

---

### **7️⃣ Method**

Use nested loops:

- Outer loop controls number of rows
- Inner loop prints required numbers per row

---

### **8️⃣ Constraints**

- 1 ≤ N ≤ 100
- Use only loops and print statements

---

### **9️⃣ Common Mistakes**

- Printing fixed count in every row
- Forgetting to go to new line after each row
- Mixing up outer and inner loop logic

---

### **🔟 Complexity**

- **Time:** O(N²)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
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
1 2
1 2 3
1 2 3 4
```

---

### **1️⃣3️⃣ Dry Run**

If `n = 4`

| Row | Printed |
| --- | ------- |
| 1   | 1       |
| 2   | 1 2     |
| 3   | 1 2 3   |
| 4   | 1 2 3 4 |

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output                                |
| ----- | ------------------------------------- |
| 1     | 1                                     |
| 3     | 1 / 1 2 / 1 2 3                       |
| 5     | 1 / 1 2 / 1 2 3 / 1 2 3 4 / 1 2 3 4 5 |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Inner loop limit depends on row number
- This is the foundation of most triangle patterns

---

### **1️⃣6️⃣ Real-Life Application**

Used in UI layout building, data grouping displays, pyramid visualizations.

---

### **1️⃣7️⃣ Practice Questions**

1. Print same triangle but starting from 5
2. Print triangle using only odd numbers

---

### **1️⃣8️⃣ Result**

Successfully prints a right angled triangle with increasing numbers.

---

### **1️⃣9️⃣ Conclusion**

This problem trains the core idea of **dynamic row-based loop control**, which is critical for all complex patterns.

---
