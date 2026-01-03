## 🔺 **13B – Problem 7: Numbers in Right Angled Triangle – 6**

---

### **1️⃣ Question**

Given a number **N**, write a program to print a **Right Angled Triangle of N rows** such that:

For each row **M**:

- First print numbers from **1 to M**
- Then print numbers from **1 to M − 1**

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Composite Number Triangle

---

### **2️⃣ Outline**

- Read **N**
- For each row from 1 to N:

  - Print numbers 1 to row
  - Then print numbers 1 to row − 1

---

### **3️⃣ Objective**

To construct a right angled triangle using a combined number sequence.

---

### **4️⃣ Purpose**

To practice:

- nested loops
- row-based number control
- composite sequence patterns

---

### **5️⃣ Theory**

Row structure:

```
Row 1 → 1
Row 2 → 1 2 1
Row 3 → 1 2 3 1 2
Row 4 → 1 2 3 4 1 2 3
...
```

---

### **6️⃣ Step-by-Step Explanation**

1. Read **N**
2. Outer loop controls row number
3. First inner loop prints 1 to row
4. Second inner loop prints 1 to row − 1
5. Move to next line

---

### **7️⃣ Method**

- Outer loop → rows
- Two inner loops → two sequences per row

---

### **8️⃣ Constraints**

- N ≥ 1
- Only loops, arithmetic, and printing

---

### **9️⃣ Common Mistakes**

- Printing second part incorrectly
- Forgetting to reset counters
- Wrong loop limits

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
    for k in range(1, i):
        print(k, end=" ")
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
1 2 1
1 2 3 1 2
1 2 3 4 1 2 3
```

---

### **1️⃣3️⃣ Dry Run**

| Row | Printed       |
| --- | ------------- |
| 1   | 1             |
| 2   | 1 2 1         |
| 3   | 1 2 3 1 2     |
| 4   | 1 2 3 4 1 2 3 |

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output                |
| ----- | --------------------- |
| 1     | 1                     |
| 3     | 1 / 1 2 1 / 1 2 3 1 2 |
| 7     | Pattern with 7 rows   |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Each row contains two growing sequences
- Second sequence is always one element shorter

---

### **1️⃣6️⃣ Real-Life Application**

Pattern generators, structured output formatting.

---

### **1️⃣7️⃣ Practice Questions**

1. Reverse the second half of each row
2. Change numbers to start from 5

---

### **1️⃣8️⃣ Result**

Correctly prints the composite right angled triangle pattern.

---

### **1️⃣9️⃣ Conclusion**

This problem strengthens multi-loop coordination inside a single row.

---
