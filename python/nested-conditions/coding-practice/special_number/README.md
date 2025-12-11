# ✅ **Special Number**

---

## **1️⃣ Question**

Given a two-digit number **N**, check whether **any** of the following conditions is true:

1. The **sum of its digits** equals **7**
2. **One of the digits** is **7**
3. **N is divisible** by **7**

If any condition is satisfied → print **"Special Number"**
Otherwise → print **"Normal Number"**.

---

## **1.5️⃣ Category**

Arithmetic → Digit Extraction → Conditions (OR)

---

## **2️⃣ Outline**

- Extract tens digit
- Extract ones digit
- Compute sum of digits
- Check: sum == 7
- Check: tens == 7 or ones == 7
- Check: N % 7 == 0
- If any true → print Special Number
- Else → print Normal Number

---

## **3️⃣ Objective**

To classify the number as “Special” by checking digit and divisibility conditions.

---

## **4️⃣ Purpose**

To practice digit extraction, arithmetic operations, and multi-condition checking using OR logic.

---

## **5️⃣ Theory**

Two-digit digits:

[
tens = N // 10
]
[
ones = N % 10
]

Conditions:

1.

[
tens + ones = 7
]

2.

[
tens = 7 \quad \text{or} \quad ones = 7
]

3.

[
N % 7 = 0
]

Final rule:

[
\text{Special Number if any condition is true}
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Extract tens digit
3. Extract ones digit
4. Compute digit sum
5. Check if digit sum equals 7
6. Check if any digit equals 7
7. Check if N divisible by 7
8. If any condition is true → print Special Number
9. Else → print Normal Number

---

## **7️⃣ Method**

- Use `%` and `//` to extract digits
- Use OR (`or`) to combine conditions
- Use a single if–else to determine result

---

## **8️⃣ Constraints**

- N is always a two-digit integer
- Output is exactly one line
- No additional wording allowed

---

## **9️⃣ Common Mistakes**

❌ Checking all three conditions with AND instead of OR
❌ Wrong digit extraction
❌ Forgetting integer conversion
❌ Incorrect output text

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

tens = N // 10
ones = N % 10

sum_digits = tens + ones

cond1 = (sum_digits == 7)
cond2 = (tens == 7 or ones == 7)
cond3 = (N % 7 == 0)

if cond1 or cond2 or cond3:
    print("Special Number")
else:
    print("Normal Number")
```

---

## **1️⃣2️⃣ Example**

### Input

```
67
```

### Output

```
Special Number
```

---

## **1️⃣3️⃣ Dry Run**

| Step | N   | tens | ones | sum | digit==7? | N%7 | Any True? | Output         |
| ---- | --- | ---- | ---- | --- | --------- | --- | --------- | -------------- |
| 1    | 67  | 6    | 7    | 13  | Yes       | 4   | True      | Special Number |
| 2    | 36  | 3    | 6    | 9   | No        | 1   | False     | Normal Number  |

---

## **1️⃣4️⃣ Test Cases Table**

| N   | digits | sum | contains 7? | N%7 | Output         |
| --- | ------ | --- | ----------- | --- | -------------- |
| 67  | 6, 7   | 13  | Yes         | 4   | Special Number |
| 36  | 3, 6   | 9   | No          | 1   | Normal Number  |
| 34  | 3, 4   | 7   | No          | 6   | Special Number |
| 70  | 7, 0   | 7   | Yes         | 0   | Special Number |
| 28  | 2, 8   | 10  | No          | 0   | Special Number |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- OR logic is used when any condition can satisfy the requirement
- Digit extraction is crucial for number analysis
- Numbers divisible by 7 often recur in special-number problems

---

## **1️⃣6️⃣ Real-Life Application**

- Validating special numeric codes
- Pattern detection in ticket/ID systems
- Filtering numbers based on rule sets

---

## **1️⃣7️⃣ Practice Questions**

1. Print “Lucky” if a two-digit number contains 5 or sum of digits is 10.
2. Check if N is divisible by 9 or contains the digit 9.
3. Print “Good Number” if N’s digits multiply to 6.

---

## **1️⃣8️⃣ Result**

The program successfully checks all three conditions and identifies whether the number is special.

---

## **1️⃣9️⃣ Conclusion**

This problem reinforces multi-condition evaluation, digit operations, and logical OR usage—key building blocks for beginner-level programming tasks.

---
