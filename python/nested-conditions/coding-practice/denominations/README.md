# ✅ **Denominations**

---

## **1️⃣ Question**

Given an amount **A**, print the **minimum number of 5-rupee notes** and **1-rupee notes** needed to make that amount.

---

## **1.5️⃣ Category**

Arithmetic → Division & Modulus → Money Denominations

---

## **2️⃣ Outline**

- Read amount **A**
- Find how many 5-rupee notes fit (`A // 5`)
- Find remaining amount (`A % 5`)
- Remaining amount becomes number of 1-rupee notes
- Print results in required format

---

## **3️⃣ Objective**

To compute optimal currency denominations using division and remainder.

---

## **4️⃣ Purpose**

Teaches greedy breakdown using simple arithmetic.

---

## **5️⃣ Theory**

- Maximum 5-rupee notes should be used first
- Remainder after dividing by 5 = number of 1-rupee notes

Formulas:

```
five_notes = A // 5
one_notes = A % 5
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read integer A
2. Divide A by 5 using integer division → number of ₹5 notes
3. Find remainder after dividing by 5 → number of ₹1 notes
4. Print results in format:

   - `5:<count>`
   - `1:<count>`

---

## **7️⃣ Method**

- Use `//` for integer division
- Use `%` for remainder
- No loops
- Simple arithmetic

---

## **8️⃣ Constraints**

- A is a non-negative integer
- Output format must match exactly

---

## **9️⃣ Common Mistakes**

❌ Using floating division `/` instead of `//`
❌ Printing extra text
❌ Miscalculating remainder

---

## 🔟 Complexity

**Time:** O(1)
**Space:** O(1)

---

## **1️⃣1️⃣ Code**

```python
A = int(input())

five_notes = A // 5
one_notes = A % 5

print("5:" + str(five_notes))
print("1:" + str(one_notes))
```

---

## **1️⃣2️⃣ Example**

### Input

```
16
```

### Output

```
5:3
1:1
```

---

## **1️⃣3️⃣ Dry Run**

| A   | A // 5 | A % 5 | 5-notes | 1-notes |
| --- | ------ | ----- | ------- | ------- |
| 16  | 3      | 1     | 3       | 1       |
| 102 | 20     | 2     | 20      | 2       |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | 5-notes | 1-notes | Output     |
| ----- | ------- | ------- | ---------- |
| 16    | 3       | 1       | 5:3 / 1:1  |
| 102   | 20      | 2       | 5:20 / 1:2 |
| 0     | 0       | 0       | 5:0 / 1:0  |
| 4     | 0       | 4       | 5:0 / 1:4  |
| 5     | 1       | 0       | 5:1 / 1:0  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Use integer division for currency denomination
- Remainder gives leftover amount
- Simple and efficient method

---

## **1️⃣6️⃣ Real-Life Application**

- ATM cash dispensing
- Currency exchange counters
- Optimizing coin and note usage

---

## **1️⃣7️⃣ Practice Questions**

1. Break amount into **₹10 and ₹1** notes.
2. Break amount into **₹100, ₹10, ₹1** notes.
3. Break coins into **quarters, dimes, nickels, pennies** (U.S. style).

---

## **1️⃣8️⃣ Result**

The program correctly prints the minimum number of ₹5 and ₹1 notes.

---

## **1️⃣9️⃣ Conclusion**

A simple but essential arithmetic problem that teaches optimal breakdown of money using division and modulus.

---
