# ✅ **Python File**

---

## **1️⃣ Question**

Given a file name with extension, write a program to check whether the file is a **Python file**.

Print **True** if the file is a Python file. Otherwise, print **False**.

---

## **1️⃣.5️⃣ Category**

String → String Methods → Validation

---

## **2️⃣ Outline**

- Read the input string
- Check if the file name ends with `.py`
- Print the result

---

## **3️⃣ Objective**

To determine whether a given file name represents a **Python file**.

---

## **4️⃣ Purpose**

This problem helps in learning:

- suffix checking in strings
- usage of the `endswith()` method
- boolean validation logic

---

## **5️⃣ Theory**

Python provides the method **`endswith()`**.

```python
filename.endswith(".py")
```

Returns **True** if the string ends with `.py`.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the file name
2. Apply `endswith(".py")`
3. Store the result
4. Print the result

---

## **7️⃣ Method**

- Input
- `endswith()`
- Output

---

## **8️⃣ Constraints**

- Input is a string
- Output must be **True** or **False**

---

## **9️⃣ Common Mistakes**

❌ Using loops unnecessarily
❌ Checking for `"py"` instead of `".py"`
❌ Searching anywhere instead of checking the end

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
file_name = input()

result = file_name.endswith(".py")

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
add_numbers.py
```

### Output

```
True
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"card.html"`
`endswith(".py")` → False
Printed → `False`

---

## **1️⃣4️⃣ Test Cases Table**

| Input          | Output |
| -------------- | ------ |
| add_numbers.py | True   |
| card.html      | False  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always use `endswith()` for extension checks
- Exact matching prevents false positives
- Simple checks are the most reliable

---

## **1️⃣6️⃣ Real-Life Application**

- File type validation
- Upload filtering
- Project file scanning

---

## **1️⃣7️⃣ Practice Questions**

1. Check if a file is an image (`.jpg`)
2. Check if a file is a text file (`.txt`)
3. Check if a file is a video (`.mp4`)

---

## **1️⃣8️⃣ Result**

The program correctly identifies whether the file is a **Python file**.

---

## **1️⃣9️⃣ Conclusion**

This is a fundamental **file validation** pattern you will reuse everywhere.

---
