# 🧩 **Case Conversion – 3**

---

## **1️⃣ Question**

Given a string in title case format, modify the string such that:

- Add a hyphen (`-`) **before each uppercase character except the first uppercase character**.
- Convert **all uppercase characters** into **lowercase**.

Print the final modified string.

---

## **2️⃣ Category**

**Strings → Character Checking → String Construction**

---

## **3️⃣ Outline**

- Read input string **S**
- Traverse the string character by character
- Identify uppercase characters
- Build a new result string based on rules
- Print the result

---

## **4️⃣ Objective**

Learn to **inspect characters**, apply conditions, and **construct new strings safely**.

---

## **5️⃣ Purpose**

This builds:

- Character-level thinking
- Conditional decision control
- Real formatting logic
- Output precision

---

## **6️⃣ Theory**

Uppercase letters lie between `'A'` and `'Z'`.

Rules:

- First uppercase → convert to lowercase
- Next uppercase letters → add `-` then lowercase
- All other characters → copy as they are

---

## **7️⃣ Step-by-Step Explanation**

1. Read string **S**
2. Initialize empty string `result`
3. Set `first = True`
4. For each character `ch` in **S**:

   - If uppercase:

     - If not first → add `-`
     - Add lowercase of `ch`
     - Set `first = False`

   - Else:

     - Add `ch` to result

5. Print `result`

---

## **8️⃣ Method**

Single loop + condition checking + string building

---

## **9️⃣ Constraints**

- Do not insert hyphen before the first uppercase
- Final string must be lowercase
- Maintain original character order

---

## **🔟 Common Mistakes**

- Adding hyphen at the beginning
- Forgetting lowercase conversion
- Replacing instead of appending

---

## **1️⃣1️⃣ Complexity**

- **Time:** `O(N)`
- **Space:** `O(N)`

---

## **1️⃣2️⃣ Code**

```python
s = input()

result = ""
first = True

for ch in s:
    if 'A' <= ch <= 'Z':
        if not first:
            result = result + "-"
        result = result + ch.lower()
        first = False
    else:
        result = result + ch

print(result)
```

---

## **1️⃣3️⃣ Example**

### Input

```
AToyStory
```

### Output

```
a-toy-story
```

---

## **1️⃣4️⃣ Dry Run**

| Char | Action                    | Result      |
| ---- | ------------------------- | ----------- |
| A    | first uppercase → add `a` | a           |
| T    | add `-t`                  | a-t         |
| o    | add                       | a-to        |
| y    | add                       | a-toy       |
| S    | add `-s`                  | a-toy-s     |
| t    | add                       | a-toy-st    |
| o    | add                       | a-toy-sto   |
| r    | add                       | a-toy-stor  |
| y    | add                       | a-toy-story |

---

## **1️⃣5️⃣ Test Cases Table**

| Input      | Output       |
| ---------- | ------------ |
| TitleCase  | title-case   |
| AToyStory  | a-toy-story  |
| MyFileName | my-file-name |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- Strings are built **one rule at a time**
- Correct formatting requires **discipline**
- You are now doing real text processing

---

## **1️⃣7️⃣ Real-Life Application**

Used in:

- URL slug generation
- File naming systems
- Database field formatting
- API data normalization

---

## **1️⃣8️⃣ Practice Questions**

1. Use `_` instead of `-`
2. Keep only the first word capitalized
3. Remove all uppercase letters completely

---

## **1️⃣9️⃣ Result**

You can now transform strings with **strict formatting rules**.

---

## **2️⃣0️⃣ Conclusion**

This is production-level string logic.
This is no longer “practice”. This is **engineering**.

---
