# ✅ **Pair of Numbers - 2**

---

## **1️⃣ Question**

Given two integers **A** and **B**, check the following conditions:

1. **A and B are divisible by 3**
2. **A or B is divisible by 12**

If **all** conditions are satisfied → print **"Pair"**
Otherwise → print **"Not a Pair"**.

---

## **1.5️⃣ Category**

Arithmetic → Logical AND + OR → Conditions

---

## **2️⃣ Outline**

- Read A and B
- Check if A % 3 == 0
- Check if B % 3 == 0
- Check if A % 12 == 0
- Check if B % 12 == 0
- Combine conditions
- Print final result

---

## **3️⃣ Objective**

To verify two divisibility conditions and determine whether A and B form a valid pair.

---

## **4️⃣ Purpose**

To practice combining multiple conditions using **AND** and **OR** in decision-making.

---

## **5️⃣ Theory**

Divisibility checks:

[
A % 3 = 0 \quad \text{and} \quad B % 3 = 0
]

[
A % 12 = 0 \quad \text{or} \quad B % 12 = 0
]

Final rule:

[
\text{Pair if (both divisible by 3) AND (at least one divisible by 12)}
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read A
2. Read B
3. Check if A divisible by 3
4. Check if B divisible by 3
5. Check if A divisible by 12
6. Check if B divisible by 12
7. Combine using:

   - `(A%3==0 and B%3==0)`
   - `(A%12==0 or B%12==0)`

8. If both true → print "Pair"
9. Else → print "Not a Pair"

---

## **7️⃣ Method**

- Use `%` for remainder checks
- Use AND to ensure both divisible by 3
- Use OR to ensure one divisible by 12
- Use a single if–else to output result

---

## **8️⃣ Constraints**

- A and B are integers
- Output must match exact text
- All conditions must be checked carefully

---

## **9️⃣ Common Mistakes**

❌ Using OR instead of AND for divisibility by 3
❌ Forgetting parentheses for clarity
❌ Checking wrong condition order
❌ Printing wrong text

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
A = int(input())
B = int(input())

cond1 = (A % 3 == 0 and B % 3 == 0)
cond2 = (A % 12 == 0 or B % 12 == 0)

if cond1 and cond2:
    print("Pair")
else:
    print("Not a Pair")
```

---

## **1️⃣2️⃣ Example**

### Input

```
15
240
```

### Output

```
Pair
```

---

## **1️⃣3️⃣ Dry Run**

| Step | A   | B   | A%3 | B%3 | A%12 | B%12 | cond1 | cond2 | Output     |
| ---- | --- | --- | --- | --- | ---- | ---- | ----- | ----- | ---------- |
| 1    | 15  | 240 | 0   | 0   | 3    | 0    | True  | True  | Pair       |
| 2    | 360 | 7   | 0   | 1   | 0    | 7    | False | True  | Not a Pair |

---

## **1️⃣4️⃣ Test Cases Table**

| A   | B   | divisible by 3 both? | divisible by 12 (A or B)? | Output     |
| --- | --- | -------------------- | ------------------------- | ---------- |
| 15  | 240 | Yes                  | Yes                       | Pair       |
| 360 | 7   | No                   | Yes                       | Not a Pair |
| 18  | 24  | Yes                  | Yes                       | Pair       |
| 9   | 11  | No                   | No                        | Not a Pair |
| 36  | 45  | Yes                  | Yes                       | Pair       |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- AND requires all conditions to be true
- OR requires only one to be true
- Combining both gives powerful logical control

---

## **1️⃣6️⃣ Real-Life Application**

- Validating pairs based on multiple rules
- Screening values for multiple criteria
- Matchmaking logic in programs

---

## **1️⃣7️⃣ Practice Questions**

1. Print “Valid” if A and B are divisible by 5 and one is divisible by 10.
2. Print “Strong Pair” if both numbers are divisible by 4 and one divisible by 8.
3. Check if A and B are divisible by 2, and at least one divisible by 3.

---

## **1️⃣8️⃣ Result**

The program correctly identifies whether A and B satisfy both divisibility conditions.

---

## **1️⃣9️⃣ Conclusion**

This problem reinforces combining AND and OR logic in real-world numeric evaluations while improving condition-handling accuracy.

---
