# ✅ **Secured URL**

---

## **1️⃣ Question**

Given a URL, write a program that checks if the URL is **secured**.

Print **True** if the URL is secured. Otherwise, print **False**.

---

## **1️⃣.5️⃣ Category**

String → String Methods → Validation

---

## **2️⃣ Outline**

- Read the input string
- Check if the URL starts with `https://`
- Print the result

---

## **3️⃣ Objective**

To verify whether a given URL is **secure**.

---

## **4️⃣ Purpose**

This problem helps in learning:

- prefix checking in strings
- usage of the `startswith()` method
- boolean output logic

---

## **5️⃣ Theory**

Python provides the method **`startswith()`**.

```python
text.startswith("https://")
```

Returns **True** if the string begins with `"https://"`.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input URL
2. Apply `startswith("https://")`
3. Store the result
4. Print the result

---

## **7️⃣ Method**

- Input
- `startswith()`
- Output

---

## **8️⃣ Constraints**

- Input is always a string
- Output must be **True** or **False**

---

## **9️⃣ Common Mistakes**

❌ Using loops unnecessarily
❌ Searching inside the string instead of checking prefix
❌ Checking only for `"https"` instead of `"https://"`

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
url = input()

result = url.startswith("https://")

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
https://docs.google.com
```

### Output

```
True
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"learning.ccbp.in"`
`startswith("https://")` → False
Printed → `False`

---

## **1️⃣4️⃣ Test Cases Table**

| Input                                              | Output |
| -------------------------------------------------- | ------ |
| [https://docs.google.com](https://docs.google.com) | True   |
| learning.ccbp.in                                   | False  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always check **exact prefix** for validation
- `startswith()` is the correct tool
- No need for loops

---

## **1️⃣6️⃣ Real-Life Application**

- Website security validation
- Link filtering
- URL verification

---

## **1️⃣7️⃣ Practice Questions**

1. Check if an email ends with `.com`
2. Check if a file name starts with `img_`
3. Check if a string starts with a digit

---

## **1️⃣8️⃣ Result**

The program correctly identifies whether the URL is **secured**.

---

## **1️⃣9️⃣ Conclusion**

This is a critical **string validation** pattern used constantly in real systems.

---
