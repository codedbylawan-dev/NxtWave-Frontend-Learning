# ✅ **Print the Score – 2**

---

## **1️⃣ Question**

Given a distance **D** in kilometers, calculate the **total score** using:

- For the **first 50 km** → **3 points per km**
- For **distance above 50 km** → **5 points per km**

---

## **1.5️⃣ Category**

Arithmetic → Conditional Logic → Piecewise Calculation

---

## **2️⃣ Outline**

- Read distance **D**
- If **D ≤ 50** → score = D × 3
- If **D > 50** → score = (50 × 3) + (D − 50) × 5
- Print score

---

## **3️⃣ Objective**

To compute total score based on different slabs of distance.

---

## **4️⃣ Purpose**

This improves understanding of:

- Slab-based calculations
- Difference between base and additional values

---

## **5️⃣ Theory**

Two cases:

### **Case 1: D ≤ 50**

[
\text{score} = D \times 3
]

### **Case 2: D > 50**

[
\text{score} = 50 \times 3 + (D - 50) \times 5
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read D
2. If D is ≤ 50:

   - Compute score as D × 3

3. Else:

   - Compute base score for 50 km → 150
   - Compute remaining distance → D − 50
   - Multiply remaining distance by 5
   - Add both parts

4. Print final score

---

## **7️⃣ Method**

Use:

- Integer arithmetic
- Conditional statements
- Difference calculation

---

## **8️⃣ Constraints**

- D is a non-negative integer
- Output must be a single integer

---

## **9️⃣ Common Mistakes**

❌ Forgetting to multiply only the remaining km by 5
❌ Applying 5-point slab to entire distance
❌ Not handling the D ≤ 50 case properly

---

## 🔟 Complexity

- **Time:** O(1)
- **Space:** O(1)

---

## **1️⃣1️⃣ Code**

```python
D = int(input())

if D <= 50:
    score = D * 3
else:
    score = 50 * 3 + (D - 50) * 5

print(score)
```

---

## **1️⃣2️⃣ Example**

### Input

```
75
```

### Output

```
275
```

---

## **1️⃣3️⃣ Dry Run**

### Example: D = 75

- First 50 km → 50 × 3 = 150
- Remaining 25 km → 25 × 5 = 125
- Total = 150 + 125 = **275**

### Example: D = 30

- Score = 30 × 3 = **90**

---

## **1️⃣4️⃣ Test Cases Table**

| D   | Score |
| --- | ----- |
| 30  | 90    |
| 50  | 150   |
| 51  | 155   |
| 75  | 275   |
| 0   | 0     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Very common pattern used in bills and scoring systems
- Always handle the slab boundary separately
- Use D − 50 only for the extra distance

---

## **1️⃣6️⃣ Real-Life Application**

- Electricity billing
- Tiered pricing systems
- Delivery charges
- Reward points calculation

---

## **1️⃣7️⃣ Practice Questions**

1. Calculate salary with overtime rates.
2. Compute internet bill with different slabs.
3. Movie ticket pricing with peak/non-peak rates.

---

## **1️⃣8️⃣ Result**

The program correctly calculates the score based on the given slab system.

---

## **1️⃣9️⃣ Conclusion**

A perfect introduction to slab-based logic—simple, practical, and widely used.

---
