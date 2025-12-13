# ✅ **Course Fee**

---

## **1️⃣ Question**

Read a student's marks **M** and decide the discount:

- If **M ≥ 90** → print **"Discount is 200"**
- If **M ≥ 50 but M < 90** → print **"Discount is 100"**
- If **M < 50** → print **"No Discount"**

---

## **1.5️⃣ Category**

Conditional Statements → Marks Evaluation → Discount Logic

---

## **2️⃣ Outline**

- Read marks M
- Check if ≥ 90
- Else check if ≥ 50
- Else no discount

---

## **3️⃣ Objective**

To classify marks into discount categories using properly ordered conditions.

---

## **4️⃣ Purpose**

This builds decision-making logic and ensures correct condition sequencing.

---

## **5️⃣ Theory**

Three exclusive conditions:

[
M \ge 90 \Rightarrow \text{Discount is 200}
]
[
50 \le M < 90 \Rightarrow \text{Discount is 100}
]
[
M < 50 \Rightarrow \text{No Discount}
]

Order is important: highest marks checked first.

---

## **6️⃣ Step-by-Step Explanation**

1. Read M
2. If M ≥ 90 → highest discount
3. Else if M ≥ 50 → mid discount
4. Else → no discount

---

## **7️⃣ Method**

- Use `if–elif–else`
- Conditions arranged from strongest to weakest

---

## **8️⃣ Constraints**

- M is an integer
- Output must match exactly
- Only one line printed

---

## **9️⃣ Common Mistakes**

❌ Checking 50 first → wrong discount
❌ Writing “No discount” instead of **No Discount**
❌ Forgetting `not greater than or equal to 90` is automatically handled by order

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

| M   | Condition Met | Output          |
| --- | ------------- | --------------- |
| 93  | M ≥ 90        | Discount is 200 |
| 75  | 50 ≤ M < 90   | Discount is 100 |
| 35  | M < 50        | No Discount     |
| 50  | M ≥ 50        | Discount is 100 |
| 90  | M ≥ 90        | Discount is 200 |

---

## **1️⃣4️⃣ Test Cases Table**

| M   | Output          |
| --- | --------------- |
| 93  | Discount is 200 |
| 75  | Discount is 100 |
| 35  | No Discount     |
| 50  | Discount is 100 |
| 90  | Discount is 200 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Correct ordering prevents logical errors
- Only one condition is true for any input
- Simple grading model for evaluations

---

## **1️⃣6️⃣ Real-Life Application**

- Scholarship eligibility
- Fee concession systems
- Employee performance-based incentives

---

## **1️⃣7️⃣ Practice Questions**

1. Assign grades based on marks (A, B, C, D).
2. Print tax bracket based on income.
3. Print health rating based on BMI.

---

## **1️⃣8️⃣ Result**

The program correctly outputs the discount category for the given marks.

---

## **1️⃣9️⃣ Conclusion**

A clear exercise in structured conditional logic—helps understand priority-based decision making in real-world systems.

---
