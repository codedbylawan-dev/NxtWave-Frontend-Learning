# ✅ **Greater than 30 and 50**

---

## **1️⃣ Question**

Read a number **X** and check:

1. Is **X > 30**?
2. If yes, also check whether **X > 50**.

Based on the conditions, print:

- **"X is Greater than 30"** → if X > 30
- **"X is Greater than 50"** on the next line → if X > 50

If X ≤ 30 → **print nothing** (as per problem statement logic).

---

## **1.5️⃣ Category**

Conditional Statements → Comparison → Multi-level Checks

---

## **2️⃣ Outline**

- Read X
- If X > 30 → print message
- If X > 50 → print second message
- End

---

## **3️⃣ Objective**

To perform sequential conditional checks and print multiple outputs depending on the number’s value.

---

## **4️⃣ Purpose**

This task helps understand:

- multi-step condition checking
- printing selective outputs
- correct ordering of conditions

---

## **5️⃣ Theory**

Conditions:

[
X > 30
]
[
X > 50
]

These checks are **independent** but must follow order:

First check 30 → then check 50.

---

## **6️⃣ Step-by-Step Explanation**

1. Read X
2. If X > 30 → print
3. Inside the same logic, check if X > 50
4. If yes → print second line
5. End

---

## **7️⃣ Method**

- Use if
- Use nested or sequential if
- No else required

---

## **8️⃣ Constraints**

- X is an integer
- Output must match exact strings
- Maintain correct line order

---

## **9️⃣ Common Mistakes**

❌ Printing the >50 message first
❌ Using “Greater” instead of “Greater than”
❌ Using if–else instead of two if statements
❌ Printing extra blank lines

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
X = int(input())

if X > 30:
    print("X is Greater than 30")
    if X > 50:
        print("X is Greater than 50")
```

---

## **1️⃣2️⃣ Example**

### Input

```
45
```

### Output

```
X is Greater than 30
```

---

## **1️⃣3️⃣ Dry Run**

| X   | X>30? | X>50? | Output                                      |
| --- | ----- | ----- | ------------------------------------------- |
| 45  | Yes   | No    | X is Greater than 30                        |
| 99  | Yes   | Yes   | X is Greater than 30 ↵ X is Greater than 50 |
| 20  | No    | No    | _(prints nothing)_                          |

---

## **1️⃣4️⃣ Test Cases Table**

| X   | Output                                      |
| --- | ------------------------------------------- |
| 45  | X is Greater than 30                        |
| 99  | X is Greater than 30 ↵ X is Greater than 50 |
| 31  | X is Greater than 30                        |
| 51  | X is Greater than 30 ↵ X is Greater than 50 |
| 30  | _(nothing)_                                 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- If both conditions are true → print two lines
- Condition checks happen in increasing threshold order
- No output is required for X ≤ 30

---

## **1️⃣6️⃣ Real-Life Application**

- Tiered eligibility checks
- Age-based or score-based filtering
- Access permissions (low → mid → high levels)

---

## **1️⃣7️⃣ Practice Questions**

1. Print “Eligible for Level 1” if score > 40, also print “Eligible for Level 2” if > 70.
2. If age > 18 print “Adult”, and if > 60 print “Senior Citizen”.
3. Print salary bonuses based on >50k and >1L checks.

---

## **1️⃣8️⃣ Result**

Program correctly handles sequential condition checks and prints the proper messages in order.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens layered condition handling — essential for real-world logic flows.

---
