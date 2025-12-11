# ✅ **Square Root of a Number**

---

## **1️⃣ Question**

Read an integer **N** and print its **square root**.

---

## **1.5️⃣ Category**

Arithmetic → Exponentiation → Square Root

---

## **2️⃣ Outline**

- Read N
- Compute square root using exponent **0.5**
- Print the result as a float

---

## **3️⃣ Objective**

To calculate and print the square root of a number using exponentiation.

---

## **4️⃣ Purpose**

To learn how square roots can be computed in programming using power operations.

---

## **5️⃣ Theory**

Square root of a number is:

[
\sqrt{N} = N^{0.5}
]

Examples:
4 → 2.0
100 → 10.0

---

## **6️⃣ Step-by-Step Explanation**

1. Read input value N
2. Compute N \*\* 0.5
3. Store the result in a variable
4. Print the final float value

---

## **7️⃣ Method**

- Use the exponent operator `**`
- Use exponent **0.5** for square root

---

## **8️⃣ Constraints**

- N is a non-negative integer
- Output is a **float**
- Must print only the square root

---

## **9️⃣ Common Mistakes**

❌ Using `^` instead of `**`
❌ Forgetting to convert to float
❌ Printing extra text

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())
result = N ** 0.5
print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
2.0
```

---

## **1️⃣3️⃣ Dry Run**

| Step | N   | N^0.5 Calculation | Output |
| ---- | --- | ----------------- | ------ |
| 1    | 4   | 4^0.5 = 2.0       | 2.0    |
| 2    | 100 | 100^0.5 = 10.0    | 10.0   |

---

## **1️⃣4️⃣ Test Cases Table**

| N   | Square Root | Output |
| --- | ----------- | ------ |
| 4   | 2.0         | 2.0    |
| 100 | 10.0        | 10.0   |
| 1   | 1.0         | 1.0    |
| 81  | 9.0         | 9.0    |
| 0   | 0.0         | 0.0    |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Square root in Python can be computed using `N ** 0.5`
- Always outputs a float
- Works for any non-negative integer

---

## **1️⃣6️⃣ Real-Life Application**

- Geometry calculations
- Physics equations
- Machine learning normalization
- Financial modeling (volatility, variance)

---

## **1️⃣7️⃣ Practice Questions**

1. Print cube root of N using exponent **1/3**.
2. Print square of the square root of N.
3. Print the sum of N and its square root.

---

## **1️⃣8️⃣ Result**

The program correctly computes the square root of the given number.

---

## **1️⃣9️⃣ Conclusion**

This problem helps understand exponent-based mathematical operations and is essential for handling scientific and analytical computations.

---
