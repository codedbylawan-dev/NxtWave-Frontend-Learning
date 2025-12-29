# ✅ **Strip Spaces**

---

## **1️⃣ Question**

Given a string, write a program that **removes the leading and trailing spaces** from the string and prints the modified string.

---

## **1️⃣.5️⃣ Category**

String → String Methods

---

## **2️⃣ Outline**

- Read the input string
- Remove leading and trailing spaces
- Print the modified string

---

## **3️⃣ Objective**

To clean a string by removing **extra spaces from both ends**.

---

## **4️⃣ Purpose**

This problem helps in learning:

- handling messy user input
- using the `strip()` string method
- producing clean output

---

## **5️⃣ Theory**

Python provides a built-in string method **`strip()`**.

- `strip()` removes spaces from the **beginning and end** of a string
- It does **not** affect spaces in the middle

Example:

```python
"   hello world   ".strip()
```

Result → `"hello world"`

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Apply `strip()` to the string
3. Store the result
4. Print the cleaned string

---

## **7️⃣ Method**

- Input
- `strip()` method
- Output

---

## **8️⃣ Constraints**

- Input may contain leading and trailing spaces
- Output must contain no spaces at both ends

---

## **9️⃣ Common Mistakes**

❌ Using loops unnecessarily
❌ Trying to remove spaces manually
❌ Forgetting that `strip()` returns a new string

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

cleaned = s.strip()

print(cleaned)
```

---

## **1️⃣2️⃣ Example**

### Input

```
   practice
```

### Output

```
practice
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"   Tech Foundations   "`
After `strip()` → `"Tech Foundations"`
Printed result → `Tech Foundations`

---

## **1️⃣4️⃣ Test Cases Table**

| Input                   | Output           |
| ----------------------- | ---------------- |
| `"   practice   "`      | practice         |
| `"  Tech Foundations "` | Tech Foundations |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `strip()` is made exactly for this problem
- Never try to manually remove spaces
- Always clean input before processing

---

## **1️⃣6️⃣ Real-Life Application**

- Cleaning user input
- Preparing text for comparison
- Formatting data for storage

---

## **1️⃣7️⃣ Practice Questions**

1. Remove only leading spaces
2. Remove only trailing spaces
3. Remove dots and commas from both ends

---

## **1️⃣8️⃣ Result**

The program correctly removes **leading and trailing spaces** from the input.

---

## **1️⃣9️⃣ Conclusion**

This is a fundamental **input-cleaning pattern** you will use constantly in real programs.

---
