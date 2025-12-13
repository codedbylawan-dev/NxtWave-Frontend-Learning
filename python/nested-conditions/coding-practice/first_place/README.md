# ✅ **First Place**

---

## **1️⃣ Question**

Given a positive integer **N**, print the digit in its **one's place**.

---

## **1.5️⃣ Category**

Arithmetic → Modulus Operator → Last Digit Extraction

---

## **2️⃣ Outline**

- Read integer N
- Compute `N % 10`
- Print the result

---

## **3️⃣ Objective**

To extract the one's place digit of any positive integer.

---

## **4️⃣ Purpose**

Helps in understanding modulus operation, digit extraction, and number manipulation.

---

## **5️⃣ Theory**

The expression:

```
N % 10
```

always gives the **last digit** of a number.

Examples:
25 % 10 → 5
200 % 10 → 0
9 % 10 → 9

---

## **6️⃣ Step-by-Step Explanation**

1. Read input number N
2. Take remainder when divided by 10
3. That remainder is the one’s place digit
4. Print the result

---

## **7️⃣ Method**

Use modulus operator `%` to extract last digit.

---

## **8️⃣ Constraints**

- N is a positive integer
- Output must be a single digit

---

## **9️⃣ Common Mistakes**

❌ Using division instead of modulus
❌ Printing extra text
❌ Forgetting integer conversion

---

## 🔟 Complexity

Time: **O(1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())
print(N % 10)
```

---

## **1️⃣2️⃣ Example**

### Input

```
25
```

### Output

```
5
```

---

## **1️⃣3️⃣ Dry Run**

| N   | Operation | Result |
| --- | --------- | ------ |
| 25  | 25 % 10   | 5      |
| 200 | 200 % 10  | 0      |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----- | ------ |
| 25    | 5      |
| 200   | 0      |
| 9     | 9      |
| 1234  | 4      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `% 10` is the quickest way to access the last digit
- Works for any size number

---

## **1️⃣6️⃣ Real-Life Application**

- Extracting last digit of OTP
- Checking even/odd using last digit
- Detecting number patterns

---

## **1️⃣7️⃣ Practice Questions**

1. Print the tens place of a number
2. Print the sum of last two digits
3. Print last digit of N²

---

## **1️⃣8️⃣ Result**

Correctly extracts and prints the one’s place digit of N.

---

## **1️⃣9️⃣ Conclusion**

A simple but essential modulus-based digit extraction problem.

---
