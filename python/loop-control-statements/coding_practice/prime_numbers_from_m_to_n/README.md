## 🔢 **Problem 9: Prime Numbers from M to N**

---

### **1️⃣ Question**

Given two numbers **M** and **N**, write a program to print all **Prime Numbers** in the range **M to N**.
If **no prime numbers exist**, print:

```
No Prime Numbers Found
```

---

### **1️⃣.5️⃣ Category**

Number Logic → Prime Numbers (Range Based)

---

### **2️⃣ Outline**

- Read **M** and **N**
- For each number from M to N:

  - Check if it is prime
  - Print it if prime

- If no primes were printed, display message

---

### **3️⃣ Objective**

To detect and display all prime numbers within a given range.

---

### **4️⃣ Purpose**

To strengthen:

- nested loops
- factor counting
- conditional control
- output validation

---

### **5️⃣ Theory**

A number is **Prime** if:

- It is greater than 1
- It has **exactly two factors**

---

### **6️⃣ Step-by-Step Explanation**

1. Read **M**
2. Read **N**
3. Set `found = False`
4. Loop `num` from M to N
5. For each `num`, count its factors
6. If factor count is 2:

   - Print the number
   - Set `found = True`

7. After loop:

   - If `found` is False, print message

---

### **7️⃣ Method**

- Outer loop → range M to N
- Inner loop → factor checking
- Flag variable to track existence of primes

---

### **8️⃣ Constraints**

- M and N are positive integers
- M ≤ N
- Use only loops, arithmetic, conditions

---

### **9️⃣ Common Mistakes**

- Treating 1 as prime
- Forgetting to reset factor count
- Printing message even when primes exist

---

### **🔟 Complexity**

- **Time:** O((N−M+1) × N)
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
m = int(input())
n = int(input())

found = False

for num in range(m, n + 1):
    if num > 1:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1

        if count == 2:
            print(num, end=" ")
            found = True

if found == False:
    print("No Prime Numbers Found")
```

---

### **1️⃣2️⃣ Example**

**Input:**

```
3
15
```

**Output:**

```
3 5 7 11 13
```

**Input:**

```
8
10
```

**Output:**

```
No Prime Numbers Found
```

---

### **1️⃣3️⃣ Dry Run**

For range 8 to 10:

| num | factors | prime? |
| --- | ------- | ------ |
| 8   | 4       | No     |
| 9   | 3       | No     |
| 10  | 4       | No     |

No primes → message printed.

---

### **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output                 |
| --- | --- | ---------------------- |
| 1   | 5   | 2 3 5                  |
| 3   | 3   | 3                      |
| 8   | 10  | No Prime Numbers Found |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Always verify existence before printing final message
- 1 is never prime
- Range logic uses same prime test repeatedly

---

### **1️⃣6️⃣ Real-Life Application**

Prime range checks in cryptography, key generation, and data validation.

---

### **1️⃣7️⃣ Practice Questions**

1. Print primes from 100 to 150
2. Count how many primes exist between M and N

---

### **1️⃣8️⃣ Result**

Correctly prints all primes in the given range or a failure message.

---

### **1️⃣9️⃣ Conclusion**

This problem trains conditional output control and range-based number analysis.

---
