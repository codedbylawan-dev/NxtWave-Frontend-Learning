# ✅ **Palindrome – 2**

---

## **1️⃣ Question**

Given a string, check whether the string is a **palindrome** or not.

**Note:** Treat uppercase and lowercase letters as **same** when comparing.

Print **True** if the string is a palindrome. Otherwise, print **False**.

---

## **1️⃣.5️⃣ Category**

String → String Methods → String Slicing → Validation

---

## **2️⃣ Outline**

- Read the input string
- Convert the string to lowercase
- Reverse the string
- Compare both strings
- Print the result

---

## **3️⃣ Objective**

To determine whether a string is a palindrome **ignoring case**.

---

## **4️⃣ Purpose**

This problem helps in learning:

- case normalization using `lower()`
- string reversal using slicing
- string comparison logic

---

## **5️⃣ Theory**

To ignore case while checking palindrome:

1. Convert the string to lowercase
2. Reverse it using slicing
3. Compare both

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Convert it to lowercase
3. Reverse the lowercase string
4. Compare original-lowercase and reversed string
5. Print True if equal, else False

---

## **7️⃣ Method**

- Input
- `lower()`
- Slicing `[::-1]`
- Comparison
- Output

---

## **8️⃣ Constraints**

- Case should not affect comparison
- Output must be **True** or **False**

---

## **9️⃣ Common Mistakes**

❌ Forgetting to normalize case
❌ Comparing original string directly
❌ Using loops unnecessarily

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

print(s == rev)
```

---

## **1️⃣2️⃣ Example**

### Input

```
Madam
```

### Output

```
True
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"Treat"`
Lowercase → `"treat"`
Reverse → `"taert"`
Comparison → `treat == taert` → False
Printed → `False`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----- | ------ |
| Madam | True   |
| Treat | False  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always normalize before comparison
- Slicing is the fastest way to reverse strings
- Case-insensitive problems always require preprocessing

---

## **1️⃣6️⃣ Real-Life Application**

- Username validation
- Data cleanup
- Pattern detection

---

## **1️⃣7️⃣ Practice Questions**

1. Check palindrome ignoring spaces
2. Check palindrome ignoring symbols
3. Check if a number is palindrome

---

## **1️⃣8️⃣ Result**

The program correctly identifies the palindrome **ignoring case**.

---

## **1️⃣9️⃣ Conclusion**

This strengthens your understanding of **string preprocessing + comparison**.

---
