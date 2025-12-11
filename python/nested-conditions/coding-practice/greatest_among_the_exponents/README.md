# ✅ **Greatest Among The Exponents**

---

## **1️⃣ Question**

Read two integers **A** and **B**, compute:

- **Aᴮ** (A power B)
- **Bᴬ** (B power A)

Print the **greater** of the two results.

---

## **1.5️⃣ Category**

Arithmetic → Exponentiation → Comparison

---

## **2️⃣ Outline**

- Read A
- Read B
- Compute Aᴮ
- Compute Bᴬ
- Compare both
- Print the greater value

---

## **3️⃣ Objective**

To determine which exponent result is larger between Aᴮ and Bᴬ.

---

## **4️⃣ Purpose**

To strengthen understanding of exponent calculations and comparisons.

---

## **5️⃣ Theory**

Exponentiation:

[
A^B = A \times A \times \dots (B \text{ times})
]

[
B^A = B \times B \times \dots (A \text{ times})
]

Comparison rule:

- If **Aᴮ > Bᴬ**, print Aᴮ
- Else, print Bᴬ

---

## **6️⃣ Step-by-Step Explanation**

1. Read A
2. Read B
3. Compute `pow1 = A ** B`
4. Compute `pow2 = B ** A`
5. Compare pow1 and pow2
6. Print the larger of the two

---

## **7️⃣ Method**

- Use exponent operator `**`
- Store results in variables
- Use simple if–else comparison

---

## **8️⃣ Constraints**

- A and B are integers
- Outputs might be large
- Print only the greater exponent result

---

## **9️⃣ Common Mistakes**

❌ Comparing A and B instead of Aᴮ and Bᴬ
❌ Using `^` (bitwise XOR) instead of `**`
❌ Forgetting to store exponent results

---

## 🔟 Complexity\*\*

- Time: O(B + A) internally
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
A = int(input())
B = int(input())

pow1 = A ** B
pow2 = B ** A

if pow1 > pow2:
    print(pow1)
else:
    print(pow2)
```

---

## **1️⃣2️⃣ Example**

### Input

```
2
3
```

### Output

```
9
```

---

## **1️⃣3️⃣ Dry Run**

| Step | A   | B   | Aᴮ  | Bᴬ  | Comparison   | Output |
| ---- | --- | --- | --- | --- | ------------ | ------ |
| 1    | 2   | 3   | 8   | 9   | 9 > 8 → True | 9      |
| 2    | 3   | 1   | 3   | 1   | 3 > 1 → True | 3      |

---

## **1️⃣4️⃣ Test Cases Table**

| A   | B   | Aᴮ  | Bᴬ  | Greater |
| --- | --- | --- | --- | ------- |
| 2   | 3   | 8   | 9   | 9       |
| 3   | 1   | 3   | 1   | 3       |
| 4   | 2   | 16  | 4   | 16      |
| 2   | 5   | 32  | 25  | 32      |
| 5   | 3   | 125 | 243 | 243     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Exponentiation grows quickly
- Always compare exponent results, not the base numbers
- Use `**` for power operations

---

## **1️⃣6️⃣ Real-Life Application**

- Scientific calculations
- Evaluating exponential growth
- Comparing exponential values in algorithms

---

## **1️⃣7️⃣ Practice Questions**

1. Print the smaller value between Aᴮ and Bᴬ.
2. Check if Aᴮ is divisible by Bᴬ.
3. Read A, B, C and print the greatest among Aᴮ, Bᶜ, and Cᴬ.

---

## **1️⃣8️⃣ Result**

The program correctly determines the greater exponent value and prints it.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens exponent evaluation and comparison logic, key ideas for mathematical and computational reasoning.

---
