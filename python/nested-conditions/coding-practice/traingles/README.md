# ✅ **Triangles**

---

## **1️⃣ Question**

Given three sides **A, B, C**, determine whether the triangle is:

- **Equilateral** → all sides equal
- **Isosceles** → any two sides equal
- **Scalene** → all sides different

---

## **1.5️⃣ Category**

Conditional Statements → Comparison Logic → Triangle Classification

---

## **2️⃣ Outline**

- Read A, B, C
- Check if all sides are equal
- Else check if any two sides are equal
- Otherwise → Scalene

---

## **3️⃣ Objective**

To classify a triangle type based purely on equality of its sides.

---

## **4️⃣ Purpose**

Helps understand multi-branch comparisons using if–elif–else.

---

## **5️⃣ Theory**

Triangle Types:

1. **Equilateral** → A == B == C
2. **Isosceles** → exactly 2 sides equal
3. **Scalene** → all three sides different

---

## **6️⃣ Step-by-Step Explanation**

1. Read side A
2. Read side B
3. Read side C
4. If all equal → Equilateral
5. Else if any two equal → Isosceles
6. Otherwise → Scalene

---

## **7️⃣ Method**

Use chained equality checks.

---

## **8️⃣ Constraints**

- Inputs are positive integers
- Output format must match exactly

---

## **9️⃣ Common Mistakes**

❌ Checking Isosceles before Equilateral
❌ Misusing "and/or" conditions
❌ Forgetting to check all three pairs

---

## 🔟 Complexity

Time: O(1)
Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
A = int(input())
B = int(input())
C = int(input())

if A == B and B == C:
    print("Equilateral")
elif A == B or B == C or A == C:
    print("Isosceles")
else:
    print("Scalene")
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
4
4
```

### Output

```
Equilateral
```

---

## **1️⃣3️⃣ Dry Run**

A = 3, B = 2, C = 3

- A == B? ❌
- B == C? ❌
- A == C? ✔
  → Isosceles

---

## **1️⃣4️⃣ Test Cases Table**

| A   | B   | C   | Output      |
| --- | --- | --- | ----------- |
| 4   | 4   | 4   | Equilateral |
| 5   | 5   | 3   | Isosceles   |
| 2   | 3   | 4   | Scalene     |
| 7   | 7   | 7   | Equilateral |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always check **all equal** first
- Isosceles requires **any two equal**
- Scalene means **no equality among sides**

---

## **1️⃣6️⃣ Real-Life Application**

- Classifying objects by measurement
- Geometry-based validation in graphics
- Structural modelling in engineering tools

---

## **1️⃣7️⃣ Practice Questions**

1. Check if three angles form a valid triangle.
2. Classify triangle based on angles (Acute/Right/Obtuse).
3. Check if sides form a Pythagorean triplet.

---

## **1️⃣8️⃣ Result**

The program correctly determines triangle type.

---

## **1️⃣9️⃣ Conclusion**

A clean comparison-based problem reinforcing multi-condition decision making.

---
