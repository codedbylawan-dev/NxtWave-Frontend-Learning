# ✅ **Print the Score**

---

## **1️⃣ Question**

Given a distance **D** (in km), calculate a score using the following rules:

- If **D ≤ 10**, the score is **D**
- If **D > 10**, the score is:
  [
  10 + (D - 10) \times 3
  ]

Print the final score.

---

## **1.5️⃣ Category**

Arithmetic → Conditions → Simple Formula Application

---

## **2️⃣ Outline**

- Read D
- If D ≤ 10 → score = D
- Else → score = 10 + (D - 10) × 3
- Print score

---

## **3️⃣ Objective**

To compute a numeric score based on a conditional rule using arithmetic calculations.

---

## **4️⃣ Purpose**

To practice conditional branching and formula-based output generation.

---

## **5️⃣ Theory**

Two scoring formulas:

### Case 1:

If:
[
D \le 10
]
[
\text{score} = D
]

### Case 2:

If:
[
D > 10
]
[
\text{score} = 10 + (D - 10) \times 3
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read integer D
2. Check if D ≤ 10
3. If yes → score = D
4. Otherwise → compute extra distance = D - 10
5. Multiply extra distance by 3
6. Add 10 to get final score
7. Print score

---

## **7️⃣ Method**

- Use if–else
- Use arithmetic operators
- Output a single integer

---

## **8️⃣ Constraints**

- D is a non-negative integer
- Output must match required value exactly

---

## **9️⃣ Common Mistakes**

❌ Forgetting parentheses in formula
❌ Using `<` instead of `<=`
❌ Doing 10 × (D - 10) instead of adding 10

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
D = int(input())

if D <= 10:
    score = D
else:
    score = 10 + (D - 10) * 3

print(score)
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
```

### Output

```
3
```

---

## **1️⃣3️⃣ Dry Run**

| Step | D   | Condition | Calculation             | Score |
| ---- | --- | --------- | ----------------------- | ----- |
| 1    | 3   | D ≤ 10    | score = D               | 3     |
| 2    | 25  | D > 10    | 10 + (25 - 10) × 3 = 55 | 55    |

---

## **1️⃣4️⃣ Test Cases Table**

| D   | Condition | Score Formula       | Output |
| --- | --------- | ------------------- | ------ |
| 3   | ≤ 10      | 3                   | 3      |
| 10  | ≤ 10      | 10                  | 10     |
| 11  | > 10      | 10 + (11–10)×3 = 13 | 13     |
| 25  | > 10      | 10 + (25–10)×3 = 55 | 55     |
| 40  | > 10      | 10 + 30×3 = 100     | 100    |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always split logic into ≤ and > cases
- Parentheses matter in arithmetic expressions
- This pattern is common in billing and scoring systems

---

## **1️⃣6️⃣ Real-Life Application**

- Taxi fare calculation
- Delivery charge rules
- Bonus scoring beyond a threshold
- Step-based pricing models

---

## **1️⃣7️⃣ Practice Questions**

1. If distance ≤ 5 score = D × 2, else score = 10 + (D - 5).
2. If number ≤ 50 print number, else print number × 2.
3. If hours > 8 compute overtime pay at 1.5× rate.

---

## **1️⃣8️⃣ Result**

The program computes the score correctly based on whether D is within or beyond the first 10 km.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens understanding of branching logic and basic arithmetic expressions—core skills for many scoring, billing, and rule-based calculations.

---
