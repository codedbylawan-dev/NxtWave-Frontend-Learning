## 🔻 **13B – Problem 6: Numbers in Right Angled Triangle – 5 (Corrected)**

---

### **1️⃣ Question**

Given two numbers **S** and **N**, write a program to print a **Right Angled Triangle of N rows** using numbers in **descending order**, starting from:

```
K + S − 1
```

where

```
K = 1 + 2 + ... + N
```

The triangle must **grow downward** and the numbers must **decrease continuously** until reaching **S**.

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Descending Number Triangle

---

### **2️⃣ Outline**

- Read **S**
- Read **N**
- Compute **K**
- Start from **K + S − 1**
- Print right angled triangle with increasing row size

---

### **3️⃣ Objective**

To generate a right angled triangle using continuous descending numbers.

---

### **4️⃣ Purpose**

To practice:

- arithmetic calculation
- nested loops
- continuous descending number control
- correct triangle construction

---

### **5️⃣ Theory**

Total numbers printed:

```
1 + 2 + ... + N = K
```

Starting number:

```
K + S − 1
```

Ending number:

```
S
```

Each row prints one more number than the previous row.

---

### **6️⃣ Step-by-Step Explanation**

1. Read **S** and **N**
2. Compute `k = n * (n + 1) // 2`
3. Set `num = k + s - 1`
4. For row from 1 to N:

   - Print current row count of numbers
   - Decrease `num` after every print

5. Move to next line

---

### **7️⃣ Method**

- Outer loop → controls rows (increasing)
- Inner loop → prints numbers
- One variable maintains descending sequence

---

### **8️⃣ Constraints**

- N ≥ 1
- Only loops, arithmetic, and printing

---

### **9️⃣ Common Mistakes**

- Printing inverted shape
- Using ascending numbers
- Resetting `num`

---

### **🔟 Complexity**

- **Time:** O(N²)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
s = int(input())
n = int(input())

k = n * (n + 1) // 2
num = k + s - 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num = num - 1
    print()
```

---

### **1️⃣2️⃣ Example**

**Input:**

```
6
4
```

**Output:**

```
15
14 13
12 11 10
9 8 7 6
```

---

### **1️⃣3️⃣ Dry Run**

| Row | Printed  |
| --- | -------- |
| 1   | 15       |
| 2   | 14 13    |
| 3   | 12 11 10 |
| 4   | 9 8 7 6  |

---

### **1️⃣4️⃣ Test Cases Table**

| S   | N   | Output                          |
| --- | --- | ------------------------------- |
| 6   | 1   | 6                               |
| 6   | 4   | 15 / 14 13 / 12 11 10 / 9 8 7 6 |
| 10  | 3   | 15 / 14 13 / 12 11 10           |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Triangle shape must match problem description
- Number flow must be continuous and descending

---

### **1️⃣6️⃣ Real-Life Application**

Reverse sequence generation, scheduling systems.

---

### **1️⃣7️⃣ Practice Questions**

1. Start from 100 instead of S
2. Change shape to inverted triangle

---

### **1️⃣8️⃣ Result**

Correctly prints a right angled triangle with descending continuous numbers.

---

### **1️⃣9️⃣ Conclusion**

This corrected version aligns perfectly with the required output shape and logic.

---
