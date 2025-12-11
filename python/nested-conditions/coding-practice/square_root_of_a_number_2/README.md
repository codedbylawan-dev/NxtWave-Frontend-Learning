# ✅ **Square Root of a Number – 2**

---

## **1️⃣ Question**

Read two integers **A** and **B**, and check whether:

[
\sqrt{A} = B
]

- If true → print **"Square root of A is equal to B"**
- Else → print **"Square root of A is not equal to B"**

---

## **1.5️⃣ Category**

Arithmetic → Square Root → Conditional Comparison

---

## **2️⃣ Outline**

- Read A
- Read B
- Compute square root of A
- Compare with B
- Print appropriate message

---

## **3️⃣ Objective**

To determine whether B is exactly the square root of A.

---

## **4️⃣ Purpose**

To apply square root calculation and equality checking in decision-making.

---

## **5️⃣ Theory**

Square root:

[
\sqrt{A} = A^{0.5}
]

Condition:

[
A^{0.5} = B
]

If yes → print equal message
Else → print not equal message

---

## **6️⃣ Step-by-Step Explanation**

1. Read A
2. Read B
3. Compute `root = A ** 0.5`
4. Compare root with B
5. If equal → print "Square root of A is equal to B"
6. Otherwise → print "Square root of A is not equal to B"

---

## **7️⃣ Method**

- Use exponent operator `** 0.5`
- Compare floats/integers carefully
- Use if–else for branching

---

## **8️⃣ Constraints**

- A is a non-negative integer
- B is an integer
- Output must match exactly

---

## **9️⃣ Common Mistakes**

❌ Using integer division
❌ Using `^` instead of `**`
❌ Forgetting exact output text
❌ Comparing strings instead of numbers

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
A = int(input())
B = int(input())

root = A ** 0.5

if root == B:
    print("Square root of A is equal to B")
else:
    print("Square root of A is not equal to B")
```

---

## **1️⃣2️⃣ Example**

### Input

```
64
8
```

### Output

```
Square root of A is equal to B
```

---

## **1️⃣3️⃣ Dry Run**

| A   | B   | √A    | Comparison | Output                             |
| --- | --- | ----- | ---------- | ---------------------------------- |
| 64  | 8   | 8.0   | 8.0 == 8   | Square root of A is equal to B     |
| 55  | 5   | 7.416 | 7.416 ≠ 5  | Square root of A is not equal to B |

---

## **1️⃣4️⃣ Test Cases Table**

| A   | B   | √A   | Equal? | Output                             |
| --- | --- | ---- | ------ | ---------------------------------- |
| 64  | 8   | 8    | Yes    | Square root of A is equal to B     |
| 55  | 5   | 7.41 | No     | Square root of A is not equal to B |
| 25  | 5   | 5    | Yes    | Square root of A is equal to B     |
| 36  | 7   | 6    | No     | Square root of A is not equal to B |
| 49  | 7   | 7    | Yes    | Square root of A is equal to B     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Square root in Python uses `** 0.5`
- Compare carefully after computing
- Square roots of perfect squares match integer B directly

---

## **1️⃣6️⃣ Real-Life Application**

- Verifying geometric lengths
- Checking square relationships in math problems
- Signal processing normalization

---

## **1️⃣7️⃣ Practice Questions**

1. Check if cube root of A is equal to B.
2. Print True if B² = A.
3. Print “Perfect Square” if √A is an integer.

---

## **1️⃣8️⃣ Result**

The program correctly determines whether B matches the square root of A.

---

## **1️⃣9️⃣ Conclusion**

A simple but fundamental problem that strengthens mathematical computation and conditional logic.

---
