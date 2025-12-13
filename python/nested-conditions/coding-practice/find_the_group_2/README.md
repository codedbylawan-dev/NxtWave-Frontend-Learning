# ✅ **Find the Group – 2**

---

## **1️⃣ Question**

Given a number **N (1–30)**, determine which **Group (1–6)** it belongs to.

Numbers are arranged in 6 groups across rows:

| Group 1 | Group 2 | Group 3 | Group 4 | Group 5 | Group 6 |
| ------- | ------- | ------- | ------- | ------- | ------- |
| 1       | 2       | 3       | 4       | 5       | 6       |
| 7       | 8       | 9       | 10      | 11      | 12      |
| 13      | 14      | 15      | 16      | 17      | 18      |
| 19      | 20      | 21      | 22      | 23      | 24      |
| 25      | 26      | 27      | 28      | 29      | 30      |

The pattern shows:

👉 The **remainder when divided by 6** tells the group.

---

## **1.5️⃣ Category**

Arithmetic → Modulus Operator → Group Classification

---

## **2️⃣ Outline**

- Read number N
- Compute `N % 6`
- If remainder is **0**, group = 6
- Otherwise, group = remainder
- Print the group

---

## **3️⃣ Objective**

To find group number using modulus-based patterns.

---

## **4️⃣ Purpose**

Shows how remainder cycles help classify values into fixed groups.

---

## **5️⃣ Theory**

For N divided by 6:

- If remainder is **1** → Group 1
- If remainder is **2** → Group 2
- If remainder is **3** → Group 3
- If remainder is **4** → Group 4
- If remainder is **5** → Group 5
- If remainder is **0** → Group 6

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Compute `rem = N % 6`
3. If rem is 0 → output Group 6
4. Else → output Group rem

---

## **7️⃣ Method**

Use:

- `%` modulus
- Simple if–else

---

## **8️⃣ Constraints**

- N is between 1 and 30
- Output must match format exactly: `Group X`

---

## **9️⃣ Common Mistakes**

❌ Forgetting that remainder 0 means Group 6
❌ Printing extra spaces
❌ Using complicated logic instead of `%`

---

## 🔟 Complexity

- **Time:** O(1)
- **Space:** O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

rem = N % 6

if rem == 0:
    print("Group 6")
else:
    print("Group " + str(rem))
```

---

## **1️⃣2️⃣ Example**

### Input

```
29
```

### Output

```
Group 5
```

---

## **1️⃣3️⃣ Dry Run**

| N   | N % 6 | Group |
| --- | ----- | ----- |
| 3   | 3     | 3     |
| 6   | 0     | 6     |
| 10  | 4     | 4     |
| 18  | 0     | 6     |
| 29  | 5     | 5     |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output  |
| ----- | ------- |
| 1     | Group 1 |
| 6     | Group 6 |
| 7     | Group 1 |
| 12    | Group 6 |
| 15    | Group 3 |
| 29    | Group 5 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Remainders can categorize items into repeating groups
- `% 6` cycles through 1–5 and 0 (→ 6)

---

## **1️⃣6️⃣ Real-Life Application**

- Batch allocation
- Seat numbering
- Grouping students or tasks in cycles of fixed size

---

## **1️⃣7️⃣ Practice Questions**

1. Divide numbers 1–50 into 4 groups using `%`.
2. Assign bank counters 1–3 in a cycle using `% 3`.
3. Print remainder-based group for `% 8`.

---

## **1️⃣8️⃣ Result**

The program correctly prints the group by using remainder logic.

---

## **1️⃣9️⃣ Conclusion**

A clean example of using modulus to distribute values into equally repeating groups.

---
