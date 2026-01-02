## 🔺 **Problem 4: Numbers in Pyramid**

---

### **1️⃣ Question**

Given two numbers **S** and **N**, write a program to print a **Pyramid of N rows** using numbers starting from **S**.

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Number Pyramid

---

### **2️⃣ Outline**

- Read **S** (starting number)
- Read **N** (number of rows)
- Print pyramid with increasing numbers and leading spaces

---

### **3️⃣ Objective**

To construct a pyramid pattern using numbers with correct alignment.

---

### **4️⃣ Purpose**

To practice:

- nested loops
- space handling
- centered pattern construction

---

### **5️⃣ Theory**

In a pyramid:

- Each row has **leading spaces**
- Numbers increase per row
- Alignment is essential

---

### **6️⃣ Step-by-Step Explanation**

1. Read **S** and **N**
2. Start outer loop from 1 to N → controls rows
3. First inner loop prints spaces: `(N - row)` times
4. Second inner loop prints numbers: from S to `(S + row - 1)`
5. Move to next line

---

### **7️⃣ Method**

Use nested loops:

- Loop 1 → spaces
- Loop 2 → numbers

---

### **8️⃣ Constraints**

- N ≥ 1
- Only basic loops and printing allowed

---

### **9️⃣ Common Mistakes**

- Wrong number of spaces
- Numbers not starting from S
- Misaligned pyramid

---

### **🔟 Complexity**

- **Time:** O(N²)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
s = int(input())
n = int(input())

for i in range(1, n + 1):
    for space in range(n - i):
        print(" ", end="")
    num = s
    for j in range(i):
        print(num, end=" ")
        num = num + 1
    print()
```

---

### **1️⃣2️⃣ Example**

**Input:**

```
7
5
```

**Output:**

```
    7
   7 8
  7 8 9
 7 8 9 10
7 8 9 10 11
```

---

### **1️⃣3️⃣ Dry Run**

If `s = 7`, `n = 3`

| Row | Spaces | Numbers |
| --- | ------ | ------- |
| 1   | 2      | 7       |
| 2   | 1      | 7 8     |
| 3   | 0      | 7 8 9   |

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output                            |
| ----- | --------------------------------- |
| 3, 3  | Pyramid of 3 rows starting from 3 |
| 5, 1  | 5                                 |
| 2, 4  | Pyramid of 4 rows starting from 2 |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Spaces control shape
- Numbers increase based on row
- Alignment is part of the problem

---

### **1️⃣6️⃣ Real-Life Application**

Data visualization, charts, console UI formatting.

---

### **1️⃣7️⃣ Practice Questions**

1. Reverse the pyramid
2. Change number increment pattern

---

### **1️⃣8️⃣ Result**

Correctly prints a centered number pyramid of N rows.

---

### **1️⃣9️⃣ Conclusion**

This problem teaches precision control over spacing and number growth in patterns.

---
