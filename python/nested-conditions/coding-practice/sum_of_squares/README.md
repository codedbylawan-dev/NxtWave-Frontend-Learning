# ✅ **Sum of Squares**

---

## **1️⃣ Question**

Read two integers **A** and **B**, compute:

[
A^2 + B^2
]

If the result is **greater than or equal to 60**, print **"Greater than or Equal to 60"**.
Otherwise, print **"Less than 60"**.

---

## **1.5️⃣ Category**

Arithmetic → Squaring Numbers → Conditional Comparison

---

## **2️⃣ Outline**

- Read A
- Read B
- Compute A²
- Compute B²
- Compute A² + B²
- Compare with 60
- Print result

---

## **3️⃣ Objective**

To calculate the sum of squares of two numbers and evaluate it against a threshold.

---

## **4️⃣ Purpose**

To apply exponentiation and conditional decision-making.

---

## **5️⃣ Theory**

Square of a number:

[
A^2 = A \times A
]
[
B^2 = B \times B
]

Sum:

[
A^2 + B^2
]

Condition:

[
\text{If } A^2 + B^2 \ge 60 \Rightarrow \text{Greater than or Equal to 60}
]
[
\text{Else } \text{Less than 60}
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read input A
2. Read input B
3. Compute square of A
4. Compute square of B
5. Compute total = A² + B²
6. Check if total ≥ 60
7. Print appropriate output

---

## **7️⃣ Method**

- Use multiplication for squaring
- Use one if–else comparison
- Print exact required output

---

## **8️⃣ Constraints**

- Inputs are integers
- Output must match exact phrasing
- No extra spaces or text

---

## **9️⃣ Common Mistakes**

❌ Using `^` instead of `**` or multiplication
❌ Forgetting parentheses
❌ Misreading “greater than or equal to”
❌ Typing wrong output message

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
A = int(input())
B = int(input())

sum_squares = (A * A) + (B * B)

if sum_squares >= 60:
    print("Greater than or Equal to 60")
else:
    print("Less than 60")
```

---

## **1️⃣2️⃣ Example**

### Input

```
10
2
```

### Output

```
Greater than or Equal to 60
```

---

## **1️⃣3️⃣ Dry Run**

| A   | B   | A²  | B²  | A² + B² | Comparison      | Output                      |
| --- | --- | --- | --- | ------- | --------------- | --------------------------- |
| 10  | 2   | 100 | 4   | 104     | 104 ≥ 60 → True | Greater than or Equal to 60 |
| 1   | 3   | 1   | 9   | 10      | 10 ≥ 60 → False | Less than 60                |

---

## **1️⃣4️⃣ Test Cases Table**

| A   | B   | Sum of Squares | Output                      |
| --- | --- | -------------- | --------------------------- |
| 10  | 2   | 104            | Greater than or Equal to 60 |
| 1   | 3   | 10             | Less than 60                |
| 5   | 7   | 74             | Greater than or Equal to 60 |
| 6   | 2   | 40             | Less than 60                |
| 8   | 4   | 80             | Greater than or Equal to 60 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Squaring is just multiplying a number with itself
- Always check “≥” carefully in condition-based problems
- Sum of squares grows quickly even with small numbers

---

## **1️⃣6️⃣ Real-Life Application**

- Pythagorean theorem
- Physics formulas involving magnitudes
- Machine learning distance metrics
- Signal processing measurements

---

## **1️⃣7️⃣ Practice Questions**

1. Check if A² − B² ≥ 20.
2. Print “High” if A² + B² + C² ≥ 100.
3. Read X and print whether X² is divisible by 5.

---

## **1️⃣8️⃣ Result**

The program successfully evaluates the sum of squares and prints the correct result.

---

## **1️⃣9️⃣ Conclusion**

This problem helps strengthen arithmetic skills and conditional reasoning—essential steps in foundational programming.

---
