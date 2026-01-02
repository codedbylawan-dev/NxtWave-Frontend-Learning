## 🔢 **Problem 8: Prime Numbers from 1 to N**

---

### **1️⃣ Question**

Given a number **N**, write a program to print all **Prime Numbers from 1 to N**, each on a new line.

A **Prime Number** is greater than 1 and has **no factors other than 1 and itself**.

---

### **1️⃣.5️⃣ Category**

Number Logic → Prime Numbers

---

### **2️⃣ Outline**

- Read integer **N**
- For each number from 2 to N:

  - Check how many factors it has
  - If factor count is exactly 2, print the number

---

### **3️⃣ Objective**

To identify and print all prime numbers in the given range.

---

### **4️⃣ Purpose**

To practice:

- nested loops
- factor counting
- conditional checking

---

### **5️⃣ Theory**

A number is **Prime** if:

- It is greater than 1
- It has **exactly two factors** → 1 and itself

---

### **6️⃣ Step-by-Step Explanation**

1. Read **N**
2. Loop `num` from 2 to N
3. For each `num`, set `count = 0`
4. Check all values from 1 to `num`
5. If a value divides `num`, increase `count`
6. After checking, if `count == 2`, print `num`

---

### **7️⃣ Method**

Use:

- Outer loop → each number from 2 to N
- Inner loop → factor checking

---

### **8️⃣ Constraints**

- N ≥ 1
- Only loops, arithmetic, and conditions allowed

---

### **9️⃣ Common Mistakes**

- Including 1 as prime
- Not resetting factor count for each number
- Stopping factor check too early

---

### **🔟 Complexity**

- **Time:** O(N²)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
n = int(input())

for num in range(2, n + 1):
    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        print(num)
```

---

### **1️⃣2️⃣ Example**

**Input:**

```
10
```

**Output:**

```
2
3
5
7
```

---

### **1️⃣3️⃣ Dry Run**

For `num = 5`

| i   | 5 % i | count |
| --- | ----- | ----- |
| 1   | 0     | 1     |
| 2   | 1     | 1     |
| 3   | 2     | 1     |
| 4   | 1     | 1     |
| 5   | 0     | 2     |

`count == 2` → Prime → printed

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output                 |
| ----- | ---------------------- |
| 1     | (no output)            |
| 5     | 2 3 5                  |
| 25    | 2 3 5 7 11 13 17 19 23 |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Prime logic is pure factor checking
- Reset counters for each number
- 1 is not prime, no matter how hard it tries

---

### **1️⃣6️⃣ Real-Life Application**

Used in encryption, security algorithms, hashing systems.

---

### **1️⃣7️⃣ Practice Questions**

1. Print primes between 50 and 100
2. Count how many primes exist from 1 to N

---

### **1️⃣8️⃣ Result**

All prime numbers from 1 to N are printed correctly.

---

### **1️⃣9️⃣ Conclusion**

This problem builds deep understanding of number validation using loops and conditions.

---
