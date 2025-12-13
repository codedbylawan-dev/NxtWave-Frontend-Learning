# ✅ **Denominations – 5**

---

## **1️⃣ Question**

Given an amount **A**, find the **minimum number of notes** needed from these denominations:

**2000, 500, 200, 50, 20, 5, 2, 1**

Print them in the exact format:

```
2000:x 500:y 200:z 50:a 20:b 5:c 2:d 1:e
```

---

## **1.5️⃣ Category**

Arithmetic Breakdown → Greedy Note Calculation

---

## **2️⃣ Outline**

- Divide amount by 2000
- Subtract used amount
- Repeat for 500
- Repeat for 200
- Repeat for 50
- Repeat for 20
- Repeat for 5
- Repeat for 2
- Remaining is 1-rupee notes

---

## **3️⃣ Objective**

To split the amount into the smallest number of currency notes.

---

## **4️⃣ Purpose**

This strengthens step-by-step arithmetic decomposition.

---

## **5️⃣ Theory**

Use:

```
number_of_notes = A // denomination
remaining = A - (number_of_notes * denomination)
```

Repeat for each denomination.

---

## **6️⃣ Step-by-Step Explanation**

If A = 2257:

1. 2257 // 2000 = 1 → remaining = 257
2. 257 // 500 = 0 → remaining = 257
3. 257 // 200 = 1 → remaining = 57
4. 57 // 50 = 1 → remaining = 7
5. 7 // 20 = 0 → remaining = 7
6. 7 // 5 = 1 → remaining = 2
7. 2 // 2 = 1 → remaining = 0
8. 0 // 1 = 0

---

## **7️⃣ Method**

Use integer division and subtraction only.

---

## **8️⃣ Constraints**

- A ≥ 0
- Output format strictly followed

---

## **9️⃣ Common Mistakes**

❌ Forgetting to update remaining
❌ Using float division instead of integer division
❌ Printing in wrong order

---

## 🔟 Complexity

Time → **O(1)**
Space → **O(1)**

---

## **1️⃣1️⃣ Code**

```python
A = int(input())

n2000 = A // 2000
A = A - n2000 * 2000

n500 = A // 500
A = A - n500 * 500

n200 = A // 200
A = A - n200 * 200

n50 = A // 50
A = A - n50 * 50

n20 = A // 20
A = A - n20 * 20

n5 = A // 5
A = A - n5 * 5

n2 = A // 2
A = A - n2 * 2

n1 = A // 1

print("2000:" + str(n2000),
      "500:" + str(n500),
      "200:" + str(n200),
      "50:" + str(n50),
      "20:" + str(n20),
      "5:" + str(n5),
      "2:" + str(n2),
      "1:" + str(n1))
```

---

## **1️⃣2️⃣ Example**

### Input

```
2257
```

### Output

```
2000:1 500:0 200:1 50:1 20:0 5:1 2:1 1:0
```

---

## **1️⃣3️⃣ Dry Run**

For A = 2345:

```
2000 → 1 (remaining 345)
500 → 0 (remaining 345)
200 → 1 (remaining 145)
50  → 2 (remaining 45)
20  → 2 (remaining 5)
5   → 1 (remaining 0)
2   → 0
1   → 0
```

Output:

```
2000:1 500:0 200:1 50:2 20:2 5:1 2:0 1:0
```

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output                                     |
| ----- | ------------------------------------------ |
| 0     | `2000:0 500:0 200:0 50:0 20:0 5:0 2:0 1:0` |
| 5     | `2000:0 500:0 200:0 50:0 20:0 5:1 2:0 1:0` |
| 57    | `2000:0 500:0 200:0 50:1 20:0 5:1 2:1 1:0` |
| 2257  | correct output                             |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always divide from **largest note first**
- Integer division ensures minimum number of notes
- Update amount after each step

---

## **1️⃣6️⃣ Real-Life Application**

- ATM cash dispensing logic
- Cash counter note counting
- Automated cash breakdown systems

---

## **1️⃣7️⃣ Practice Questions**

1. Break amount using notes: 1000, 100, 10, 1
2. Break amount using coins: 25, 10, 5, 1
3. Compute total notes needed for a list of amounts

---

## **1️⃣8️⃣ Result**

You correctly compute note denominations using step-based subtraction.

---

## **1️⃣9️⃣ Conclusion**

A good exercise in greedy arithmetic processing and currency breakdown.

---
