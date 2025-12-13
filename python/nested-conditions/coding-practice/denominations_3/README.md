# ✅ **Denominations – 3**

---

## **1️⃣ Question**

Given an amount **A**, calculate the **minimum number of**:

- 500 rupee notes
- 50 rupee notes
- 10 rupee notes
- 1 rupee notes

Then print them **in a single line** in the format:

```
500: x 50: y 10: z 1: w
```

---

## **1.5️⃣ Category**

Arithmetic → Modulus & Division → Currency Breakdown

---

## **2️⃣ Outline**

- Read amount A
- Calculate 500 rupee notes
- Calculate 50 rupee notes
- Calculate 10 rupee notes
- Remaining amount becomes 1 rupee notes
- Print all in one line

---

## **3️⃣ Objective**

To find the smallest number of notes needed to form the given amount.

---

## **4️⃣ Purpose**

Shows practical use of integer division and remainder logic.

---

## **5️⃣ Theory**

Use greedy method:

```
fivehund = A // 500
A = A % 500

fifty = A // 50
A = A % 50

ten = A // 10
A = A % 10

one = A
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read amount A
2. Divide by 500 → number of 500 notes
3. Take remainder
4. Divide remainder by 50 → number of 50 notes
5. Divide by 10 → number of 10 notes
6. Leftover amount → number of 1 notes
7. Print in required format

---

## **7️⃣ Method**

- Use `//` for integer division
- Use `%` for remainder
- Print everything in a single line

---

## **8️⃣ Constraints**

- A is a non-negative integer
- Output must match the sample format exactly

---

## **9️⃣ Common Mistakes**

❌ Using `/` instead of `//`
❌ Printing in multiple lines
❌ Using commas instead of spaces

---

## 🔟 Complexity

Time: **O(1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
A = int(input())

n500 = A // 500
A = A % 500

n50 = A // 50
A = A % 50

n10 = A // 10
A = A % 10

n1 = A

print("500:", n500, "50:", n50, "10:", n10, "1:", n1)
```

---

## **1️⃣2️⃣ Example**

### Input

```
1543
```

### Output

```
500: 3 50: 0 10: 4 1: 3
```

---

## **1️⃣3️⃣ Dry Run**

| Step | Remaining Amount | Notes Calculation | Count |
| ---- | ---------------- | ----------------- | ----- |
| 1    | 1543             | 1543 // 500 = 3   | 3     |
| 2    | 43               | 43 // 50 = 0      | 0     |
| 3    | 43               | 43 // 10 = 4      | 4     |
| 4    | 3                | leftover = 3      | 3     |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | 500 | 50  | 10  | 1   | Output                  |
| ----- | --- | --- | --- | --- | ----------------------- |
| 1543  | 3   | 0   | 4   | 3   | 500: 3 50: 0 10: 4 1: 3 |
| 1259  | 2   | 5   | 0   | 9   | 500: 2 50: 5 10: 0 1: 9 |
| 500   | 1   | 0   | 0   | 0   | 500: 1 50: 0 10: 0 1: 0 |
| 48    | 0   | 0   | 4   | 8   | 500: 0 50: 0 10: 4 1: 8 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Largest notes first → minimum notes
- Always use integer division for denomination problems
- Final output must be **in one line**

---

## **1️⃣6️⃣ Real-Life Application**

- ATM dispensing
- Currency counters
- Cashier software

---

## **1️⃣7️⃣ Practice Questions**

1. Break amount into **2000, 500, 200, 100** notes.
2. Convert amount into **dollars and coins**.
3. Compute minimum coins for **1, 2, 5, 10** denominations.

---

## **1️⃣8️⃣ Result**

The program correctly prints the minimum number of notes for 500, 50, 10, and 1.

---

## **1️⃣9️⃣ Conclusion**

A practical and efficient greedy method solved cleanly using simple arithmetic operations.

---
