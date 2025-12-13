# ✅ **Name of the Polygon**

---

## **1️⃣ Question**

Given an integer **N** representing the number of sides, print the **name of the polygon**:

- If **N < 3** → print **"Not Polygon"**
- If **N == 3** → print **"Triangle"**
- If **N == 4** → print **"Quadrilateral"**
- If **N == 5** → print **"Pentagon"**
- If **N > 5** → print **"Big Polygon"**

---

## **1.5️⃣ Category**

Conditional Statements → Geometry → Classification

---

## **2️⃣ Outline**

- Read N
- Check polygon rules in correct order
- Print appropriate name

---

## **3️⃣ Objective**

To classify a shape based on its number of sides.

---

## **4️⃣ Purpose**

This problem reinforces structured conditional branching and classification logic.

---

## **5️⃣ Theory**

A polygon must have **at least 3 sides**.
Names based on sides:

| Sides | Name          |
| ----- | ------------- |
| < 3   | Not Polygon   |
| 3     | Triangle      |
| 4     | Quadrilateral |
| 5     | Pentagon      |
| > 5   | Big Polygon   |

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. If N < 3 → print Not Polygon
3. Else if N == 3 → print Triangle
4. Else if N == 4 → print Quadrilateral
5. Else if N == 5 → print Pentagon
6. Else → print Big Polygon

---

## **7️⃣ Method**

- Use if–elif–else
- Compare using `<`, `==`, `>`

---

## **8️⃣ Constraints**

- N is an integer
- Output must match exactly
- Only one line is printed

---

## **9️⃣ Common Mistakes**

❌ Forgetting N < 3 case
❌ Using else too early
❌ Incorrect spellings of shape names
❌ Not respecting order of conditions

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

if N < 3:
    print("Not Polygon")
elif N == 3:
    print("Triangle")
elif N == 4:
    print("Quadrilateral")
elif N == 5:
    print("Pentagon")
else:
    print("Big Polygon")
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
Quadrilateral
```

---

## **1️⃣3️⃣ Dry Run**

| N   | Condition Met | Output        |
| --- | ------------- | ------------- |
| 4   | N == 4        | Quadrilateral |
| 2   | N < 3         | Not Polygon   |
| 3   | N == 3        | Triangle      |
| 7   | N > 5         | Big Polygon   |

---

## **1️⃣4️⃣ Test Cases Table**

| N   | Output        |
| --- | ------------- |
| 4   | Quadrilateral |
| 2   | Not Polygon   |
| 3   | Triangle      |
| 5   | Pentagon      |
| 10  | Big Polygon   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Polygon must have ≥ 3 sides
- Conditions must be checked in correct order
- Very common structure in geometry-based problems

---

## **1️⃣6️⃣ Real-Life Application**

- Computer graphics and shape classification
- Geometry problem-solving
- Input validation for polygon-based algorithms

---

## **1️⃣7️⃣ Practice Questions**

1. Print type of triangle based on angles.
2. Classify quadrilaterals (square, rectangle, etc.).
3. Print shape name based on the number of vertices.

---

## **1️⃣8️⃣ Result**

The program successfully prints the correct polygon name based on number of sides.

---

## **1️⃣9️⃣ Conclusion**

A clear and structured exercise in conditional classification — essential for logical decision-making in programming.

---

Say **Next** for the next problem.
