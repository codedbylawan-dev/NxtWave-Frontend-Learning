# ✅ **Factors of a Number**

---

## **1️⃣ Question**

Given a number **N**, print **all the factors of N**, each on a new line.

---

## **1️⃣.5️⃣ Category**

For Loop → Divisibility → Factors

---

## **2️⃣ Outline**

- Read N
- Traverse numbers from 1 to N
- Check divisibility
- Print numbers that divide N

---

## **3️⃣ Objective**

To find and print **all factors** of a given number.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- divisibility
- remainder operator `%`
- looping through a range

---

## **5️⃣ Theory**

A **factor** of a number is a number that divides it **exactly**, leaving remainder 0.

Example:
For N = 6
Factors are: 1, 2, 3, 6

Because:

- 6 % 1 = 0
- 6 % 2 = 0
- 6 % 3 = 0
- 6 % 6 = 0

---

## **6️⃣ Step-by-Step Explanation**

1. Read the number N
2. Start a loop from 1 to N
3. Check if N % i == 0
4. If yes, print i
5. Continue till loop ends

---

## **7️⃣ Method**

Use:

- for loop
- modulo operator `%`
- conditional statement

---

## **8️⃣ Constraints**

- N is a positive integer

---

## **9️⃣ Common Mistakes**

❌ Starting loop from 0
❌ Using division instead of modulo
❌ Printing non-divisible numbers

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(1, N + 1):
    if N % i == 0:
        print(i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
6
```

### Output

```
1
2
3
6
```

---

## **1️⃣3️⃣ Dry Run**

N = 6

- i = 1 → 6 % 1 = 0 → print 1
- i = 2 → 6 % 2 = 0 → print 2
- i = 3 → 6 % 3 = 0 → print 3
- i = 4 → remainder ≠ 0 → skip
- i = 5 → remainder ≠ 0 → skip
- i = 6 → 6 % 6 = 0 → print 6

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output  |
| ----: | ------- |
|     6 | 1 2 3 6 |
|     9 | 1 3 9   |
|     1 | 1       |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Factors divide the number exactly
- `%` operator is key
- Loop must start from 1

---

## **1️⃣6️⃣ Real-Life Application**

- Finding divisors
- Mathematics problems
- Number theory basics

---

## **1️⃣7️⃣ Practice Questions**

1. Print factors in one line
2. Count number of factors
3. Find sum of factors

---

## **1️⃣8️⃣ Result**

The program correctly prints **all factors of the given number**.

---

## **1️⃣9️⃣ Conclusion**

A fundamental problem that builds strong understanding of **loops and divisibility**.

---
