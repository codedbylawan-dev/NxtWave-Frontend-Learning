# ✅ **Sum of N Terms in X Series**

---

## **1️⃣ Question**

Given two numbers **X** and **N**, print the **sum of the first N terms** in the following series:

```
X
XX
XXX
XXXX
...
```

---

## **1️⃣.5️⃣ Category**

For Loop → Series → Sum Calculation

---

## **2️⃣ Outline**

- Read X
- Read N
- Initialize empty string
- Initialize sum as 0
- Loop N times
- Build the series using X
- Convert each term to integer
- Add to sum
- Print sum

---

## **3️⃣ Objective**

To calculate the **sum of a digit-based series** formed using a given number X.

---

## **4️⃣ Purpose**

This problem helps you understand:

- dynamic series generation
- string repetition logic
- accumulation using loops

---

## **5️⃣ Theory**

Each term is formed by **adding one more X** to the previous term.

Example for X = 7, N = 4:

```
Terms: 7, 77, 777, 7777
Sum = 7 + 77 + 777 + 7777 = 8638
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read X and N
2. Convert X to string
3. Initialize `term` as empty string
4. Initialize `total = 0`
5. Loop N times
6. In each iteration:

   - append X to `term`
   - convert `term` to integer
   - add it to `total`

7. Print `total`

---

## **7️⃣ Method**

Use:

- for loop
- string concatenation
- `int()`
- addition

---

## **8️⃣ Constraints**

- N ≥ 1
- X is a single digit number

---

## **9️⃣ Common Mistakes**

❌ Resetting the term inside loop
❌ Treating X as integer while concatenating
❌ Printing result inside loop

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
X = input()
N = int(input())

term = ""
total = 0

for i in range(N):
    term = term + X
    total = total + int(term)

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
7
4
```

### Output

```
8638
```

---

## **1️⃣3️⃣ Dry Run**

X = "7", N = 4

- i = 0 → term = "7" → total = 7
- i = 1 → term = "77" → total = 84
- i = 2 → term = "777" → total = 861
- i = 3 → term = "7777" → total = 8638

---

## **1️⃣4️⃣ Test Cases Table**

| X   | N   | Output |
| --- | --- | ------ |
| 7   | 4   | 8638   |
| 6   | 2   | 72     |
| 3   | 3   | 369    |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always treat X as string for concatenation
- Convert to integer only while adding
- Series logic builds step by step

---

## **1️⃣6️⃣ Real-Life Application**

- Pattern-based calculations
- Series logic in coding tests
- Competitive programming

---

## **1️⃣7️⃣ Practice Questions**

1. Print the series instead of sum
2. Sum of X series till value exceeds 1000
3. Count digits in final sum

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of N terms in X series**.

---

## **1️⃣9️⃣ Conclusion**

This problem perfectly combines **loops, strings, and arithmetic**, strengthening your fundamentals.

---
