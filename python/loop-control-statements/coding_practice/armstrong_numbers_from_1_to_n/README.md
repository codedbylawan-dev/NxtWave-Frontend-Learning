## 🔢 **Problem 7: Armstrong Numbers from 1 to N**

---

### **1️⃣ Question**

Given a number **N**, write a program to print all **Armstrong numbers from 1 to N**, each on a new line.

A number is called **Armstrong** if the **sum of each digit raised to the power of the number of digits** equals the number itself.

---

### **1️⃣.5️⃣ Category**

Number Logic → Armstrong Numbers

---

### **2️⃣ Outline**

- Read integer **N**
- For each number from 1 to N:

  - Count digits
  - Compute sum of digit powers
  - Check if equal to the number
  - Print if true

---

### **3️⃣ Objective**

To identify and print all Armstrong numbers in a given range.

---

### **4️⃣ Purpose**

To practice:

- nested loops
- digit extraction
- mathematical expressions
- conditional checking

---

### **5️⃣ Theory**

For a number with **L digits**:

If
`(sum of each digit ^ L) == number`
then the number is **Armstrong**.

Example:
153 → 1³ + 5³ + 3³ = 153

---

### **6️⃣ Step-by-Step Explanation**

1. Read **N**
2. Loop number from 1 to N
3. Store current number in temp
4. Count digits using division
5. Again extract digits and compute power sum
6. Compare sum with original number
7. If equal, print the number

---

### **7️⃣ Method**

Use:

- Outer loop for checking each number
- Two inner loops:

  - One for counting digits
  - One for computing Armstrong sum

---

### **8️⃣ Constraints**

- N ≥ 1
- Only loops, arithmetic, and conditions allowed

---

### **9️⃣ Common Mistakes**

- Forgetting to reset sum for each number
- Modifying the original number accidentally
- Incorrect digit count logic

---

### **🔟 Complexity**

- **Time:** O(N × D) where D is digits count
- **Space:** O(1)

---

### **1️⃣1️⃣ Code**

```python
n = int(input())

for num in range(1, n + 1):
    temp = num
    count = 0

    while temp > 0:
        count = count + 1
        temp = temp // 10

    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + (digit ** count)
        temp = temp // 10

    if total == num:
        print(num)
```

---

### **1️⃣2️⃣ Example**

**Input:**

```
200
```

**Output:**

```
1
2
3
4
5
6
7
8
9
153
```

---

### **1️⃣3️⃣ Dry Run**

For `num = 153`

- Digits = 3
- Calculation = 1³ + 5³ + 3³ = 153
- Condition true → printed

---

### **1️⃣4️⃣ Test Cases Table**

| Input | Output                |
| ----- | --------------------- |
| 10    | 1 2 3 4 5 6 7 8 9     |
| 200   | 1 2 3 4 5 6 7 8 9 153 |
| 1     | 1                     |

---

### **1️⃣5️⃣ Notes / Key Takeaways**

- Armstrong checking needs **two passes**
- Always preserve the original number
- Reset all counters per number

---

### **1️⃣6️⃣ Real-Life Application**

Number property validation in cryptography and data science algorithms.

---

### **1️⃣7️⃣ Practice Questions**

1. Print Armstrong numbers from 100 to 1000
2. Count how many Armstrong numbers exist up to N

---

### **1️⃣8️⃣ Result**

All Armstrong numbers from 1 to N are correctly printed.

---

### **1️⃣9️⃣ Conclusion**

This problem builds serious control over digit logic, nested loops, and condition-based validation.

---
