## 🧱 **Problem 12: Half Pyramid – 2**

---

### **1️⃣ Question**

Write a program to print numbers in **N rows** in a **half pyramid pattern** using **consecutive numbers**.

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Half Pyramid (Continuous Numbers)

---

### **2️⃣ Outline**

- Read integer **N**
- Maintain a continuous counter starting from 1
- Print increasing number of values per row

---

### **3️⃣ Objective**

To build a half pyramid using continuous increasing numbers.

---

### **4️⃣ Purpose**

To practice:

- nested loops
- continuous number tracking
- increasing pattern logic

---

### **5️⃣ Theory**

In this pattern:

- Row 1 → 1 number
- Row 2 → 2 numbers
- …
- Row N → N numbers
- Numbers increase continuously across rows

---

### **6️⃣ Step-by-Step Explanation**

1. Read **N**
2. Set `num = 1`
3. Outer loop from 1 to N
4. Inner loop runs current row count times
5. Print `num` and increase it
6. After each row, move to new line

---

### **7️⃣ Method**

Use:

- Outer loop → controls rows
- Inner loop → prints row values
- Single counter variable for continuity

---

### **8️⃣ Constraints**

- N ≥ 1
- Only loops, arithmetic, and printing allowed

---

### **9️⃣ Common Mistakes**

- Resetting `num` each row
- Printing fixed amount per row
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
5
```

**Output:**

```
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
```

---

### **1️⃣3️⃣ Dry Run**

If `n = 4`

| Row | Printed  | num after |
| --- | -------- | --------- |
| 1   | 1        | 2         |
| 2   | 2 3      | 4         |
| 3   | 4 5 6    | 7         |
| 4   | 7 8 9 10 | 11        |

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output                     |
| ----- | -------------------------- |
| 1     | 1                          |
| 3     | 1 / 2 3 / 4 5 6            |
| 5     | Half pyramid of 15 numbers |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Continuous counting across nested loops
- Inner loop length defines pyramid width
- Outer loop defines height

---

### **1️⃣6️⃣ Real-Life Application**

Numbered task lists, ordered display structures, report formatting.

---

### **1️⃣7️⃣ Practice Questions**

1. Start from 10 instead of 1
2. Print only odd numbers in pyramid

---

### **1️⃣8️⃣ Result**

Successfully prints a half pyramid with continuous numbers.

---

### **1️⃣9️⃣ Conclusion**

This problem completes the entire **13A problem set**, proving full control over nested loops, patterns, and number flow.
