## 🔻 **Problem 11: Numbers in Inverted Right Angled Triangle**

---

### **1️⃣ Question**

Given a number **N**, write a program to print an **Inverted Right Angled Triangle of N rows** using numbers starting from **1**.

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Inverted Triangle

---

### **2️⃣ Outline**

- Read integer **N**
- For each row from N down to 1
- Print numbers from 1 up to current row count

---

### **3️⃣ Objective**

To construct an inverted right angled triangle with decreasing width.

---

### **4️⃣ Purpose**

To practice:

- reverse loop control
- nested loops
- decreasing patterns

---

### **5️⃣ Theory**

In this triangle:

- Row 1 prints N numbers
- Row 2 prints N−1 numbers
- …
- Last row prints 1 number

---

### **6️⃣ Step-by-Step Explanation**

1. Read **N**
2. Start outer loop from N down to 1
3. Inner loop prints numbers from 1 to current row count
4. Move to next line after each row

---

### **7️⃣ Method**

Use:

- Outer loop → decreasing rows
- Inner loop → printing numbers

---

### **8️⃣ Constraints**

- N ≥ 1
- Only loops and printing

---

### **9️⃣ Common Mistakes**

- Looping rows in wrong direction
- Printing fixed width each row
- Forgetting line breaks

---

### **🔟 Complexity**

- **Time:** O(N²)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
n = int(input())

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
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
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
```

---

### **1️⃣3️⃣ Dry Run**

If `n = 4`

| Row | Printed |
| --- | ------- |
| 4   | 1 2 3 4 |
| 3   | 1 2 3   |
| 2   | 1 2     |
| 1   | 1       |

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output                |
| ----- | --------------------- |
| 1     | 1                     |
| 3     | 1 2 3 / 1 2 / 1       |
| 6     | 6→1 inverted triangle |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Outer loop direction controls pattern shape
- Inner loop length controls row width

---

### **1️⃣6️⃣ Real-Life Application**

Console visual formatting, decreasing data group displays.

---

### **1️⃣7️⃣ Practice Questions**

1. Print inverted triangle using descending numbers
2. Print inverted triangle starting from 5 instead of 1

---

### **1️⃣8️⃣ Result**

Correctly prints an inverted right angled triangle.

---

### **1️⃣9️⃣ Conclusion**

This problem solidifies control over decreasing patterns and loop direction.

---
