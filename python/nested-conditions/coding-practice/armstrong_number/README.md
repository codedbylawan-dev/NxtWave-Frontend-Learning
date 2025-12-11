# ✅ **Armstrong Number**

---

## **1️⃣ Question**

Read a **three-digit number N** and check whether it is an **Armstrong Number**.

An Armstrong Number is a number whose value is equal to the **sum of each digit raised to the power of the number of digits** (which is 3 for a 3-digit number).

If true → print **True**
Else → print **False**

---

## **1.5️⃣ Category**

Number Theory → Digit Extraction → Exponentiation → Condition Check

---

## **2️⃣ Outline**

- Read N
- Extract three digits
- Compute cube of each digit
- Compute their sum
- Compare with original number
- Print True or False

---

## **3️⃣ Objective**

To determine whether a 3-digit number satisfies the Armstrong condition.

---

## **4️⃣ Purpose**

To apply digit extraction, power calculation, and equality comparison in a meaningful mathematical task.

---

## **5️⃣ Theory**

For a 3-digit number:

[
N = 100a + 10b + c
]

Armstrong condition:

[
a^3 + b^3 + c^3 = N
]

Examples:

- **371** → (3^3 + 7^3 + 1^3 = 371) → Armstrong
- **351** → (3^3 + 5^3 + 1^3 = 343) → Not Armstrong

---

## **6️⃣ Step-by-Step Explanation**

1. Read integer N
2. Extract digits using division and modulo
3. Compute cube of each digit
4. Add cubes
5. Compare sum with N
6. If equal → True
7. Otherwise → False

---

## **7️⃣ Method**

- Use `//` and `%` for digit extraction
- Use exponent operator `**` for cubes
- Use a single if–else for final decision

---

## **8️⃣ Constraints**

- N is always a 3-digit integer (100 to 999)
- Output must be exactly `True` or `False`

---

## **9️⃣ Common Mistakes**

❌ Wrong digit extraction
❌ Using `^` instead of `**`
❌ Forgetting that it’s a 3-digit number → power should be 3
❌ Printing strings instead of boolean words (True/False)

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

a = N // 10 // 10      # hundreds digit
b = (N // 10) % 10     # tens digit
c = N % 10             # ones digit

sum_cubes = (a ** 3) + (b ** 3) + (c ** 3)

if sum_cubes == N:
    print("True")
else:
    print("False")
```

---

## **1️⃣2️⃣ Example**

### Input

```
371
```

### Output

```
True
```

---

## **1️⃣3️⃣ Dry Run**

| N   | a   | b   | c   | a³  | b³  | c³  | Sum | Sum == N? | Output |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------ |
| 371 | 3   | 7   | 1   | 27  | 343 | 1   | 371 | Yes       | True   |
| 351 | 3   | 5   | 1   | 27  | 125 | 1   | 153 | No        | False  |

---

## **1️⃣4️⃣ Test Cases Table**

| N   | Digits | Sum of Cubes | Output |
| --- | ------ | ------------ | ------ |
| 371 | 3,7,1  | 371          | True   |
| 153 | 1,5,3  | 153          | True   |
| 370 | 3,7,0  | 370          | True   |
| 407 | 4,0,7  | 407          | True   |
| 351 | 3,5,1  | 153          | False  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Armstrong numbers are rare special numbers
- Digit extraction is essential for this type of problem
- Cubes grow fast, so results vary significantly

---

## **1️⃣6️⃣ Real-Life Application**

- Digital security pattern checks
- Mathematical curiosity and number theory problems
- Used in some checksum validation techniques

---

## **1️⃣7️⃣ Practice Questions**

1. Check if a **4-digit** number is an Armstrong number.
2. Print the sum of digits each raised to the power of 3 (for any N).
3. Check if the sum of cubes of digits is divisible by 7.

---

## **1️⃣8️⃣ Result**

The program correctly checks whether a 3-digit number is an Armstrong number.

---

## **1️⃣9️⃣ Conclusion**

Armstrong numbers combine digit operations and exponentiation, helping build strong number-manipulation logic skills.

---
