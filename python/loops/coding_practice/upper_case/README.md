# ✅ **Upper Case**

---

## **1️⃣ Question**

Given a string, write a program to check whether **all characters are in uppercase**.

Print **True** if they are, otherwise print **False**.

---

## **1️⃣.5️⃣ Category**

String → String Methods → Validation

---

## **2️⃣ Outline**

- Read the input string
- Check if all characters are uppercase
- Print the result

---

## **3️⃣ Objective**

To validate whether a string contains **only uppercase characters**.

---

## **4️⃣ Purpose**

This problem helps in learning:

- string validation
- usage of the `isupper()` method
- boolean output handling

---

## **5️⃣ Theory**

Python provides a string method **`isupper()`**.

- Returns **True** if all alphabet characters are uppercase
- Returns **False** otherwise

Examples:

```python
"IEEE".isupper()    # True
"CommuNiTy".isupper()  # False
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Apply `isupper()` to the string
3. Store the result
4. Print the result

---

## **7️⃣ Method**

- Input
- `isupper()`
- Output

---

## **8️⃣ Constraints**

- Input is a string
- Output must be **True** or **False**

---

## **9️⃣ Common Mistakes**

❌ Using loops unnecessarily
❌ Checking only one character
❌ Confusing `upper()` with `isupper()`

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

result = s.isupper()

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
IEEE
```

### Output

```
True
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"CommuNiTy"`
`isupper()` → False
Printed → `False`

---

## **1️⃣4️⃣ Test Cases Table**

| Input            | Output |
| ---------------- | ------ |
| IEEE             | True   |
| CommuNiTy        | False  |
| MALALA YouSaFZAI | False  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `isupper()` validates the **entire string**
- Used heavily in text validation
- Avoid confusing it with `upper()`

---

## **1️⃣6️⃣ Real-Life Application**

- Checking codes
- Validating formatted input
- Data normalization checks

---

## **1️⃣7️⃣ Practice Questions**

1. Check if all characters are lowercase
2. Check if a string contains only alphabets
3. Check if a string contains only digits

---

## **1️⃣8️⃣ Result**

The program correctly validates whether the string is **fully uppercase**.

---

## **1️⃣9️⃣ Conclusion**

Another important **string validation pattern** locked in.

---
