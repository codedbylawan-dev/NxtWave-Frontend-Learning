# ✅ **Sum of The Digits – 2**

---

## **1️⃣ Question**

Given an integer between **0 and 10000**, print the **sum of its digits**.

---

## **1.5️⃣ Category**

Strings → Indexing → Type Conversion → Arithmetic

---

## **2️⃣ Outline**

- Read number as string
- Find its length
- Extract each digit
- Convert to int
- Add them
- Print sum

---

## **3️⃣ Objective**

To compute the digit sum using string indexing without loops.

---

## **4️⃣ Purpose**

Strengthens your understanding of:

- String-to-integer conversions
- Indexing
- Conditional handling of varying lengths

---

## **5️⃣ Theory**

Any number `N` can be treated as a string `"N"`.

Example:
`"692"` → digits are `"6"`, `"9"`, `"2"`
Sum = `6 + 9 + 2 = 17`

Length determines how many digits exist.

---

## **6️⃣ Step-by-Step Explanation**

1. Read number as string
2. Determine its length using `len()`
3. If length is 1 → add that digit
4. If length is 2 → add both digits
5. If length is 3 → add three digits
6. If length is 4 → add four digits
7. If length is 5 → add five digits
8. Print the result

---

## **7️⃣ Method**

Use:

- `str()` input
- `len()`
- Indexing: `s[0]`, `s[1]`, …
- Convert each digit using `int()`

No loops are used.

---

## **8️⃣ Constraints**

- 0 ≤ N ≤ 10000
- Length between 1 and 5
- No loops allowed
- Output must be a single number

---

## **9️⃣ Common Mistakes**

❌ Forgetting to convert characters to integers
❌ Trying to use loops (not yet learned)
❌ Mis-indexing digits
❌ Not handling the `0` case

---

## 🔟 Complexity

Time: **O(1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
s = input()
L = len(s)

if L == 1:
    total = int(s[0])
elif L == 2:
    total = int(s[0]) + int(s[1])
elif L == 3:
    total = int(s[0]) + int(s[1]) + int(s[2])
elif L == 4:
    total = int(s[0]) + int(s[1]) + int(s[2]) + int(s[3])
else:  # length == 5
    total = int(s[0]) + int(s[1]) + int(s[2]) + int(s[3]) + int(s[4])

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
692
```

### Output

```
17
```

---

## **1️⃣3️⃣ Dry Run**

| Input  | Digits  | Sum            |
| ------ | ------- | -------------- |
| `25`   | 2, 5    | 2 + 5 = 7      |
| `692`  | 6, 9, 2 | 6 + 9 + 2 = 17 |
| `9999` | 9,9,9,9 | 36             |
| `0`    | 0       | 0              |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----- | ------ |
| 25    | 7      |
| 692   | 17     |
| 9999  | 36     |
| 10000 | 1      |
| 5     | 5      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Strings make digit extraction easy
- Indexing avoids loops
- Always convert characters to integers before adding

---

## **1️⃣6️⃣ Real-Life Application**

- Digital sum checks (banking, validation)
- Numerology calculations
- Checksums in data encoding

---

## **1️⃣7️⃣ Practice Questions**

1. Print the product of digits of a number.
2. Reverse a number using string indexing.
3. Check if a number is a palindrome without loops.

---

## **1️⃣8️⃣ Result**

The program correctly calculates the digit sum for any number up to 10000.

---

## **1️⃣9️⃣ Conclusion**

A clean and simple method to compute digit sum using only string indexing — no advanced concepts required.

---
