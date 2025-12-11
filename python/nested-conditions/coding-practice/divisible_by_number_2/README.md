# ✅ **Divisible by Number - 2**

---

## **1️⃣ Question**

Read a number **N** and check whether **triple of N** (3 × N) is divisible by **6**.

- If **3N is divisible by 6**, print **3N**
- Otherwise, print **N**

---

## **1.5️⃣ Category**

Arithmetic → Multiplication → Divisibility Check

---

## **2️⃣ Outline**

- Read N
- Compute triple = 3 × N
- Check divisibility of triple by 6
- If divisible → print triple
- Else → print N

---

## **3️⃣ Objective**

To determine whether the triple of a number meets a divisibility condition.

---

## **4️⃣ Purpose**

To build understanding of combining multiplication and divisibility checking.

---

## **5️⃣ Theory**

Triple:

[
3N = 3 \times N
]

Divisibility rule:

[
3N % 6 = 0
]

If true → output 3N
Else → output N

---

## **6️⃣ Step-by-Step Explanation**

1. Read integer N
2. Compute triple = 3 × N
3. Check if triple % 6 == 0
4. If yes → print triple
5. Else → print N

---

## **7️⃣ Method**

- Use arithmetic multiplication
- Use modulus operator for divisibility
- Use simple if–else

---

## **8️⃣ Constraints**

- N is an integer
- Output is a single integer

---

## **9️⃣ Common Mistakes**

❌ Checking divisibility of N instead of 3N
❌ Printing extra text
❌ Using wrong multiplication

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣11️⃣ Code**

```python
N = int(input())

triple = 3 * N

if triple % 6 == 0:
    print(triple)
else:
    print(N)
```

---

## **1️⃣2️⃣ Example**

### Input

```
6
```

### Output

```
18
```

---

## **1️⃣3️⃣ Dry Run**

| N   | 3N  | 3N % 6 | Condition     | Output |
| --- | --- | ------ | ------------- | ------ |
| 6   | 18  | 0      | Divisible     | 18     |
| 9   | 27  | 3      | Not divisible | 9      |

---

## **1️⃣4️⃣ Test Cases Table**

| N   | 3×N | 3×N % 6 | Output |
| --- | --- | ------- | ------ |
| 6   | 18  | 0       | 18     |
| 9   | 27  | 3       | 9      |
| 2   | 6   | 0       | 6      |
| 5   | 15  | 3       | 5      |
| 12  | 36  | 0       | 36     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- You check divisibility of **triple**, not the original number
- `% 6 == 0` ensures number divisible by both **2** and **3**
- Simple arithmetic + condition problems strengthen fundamentals

---

## **1️⃣6️⃣ Real-Life Application**

- Scaling values before applying rules
- Preprocessing data (multiplying before validation)
- Financial adjustments before evaluating eligibility

---

## **1️⃣7️⃣ Practice Questions**

1. Print double of N if double is divisible by 4, else print N.
2. Print square of N if square is divisible by 5.
3. Print N³ if N³ is even, else print N.

---

## **1️⃣8️⃣ Result**

The program correctly outputs triple of N when divisible by 6; otherwise returns N.

---

## **1️⃣9️⃣ Conclusion**

This exercise improves your understanding of combining multiplication and divisibility checks to produce conditional output—an essential programming pattern.

---
