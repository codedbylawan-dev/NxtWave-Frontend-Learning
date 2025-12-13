# ✅ **Denominations – 4**

---

## **1️⃣ Question**

Given an amount **A**, calculate the **minimum number of 100, 50, 20, and 10 rupee notes** needed to make that amount.

---

## **1.5️⃣ Category**

Arithmetic → Floor Division & Remainder → Denomination Breakdown

---

## **2️⃣ Outline**

- Read amount **A**
- Find how many 100 notes → subtract their value
- Find how many 50 notes → subtract
- Find how many 20 notes → subtract
- Find how many 10 notes
- Print all four values in required format

---

## **3️⃣ Objective**

To break down a given amount using the largest possible notes first.

---

## **4️⃣ Purpose**

This builds your skill in:

- using integer division
- using remainders
- performing step-by-step reductions

---

## **5️⃣ Theory**

Denominations work like this:

| Note | How many?         |
| ---- | ----------------- |
| 100  | A // 100          |
| 50   | (remaining) // 50 |
| 20   | (remaining) // 20 |
| 10   | (remaining) // 10 |

---

## **6️⃣ Step-by-Step Explanation**

1. Divide amount by **100** to get count of 100-rupee notes
2. Subtract their total from the amount
3. Divide remaining by **50**
4. Subtract
5. Divide remaining by **20**
6. Subtract
7. Divide remaining by **10**
8. Print all results

---

## **7️⃣ Method**

Use:

- integer division (`//`)
- subtraction
- sequential denomination reduction

---

## **8️⃣ Constraints**

- Amount A ≥ 0
- No fractional notes
- Always print all four notes

---

## **9️⃣ Common Mistakes**

❌ Not updating remaining amount
❌ Using float division instead of integer division
❌ Wrong output format

---

## 🔟 Complexity

Time: **O(1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
A = int(input())

hund = A // 100
remaining = A - hund * 100

fifty = remaining // 50
remaining = remaining - fifty * 50

twenty = remaining // 20
remaining = remaining - twenty * 20

ten = remaining // 10

print("100 Notes: " + str(hund))
print("50 Notes: " + str(fifty))
print("20 Notes: " + str(twenty))
print("10 Notes: " + str(ten))
```

---

## **1️⃣2️⃣ Example**

### Input

```
370
```

### Output

```
100 Notes: 3
50 Notes: 1
20 Notes: 1
10 Notes: 0
```

---

## **1️⃣3️⃣ Dry Run**

Amount = 370

- 370 // 100 = 3 → remaining = 70
- 70 // 50 = 1 → remaining = 20
- 20 // 20 = 1 → remaining = 0
- 0 // 10 = 0

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Expected Output         |
| ----- | ----------------------- |
| 370   | 100:3, 50:1, 20:1, 10:0 |
| 130   | 100:1, 50:0, 20:1, 10:1 |
| 20    | 100:0, 50:0, 20:1, 10:0 |
| 10    | 100:0, 50:0, 20:0, 10:1 |
| 0     | 100:0, 50:0, 20:0, 10:0 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always start with the **largest** denomination
- Update remaining amount step-by-step
- Use `//` for faster, cleaner calculations

---

## **1️⃣6️⃣ Real-Life Application**

- ATM cash dispensing
- Currency exchange counters
- Cash register optimization

---

## **1️⃣7️⃣ Practice Questions**

1. Break amount into 2000, 500, 200, 100
2. Break amount into 50, 5, and 1
3. Add coin denominations (5, 2, 1)

---

## **1️⃣8️⃣ Result**

The program correctly prints the minimum number of notes needed.

---

## **1️⃣9️⃣ Conclusion**

A simple but crucial problem that strengthens logical breakdown and denomination handling.

---
