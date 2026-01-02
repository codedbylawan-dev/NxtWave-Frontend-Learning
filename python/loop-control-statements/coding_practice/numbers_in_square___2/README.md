## 🔲 **Problem 5: Numbers in Square – 2**

---

### **1️⃣ Question**

Given a number **N**, write a program to print a **square of N rows** using numbers from **N to 1** (descending order).

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Number Square (Descending)

---

### **2️⃣ Outline**

- Read integer **N**
- For each row, print numbers from **N down to 1**

---

### **3️⃣ Objective**

To construct a square pattern where each row prints descending numbers.

---

### **4️⃣ Purpose**

To practice:

- reverse number logic
- nested loops
- controlled printing

---

### **5️⃣ Theory**

A square has:

- **N rows**
- **N columns**
- Each row prints the same descending sequence

---

### **6️⃣ Step-by-Step Explanation**

1. Read input **N**
2. Start outer loop from 1 to N → controls rows
3. Start inner loop from N down to 1
4. Print each number with space
5. After inner loop, move to next line

---

### **7️⃣ Method**

Use nested loops:

- Outer loop for rows
- Inner loop for descending number print

---

### **8️⃣ Constraints**

- N ≥ 1
- Only loops and printing

---

### **9️⃣ Common Mistakes**

- Printing in ascending order
- Forgetting to reset number for each row
- Incorrect spacing

---

### **🔟 Complexity**

- **Time:** O(N²)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
n = int(input())

for i in range(n):
    for j in range(n, 0, -1):
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
3 2 1
3 2 1
3 2 1
```

---

### **1️⃣3️⃣ Dry Run**

If `n = 3`

| Row | Printed |
| --- | ------- |
| 1   | 3 2 1   |
| 2   | 3 2 1   |
| 3   | 3 2 1   |

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output             |
| ----- | ------------------ |
| 1     | 1                  |
| 4     | 4 3 2 1 (4 rows)   |
| 5     | 5 4 3 2 1 (5 rows) |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Reverse counting handled inside inner loop
- Reset happens automatically due to loop range

---

### **1️⃣6️⃣ Real-Life Application**

Countdown displays, reverse indexing tables.

---

### **1️⃣7️⃣ Practice Questions**

1. Start from 10 instead of N
2. Print only odd numbers in descending square

---

### **1️⃣8️⃣ Result**

Successfully prints a square of descending numbers.

---

### **1️⃣9️⃣ Conclusion**

This problem strengthens understanding of loop direction and number control.

---
