## 🔢 **13B – Problem 9: Triplets of Numbers**

---

### **1️⃣ Question**

Given a number **N**, write a program to print the **count of triplets (A, B, C)** from **1 to N** such that:

```
A + B + C = N   and   A < B < C
```

---

### **1️⃣.5️⃣ Category**

Number Logic → Triplet Counting

---

### **2️⃣ Outline**

- Read integer **N**
- Check all possible triplets (A, B, C)
- Count those satisfying sum and order condition

---

### **3️⃣ Objective**

To compute the number of valid triplets whose sum equals N.

---

### **4️⃣ Purpose**

To practice:

- triple nested loops
- strict conditional logic
- controlled counting

---

### **5️⃣ Theory**

A valid triplet must satisfy:

- The sum equals **N**
- Numbers are strictly increasing: **A < B < C**

---

### **6️⃣ Step-by-Step Explanation**

1. Read **N**
2. Set `count = 0`
3. Loop A from 1 to N
4. Loop B from 1 to N
5. Loop C from 1 to N
6. If `A + B + C == N` and `A < B` and `B < C`, increment count
7. After loops, print count

---

### **7️⃣ Method**

- Three nested loops for A, B, C
- One counter
- One compound condition

---

### **8️⃣ Constraints**

- N ≥ 1
- Only loops, arithmetic, and conditions

---

### **9️⃣ Common Mistakes**

- Forgetting strict inequality
- Counting duplicates
- Wrong loop limits

---

### **🔟 Complexity**

- **Time:** O(N³)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
n = int(input())

count = 0

for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(1, n + 1):
            if a + b + c == n and a < b and b < c:
                count = count + 1

print(count)
```

---

### **1️⃣2️⃣ Example**

**Input:**

```
10
```

**Output:**

```
4
```

---

### **1️⃣3️⃣ Dry Run**

For `n = 10`

Valid triplets:

- (1,2,7)
- (1,3,6)
- (1,4,5)
- (2,3,5)

Total = **4**

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----- | ------ |
| 7     | 1      |
| 10    | 4      |
| 12    | 7      |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Enforce strict ordering
- Do not count permutations
- Reset counter only once

---

### **1️⃣6️⃣ Real-Life Application**

Combinatorial analysis, constraint-based optimization problems.

---

### **1️⃣7️⃣ Practice Questions**

1. Print the actual triplets
2. Count triplets where A ≤ B ≤ C

---

### **1️⃣8️⃣ Result**

Correctly counts all valid triplets for given N.

---

### **1️⃣9️⃣ Conclusion**

This problem pushes nested loop reasoning to a new level of control and precision.

---
