# ✅ **Electricity Bill**

---

## **1️⃣ Question**

Given the number of electricity units consumed, calculate the total bill using **slab-wise rates** and add a **20% surcharge** on the total.

---

## **1.5️⃣ Category**

Arithmetic → Slab Calculation → Billing System

---

## **2️⃣ Outline**

- Read units
- Apply slab-wise charges
- Compute total amount
- Add 20% surcharge
- Print final bill

---

## **3️⃣ Objective**

To compute a real-world electricity bill using incremental slab logic and percentage surcharge.

---

## **4️⃣ Purpose**

This introduces slab-based billing, cumulative calculations, and percentage operations—common in finance and utilities.

---

## **5️⃣ Theory**

Slab charges:

| Units Range | Rate per Unit |
| ----------- | ------------- |
| 0–50        | 2             |
| 51–150      | 3             |
| 151–250     | 5             |
| 251+        | 8             |

Surcharge:

[
\text{Surcharge} = 0.2 \times \text{Total}
]

Final bill:

[
\text{Bill} = \text{Total} + \text{Surcharge}
]

---

## **6️⃣ Step-by-Step Explanation**

1. Check if units ≤ 50 → charge all at 2/unit
2. If units > 50 →

   - First 50 → 50×2
   - Next 100 → min(units−50, 100)×3

3. If units > 150 →

   - Next 100 → min(units−150, 100)×5

4. If units > 250 →

   - Remaining → (units−250)×8

5. Add all charges
6. Add 20% surcharge
7. Print final amount

---

## **7️⃣ Method**

- Use step-wise subtraction
- Add charges slab by slab
- Use float for final output

---

## **8️⃣ Constraints**

- Units ≥ 0
- Output should be float (e.g., `120.0`)
- Must follow slab order strictly

---

## **9️⃣ Common Mistakes**

❌ Charging all units at a single rate
❌ Forgetting surcharge
❌ Calculating surcharge incorrectly (should be 20% of total, not per slab)
❌ Not using min() logic for partial slabs

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
units = int(input())
bill = 0

if units <= 50:
    bill = units * 2
else:
    bill += 50 * 2
    units -= 50

    if units <= 100:
        bill += units * 3
    else:
        bill += 100 * 3
        units -= 100

        if units <= 100:
            bill += units * 5
        else:
            bill += 100 * 5
            units -= 100

            bill += units * 8

bill = bill + (bill * 0.2)
print(float(bill))
```

---

## **1️⃣2️⃣ Example**

### Input

```
50
```

### Output

```
120.0
```

---

## **1️⃣3️⃣ Dry Run**

### For 200 units

| Slab    | Units Used | Rate | Amount |
| ------- | ---------- | ---- | ------ |
| 0–50    | 50         | 2    | 100    |
| 51–150  | 100        | 3    | 300    |
| 151–250 | 50         | 5    | 250    |
| 251+    | 0          | 8    | 0      |

Total = 650
Surcharge = 130
Final Bill = **780.0**

---

## **1️⃣4️⃣ Test Cases Table**

| Units | Expected Bill                               |
| ----- | ------------------------------------------- |
| 50    | 120.0                                       |
| 200   | 780.0                                       |
| 0     | 0.0                                         |
| 300   | 50×2 + 100×3 + 100×5 + 50×8 = 1150 → 1380.0 |
| 151   | 50×2 + 100×3 + 1×5 = 355 → 426.0            |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Slab calculations must be cumulative
- Each slab applies only to remaining units
- Surcharge is added _after_ total slab calculation

---

## **1️⃣6️⃣ Real-Life Application**

- Electricity bill computation
- Water usage billing
- Telecom data billing
- Tier-based subscription pricing

---

## **1️⃣7️⃣ Practice Questions**

1. Water bill with 3 slabs and no surcharge
2. Mobile data usage bill with overage charges
3. Income tax calculation using slab system

---

## **1️⃣8️⃣ Result**

The program accurately calculates bill amount with correct slab logic and surcharge.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens your understanding of layered conditions, cumulative billing, and percentage operations—essential for real-world financial programming.

---
