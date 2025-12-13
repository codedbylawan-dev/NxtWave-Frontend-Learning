# ✅ **Profit or Loss**

---

## **1️⃣ Question**

Given **Cost Price (CP)** and **Selling Price (SP)**, determine whether the transaction resulted in:

- **Profit** (SP > CP)
- **Loss** (SP < CP)
- **No Profit - No Loss** (SP == CP)

---

## **1.5️⃣ Category**

Comparison → Business Logic → Decision Making

---

## **2️⃣ Outline**

- Read CP
- Read SP
- Compare SP with CP
- Print Profit / Loss / No Profit - No Loss

---

## **3️⃣ Objective**

To identify the financial outcome of a sale using simple comparison logic.

---

## **4️⃣ Purpose**

This strengthens real-world decision-making logic based on numeric comparisons.

---

## **5️⃣ Theory**

Three exclusive cases:

[
SP > CP \Rightarrow \text{Profit}
]
[
SP < CP \Rightarrow \text{Loss}
]
[
SP = CP \Rightarrow \text{No Profit - No Loss}
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read CP
2. Read SP
3. If SP > CP → print Profit
4. Else if SP < CP → print Loss
5. Else → values are equal → No Profit - No Loss

---

## **7️⃣ Method**

- Use basic relational operators
- Use `if–elif–else`

---

## **8️⃣ Constraints**

- CP and SP are integers
- Only one output line
- Capitalization must match exactly

---

## **9️⃣ Common Mistakes**

❌ Reversing CP and SP
❌ Writing "No Profit No Loss" (missing hyphens)
❌ Missing equality check

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
CP = int(input())
SP = int(input())

if SP > CP:
    print("Profit")
elif SP < CP:
    print("Loss")
else:
    print("No Profit - No Loss")
```

---

## **1️⃣2️⃣ Example**

### Input

```
143
155
```

### Output

```
Profit
```

---

## **1️⃣3️⃣ Dry Run**

| CP  | SP  | Condition | Output              |
| --- | --- | --------- | ------------------- |
| 143 | 155 | SP > CP   | Profit              |
| 165 | 125 | SP < CP   | Loss                |
| 100 | 100 | SP == CP  | No Profit - No Loss |

---

## **1️⃣4️⃣ Test Cases Table**

| CP  | SP  | Output              |
| --- | --- | ------------------- |
| 143 | 155 | Profit              |
| 165 | 125 | Loss                |
| 10  | 10  | No Profit - No Loss |
| 0   | 50  | Profit              |
| 75  | 75  | No Profit - No Loss |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- SP > CP → gain
- SP < CP → loss
- SP == CP → break-even
- Straightforward usage of comparison operators

---

## **1️⃣6️⃣ Real-Life Application**

- Retail billing
- Stock trading (buy vs sell prices)
- Financial transactions
- Business accounting

---

## **1️⃣7️⃣ Practice Questions**

1. Find profit or loss value (SP−CP).
2. Print percentage profit or loss.
3. Determine if a shop made profit overall after multiple transactions.

---

## **1️⃣8️⃣ Result**

The program successfully prints whether the transaction resulted in a profit, loss, or neither.

---

## **1️⃣9️⃣ Conclusion**

A practical and simple comparison exercise that strengthens foundational programming logic useful in finance and real-world decision-making.

---
