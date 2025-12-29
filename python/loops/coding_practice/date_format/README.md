# ✅ **Date Format**

---

## **1️⃣ Question**

Given a string in the format **dd-mm-yy**, write a program to convert it into **dd/mm/yy** format.

---

## **1️⃣.5️⃣ Category**

String → String Methods → Formatting

---

## **2️⃣ Outline**

- Read the input string
- Replace `-` with `/`
- Print the modified string

---

## **3️⃣ Objective**

To convert a date string from **dash format** to **slash format**.

---

## **4️⃣ Purpose**

This problem helps in learning:

- string replacement
- formatting transformations
- usage of the `replace()` method

---

## **5️⃣ Theory**

Python provides the **`replace()`** method.

```python
text.replace(old, new)
```

It replaces all occurrences of `old` with `new`.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Apply `replace("-", "/")`
3. Store the result
4. Print the formatted date

---

## **7️⃣ Method**

- Input
- `replace()` method
- Output

---

## **8️⃣ Constraints**

- Input will always be in `dd-mm-yy` format
- Output must be in `dd/mm/yy` format

---

## **9️⃣ Common Mistakes**

❌ Trying to split the string unnecessarily
❌ Using loops instead of `replace()`

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

formatted = s.replace("-", "/")

print(formatted)
```

---

## **1️⃣2️⃣ Example**

### Input

```
07-11-2020
```

### Output

```
07/11/2020
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"12-10-2222"`
After replace → `"12/10/2222"`
Printed → `12/10/2222`

---

## **1️⃣4️⃣ Test Cases Table**

| Input      | Output     |
| ---------- | ---------- |
| 07-11-2020 | 07/11/2020 |
| 12-10-2222 | 12/10/2222 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `replace()` is your best friend for formatting
- No loops needed
- Keep transformations simple

---

## **1️⃣6️⃣ Real-Life Application**

- Date formatting
- Log cleanup
- Data standardization

---

## **1️⃣7️⃣ Practice Questions**

1. Replace spaces with underscores
2. Replace commas with semicolons
3. Convert `:` to `-`

---

## **1️⃣8️⃣ Result**

The program correctly converts the date format.

---

## **1️⃣9️⃣ Conclusion**

Another classic **string formatting** problem mastered.

---
