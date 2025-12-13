# ✅ **Denominations – 2**

---

## **1️⃣ Question**

Given an amount **A**, print the **minimum number of**:

- 100 rupee notes
- 50 rupee notes
- 10 rupee notes
- 1 rupee notes

needed to make the amount.

---

## **1.5️⃣ Category**

Arithmetic → Division & Modulus → Currency Breakdown

---

## **2️⃣ Outline**

- Read amount A
- Compute notes in decreasing order: 100, 50, 10, 1
- Print each count in required format

---

## **3️⃣ Objective**

To break down an amount into the smallest number of notes.

---

## **4️⃣ Purpose**

Teaches how to extract denominations using greedy logic with integer division.

---

## **5️⃣ Theory**

For each denomination:

```
count = A // denomination
A = A % denomination
```

Denominations: 100 → 50 → 10 → 1

---

## **6️⃣ Step-by-Step Explanation**

1. Read amount A
2. Find number of 100-rupee notes
3. Subtract their total value
4. Find number of 50-rupee notes
5. Find number of 10-rupee notes
6. Remainder becomes number of 1-rupee notes
7. Print results

---

## **7️⃣ Method**

- Use `//` for integer division
- Use `%` for remainder
- No loops

---

## **8️⃣ Constraints**

- A is a non-negative integer
- Output must match exactly with format:

  - `100:x`
  - `50:y`
  - `10:z`
  - `1:w`

---

## **9️⃣ Common Mistakes**

❌ Using floating division
❌ Wrong order of notes
❌ Incorrect remainder calculation

---

## 🔟 Complexity

**Time:** O(1)
**Space:** O(1)

---

## **1️⃣1️⃣ Code**

```python
A = int(input())

hund = A // 100
A = A % 100

fifty = A // 50
A = A % 50

ten = A // 10
A = A % 10

one = A

print("100:" + str(hund))
print("50:" + str(fifty))
print("10:" + str(ten))
print("1:" + str(one))
```

---

## **1️⃣2️⃣ Example**

### Input

```
893
```

### Output

```
100:8
50:1
10:4
1:3
```

---

## **1️⃣3️⃣ Dry Run**

| Remaining Amount | Operation      | Notes Count |
| ---------------- | -------------- | ----------- |
| 893              | 893 // 100 = 8 | 8           |
| 93               | 93 // 50 = 1   | 1           |
| 43               | 43 // 10 = 4   | 4           |
| 3                | leftover       | 3           |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | 100 | 50  | 10  | 1   | Output                    |
| ----- | --- | --- | --- | --- | ------------------------- |
| 893   | 8   | 1   | 4   | 3   | 100:8 / 50:1 / 10:4 / 1:3 |
| 250   | 2   | 1   | 0   | 0   | 100:2 / 50:1 / 10:0 / 1:0 |
| 49    | 0   | 0   | 4   | 9   | 100:0 / 50:0 / 10:4 / 1:9 |
| 0     | 0   | 0   | 0   | 0   | 100:0 / 50:0 / 10:0 / 1:0 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Denomination problems are solved using integer division + remainder
- Always start from the highest denomination
- Greedy method ensures minimum notes

---

## **1️⃣6️⃣ Real-Life Application**

- ATMs dispensing cash
- Change calculation in shops
- Currency sorting machines

---

## **1️⃣7️⃣ Practice Questions**

1. Break amount into **500, 200, 50, 10, 1** notes.
2. Break amount into **20, 5, 1** coins.
3. Convert amount into **dollars, quarters, dimes, nickels, pennies**.

---

## **1️⃣8️⃣ Result**

You correctly compute the exact minimum number of notes for the given amount.

---

## **1️⃣9️⃣ Conclusion**

A neat and practical arithmetic problem showing how modulus and integer division power real-world currency operations.

---
