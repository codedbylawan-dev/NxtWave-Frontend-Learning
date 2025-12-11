# ✅ **Lucky Number - 2**

---

## **1️⃣ Question**

Given a two-digit number **N**, check if **any** of the following conditions is true:

1. **N is divisible by 9**
2. **One of the digits of N is equal to 9**

If any condition is satisfied, print **"Lucky Number"**, otherwise print **"Unlucky Number"**.

---

## **1.5️⃣ Category**

Arithmetic → Digit Extraction → Conditions → Logical OR

---

## **2️⃣ Outline**

- Extract tens digit
- Extract ones digit
- Check if N % 9 == 0
- Check if tens digit is 9
- Check if ones digit is 9
- If any condition true → Lucky Number
- Otherwise → Unlucky Number

---

## **3️⃣ Objective**

To determine if the number meets at least one of the conditions related to 9.

---

## **4️⃣ Purpose**

To practice divisibility checks, digit extraction, and multiple condition evaluation using logical OR.

---

## **5️⃣ Theory**

A two-digit number N has:

[
\text{tens} = N // 10
]
[
\text{ones} = N % 10
]

Conditions:

[
N % 9 = 0
]
[
\text{tens} = 9
]
[
\text{ones} = 9
]

If **any** of the above is true:

[
\text{Output} = \text{Lucky Number}
]

Else:

[
\text{Output} = \text{Unlucky Number}
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Extract tens digit
3. Extract ones digit
4. Check if N divisible by 9
5. Check if tens digit is 9
6. Check if ones digit is 9
7. If any check is true → print Lucky Number
8. Else → print Unlucky Number

---

## **7️⃣ Method**

- Use `%` for remainder
- Use `//` to extract tens digit
- Use `%` to extract ones digit
- Use logical OR to combine conditions

---

## **8️⃣ Constraints**

- N is a two-digit integer
- Output must be exactly one line
- Conditions use only digits and divisibility

---

## **9️⃣ Common Mistakes**

❌ Checking only divisibility and forgetting digit-check
❌ Using `and` instead of `or`
❌ Extracting digits incorrectly
❌ Printing wrong output text

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

cond1 = (N % 9 == 0)
cond2 = (tens == 9)
cond3 = (ones == 9)

if cond1 or cond2 or cond3:
    print("Lucky Number")
else:
    print("Unlucky Number")
```

---

## **1️⃣2️⃣ Example**

### Input

```
18
```

### Output

```
Lucky Number
```

---

## **1️⃣3️⃣ Dry Run**

| Step | N   | tens | ones | N%9 | tens==9 | ones==9 | Condition | Output         |
| ---- | --- | ---- | ---- | --- | ------- | ------- | --------- | -------------- |
| 1    | 18  | 1    | 8    | 0   | False   | False   | True      | Lucky Number   |
| 2    | 13  | 1    | 3    | 4   | False   | False   | False     | Unlucky Number |

---

## **1️⃣4️⃣ Test Cases Table**

| N   | N%9 | tens | ones | Lucky? | Output         |
| --- | --- | ---- | ---- | ------ | -------------- |
| 18  | 0   | 1    | 8    | Yes    | Lucky Number   |
| 13  | 4   | 1    | 3    | No     | Unlucky Number |
| 99  | 0   | 9    | 9    | Yes    | Lucky Number   |
| 49  | 4   | 4    | 9    | Yes    | Lucky Number   |
| 90  | 0   | 9    | 0    | Yes    | Lucky Number   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Logical OR is used when **any one** condition is enough
- Divisibility plus digit-based rules make strong number checks
- Two-digit extraction uses `//` and `%`

---

## **1️⃣6️⃣ Real-Life Application**

- Pattern-based number validation
- Special numeric filters in games or lotteries
- Checking for numbers with special properties

---

## **1️⃣7️⃣ Practice Questions**

1. Print “Special” if N is divisible by 5 **or** one digit is 5.
2. Print “Magic” if any digit of N is 7.
3. Print the sum of digits if N is divisible by either digit.

---

## **1️⃣8️⃣ Result**

The program correctly identifies whether the number satisfies at least one Lucky Number condition.

---

## **1️⃣9️⃣ Conclusion**

This problem enhances multi-condition evaluation skills using simple arithmetic and logical operations.

---
