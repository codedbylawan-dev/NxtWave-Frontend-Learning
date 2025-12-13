# ✅ **Win or Lose or Draw**

---

## **1️⃣ Question**

Read two integers **A** and **B** representing scores and compare them:

- If **A > B**, print **"Win"**
- If **A == B**, print **"Draw"**
- If **A < B**, print **"Lose"**

---

## **1.5️⃣ Category**

Comparison → Conditional Statements → Game Logic

---

## **2️⃣ Outline**

- Read score A
- Read score B
- Compare A and B
- Print Win / Draw / Lose accordingly

---

## **3️⃣ Objective**

To correctly determine the match outcome by comparing two numbers.

---

## **4️⃣ Purpose**

This builds strong fundamentals in comparison operators and conditional branching.

---

## **5️⃣ Theory**

Three possible comparisons:

[
A > B \Rightarrow \text{Win}
]
[
A = B \Rightarrow \text{Draw}
]
[
A < B \Rightarrow \text{Lose}
]

These are **mutually exclusive** conditions.

---

## **6️⃣ Step-by-Step Explanation**

1. Read A
2. Read B
3. If A > B → print Win
4. Else if A == B → print Draw
5. Else → print Lose

---

## **7️⃣ Method**

- Use relational operators: `>`, `==`, `<`
- Use `if`, `elif`, `else`
- Print exact strings

---

## **8️⃣ Constraints**

- A and B are integers
- Only one output must be printed
- Must match capitalization exactly

---

## **9️⃣ Common Mistakes**

❌ Using assignment `=` instead of comparison `==`
❌ Forgetting to print only one result
❌ Misspelling Win / Lose / Draw
❌ Incorrect comparison order

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
A = int(input())
B = int(input())

if A > B:
    print("Win")
elif A == B:
    print("Draw")
else:
    print("Lose")
```

---

## **1️⃣2️⃣ Example**

### Input

```
26
47
```

### Output

```
Lose
```

---

## **1️⃣3️⃣ Dry Run**

| A   | B   | Condition Met | Output |
| --- | --- | ------------- | ------ |
| 26  | 47  | A < B         | Lose   |
| 24  | 15  | A > B         | Win    |
| 20  | 20  | A == B        | Draw   |

---

## **1️⃣4️⃣ Test Cases Table**

| A   | B   | Output |
| --- | --- | ------ |
| 26  | 47  | Lose   |
| 24  | 15  | Win    |
| 10  | 10  | Draw   |
| -3  | 5   | Lose   |
| 8   | -1  | Win    |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Relational operators are simple but powerful
- Only one outcome is correct for any pair of values
- Ordering of conditions avoids mistakes

---

## **1️⃣6️⃣ Real-Life Application**

- Leaderboards
- Comparing player scores
- Evaluating performance metrics

---

## **1️⃣7️⃣ Practice Questions**

1. Print Pass / Fail based on marks.
2. Compare ages of two people.
3. Check if temperature is higher, lower, or same as previous day.

---

## **1️⃣8️⃣ Result**

The program correctly determines whether A wins, loses, or draws against B.

---

## **1️⃣9️⃣ Conclusion**

A foundational problem that builds strong confidence in relational operators and branching logic.

---
