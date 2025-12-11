# ✅ **Armstrong Number – 2**

---

## **1️⃣ Question**

Read a **four-digit number N** and check whether it is an **Armstrong Number**.

If it is → print **"Armstrong Number"**
Else → print **"Not an Armstrong Number"**

---

## **1.5️⃣ Category**

Number Theory → Digit Extraction → Exponentiation

---

## **2️⃣ Outline**

- Read N
- Extract four digits
- Raise each digit to the power 4
- Add all powers
- Compare sum with N
- Print result

---

## **3️⃣ Objective**

To determine if a 4-digit number satisfies the Armstrong number condition.

---

## **4️⃣ Purpose**

This problem strengthens your understanding of:

- digit extraction
- exponentiation
- equality checking

All common patterns in programming.

---

## **5️⃣ Theory**

A number is Armstrong if:

[
a^4 + b^4 + c^4 + d^4 = N
]

For example:

[
1^4 + 6^4 + 3^4 + 4^4 = 1634
]

So 1634 is an Armstrong number.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Extract digits using division and modulo
3. Compute power 4 of all digits
4. Add the powers
5. Compare with N
6. If equal → Armstrong Number
7. Else → Not an Armstrong Number

---

## **7️⃣ Method**

- Use `%` and `//` for digit extraction
- Use exponent operator `**` for 4th power
- Use simple if–else for decision

---

## **8️⃣ Constraints**

- N is a 4-digit integer
- Output text must match exactly

---

## **9️⃣ Common Mistakes**

❌ Using power 3 instead of 4
❌ Incorrect digit extraction
❌ Mixing digit order
❌ Printing wrong string (“Numbe”)

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

a = N // 1000          # thousands digit
b = (N // 100) % 10    # hundreds digit
c = (N // 10) % 10     # tens digit
d = N % 10             # ones digit

sum_powers = (a**4) + (b**4) + (c**4) + (d**4)

if sum_powers == N:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
```

---

## **1️⃣2️⃣ Example**

### Input

```
1634
```

### Output

```
Armstrong Number
```

---

## **1️⃣3️⃣ Dry Run**

| N    | Digits  | Powers (⁴)      | Sum              | Armstrong? |
| ---- | ------- | --------------- | ---------------- | ---------- |
| 1634 | 1,6,3,4 | 1,1296,81,256   | 1634             | Yes        |
| 1568 | 1,5,6,8 | 1,625,1296,4096 | 602 + ... ≠ 1568 | No         |

---

## **1️⃣4️⃣ Test Cases Table**

| N    | Sum of 4th powers | Output                  |
| ---- | ----------------- | ----------------------- |
| 1634 | 1634              | Armstrong Number        |
| 8208 | 8208              | Armstrong Number        |
| 9474 | 9474              | Armstrong Number        |
| 1568 | ≠ 1568            | Not an Armstrong Number |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- A 4-digit Armstrong number uses power 4
- Only a few Armstrong numbers exist
- Digit extraction is critical and frequently used

---

## **1️⃣6️⃣ Real-Life Application**

- Checksum logic
- Data validation using mathematical signatures
- Cryptography toy examples

---

## **1️⃣7️⃣ Practice Questions**

1. Check whether a **5-digit** number is an Armstrong number.
2. Print the sum of 4th powers of a number’s digits.
3. Check if sum of 4th powers is divisible by 7.

---

## **1️⃣8️⃣ Result**

The program correctly evaluates whether a 4-digit number is Armstrong.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens numerical reasoning, digit manipulation, and exponentiation skills—a key step toward mastering algorithmic thinking.

---
