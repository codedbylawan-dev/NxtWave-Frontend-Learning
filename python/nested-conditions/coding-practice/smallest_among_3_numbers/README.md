# ✅ **Smallest Among 3 Numbers**

---

## **1️⃣ Question**

Given three integers **A**, **B**, and **C**, print the **smallest value** among them.

---

## **1.5️⃣ Category**

Comparison → Minimum of Three Numbers → Basic Decision Making

---

## **2️⃣ Outline**

- Read A
- Read B
- Read C
- Compare the three values
- Print the smallest

---

## **3️⃣ Objective**

To determine the minimum of three numbers using comparison logic.

---

## **4️⃣ Purpose**

This strengthens understanding of logical comparisons and evaluating multiple conditions.

---

## **5️⃣ Theory**

To find the smallest:

[
\text{Smallest} = \min(A, B, C)
]

But manually using conditions:

- Check if A is smallest
- Else check if B is smallest
- Else C is smallest

---

## **6️⃣ Step-by-Step Explanation**

1. Read A, B, C
2. Assume A is smallest
3. Compare B with current smallest → update if needed
4. Compare C with current smallest → update if needed
5. Print the smallest value

---

## **7️⃣ Method**

Use comparison operators with if–elif–else.

---

## **8️⃣ Constraints**

- A, B, C are integers
- All three may be equal
- Only one output line

---

## **9️⃣ Common Mistakes**

❌ Using incorrect comparison chains
❌ Forgetting equal-value cases
❌ Printing multiple numbers instead of only smallest

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
A = int(input())
B = int(input())
C = int(input())

if A <= B and A <= C:
    print(A)
elif B <= A and B <= C:
    print(B)
else:
    print(C)
```

---

## **1️⃣2️⃣ Example**

### Input

```
6
5
4
```

### Output

```
4
```

---

## **1️⃣3️⃣ Dry Run**

| A      | B      | C      | Smallest |
| ------ | ------ | ------ | -------- |
| 6      | 5      | 4      | 4        |
| -10000 | -10000 | -10000 | -10000   |
| 3      | 8      | 8      | 3        |
| 9      | 2      | 7      | 2        |

---

## **1️⃣4️⃣ Test Cases Table**

| A      | B      | C      | Output |
| ------ | ------ | ------ | ------ |
| 6      | 5      | 4      | 4      |
| -10000 | -10000 | -10000 | -10000 |
| 7      | -1     | 3      | -1     |
| 0      | 9      | 2      | 0      |
| 5      | 5      | 2      | 2      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always include `<=` to handle equal values
- Think logically: smallest is the one not greater than others
- Clean and simple condition chain works best

---

## **1️⃣6️⃣ Real-Life Application**

- Finding smallest cost, smallest score
- Minimum temperature readings
- Algorithm comparisons (picking smallest weight, smallest distance)

---

## **1️⃣7️⃣ Practice Questions**

1. Print the largest among three numbers.
2. Print the median (middle) of three numbers.
3. Print smallest among four numbers.

---

## **1️⃣8️⃣ Result**

The program accurately identifies and prints the smallest of the three numbers.

---

## **1️⃣9️⃣ Conclusion**

A foundational comparison problem that builds confidence in multi-condition logic and selection.

---
