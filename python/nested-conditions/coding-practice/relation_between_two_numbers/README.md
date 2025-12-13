# ✅ **Relation Between Two Numbers**

---

## **1️⃣ Question**

Given two integers **A** and **B**, print their relationship:

- Print **"A == B"** if A is equal to B
- Print **"A > B"** if A is greater than B
- Print **"A < B"** if A is less than B

---

## **1.5️⃣ Category**

Comparison → Relational Operators → Basic Decision Making

---

## **2️⃣ Outline**

- Read A
- Read B
- Compare A and B
- Print the correct relational expression

---

## **3️⃣ Objective**

To understand and apply relational operators to compare two numbers.

---

## **4️⃣ Purpose**

This problem helps build logical thinking for conditions, sorting, and validations.

---

## **5️⃣ Theory**

Three mutually exclusive possibilities:

[
A = B \rightarrow \text{"A == B"}
]
[
A > B \rightarrow \text{"A > B"}
]
[
A < B \rightarrow \text{"A < B"}
]

These cover all integer comparisons.

---

## **6️⃣ Step-by-Step Explanation**

1. Read A
2. Read B
3. Check if A equals B
4. Else check if A is greater than B
5. Else A must be less than B
6. Print the correct relational statement

---

## **7️⃣ Method**

- Use relational operators: `==`, `>`, `<`
- Use `if–elif–else`
- Output must match exactly

---

## **8️⃣ Constraints**

- A and B are integers
- Only one relational expression should be printed
- Output formatting must be exact

---

## **9️⃣ Common Mistakes**

❌ Writing `"A < B"` incorrectly (spacing matters)
❌ Using `=` instead of `==`
❌ Printing extra text
❌ Missing equal case

---

## 🔟 Complexity

- **Time:** O(1)
- **Space:** O(1)

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

| A   | B   | Condition Met | Output |
| --- | --- | ------------- | ------ |
| 3   | 4   | A < B         | A < B  |
| 4   | 4   | A == B        | A == B |
| 10  | 5   | A > B         | A > B  |

---

## **1️⃣4️⃣ Test Cases Table**

| A   | B   | Output |
| --- | --- | ------ |
| 3   | 4   | A < B  |
| 4   | 4   | A == B |
| 7   | 2   | A > B  |
| -1  | -1  | A == B |
| -5  | 10  | A < B  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Relational operators help compare values
- Only one condition is true for any pair
- Always check equality first for clean logic

---

## **1️⃣6️⃣ Real-Life Application**

- Sorting numbers
- Comparing student scores
- Ranking systems
- Input validation

---

## **1️⃣7️⃣ Practice Questions**

1. Print relationship between three numbers (A, B, C).
2. Check if a number lies between two other numbers.
3. Compare two ages and print who is older.

---

## **1️⃣8️⃣ Result**

The program accurately prints the relationship between two numbers.

---

## **1️⃣9️⃣ Conclusion**

A fundamental problem that strengthens comparison logic — essential for decision-making branching in all programs.

---
