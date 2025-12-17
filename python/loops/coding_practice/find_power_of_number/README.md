# ✅ **Find Power of a Number**

---

## **1️⃣ Question**

Given a number **N** and another number **M**, print the value of **N raised to the power M**
(i.e., **N × N × … × N** → M times).

---

## **1️⃣.5️⃣ Category**

For Loop → Repeated Multiplication → Power Calculation

---

## **2️⃣ Outline**

- Read N
- Read M
- Initialize result as 1
- Multiply N, M times
- Print result

---

## **3️⃣ Objective**

To calculate **power of a number** using **only a for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- repeated multiplication
- using loops instead of operators
- building logic step by step

---

## **5️⃣ Theory**

Power means **multiplying the same number multiple times**.

Examples:

- 2³ = 2 × 2 × 2
- 5² = 5 × 5
- Any number to power 1 is the number itself

We start with `1` and keep multiplying.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N and M
2. Set `result = 1`
3. Run a loop M times
4. Multiply result by N in each iteration
5. Print the final result

---

## **7️⃣ Method**

Use:

- for loop
- multiplication
- accumulator variable

---

## **8️⃣ Constraints**

- N ≥ 1
- M ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Starting result as 0
❌ Using `**` operator
❌ Printing inside the loop

---

## **🔟 Complexity**

Time: **O(M)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())
M = int(input())

result = 1

for i in range(M):
    result = result * N

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
2
3
```

### Output

```
8
```

---

## **1️⃣3️⃣ Dry Run**

N = 3, M = 4

- result = 1
- 1 × 3 = 3
- 3 × 3 = 9
- 9 × 3 = 27
- 27 × 3 = 81

Output → **81**

---

## **1️⃣4️⃣ Test Cases Table**

| N   | M   | Output |
| --- | --- | ------ |
| 2   | 3   | 8      |
| 3   | 1   | 3      |
| 5   | 2   | 25     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Power = repeated multiplication
- Loop count decides exponent
- Start result from 1, not 0

---

## **1️⃣6️⃣ Real-Life Application**

- Mathematical calculations
- Growth formulas
- Algorithm foundations

---

## **1️⃣7️⃣ Practice Questions**

1. Find square of a number
2. Find cube of a number
3. Multiply a number N times

---

## **1️⃣8️⃣ Result**

The program correctly calculates **N power M** without using `**`.

---

## **1️⃣9️⃣ Conclusion**

A foundational problem that strengthens **loop-based multiplication logic**.

---
