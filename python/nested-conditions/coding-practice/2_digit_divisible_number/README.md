# ✅ **2 Digit Divisible Number**

---

## **1️⃣ Question**

Given a two-digit number **N**, check if **N is divisible by both digits of N**.
If yes, print **double of N**. Otherwise, print **N**.

---

## **1.5️⃣ Category**

Arithmetic → Digit Extraction → Conditions

---

## **2️⃣ Outline**

- Extract tens digit
- Extract ones digit
- Check divisibility by both digits
- If divisible by both → print double
- Otherwise → print N

---

## **3️⃣ Objective**

To determine whether N is divisible by both of its digits and output the correct value.

---

## **4️⃣ Purpose**

To apply digit extraction, remainder operations, and conditional logic.

---

## **5️⃣ Theory**

A two-digit number has:

[
\text{tens} = N // 10
]
[
\text{ones} = N % 10
]

N is divisible by its digits if:

[
N % \text{tens} = 0
]
[
N % \text{ones} = 0
]

If both are true:

[
\text{answer} = 2 \times N
]

Otherwise:

[
\text{answer} = N
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Extract tens and ones digits
3. Check divisibility by tens digit
4. Check divisibility by ones digit (only if ones ≠ 0)
5. If both conditions true → output N × 2
6. Else → output N

---

## **7️⃣ Method**

- Use `%` and `//` for digit operations
- Use separate conditions for divisibility
- Use a single final if–else to print the answer

---

## **8️⃣ Constraints**

- N is a two-digit number
- Ones digit may be zero
- Output is a single integer

---

## **9️⃣ Common Mistakes**

❌ Forgetting to extract digits correctly
❌ Dividing by zero
❌ Checking only one digit

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

cond1 = (N % tens == 0)
cond2 = (ones != 0 and N % ones == 0)

if cond1 and cond2:
    print(N * 2)
else:
    print(N)
```

---

## **1️⃣2️⃣ Example**

### Input

```
15
```

### Output

```
30
```

---

## **1️⃣3️⃣ Dry Run**

| Step | N   | tens | ones | N%tens | N%ones | cond1 | cond2 | Output |
| ---- | --- | ---- | ---- | ------ | ------ | ----- | ----- | ------ |
| 1    | 15  | 1    | 5    | 0      | 0      | True  | True  | 30     |
| 2    | 26  | 2    | 6    | 0      | 2      | True  | False | 26     |

---

## **1️⃣4️⃣ Test Cases Table**

| N   | tens | ones | cond1 | cond2 | Output |
| --- | ---- | ---- | ----- | ----- | ------ |
| 15  | 1    | 5    | True  | True  | 30     |
| 26  | 2    | 6    | True  | False | 26     |
| 12  | 1    | 2    | True  | True  | 24     |
| 20  | 2    | 0    | True  | False | 20     |
| 44  | 4    | 4    | True  | True  | 88     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Use `//` for tens digit
- Use `%` for ones digit
- Use logical AND to combine checks

---

## **1️⃣6️⃣ Real-Life Application**

- Validating number patterns
- Logical checks in digit-based systems
- Simple numeric filtering tasks

---

## **1️⃣7️⃣ Practice Questions**

1. Print triple of N if divisible by its tens digit.
2. Check if both digits of N are even.
3. Print the sum of digits if N is divisible by its ones digit.

---

## **1️⃣8️⃣ Result**

The program outputs double of N if divisible by both digits; otherwise, it outputs N.

---

## **1️⃣9️⃣ Conclusion**

Digit extraction and condition checks allow powerful number validation and basic problem-solving patterns.

---
