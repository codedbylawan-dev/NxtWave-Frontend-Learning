# ✅ **Not divisible by Numbers**

---

## **1️⃣ Question**

Read a number **N** and check whether **N is NOT divisible** by **all** of these numbers:

- 2
- 3
- 5
- 7

If N is **not divisible by every one of them**, print **True**.
Otherwise, print **False**.

---

## **1.5️⃣ Category**

Arithmetic → Divisibility → Logical AND (all conditions must be true)

---

## **2️⃣ Outline**

- Read N
- Check N%2, N%3, N%5, N%7
- Confirm all are non-zero
- Print True if all are non-zero, else False

---

## **3️⃣ Objective**

To determine if a number is simultaneously **not divisible** by 2, 3, 5, and 7.

---

## **4️⃣ Purpose**

To understand combined logical conditions using AND for multiple constraints.

---

## **5️⃣ Theory**

A number is **not divisible** by X if:

[
N % X \neq 0
]

Conditions:

[
N%2 \neq 0
]
[
N%3 \neq 0
]
[
N%5 \neq 0
]
[
N%7 \neq 0
]

Final rule:

[
\text{True if ALL are non-zero}
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Check if N % 2 != 0
3. Check if N % 3 != 0
4. Check if N % 5 != 0
5. Check if N % 7 != 0
6. If **all** checks are true → print True
7. Else → print False

---

## **7️⃣ Method**

- Use `%` operator
- Combine checks using AND (`and`)
- Use boolean output

---

## **8️⃣ Constraints**

- N is an integer
- Output must be **True** or **False**
- Exact capitalization matters

---

## **9️⃣ Common Mistakes**

❌ Using OR instead of AND
❌ Forgetting "not divisible" means `% != 0`
❌ Misplacing parentheses
❌ Printing lowercase true/false

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

cond = (N % 2 != 0) and (N % 3 != 0) and (N % 5 != 0) and (N % 7 != 0)

if cond:
    print("True")
else:
    print("False")
```

---

## **1️⃣2️⃣ Example**

### Input

```
5633
```

### Output

```
True
```

---

## **1️⃣3️⃣ Dry Run**

| N    | %2  | %3  | %5  | %7  | All non-zero? | Output |
| ---- | --- | --- | --- | --- | ------------- | ------ |
| 5633 | 1   | 2   | 3   | 6   | Yes           | True   |
| 1000 | 0   | 1   | 0   | 6   | No            | False  |

---

## **1️⃣4️⃣ Test Cases Table**

| N    | Divisible by any of 2,3,5,7? | Output |
| ---- | ---------------------------- | ------ |
| 5633 | No                           | True   |
| 1000 | Yes (2 & 5)                  | False  |
| 49   | Yes (7)                      | False  |
| 81   | Yes (3)                      | False  |
| 121  | Yes (??) → 11 only → No      | True   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- AND ensures _all_ conditions must be true
- `% != 0` means "not divisible"
- Useful pattern for filtering numbers

---

## **1️⃣6️⃣ Real-Life Application**

- Validating numbers that must avoid certain divisors
- Prime-checking building block
- Filtering IDs that should not be divisible by specific rules

---

## **1️⃣7️⃣ Practice Questions**

1. Check if a number is not divisible by 4, 6, or 9.
2. Print True if N is not divisible by any number from 2 to 10.
3. Check if N is divisible by none of {3, 4, 8}.

---

## **1️⃣8️⃣ Result**

The program correctly identifies whether N avoids divisibility by 2, 3, 5, and 7.

---

## **1️⃣9️⃣ Conclusion**

A simple but powerful exercise that reinforces AND-based validation logic and modulus operations.

---
