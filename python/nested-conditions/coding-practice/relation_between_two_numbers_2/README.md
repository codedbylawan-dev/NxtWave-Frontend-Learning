# ✅ **Relation Between Two Numbers – 2**

---

## **1️⃣ Question**

Given two integers **A** and **B**, print the relationship between them:

- **"A == B"** → if A equals B
- **"A > B"** → if A is greater
- **"A < B"** → if A is smaller

---

## **1.5️⃣ Category**

Comparison → Relational Operators → Basic Condition Checking

---

## **2️⃣ Outline**

- Read A
- Read B
- Compare A and B
- Print corresponding relation

---

## **3️⃣ Objective**

To understand and apply fundamental comparison operations between two integers.

---

## **4️⃣ Purpose**

This reinforces relational logic used in sorting, filtering, and decision-making.

---

## **5️⃣ Theory**

The three mutually exclusive outcomes:

[
A = B \Rightarrow A == B
]
[
A > B \Rightarrow A > B
]
[
A < B \Rightarrow A < B
]

Only one can be true for any pair of numbers.

---

## **6️⃣ Step-by-Step Explanation**

1. Read A
2. Read B
3. Check if A equals B
4. Else check if A is greater than B
5. Else → A must be less

---

## **7️⃣ Method**

Use `if–elif–else` with relational operators: `==`, `>`, `<`.

---

## **8️⃣ Constraints**

- Exactly one line of output
- A and B are integers
- Output format must match exactly

---

## **9️⃣ Common Mistakes**

❌ Using `=` instead of `==`
❌ Reversing the comparison
❌ Printing multiple results
❌ Incorrect spacing (must be `"A < B"` not `"A<B"`)

---

## 🔟 Complexity

- Time: **O(1)**
- Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
A = int(input())
B = int(input())

if A == B:
    print("A == B")
elif A > B:
    print("A > B")
else:
    print("A < B")
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
A < B
```

---

## **1️⃣3️⃣ Dry Run**

| A   | B   | Result |
| --- | --- | ------ |
| 3   | 4   | A < B  |
| 4   | 4   | A == B |
| 10  | 2   | A > B  |
| -1  | 5   | A < B  |

---

## **1️⃣4️⃣ Test Cases Table**

| A   | B   | Expected Output |
| --- | --- | --------------- |
| 3   | 4   | A < B           |
| 4   | 4   | A == B          |
| 8   | 2   | A > B           |
| -5  | -10 | A > B           |
| 0   | 7   | A < B           |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- One and only one relation will be true
- Relational operators are foundational in programming
- Exact formatting matters

---

## **1️⃣6️⃣ Real-Life Application**

- Comparing prices
- Ranking scores
- Validating thresholds
- Sorting algorithms

---

## **1️⃣7️⃣ Practice Questions**

1. Print largest of A and B.
2. Print smallest of A and B.
3. Compare three numbers and find relationships.

---

## **1️⃣8️⃣ Result**

The program correctly prints the relationship between A and B.

---

## **1️⃣9️⃣ Conclusion**

A straightforward yet essential comparison problem that strengthens your understanding of relational logic in programs.

---
