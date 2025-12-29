# ✅ **Palindrome – 4**

---

## **1️⃣ Question**

Given a string, check whether it is a **palindrome**.

Rules:

- Treat **uppercase and lowercase letters as the same**
- **Ignore spaces and quotes** in the string

Print **True** if it is a palindrome. Otherwise, print **False**.

---

## **1️⃣.5️⃣ Category**

String → For Loop → String Methods → Validation

---

## **2️⃣ Outline**

- Read the input string
- Convert string to lowercase
- Remove spaces
- Remove quotes
- Reverse the cleaned string
- Compare both strings
- Print the result

---

## **3️⃣ Objective**

To verify whether a string is a palindrome **after cleaning and normalizing** the input.

---

## **4️⃣ Purpose**

This problem helps in learning:

- input cleaning
- string normalization
- reliable comparison logic

---

## **5️⃣ Theory**

A palindrome remains the same when reversed.
Before comparison, we normalize the string by:

- converting to lowercase
- removing spaces
- removing quotes

---

## **6️⃣ Step-by-Step Explanation**

1. Read input string
2. Convert the string to lowercase
3. Remove all spaces
4. Remove single quotes (`'`)
5. Reverse the processed string
6. Compare both strings
7. Print `True` or `False`

---

## **7️⃣ Method**

- `lower()`
- `replace()`
- slicing (`[::-1]`)

---

## **8️⃣ Constraints**

- Only spaces and quotes must be ignored
- Output must be exactly:

  - `True`
  - `False`

---

## **9️⃣ Common Mistakes**

❌ Forgetting to remove quotes
❌ Comparing before cleaning
❌ Printing lowercase `true` or `false`

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

s = s.lower()
s = s.replace(" ", "")
s = s.replace("'", "")

rev = s[::-1]

if s == rev:
    print(True)
else:
    print(False)
```

---

## **1️⃣2️⃣ Example**

### Input

```
No lemon no melon
```

### Output

```
True
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"No 'lemon' no melon"`

After lowercase → `no 'lemon' no melon`
Remove spaces → `no'lemon'nomelon`
Remove quotes → `nolemonnomelon`
Reverse → `nolemonnomelon`
Compare → equal

Output → `True`

---

## **1️⃣4️⃣ Test Cases Table**

| Input               | Output |
| ------------------- | ------ |
| No lemon no melon   | True   |
| No 'lemon' no melon | True   |
| Race Cars           | False  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Input cleaning is a **core programming skill**
- Comparison without normalization leads to wrong results
- Tiny changes in preprocessing matter hugely

---

## **1️⃣6️⃣ Real-Life Application**

- Text validation systems
- Natural language processing
- Search and matching engines

---

## **1️⃣7️⃣ Practice Questions**

1. Ignore punctuation also
2. Count removed characters
3. Find first mismatch index

---

## **1️⃣8️⃣ Result**

The program correctly checks whether a string is a palindrome after cleaning.

---

## **1️⃣9️⃣ Conclusion**

This version is **production-ready logic**.
Clean input → correct output → zero surprises.

---
