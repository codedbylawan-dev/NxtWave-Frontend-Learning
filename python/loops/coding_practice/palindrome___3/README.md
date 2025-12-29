# ✅ **Palindrome – 3**

---

## **1️⃣ Question**

Given a string, check whether it is a **palindrome**.

Print:

- **Palindrome** if the string is a palindrome
- **Not a Palindrome** otherwise

Comparison must **ignore case**
(`"M"` and `"m"` are considered equal)

---

## **1️⃣.5️⃣ Category**

String → For Loop → String Methods → Validation

---

## **2️⃣ Outline**

- Read the input string
- Convert string to lowercase
- Reverse the string
- Compare original and reversed
- Print result

---

## **3️⃣ Objective**

To verify whether a string reads the same **forward and backward** ignoring case.

---

## **4️⃣ Purpose**

This problem trains:

- string normalization
- reverse logic
- accurate comparison

---

## **5️⃣ Theory**

A palindrome remains unchanged when reversed.

Lowercase conversion ensures case-insensitive comparison.

---

## **6️⃣ Step-by-Step Explanation**

1. Read input
2. Convert string to lowercase
3. Reverse the string using slicing
4. Compare both strings
5. Print result

---

## **7️⃣ Method**

- String slicing
- `lower()`
- Direct comparison

---

## **8️⃣ Constraints**

- Output must be exactly:

  - `Palindrome`
  - `Not a Palindrome`

---

## **9️⃣ Common Mistakes**

❌ Forgetting case normalization
❌ Comparing wrong variables
❌ Printing inside condition incorrectly

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

s = s.lower()
rev = s[::-1]

if s == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")
```

---

## **1️⃣2️⃣ Example**

### Input

```
Madam
```

### Output

```
Palindrome
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"ROVER"`

Convert to lowercase → `"rover"`
Reverse → `"revor"`
Compare → Not equal

Output → `Not a Palindrome`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output           |
| ----- | ---------------- |
| Madam | Palindrome       |
| ROVER | Not a Palindrome |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always normalize before comparing
- Slicing makes reversal simple and clean
- This pattern appears constantly in interviews

---

## **1️⃣6️⃣ Real-Life Application**

- Text validation
- Symmetry checks
- Data integrity validation

---

## **1️⃣7️⃣ Practice Questions**

1. Ignore spaces while checking palindrome
2. Ignore special characters
3. Count how many characters matched

---

## **1️⃣8️⃣ Result**

The program correctly identifies whether a string is a palindrome.

---

## **1️⃣9️⃣ Conclusion**

This problem reinforces **string normalization and comparison discipline**.

---
