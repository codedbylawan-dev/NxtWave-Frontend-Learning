# ✅ **Print the Score – 3**

---

## **1️⃣ Question**

Given a distance **D** in km, compute the **total score** based on:

- **0–20 km** → 2 points per km
- **21–60 km** → 4 points per km
- **Above 60 km** → 6 points per km
- **Bonus score:** +30 to the final result

---

## **1.5️⃣ Category**

Slab Calculation → Conditional Logic → Arithmetic

---

## **2️⃣ Outline**

- Read D
- If D ≤ 20 → score = D × 2
- Else if D ≤ 60 → score = (20 × 2) + (D − 20) × 4
- Else → score = (20 × 2) + (40 × 4) + (D − 60) × 6
- Add bonus = +30
- Print result

---

## **3️⃣ Objective**

To compute scores from multiple slabs and add a fixed bonus.

---

## **4️⃣ Purpose**

This type of problem is extremely common in billing, rewards, and step-based pricing systems.

---

## **5️⃣ Theory**

### **Case 1: D ≤ 20**

[
\text{score} = D \times 2
]

### **Case 2: 21 ≤ D ≤ 60**

[
\text{score} = 20 \times 2 + (D - 20) \times 4
]

### **Case 3: D > 60**

[
\text{score} = (20 \times 2) + (40 \times 4) + (D - 60) \times 6
]

Then:

[
\text{Total Score} = \text{score} + 30
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read integer D
2. Check if D ≤ 20
3. Else if D ≤ 60
4. Else compute for > 60
5. Add bonus 30
6. Print total

---

## **7️⃣ Method**

Use:

- Conditional checks
- Arithmetic with constants
- Slab breakdown

---

## **8️⃣ Constraints**

- D ≥ 0
- Output is always an integer
- Bonus is always added

---

## **9️⃣ Common Mistakes**

❌ Forgetting to add the bonus
❌ Applying wrong slab multipliers
❌ Using negative values when subtracting slab boundaries

---

## 🔟 Complexity

- Time: **O(1)**
- Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
D = int(input())

if D <= 20:
    score = D * 2
elif D <= 60:
    score = 20 * 2 + (D - 20) * 4
else:
    score = 20 * 2 + 40 * 4 + (D - 60) * 6

total_score = score + 30
print(total_score)
```

---

## **1️⃣2️⃣ Example**

### Input

```
125
```

### Output

```
620
```

---

## **1️⃣3️⃣ Dry Run**

### Example 1: D = 125

- First 20 km → 20 × 2 = 40
- Next 40 km → 40 × 4 = 160
- Remaining 65 km → 65 × 6 = 390
- Total before bonus = 40 + 160 + 390 = 590
- Final = 590 + 30 = **620**

### Example 2: D = 15

- 15 × 2 = 30
- +30 bonus → **60**

---

## **1️⃣4️⃣ Test Cases Table**

| D   | Score |
| --- | ----- |
| 15  | 60    |
| 20  | 70    |
| 50  | 230   |
| 60  | 310   |
| 70  | 370   |
| 125 | 620   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always break distance into slabs
- Each slab has its own multiplier
- Bonus is added _after_ computing slab score

---

## **1️⃣6️⃣ Real-Life Application**

- Telecom data plans
- Billing calculations
- Reward point systems
- Fitness app scoring

---

## **1️⃣7️⃣ Practice Questions**

1. Add a new slab above 200 km with multiplier 10.
2. Convert slabs into a water bill calculation.
3. Add separate bonuses for each slab.

---

## **1️⃣8️⃣ Result**

Program correctly computes score using slab-wise rules + bonus.

---

## **1️⃣9️⃣ Conclusion**

A great real-world style problem showing how to combine conditional logic and arithmetic to handle multi-layer calculations.

---
