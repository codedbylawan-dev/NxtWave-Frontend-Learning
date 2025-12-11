# ✅ **Cube of a Number**

---

## **1️⃣ Question**

Read an integer **N** and print its **cube**, which is:

[
N^3 = N \times N \times N
]

---

## **1.5️⃣ Category**

Arithmetic → Exponentiation → Basic Calculation

---

## **2️⃣ Outline**

- Read N
- Compute N × N × N
- Print the result

---

## **3️⃣ Objective**

To compute and output the cube of a given number.

---

## **4️⃣ Purpose**

To strengthen arithmetic calculation skills and expression evaluation in programming.

---

## **5️⃣ Theory**

The cube of a number is:

[
\text{Cube} = N^3 = N \times N \times N
]

Examples:
4³ = 64
10³ = 1000

---

## **6️⃣ Step-by-Step Explanation**

1. Read integer N
2. Multiply N by itself three times
3. Store result
4. Print result

---

## **7️⃣ Method**

- Use multiplication operator `*`
- No conditions required

---

## **8️⃣ Constraints**

- N can be any integer
- Output must be a single integer

---

## **9️⃣ Common Mistakes**

❌ Using N³ notation directly (not valid in basic Python)
❌ Forgetting parentheses when needed
❌ Using exponent operator incorrectly

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())
cube = N * N * N
print(cube)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
64
```

---

## **1️⃣3️⃣ Dry Run**

| Step | N   | Calculation       | Output |
| ---- | --- | ----------------- | ------ |
| 1    | 4   | 4 × 4 × 4 = 64    | 64     |
| 2    | 10  | 10 × 10 × 10=1000 | 1000   |

---

## **1️⃣4️⃣ Test Cases Table**

| N   | N³ calculation  | Output |
| --- | --------------- | ------ |
| 4   | 4×4×4 = 64      | 64     |
| 10  | 10×10×10 = 1000 | 1000   |
| 1   | 1×1×1 = 1       | 1      |
| -3  | -3×-3×-3 = -27  | -27    |
| 7   | 7×7×7 = 343     | 343    |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Cube is simply N multiplied 3 times
- Works for positive, negative, and zero
- Avoid unnecessary operators—simple multiplication is enough

---

## **1️⃣6️⃣ Real-Life Application**

- Volume of a cube (side³)
- Exponential growth modeling
- Physics calculations involving cubic measurements

---

## **1️⃣7️⃣ Practice Questions**

1. Print the square of a number (N²).
2. Print N⁴ using multiplication.
3. Print the product of N and N².

---

## **1️⃣8️⃣ Result**

The program correctly calculates and prints the cube of the input number.

---

## **1️⃣9️⃣ Conclusion**

This problem reinforces arithmetic multiplication and expression building—foundation skills for solving more complex mathematical problems in programming.

---
