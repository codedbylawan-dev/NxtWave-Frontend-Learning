## 🔢 **Problem 13: Prime Numbers from M to N (2nd Version)**

---

### **1️⃣ Question**

Given two integers **M** and **N**, write a program to print all the **Prime Numbers from M to N**, each on a new line.

---

### **1️⃣.5️⃣ Category**

Number Logic → Prime Numbers (Range Based, Line Output)

---

### **2️⃣ Outline**

- Read integer **M**
- Read integer **N**
- For each number from M to N:

  - Check if it is prime
  - Print it on a new line if prime

---

### **3️⃣ Objective**

To detect and print all prime numbers within a given range, one per line.

---

### **4️⃣ Purpose**

To strengthen:

- nested loops
- factor counting
- range-based validation
- strict output control

---

### **5️⃣ Theory**

A number is **Prime** if:

- It is greater than 1
- It has **exactly two factors**: 1 and itself

---

### **6️⃣ Step-by-Step Explanation**

1. Read **M**
2. Read **N**
3. Loop from **M to N**
4. For each number:

   - Count its factors

5. If factor count is exactly 2:

   - Print the number on a new line

---

### **7️⃣ Method**

- Outer loop → iterates from M to N
- Inner loop → checks all possible factors
- Condition → decides if the number is prime

---

### **8️⃣ Constraints**

- M and N are positive integers
- M ≤ N
- Only loops, arithmetic, and conditions allowed

---

### **9️⃣ Common Mistakes**

- Printing 1 as a prime number
- Forgetting to reset factor counter
- Printing in the same line instead of new line

---

### **🔟 Complexity**

- **Time:** O((N − M + 1) × N)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
m = int(input())
n = int(input())

for num in range(m, n + 1):
    if num > 1:
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
5
11
```

**Output:**

```
5
7
11
```

---

### **1️⃣3️⃣ Dry Run**

For range 5 to 11:

| num | factors | prime? | printed |
| --- | ------- | ------ | ------- |
| 5   | 2       | Yes    | 5       |
| 6   | 4       | No     | —       |
| 7   | 2       | Yes    | 7       |
| 8   | 4       | No     | —       |
| 9   | 3       | No     | —       |
| 10  | 4       | No     | —       |
| 11  | 2       | Yes    | 11      |

---

### **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output                 |
| --- | --- | ---------------------- |
| 5   | 11  | 5 / 7 / 11             |
| 18  | 40  | 19 / 23 / 29 / 31 / 37 |
| 1   | 5   | 2 / 3 / 5              |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Always exclude numbers ≤ 1
- Prime detection is pure factor logic
- One line per prime is mandatory here

---

### **1️⃣6️⃣ Real-Life Application**

Used in cryptography, secure key generation, and number theory systems.

---

### **1️⃣7️⃣ Practice Questions**

1. Print primes from 50 to 100
2. Count how many primes exist between 1 and N

---

### **1️⃣8️⃣ Result**

All prime numbers between **M and N** are printed correctly, one per line.

---

### **1️⃣9️⃣ Conclusion**

This final problem completes your **13-problem logic set**, proving full control over nested loops, conditions, and number validation.

---
