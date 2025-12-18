# ✅ **Sum of All Factors**

---

## **1️⃣ Question**

Given a number **N**, print the **sum of all the factors of N**.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditions → Factors → Summation

---

## **2️⃣ Outline**

- Read N
- Start loop from 1 to N
- Check which numbers divide N
- Add those numbers to sum
- Print the final sum

---

## **3️⃣ Objective**

To calculate the **sum of all factors** of a given number using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- factor identification
- conditional checking
- accumulation using a loop

---

## **5️⃣ Theory**

A **factor** of a number divides it exactly.

Example:
For N = 12
Factors → 1, 2, 3, 4, 6, 12
Sum → 1 + 2 + 3 + 4 + 6 + 12 = **28**

---

## **6️⃣ Step-by-Step Explanation**

1. Read the number N
2. Initialize `total = 0`
3. Loop from 1 to N
4. If N % i == 0, add i to total
5. After loop ends, print total

---

## **7️⃣ Method**

Use:

- for loop
- modulo operator (%)
- integer addition

---

## **8️⃣ Constraints**

- N is a positive integer
- Output should be a single number

---

## **9️⃣ Common Mistakes**

❌ Adding non-factors
❌ Forgetting to initialize sum
❌ Printing inside the loop

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

total = 0

for i in range(1, N + 1):
    if N % i == 0:
        total = total + i

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
12
```

### Output

```
28
```

---

## **1️⃣3️⃣ Dry Run**

N = 6

- i = 1 → factor → sum = 1
- i = 2 → factor → sum = 3
- i = 3 → factor → sum = 6
- i = 6 → factor → sum = 12

Final Output → **12**

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----: | -----: |
|     6 |     12 |
|     8 |     15 |
|    12 |     28 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Every factor contributes to the sum
- `%` is essential for factor checking
- Loop must go till N

---

## **1️⃣6️⃣ Real-Life Application**

- Mathematical analysis
- Divisor-based problems
- Competitive programming basics

---

## **1️⃣7️⃣ Practice Questions**

1. Sum of factors excluding the number
2. Count of factors
3. Check if number is perfect

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of all factors** of the given number.

---

## **1️⃣9️⃣ Conclusion**

A strong foundational problem that improves **loop logic and factor understanding**.

---
