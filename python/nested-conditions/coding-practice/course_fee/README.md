# ✅ **Course Fee**

---

## **1️⃣ Question**

Given the marks **M** of a student, print the discount they receive:

- If **M ≥ 90** → print **"Discount is 200"**
- If **50 ≤ M < 90** → print **"Discount is 100"**
- If **M < 50** → print **"No Discount"**

---

## **1.5️⃣ Category**

Condition Checking → Range Classification → Discounts

---

## **2️⃣ Outline**

- Read M
- Check if ≥ 90
- Else check if ≥ 50
- Else print No Discount

---

## **3️⃣ Objective**

To categorize marks into discount brackets using ordered conditions.

---

## **4️⃣ Purpose**

This problem teaches range checking and proper ordering of conditions to ensure correct output.

---

## **5️⃣ Theory**

Three mutually exclusive ranges:

[
M \geq 90 \Rightarrow \text{Discount is 200}
]

[
50 \leq M < 90 \Rightarrow \text{Discount is 100}
]

[
M < 50 \Rightarrow \text{No Discount}
]

Order matters to avoid incorrect matching.

---

## **6️⃣ Step-by-Step Explanation**

1. Read M
2. If M ≥ 90 → print Discount is 200
3. Else if M ≥ 50 → print Discount is 100
4. Else → print No Discount

---

## **7️⃣ Method**

- Use `if`, `elif`, `else`
- Use relational operators: `>=`, `<`

---

## **8️⃣ Constraints**

- Marks are integers
- Output must match exactly
- Print only one line

---

## **9️⃣ Common Mistakes**

❌ Checking M ≥ 50 before M ≥ 90
❌ Printing “No discount” instead of exactly “No Discount”
❌ Missing the condition "not greater than or equal to 90" (handled automatically by ordering)

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
M = int(input())

if M >= 90:
    print("Discount is 200")
elif M >= 50:
    print("Discount is 100")
else:
    print("No Discount")
```

---

## **1️⃣2️⃣ Example**

### Input

```
93
```

### Output

```
Discount is 200
```

---

## **1️⃣3️⃣ Dry Run**

| M   | Condition Met   | Output          |
| --- | --------------- | --------------- |
| 93  | M ≥ 90          | Discount is 200 |
| 75  | 50 ≤ M < 90     | Discount is 100 |
| 35  | M < 50          | No Discount     |
| 50  | M ≥ 50 and < 90 | Discount is 100 |

---

## **1️⃣4️⃣ Test Cases Table**

| M   | Output          |
| --- | --------------- |
| 93  | Discount is 200 |
| 75  | Discount is 100 |
| 35  | No Discount     |
| 90  | Discount is 200 |
| 49  | No Discount     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Condition order impacts correctness
- Using `elif` prevents overlapping conditions
- Clean range checking improves readability

---

## **1️⃣6️⃣ Real-Life Application**

- Course fee discounts
- Scholarship eligibility
- Reward tier systems
- Insurance premium discounts

---

## **1️⃣7️⃣ Practice Questions**

1. Print grade (A, B, C, D) based on marks.
2. Tax calculation based on income range.
3. Categorize age groups (Child, Teen, Adult, Senior).

---

## **1️⃣8️⃣ Result**

The program correctly determines and prints the student’s discount based on their marks.

---

## **1️⃣9️⃣ Conclusion**

A clear and practical exercise in structured conditional logic—important for building robust decision-based programs.

---
