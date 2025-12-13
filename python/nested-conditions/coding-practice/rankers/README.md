# ✅ **Rankers**

---

## **1️⃣ Question**

Read a student’s rank **R** and check:

1. If **R ≤ 3**, print **"One of Top 3"**
2. If **R > 3 but R ≤ 10**, print **"Not Top 3 but One of Top 10"**

---

## **1.5️⃣ Category**

Conditional Statements → Range Checking → Multi-level Decision

---

## **2️⃣ Outline**

- Read R
- Check if R ≤ 3 → print first message
- Else check if R ≤ 10 → print second message

---

## **3️⃣ Objective**

To categorize a student's rank based on predefined ranges.

---

## **4️⃣ Purpose**

This problem helps practice layered decision logic — a core idea in classification tasks.

---

## **5️⃣ Theory**

Two exclusive conditions:

[
R \le 3
]

Else:

[
3 < R \le 10
]

Each condition prints a different message.

---

## **6️⃣ Step-by-Step Explanation**

1. Read R
2. If R ≤ 3 → print **One of Top 3**
3. Else if R ≤ 10 → print **Not Top 3 but One of Top 10**
4. End

---

## **7️⃣ Method**

- Use `if` and `elif`
- Compare using ≤
- Print exact message required

---

## **8️⃣ Constraints**

- R is a positive integer
- Only one line of output should be printed
- Output must match exactly

---

## **9️⃣ Common Mistakes**

❌ Using `<` instead of `≤`
❌ Printing both messages
❌ Forgetting the second condition
❌ Wrong capitalization or spacing

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
R = int(input())

if R <= 3:
    print("One of Top 3")
elif R <= 10:
    print("Not Top 3 but One of Top 10")
```

---

## **1️⃣2️⃣ Example**

### Input

```
7
```

### Output

```
Not Top 3 but One of Top 10
```

---

## **1️⃣3️⃣ Dry Run**

| R   | R ≤ 3 | R ≤ 10 | Output                            |
| --- | ----- | ------ | --------------------------------- |
| 3   | Yes   | —      | One of Top 3                      |
| 7   | No    | Yes    | Not Top 3 but One of Top 10       |
| 12  | No    | No     | _(no output required by problem)_ |

---

## **1️⃣4️⃣ Test Cases Table**

| R   | Output                      |
| --- | --------------------------- |
| 3   | One of Top 3                |
| 1   | One of Top 3                |
| 7   | Not Top 3 but One of Top 10 |
| 10  | Not Top 3 but One of Top 10 |
| 11  | _(no output)_               |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Ranges must be checked in correct order
- Only one message is printed
- The second condition only applies if the first fails

---

## **1️⃣6️⃣ Real-Life Application**

- Categorizing ranks, marks, or performance levels
- Access levels in systems
- Filtering customers into tiers

---

## **1️⃣7️⃣ Practice Questions**

1. Categorize marks: top 5, top 20, others.
2. Classify ages into child, teen, adult.
3. Print membership status: gold, silver, basic.

---

## **1️⃣8️⃣ Result**

The program correctly identifies whether the student belongs to **Top 3** or **Top 10**.

---

## **1️⃣9️⃣ Conclusion**

This problem builds understanding of range-based condition checks — an essential concept for many classification and decision-making programs.

---
