## 🧮 **Problem 1: Numbers in Square**

---

### **1️⃣ Question**

Given a number **N**, write a program to print a **square of N rows** using numbers starting from **1**.

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Number Square

---

### **2️⃣ Outline**

- Read integer **N**
- For each row from 1 to N
- Print numbers from 1 to N in one line

---

### **3️⃣ Objective**

To generate a square pattern of size **N × N** using numbers from **1** to **N**.

---

### **4️⃣ Purpose**

To practice:

- `for` loops
- number printing
- basic pattern building

---

### **5️⃣ Theory**

A square pattern means:

- **Same number of rows and columns**
- Each row prints the same sequence of numbers

---

### **6️⃣ Step-by-Step Explanation**

1. Take input **N**
2. Start outer loop for rows → repeat **N** times
3. Inside it, start inner loop for columns from **1 to N**
4. Print each number with a space
5. After inner loop, move to next line

---

### **7️⃣ Method**

Use **nested for-loops**:

- Outer loop → controls rows
- Inner loop → controls columns and printing

---

### **8️⃣ Constraints**

- **1 ≤ N ≤ 100** (assumed reasonable input)
- Only basic loops and printing allowed

---

### **9️⃣ Common Mistakes**

- Forgetting to move to next line after each row
- Printing without space formatting
- Using extra loops or advanced features

---

### **🔟 Complexity**

- **Time:** O(N²)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
n = int(input())

for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
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
1 2 3
1 2 3
```

---

### **1️⃣3️⃣ Dry Run**

If `n = 3`

| Outer Loop | Inner Loop prints | Output Row |
| ---------- | ----------------- | ---------- |
| i = 0      | 1 2 3             | 1 2 3      |
| i = 1      | 1 2 3             | 1 2 3      |
| i = 2      | 1 2 3             | 1 2 3      |

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output             |
| ----- | ------------------ |
| 1     | 1                  |
| 2     | 1 2 / 1 2          |
| 5     | 1 2 3 4 5 (5 rows) |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Outer loop controls **rows**
- Inner loop controls **columns**
- Pattern logic always follows row–column thinking

---

### **1️⃣6️⃣ Real-Life Application**

Grid printing, game boards, matrix displays, tabular layouts.

---

### **1️⃣7️⃣ Practice Questions**

1. Print same square but starting from 5 instead of 1
2. Print square using only even numbers

---

### **1️⃣8️⃣ Result**

Successfully prints an **N × N number square** starting from 1.

---

### **1️⃣9️⃣ Conclusion**

This problem builds the core idea of **nested loops and structured pattern construction**, which is the backbone of all upcoming pattern problems.

---
