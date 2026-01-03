## 🔢 **13B – Problem 8: Pair of Numbers**

---

### **1️⃣ Question**

Given a number **N**, write a program to print the **count of pairs (A, B)** from **1 to N** such that:

```
A + B = N   and   A < B
```

---

### **1️⃣.5️⃣ Category**

Number Logic → Pair Counting

---

### **2️⃣ Outline**

- Read integer **N**
- Check all possible pairs (A, B)
- Count pairs where A + B = N and A < B
- Print the count

---

### **3️⃣ Objective**

To compute how many valid number pairs satisfy the given condition.

---

### **4️⃣ Purpose**

To practice:

- nested loops
- conditional logic
- counting with constraints

---

### **5️⃣ Theory**

For numbers 1 to N:

- Every pair is tested
- Only pairs with **A + B = N** and **A < B** are valid

---

### **6️⃣ Step-by-Step Explanation**

1. Read **N**
2. Set `count = 0`
3. Loop A from 1 to N
4. Loop B from 1 to N
5. If `A + B == N` and `A < B`, increase count
6. After loops, print count

---

### **7️⃣ Method**

- Two nested loops for A and B
- One counter to track valid pairs
- One condition to filter correct pairs

---

### **8️⃣ Constraints**

- N ≥ 1
- Only loops, arithmetic, and conditions

---

### **9️⃣ Common Mistakes**

- Forgetting `A < B`
- Counting the same pair twice
- Using incorrect range

---

### **🔟 Complexity**

- **Time:** O(N²)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
n = int(input())

count = 0

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a + b == n and a < b:
            count = count + 1

print(count)
```

---

### **1️⃣2️⃣ Example**

**Input:**

```
7
```

**Output:**

```
3
```

---

### **1️⃣3️⃣ Dry Run**

For `n = 7`

Valid pairs:

- (1,6)
- (2,5)
- (3,4)

Total = **3**

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----- | ------ |
| 5     | 2      |
| 7     | 3      |
| 10    | 4      |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Always enforce `A < B`
- Count only valid pairs

---

### **1️⃣6️⃣ Real-Life Application**

Budget splitting, combination analysis, constraint-based pairing systems.

---

### **1️⃣7️⃣ Practice Questions**

1. Print the actual pairs instead of count
2. Count pairs where A ≤ B

---

### **1️⃣8️⃣ Result**

Correctly counts all valid pairs whose sum equals N.

---

### **1️⃣9️⃣ Conclusion**

This problem introduces systematic pair evaluation using nested loops and conditions.

---
