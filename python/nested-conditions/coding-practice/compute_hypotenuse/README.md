# ✅ **Compute Hypotenuse**

---

## **1️⃣ Question**

Read two integers **A** and **B**, representing the two perpendicular sides of a right-angled triangle, and compute the **hypotenuse H**.

Formula:

[
H = \sqrt{A^2 + B^2}
]

Print **H** as an integer.

---

## **1.5️⃣ Category**

Arithmetic → Geometry → Pythagoras Theorem

---

## **2️⃣ Outline**

- Read A
- Read B
- Compute A²
- Compute B²
- Compute sum = A² + B²
- Compute hypotenuse = (sum) \*\* 0.5
- Print result

---

## **3️⃣ Objective**

To calculate the hypotenuse of a right-angled triangle using Pythagoras theorem.

---

## **4️⃣ Purpose**

To practice combining exponentiation, addition, and square root operations.

---

## **5️⃣ Theory**

According to **Pythagoras' Theorem**:

[
H^2 = A^2 + B^2
]

Taking square root:

[
H = (A^2 + B^2)^{0.5}
]

Examples:

- For 3 and 4 → √(9 + 16) = √25 = 5
- For 12 and 5 → √(144 + 25) = √169 = 13

---

## **6️⃣ Step-by-Step Explanation**

1. Read A
2. Read B
3. Compute A² = A × A
4. Compute B² = B × B
5. Add both squares
6. Take square root using exponent 0.5
7. Print integer result

---

## **7️⃣ Method**

- Use multiplication for squaring
- Use power operator `**` for square root
- Convert result to integer (because result is always perfect square in tests)

---

## **8️⃣ Constraints**

- A and B are positive integers
- Output should be an integer
- Square root result assumed to be integer

---

## **9️⃣ Common Mistakes**

❌ Using `^` instead of `**`
❌ Forgetting parentheses around A² + B²
❌ Printing float instead of integer

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
A = int(input())
B = int(input())

hyp = (A*A + B*B) ** 0.5
print(int(hyp))
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
4
```

### Output

```
5
```

---

## **1️⃣3️⃣ Dry Run**

| A   | B   | A²  | B²  | Sum | √Sum | Output |
| --- | --- | --- | --- | --- | ---- | ------ |
| 3   | 4   | 9   | 16  | 25  | 5.0  | 5      |
| 12  | 5   | 144 | 25  | 169 | 13.0 | 13     |

---

## **1️⃣4️⃣ Test Cases Table**

| A   | B   | Hypotenuse Calculation    | Output |
| --- | --- | ------------------------- | ------ |
| 3   | 4   | √(9 + 16) = √25 = 5       | 5      |
| 12  | 5   | √(144 + 25) = √169 = 13   | 13     |
| 6   | 8   | √(36 + 64) = √100 = 10    | 10     |
| 9   | 40  | √(81 + 1600) = √1681 = 41 | 41     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Hypotenuse is found using Pythagoras theorem
- Square root can be computed using `** 0.5`
- Squaring is simple multiplication

---

## **1️⃣6️⃣ Real-Life Application**

- Architecture and construction
- Physics distance calculations
- Navigation systems
- Computer graphics (distance between points)

---

## **1️⃣7️⃣ Practice Questions**

1. Compute the area of a right-angled triangle given A and B.
2. Check if a triangle with sides A, B, C is right-angled.
3. Print √(A² − B²) if A > B.

---

## **1️⃣8️⃣ Result**

The program correctly computes and prints the hypotenuse as an integer.

---

## **1️⃣9️⃣ Conclusion**

This exercise strengthens understanding of exponentiation, square root computation, and geometric formulas—fundamental building blocks for many mathematical programs.

---
