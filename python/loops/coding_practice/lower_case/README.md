# ✅ **Lower Case**

---

## **1️⃣ Question**

Given a string, write a program to print the string by converting **all characters to lowercase**.

---

## **1️⃣.5️⃣ Category**

String → String Methods

---

## **2️⃣ Outline**

- Read the input string
- Convert all characters to lowercase
- Print the modified string

---

## **3️⃣ Objective**

To transform the string so that **every character is in lowercase**.

---

## **4️⃣ Purpose**

This problem helps in learning:

- case conversion in strings
- usage of the `lower()` method
- text normalization

---

## **5️⃣ Theory**

Python provides a string method called **`lower()`**.

- `lower()` converts all uppercase letters to lowercase
- Lowercase letters and symbols remain unchanged

Example:

```python
"NOVEMBER".lower()
```

Result → `"november"`

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Apply `lower()` to the string
3. Store the result
4. Print the modified string

---

## **7️⃣ Method**

- Input
- `lower()` method
- Output

---

## **8️⃣ Constraints**

- Input may contain uppercase letters, lowercase letters, spaces, and symbols
- Output must contain only lowercase letters where applicable

---

## **9️⃣ Common Mistakes**

❌ Using loops unnecessarily
❌ Trying to convert character-by-character manually
❌ Forgetting that `lower()` returns a new string

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

result = s.lower()

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
NOVEMBER
```

### Output

```
november
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"Amazing Journey"`
After `lower()` → `"amazing journey"`
Printed result → `amazing journey`

---

## **1️⃣4️⃣ Test Cases Table**

| Input           | Output          |
| --------------- | --------------- |
| NOVEMBER        | november        |
| Amazing Journey | amazing journey |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always normalize text before processing
- `lower()` is essential for comparisons and validation
- No loops needed for this transformation

---

## **1️⃣6️⃣ Real-Life Application**

- Case-insensitive search
- Text normalization in databases
- Input validation

---

## **1️⃣7️⃣ Practice Questions**

1. Convert string to uppercase
2. Capitalize the first character of a string
3. Swap the case of all characters

---

## **1️⃣8️⃣ Result**

The program correctly converts the string to **lowercase**.

---

## **1️⃣9️⃣ Conclusion**

This is a basic but extremely important **string normalization operation**.

---
