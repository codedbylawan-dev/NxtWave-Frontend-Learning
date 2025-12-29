# ✅ **Case Conversion – 2**

---

## **1️⃣ Question**

Given a string, modify it as follows:

- Add a hyphen (`-`) **before each uppercase character**
- Convert uppercase characters to **lowercase**

Print the modified string.

---

## **1️⃣.5️⃣ Category**

String → For Loop → String Methods → Formatting

---

## **2️⃣ Outline**

- Read the input string
- Initialize empty result
- Traverse characters
- If character is uppercase:

  - Add `-`
  - Convert it to lowercase

- Otherwise, append character
- Print the result

---

## **3️⃣ Objective**

To transform a CamelCase-style string into a **hyphen-separated lowercase string**.

---

## **4️⃣ Purpose**

This problem helps in learning:

- conditional character transformation
- combined usage of `isupper()` and `lower()`
- structured string building

---

## **5️⃣ Theory**

Uppercase detection:

```python
ch.isupper()
```

Lowercase conversion:

```python
ch.lower()
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read input string
2. Create empty `result`
3. Loop through each character
4. If character is uppercase:

   - Append `-`
   - Append lowercase version of the character

5. Else append the character
6. Print result

---

## **7️⃣ Method**

- One `for` loop
- `isupper()`
- `lower()`
- String concatenation

---

## **8️⃣ Constraints**

- Every uppercase letter introduces a hyphen
- Output must be completely lowercase except hyphens

---

## **9️⃣ Common Mistakes**

❌ Forgetting to convert uppercase to lowercase
❌ Using replace instead of logic
❌ Printing inside the loop

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

result = ""

for ch in s:
    if ch.isupper():
        result = result + "-" + ch.lower()
    else:
        result = result + ch

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
aChristmasStory
```

### Output

```
a-christmas-story
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"theFox"`

Processing:

- t → result = "t"
- h → "th"
- e → "the"
- F → add "-" + "f" → "the-f"
- o → "the-fo"
- x → "the-fox"

---

## **1️⃣4️⃣ Test Cases Table**

| Input           | Output            |
| --------------- | ----------------- |
| aChristmasStory | a-christmas-story |
| theFox          | the-fox           |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Combined transformations require precise control
- Character-level logic is fundamental
- This pattern appears constantly in data formatting

---

## **1️⃣6️⃣ Real-Life Application**

- URL slug generation
- Converting class names to CSS format
- Text normalization

---

## **1️⃣7️⃣ Practice Questions**

1. Convert camelCase to snake_case
2. Count hyphens added
3. Reverse the final output string

---

## **1️⃣8️⃣ Result**

The program correctly transforms the string based on the rules.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens your **conditional string processing** skills.

---
