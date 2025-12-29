# 🧩 **Letter, Digit or Special Character**

---

## **1️⃣ Question**

Given a character **C**, determine whether it is:

- **Lowercase Letter**
- **Uppercase Letter**
- **Digit**
- **Special Character**

Print the correct category.

---

## **1️⃣.5️⃣ Category**

String → Character Classification → Conditional Logic

---

## **2️⃣ Outline**

- Read the character `C`
- Check if `C` is between `'a'` and `'z'`
- Else check if `C` is between `'A'` and `'Z'`
- Else check if `C` is between `'0'` and `'9'`
- Otherwise → Special Character

---

## **3️⃣ Objective**

To classify a single character into its correct type.

---

## **4️⃣ Purpose**

This problem builds understanding of:

- ASCII ordering
- Character ranges
- Multi-condition decision logic

---

## **5️⃣ Theory**

Characters in computers follow an ordered sequence.

- `'a'` to `'z'` → lowercase
- `'A'` to `'Z'` → uppercase
- `'0'` to `'9'` → digits
- Everything else → special characters

---

## **6️⃣ Step-by-Step Explanation**

1. Read input character `c`
2. Compare it with lowercase range
3. If not, compare with uppercase range
4. If not, compare with digit range
5. Else classify as special character

---

## **7️⃣ Method**

Sequential conditional checks using character comparison.

---

## **8️⃣ Constraints**

- Input contains exactly one character
- Case-sensitive classification

---

## **9️⃣ Common Mistakes**

❌ Using `isalpha()` and forgetting case
❌ Checking digit before letters
❌ Misclassifying symbols like `@`, `#`, `%`

---

## **🔟 Complexity**

- Time: **O(1)**
- Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
c = input()

if 'a' <= c <= 'z':
    print("Lowercase Letter")
elif 'A' <= c <= 'Z':
    print("Uppercase Letter")
elif '0' <= c <= '9':
    print("Digit")
else:
    print("Special Character")
```

---

## **1️⃣2️⃣ Example**

### Input

```
9
```

### Output

```
Digit
```

---

## **1️⃣3️⃣ Dry Run**

Input: `&`

Not between `a-z`
Not between `A-Z`
Not between `0-9`

➡ Classified as **Special Character**

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output            |
| ----- | ----------------- |
| 9     | Digit             |
| A     | Uppercase Letter  |
| g     | Lowercase Letter  |
| &     | Special Character |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Character comparison is faster and safer than heavy functions
- This logic is foundational for password validation, compilers, scanners

---

## **1️⃣6️⃣ Real-Life Application**

- Password validation systems
- Form input sanitization
- Tokenizers and compilers

---

## **1️⃣7️⃣ Practice Questions**

1. Count number of digits in a string
2. Count special characters in a password
3. Validate username characters

---

## **1️⃣8️⃣ Result**

The program accurately classifies any input character.

---

## **1️⃣9️⃣ Conclusion**

If you control characters, you control strings.
If you control strings, you control data.
