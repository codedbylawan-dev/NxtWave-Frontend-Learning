# ✅ **Print the Score – 5**

---

## **1️⃣ Question**

Given a distance **D** in km, calculate the total score based on these rules:

- **0–50 km:** 3 points per km
- **51–100 km:** 5 points per km
- **101–200 km:** 6 points per km
- **Above 200 km:** 10 points per km
- **Bonus:** +100 points added to every final score

---

## **1.5️⃣ Category**

Arithmetic → Tier-Based Calculation → Conditional Logic

---

## **2️⃣ Outline**

- Read D
- If D ≤ 50 → only first slab applies
- If 50 < D ≤ 100 → calculate first 50 + remaining
- If 100 < D ≤ 200 → calculate first 100 + remaining
- If D > 200 → calculate all slabs
- Add bonus
- Print total

---

## **3️⃣ Objective**

To compute a score based on multi-level distance slabs.

---

## **4️⃣ Purpose**

Strengthens tier-based calculation skills using sequential conditions.

---

## **5️⃣ Theory**

Score breakdown:

1. First 50 km → `50 * 3 = 150` max
2. Next 50 km → `50 * 5 = 250` max
3. Next 100 km → `100 * 6 = 600` max
4. Remaining above 200 km → `(D - 200) * 10`

Bonus: **Always +100**

---

## **6️⃣ Step-by-Step Explanation**

1. Read D
2. If D ≤ 50 → score = (D × 3)
3. Else if D ≤ 100 → score = 150 + (D – 50) × 5
4. Else if D ≤ 200 → score = 150 + 250 + (D – 100) × 6
5. Else → score = 150 + 250 + 600 + (D – 200) × 10
6. Add 100 bonus
7. Print total

---

## **7️⃣ Method**

Use:

- subtraction
- multiplication
- if–elif–else

---

## **8️⃣ Constraints**

- D is a non-negative integer
- Bonus always added

---

## **9️⃣ Common Mistakes**

❌ Forgetting to subtract previous slabs
❌ Adding bonus more than once
❌ Wrong order of conditions

---

## 🔟 Complexity

Time: **O(1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
D = int(input())

if D <= 50:
    score = D * 3
elif D <= 100:
    score = 150 + (D - 50) * 5
elif D <= 200:
    score = 150 + 250 + (D - 100) * 6
else:
    score = 150 + 250 + 600 + (D - 200) * 10

score = score + 100

print(score)
```

---

## **1️⃣2️⃣ Example**

### Input

```
120
```

### Output

```
620
```

---

## **1️⃣3️⃣ Dry Run**

For **120**:

- First 50 → 150
- Next 50 → 250
- Next 20 → 20 × 6 = 120
- Subtotal = 520
- Bonus 100 → 620

---

## **1️⃣4️⃣ Test Cases Table**

| D   | Calculation                          | Output |
| --- | ------------------------------------ | ------ |
| 50  | 50×3 + 100                           | 250    |
| 75  | 150 + 25×5 + 100                     | 375    |
| 120 | 150 + 250 + 20×6 + 100               | 620    |
| 200 | 150 + 250 + 100×6 + 100              | 850    |
| 250 | 150 + 250 + 600 + 50×10 + 100 = 1600 | 1600   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Tier-based problems require careful subtraction
- Always add bonus last
- Ordering conditions is important

---

## **1️⃣6️⃣ Real-Life Application**

- Electricity bills
- Mobile data plans
- Delivery distance pricing

---

## **1️⃣7️⃣ Practice Questions**

1. Write slab pricing for water usage.
2. Create a billing system where tax applies after threshold.
3. Compute delivery charges with 3-tier distance rules.

---

## **1️⃣8️⃣ Result**

The program successfully calculates distance-based score with bonus.

---

## **1️⃣9️⃣ Conclusion**

A structured tier-based scoring problem that reinforces conditional slabs and arithmetic logic.

---
