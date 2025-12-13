# ✅ **Print the Score – 4**

---

## **1️⃣ Question**

Given distance **D**, calculate total score using slabs:

- 0–40 km → 2 points per km
- 41–60 km → 4 points per km
- 61–120 km → 6 points per km
- Above 120 km → 8 points per km
- Add a **bonus of 50**

---

## **1.5️⃣ Category**

Conditional Statements → Slab-Based Calculation

---

## **2️⃣ Outline**

- Read D
- Check which slab D falls in
- Calculate score accordingly
- Add 50 bonus
- Print total

---

## **3️⃣ Objective**

Compute the final score using step-by-step slab rates.

---

## **4️⃣ Purpose**

Slab-based billing or scoring is used in electricity bills, fuel charges, reward systems, etc.

---

## **5️⃣ Theory**

Break D into slabs:

| Slab Range | Rate per km |
| ---------- | ----------- |
| 0–40       | 2           |
| 41–60      | 4           |
| 61–120     | 6           |
| 121+       | 8           |

Bonus = +50 added at the end.

---

## **6️⃣ Step-by-Step Explanation**

1. If D ≤ 40 → D × 2
2. Else if D ≤ 60 →
   (40 × 2) + (D − 40) × 4
3. Else if D ≤ 120 →
   (40 × 2) + (20 × 4) + (D − 60) × 6
4. Else →
   (40 × 2) + (20 × 4) + (60 × 6) + (D − 120) × 8
5. Add bonus 50
6. Print final score

---

## **7️⃣ Method**

Use simple arithmetic and chained conditions.

---

## **8️⃣ Constraints**

- D ≥ 0
- Score is always integer
- Bonus always added

---

## **9️⃣ Common Mistakes**

❌ Forgetting to subtract previous slab lengths
❌ Forgetting bonus
❌ Miscalculating ranges

---

## 🔟 Complexity

- Time: **O(1)**
- Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
D = int(input())

if D <= 40:
    score = D * 2
elif D <= 60:
    score = 40 * 2 + (D - 40) * 4
elif D <= 120:
    score = 40 * 2 + 20 * 4 + (D - 60) * 6
else:
    score = 40 * 2 + 20 * 4 + 60 * 6 + (D - 120) * 8

total = score + 50
print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
70
```

### Output

```
270
```

---

## **1️⃣3️⃣ Dry Run**

### D = 70

- First 40 → 40 × 2 = 80
- Next 20 → 20 × 4 = 80
- Remaining 10 → 10 × 6 = 60
- Subtotal = 220
- Bonus = 50
- Final = **270**

---

## **1️⃣4️⃣ Test Cases Table**

| D   | Output |
| --- | ------ |
| 4   | 58     |
| 40  | 130    |
| 60  | 210    |
| 70  | 270    |
| 120 | 430    |
| 135 | 690    |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Break the distance into slabs carefully
- Each slab has a fixed rate
- Always add bonus at end

---

## **1️⃣6️⃣ Real-Life Application**

- Transport fare calculation
- Electricity & water billing
- Fitness distance reward systems

---

## **1️⃣7️⃣ Practice Questions**

1. Add a new slab above 200 km → rate 12
2. Modify the bonus based on D
3. Create a reverse scoring system (higher km = lower score)

---

## **1️⃣8️⃣ Result**

The program correctly computes total score using slab logic + bonus.

---

## **1️⃣9️⃣ Conclusion**

A solid problem to master slab-based calculations with clean conditional logic.

---
