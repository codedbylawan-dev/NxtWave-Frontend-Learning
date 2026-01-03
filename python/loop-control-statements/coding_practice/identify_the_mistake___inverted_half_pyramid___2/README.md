## 🔻 **13B – Problem 10: Identify the Mistake – Inverted Half Pyramid – 2 (Final Rewrite)**

---

### **1️⃣ Question**

Given a number **N**, write a program to print an **Inverted Right Angled Triangle of N rows** using numbers in **descending order**, with **no spaces between numbers** in each row.

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Inverted Triangle (No-Space Numbers)

---

### **2️⃣ Outline**

- Read integer **N**
- For each row from **N down to 1**
- Print numbers from row value down to 1
- Print each row on a new line

---

### **3️⃣ Objective**

To generate a descending inverted half pyramid using strict formatting.

---

### **4️⃣ Purpose**

To practice:

- loop direction control
- string building
- descending number patterns

---

### **5️⃣ Theory**

For `N = 5`, output must be:

```
54321
4321
321
21
1
```

---

### **6️⃣ Step-by-Step Explanation**

1. Read **N**
2. Loop from **N to 1**
3. For each row:

   - Build a string of descending numbers
   - Print the string

---

### **7️⃣ Method**

- Outer loop → controls number of rows
- Inner loop → builds each row’s sequence
- String concatenation used for output

---

### **8️⃣ Constraints**

- N ≥ 1
- Only loops, arithmetic, and strings allowed

---

### **9️⃣ Common Mistakes**

- Looping upward instead of downward
- Printing spaces between digits
- Wrong loop limits

---

### **🔟 Complexity**

- **Time:** O(N²)
- **Space:** O(N)

---

### **1️⃣1️⃣ Code** ← **Your Final Answer**

```python
n = int(input())

for row_num in range(n, 0, -1):
    row_output = ""
    seq_num = row_num

    while seq_num > 0:
        row_output = row_output + str(seq_num)
        seq_num = seq_num - 1

    print(row_output)
```

---

### **1️⃣2️⃣ Example**

**Input**

```
5
```

**Output**

```
54321
4321
321
21
1
```

---

### **1️⃣3️⃣ Dry Run**

| Row | Printed |
| --- | ------- |
| 5   | 54321   |
| 4   | 4321    |
| 3   | 321     |
| 2   | 21      |
| 1   | 1       |

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output                      |
| ----- | --------------------------- |
| 3     | 321 / 21 / 1                |
| 4     | 4321 / 321 / 21 / 1         |
| 5     | 54321 / 4321 / 321 / 21 / 1 |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Correct loop direction is everything
- Build row as a string before printing
- No spaces allowed between digits

---

### **1️⃣6️⃣ Real-Life Application**

Console UI formatting, data visualization, report printing.

---

### **1️⃣7️⃣ Practice Questions**

1. Print same pattern but with ascending numbers
2. Print all rows on a single line separated by spaces

---

### **1️⃣8️⃣ Result**

Successfully prints the required inverted half pyramid.

---

### **1️⃣9️⃣ Conclusion**

This solution demonstrates precise loop control and formatting mastery.

---

You didn’t just fix the code.
You **understood** the problem.
That’s the real upgrade.
