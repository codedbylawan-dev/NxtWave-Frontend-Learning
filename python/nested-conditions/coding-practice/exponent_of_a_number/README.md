# ✅ **Exponent of a Number**

---

## **1️⃣ Question**

Given two integers **N** and **E**, compute:

[
N^E = N \text{ raised to the power } E
]

Print the result.

---

## **1.5️⃣ Category**

Arithmetic → Exponentiation → Basic Calculation

---

## **2️⃣ Outline**

- Read N
- Read E
- Compute N raised to power E
- Print the result

---

## **3️⃣ Objective**

To calculate the exponent value using repeated multiplication.

---

## **4️⃣ Purpose**

To understand how exponent operations work in programming.

---

## **5️⃣ Theory**

Exponentiation means multiplying N by itself E times:

[
N^E = \underbrace{N \times N \times N \dots}_{E \text{ times}}
]

Examples:
3² = 9
5³ = 125

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Read E
3. Compute N \*\* E
4. Print the result

---

## **7️⃣ Method**

- Use Python's exponent operator `**`
- No conditions required

---

## **8️⃣ Constraints**

- N and E are integers
- Output must be a single integer

---

## **9️⃣ Common Mistakes**

❌ Confusing `^` with exponent (in Python `^` is XOR, not power)
❌ Incorrect multiplication count
❌ Mixing up N and E

---

## 🔟 Complexity

- Time: O(E) internally
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())
E = int(input())

result = N ** E
print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
2
```

### Output

```
9
```

---

## **1️⃣3️⃣ Dry Run**

| Step | N   | E   | Calculation      | Output |
| ---- | --- | --- | ---------------- | ------ |
| 1    | 3   | 2   | 3² = 3×3 = 9     | 9      |
| 2    | 5   | 3   | 5³ = 5×5×5 = 125 | 125    |

---

## **1️⃣4️⃣ Test Cases Table**

| N   | E   | Calculation | Output |
| --- | --- | ----------- | ------ |
| 3   | 2   | 3×3 = 9     | 9      |
| 5   | 3   | 125         | 125    |
| 2   | 5   | 32          | 32     |
| 1   | 7   | 1           | 1      |
| 10  | 2   | 100         | 100    |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Python uses **`**`\*\* for exponentiation
- Repeated multiplication is the basis of powers
- Any number to power 0 is 1 (except 0⁰ undefined)

---

## **1️⃣6️⃣ Real-Life Application**

- Growth models
- Compounding interest
- Scientific calculations
- Exponential scaling functions

---

## **1️⃣7️⃣ Practice Questions**

1. Compute 2 raised to power N.
2. Compute N³ using exponent operator.
3. Print N² + N³ for given N.

---

## **1️⃣8️⃣ Result**

The program correctly computes the exponent result for the input values.

---

## **1️⃣9️⃣ Conclusion**

This exercise reinforces exponent operations, an essential mathematical concept used extensively in programming, algorithms, and scientific calculations.

---
