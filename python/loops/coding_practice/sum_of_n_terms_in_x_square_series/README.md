# ✅ **Sum of N Terms in X Square Series**

---

## **1️⃣ Question**

Given two numbers **X** and **N**, print the **sum of N terms** in the following series:

```
(X)², (XX)², (XXX)², ...
```

---

## **1️⃣.5️⃣ Category**

For Loop → Series → Square → Summation

---

## **2️⃣ Outline**

- Read X
- Read N
- Initialize empty string
- Initialize sum as 0
- Loop from 1 to N
- Build the number using X
- Convert to integer
- Square the number
- Add to sum
- Print sum

---

## **3️⃣ Objective**

To calculate the **sum of squares** of numbers formed by repeating **X**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- series building using strings
- square calculation
- accumulation using loops

---

## **5️⃣ Theory**

Each term is formed by:

1. Repeating **X**
2. Converting it to a number
3. Squaring it

Example for **X = 4, N = 3**:

```
4²   = 16
44²  = 1936
444² = 197136
Sum  = 199088
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read X and N
2. Store X as a string
3. Initialize `term = ""`
4. Initialize `total = 0`
5. Loop N times
6. Append X to `term`
7. Convert `term` to integer
8. Square the value
9. Add to `total`
10. Print `total`

---

## **7️⃣ Method**

Use:

- for loop
- string concatenation
- integer conversion
- multiplication

---

## **8️⃣ Constraints**

- N ≥ 1
- X is a single digit

---

## **9️⃣ Common Mistakes**

❌ Using nested loops unnecessarily
❌ Forgetting to square the number
❌ Resetting term inside loop

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
    number = int(term)
    total = total + (number * number)

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
3
```

### Output

```
199088
```

---

## **1️⃣3️⃣ Dry Run**

X = "4", N = 3

- i = 0 → term = "4" → 4² = 16 → total = 16
- i = 1 → term = "44" → 44² = 1936 → total = 1952
- i = 2 → term = "444" → 444² = 197136 → total = 199088

---

## **1️⃣4️⃣ Test Cases Table**

| X   | N   | Output   |
| --- | --- | -------- |
| 4   | 3   | 199088   |
| 7   | 4   | 61091436 |
| 2   | 2   | 484      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Series is built step-by-step
- Square using `number * number`
- No nested loops required

---

## **1️⃣6️⃣ Real-Life Application**

- Pattern-based numeric series
- Competitive programming
- Mathematical modeling

---

## **1️⃣7️⃣ Practice Questions**

1. Sum of cubes of X series
2. Print X square series
3. Stop when sum exceeds 1,00,000

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of N terms in X square series**.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens **series logic, squaring, and accumulation** using a clean single loop.

---
