## 🧱 **13B – Problem 4: Numbers in Rectangle – 3**

---

### **1️⃣ Question**

Given two numbers **M** and **N**, write a program to print a **Rectangle of M rows and N columns** using numbers starting from **K** in **descending order**, where:

```
K = M × N
```

---

### **1️⃣.5️⃣ Category**

Pattern Printing → Descending Number Rectangle

---

### **2️⃣ Outline**

- Read **M**
- Read **N**
- Compute **K = M × N**
- Print rectangle with numbers from K down to 1

---

### **3️⃣ Objective**

To construct a rectangle pattern using descending numbers.

---

### **4️⃣ Purpose**

To practice:

- arithmetic computation
- nested loops
- reverse number flow

---

### **5️⃣ Theory**

Rectangle has:

- **M rows**
- **N columns**
- Total numbers = **M × N**
- Numbers printed in descending order

---

### **6️⃣ Step-by-Step Explanation**

1. Read **M** and **N**
2. Compute `k = m * n`
3. Set `num = k`
4. Outer loop runs M times
5. Inner loop runs N times
6. Print `num` then decrement
7. Move to next row

---

### **7️⃣ Method**

- Outer loop → rows
- Inner loop → columns
- Single variable controls descending numbers

---

### **8️⃣ Constraints**

- M ≥ 1, N ≥ 1
- Only loops, arithmetic, printing

---

### **9️⃣ Common Mistakes**

- Forgetting to calculate K correctly
- Resetting num each row
- Printing in ascending order by mistake

---

### **🔟 Complexity**

- **Time:** O(M × N)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
m = int(input())
n = int(input())

k = m * n
num = k

for i in range(m):
    for j in range(n):
        print(num, end=" ")
        num = num - 1
    print()
```

---

### **1️⃣2️⃣ Example**

**Input:**

```
2
3
```

**Output:**

```
6 5 4
3 2 1
```

---

### **1️⃣3️⃣ Dry Run**

If `m = 2`, `n = 3`

| Step  | Printed | num |
| ----- | ------- | --- |
| Start | —       | 6   |
| Row 1 | 6 5 4   | 3   |
| Row 2 | 3 2 1   | 0   |

---

### **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output          |
| --- | --- | --------------- |
| 1   | 4   | 4 3 2 1         |
| 3   | 2   | 6 5 / 4 3 / 2 1 |
| 6   | 5   | 30 to 1 grid    |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Compute total count before printing
- Do not reset the counter inside loops

---

### **1️⃣6️⃣ Real-Life Application**

Reverse indexing, countdown tables, report ordering.

---

### **1️⃣7️⃣ Practice Questions**

1. Start from 100 instead of M × N
2. Print rectangle using only even numbers descending

---

### **1️⃣8️⃣ Result**

Successfully prints descending number rectangle.

---

### **1️⃣9️⃣ Conclusion**

This problem trains descending control inside structured nested loops.

---
