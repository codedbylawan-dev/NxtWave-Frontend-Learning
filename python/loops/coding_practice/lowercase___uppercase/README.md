# ✅ **Lowercase & Uppercase**

---

## **1️⃣ Question**

Given a string, write a program that prints:

- The string converted to **lowercase**
- The string converted to **uppercase**

---

## **1️⃣.5️⃣ Category**

String → String Methods → Formatting

---

## **2️⃣ Outline**

- Read the input string
- Convert it to lowercase
- Convert it to uppercase
- Print both results on separate lines

---

## **3️⃣ Objective**

To generate both lowercase and uppercase versions of a string.

---

## **4️⃣ Purpose**

This problem helps in learning:

- multiple transformations on a string
- usage of `lower()` and `upper()`
- formatting multi-line output

---

## **5️⃣ Theory**

- `lower()` converts all characters to lowercase
- `upper()` converts all characters to uppercase

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Apply `lower()` and store result
3. Apply `upper()` and store result
4. Print both results

---

## **7️⃣ Method**

- Input
- `lower()`
- `upper()`
- Output

---

## **8️⃣ Constraints**

- Input is a string
- Output must contain two lines:

  - lowercase
  - uppercase

---

## **9️⃣ Common Mistakes**

❌ Printing on the same line
❌ Forgetting the order
❌ Modifying the original string

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

low = s.lower()
up = s.upper()

print(low)
print(up)
```

---

## **1️⃣2️⃣ Example**

### Input

```
Learning
```

### Output

```
learning
LEARNING
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"Transportation"`
Lower → `"transportation"`
Upper → `"TRANSPORTATION"`

---

## **1️⃣4️⃣ Test Cases Table**

| Input          | Output (2 lines)                 |
| -------------- | -------------------------------- |
| Learning       | learning<br>LEARNING             |
| Transportation | transportation<br>TRANSPORTATION |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- String methods do not modify the original string
- Order of output matters
- Formatting is part of the problem

---

## **1️⃣6️⃣ Real-Life Application**

- Display formatting
- Text normalization
- Case-insensitive comparisons

---

## **1️⃣7️⃣ Practice Questions**

1. Print original, lowercase, and uppercase
2. Convert input to title case
3. Swap the case of all characters

---

## **1️⃣8️⃣ Result**

The program correctly prints both lowercase and uppercase forms.

---

## **1️⃣9️⃣ Conclusion**

This is a foundational **string transformation** problem.

---
