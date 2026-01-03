## 🔻 **13B – Problem 5: Numbers in Inverted Right Angled Triangle – 2**

---

### **1️⃣ Question**

Given a number **N**, write a program to print an **Inverted Right Angled Triangle of N rows** using numbers starting from **K** in **descending order**, where:

```
K = sum of numbers from 1 to N
```

The triangle must be **right-shifted** such that every next row starts with **two more spaces**.

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Inverted Triangle (Descending with Alignment)

---

### **2️⃣ Outline**

- Read **N**
- Compute **K**
- Print inverted triangle using descending numbers
- Increase left spaces by 2 each row

---

### **3️⃣ Objective**

To generate an inverted triangle with descending numbers and correct indentation.

---

### **4️⃣ Purpose**

To practice:

- arithmetic calculation
- nested loops
- descending number control
- space alignment logic

---

### **5️⃣ Theory**

For N rows:

- Total numbers = `1 + 2 + ... + N`
- Numbers start from **K** and decrease continuously
- Each next row shifts **two spaces right**

---

### **6️⃣ Step-by-Step Explanation**

1. Read **N**
2. Compute `k = n * (n + 1) // 2`
3. Set `num = k`
4. Initialize `space = 0`
5. For each row from **N to 1**:

   - Print `space` spaces
   - Print current row count of numbers
   - Decrease numbers continuously
   - Increase `space` by 2

---

### **7️⃣ Method**

- Outer loop → controls rows
- Inner loop → prints numbers
- One variable for numbers
- One variable for indentation

---

### **8️⃣ Constraints**

- N ≥ 1
- Only loops, arithmetic, and printing

---

### **9️⃣ Common Mistakes**

- Wrong formula for **K**
- Resetting `num`
- Forgetting to update spaces
- Misalignment

---

### **🔟 Complexity**

- **Time:** O(N²)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
n = int(input())

k = n * (n + 1) // 2
num = k
space = 0

for i in range(n, 0, -1):
    print(" " * space, end="")
    for j in range(i):
        print(num, end=" ")
        num = num - 1
    print()
    space = space + 2
```

---

### **1️⃣2️⃣ Example**

**Input:**

```
4
```

**Output:**

```
10 9 8 7
  6 5 4
    3 2
      1
```

---

### **1️⃣3️⃣ Dry Run**

| Row | Spaces | Printed  |
| --- | ------ | -------- |
| 4   | 0      | 10 9 8 7 |
| 3   | 2      | 6 5 4    |
| 2   | 4      | 3 2      |
| 1   | 6      | 1        |

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output                                  |
| ----- | --------------------------------------- |
| 1     | 1                                       |
| 3     | 6 5 4 / 3 2 / 1 (right-shifted)         |
| 5     | 15 → 1 inverted triangle with alignment |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Alignment is controlled by spaces
- Descending sequence must never reset
- Indentation increases consistently

---

### **1️⃣6️⃣ Real-Life Application**

Console UI formatting, pyramid-style visualizations.

---

### **1️⃣7️⃣ Practice Questions**

1. Print same triangle starting from 100
2. Print only even numbers in same pattern

---

### **1️⃣8️⃣ Result**

Correctly prints an aligned inverted right angled triangle with descending numbers.

---

### **1️⃣9️⃣ Conclusion**

This problem combines **arithmetic**, **nested loops**, and **visual alignment control**, completing a serious pattern challenge.

---
