# ✅ **Strip Stars**

---

## **1️⃣ Question**

Given a string, write a program that **removes the leading and trailing stars (`*`)** from the string and prints the modified string.

---

## **1️⃣.5️⃣ Category**

String → String Methods

---

## **2️⃣ Outline**

- Read the input string
- Remove leading and trailing `*` characters
- Print the modified string

---

## **3️⃣ Objective**

To clean a string by removing **extra stars from both ends**.

---

## **4️⃣ Purpose**

This problem helps in learning:

- custom trimming of characters
- correct usage of `strip()` with parameters
- string cleaning techniques

---

## **5️⃣ Theory**

The `strip()` method can remove **specific characters** from both ends.

```python
text.strip("*")
```

Removes only `*` from the **start and end**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Apply `strip("*")` to the string
3. Store the result
4. Print the cleaned string

---

## **7️⃣ Method**

- Input
- `strip("*")` method
- Output

---

## **8️⃣ Constraints**

- Input may contain stars at the beginning and end
- Output must contain no stars at both ends

---

## **9️⃣ Common Mistakes**

❌ Using loops unnecessarily
❌ Trying to remove stars manually
❌ Forgetting that `strip()` returns a new string

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

cleaned = s.strip("*")

print(cleaned)
```

---

## **1️⃣2️⃣ Example**

### Input

```
****python****
```

### Output

```
python
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"**ccb4.0********************"`
After `strip("*")` → `"ccb4.0"`
Printed result → `ccb4.0`

---

## **1️⃣4️⃣ Test Cases Table**

| Input                      | Output |
| -------------------------- | ------ |
| `****python****`           | python |
| `**ccb4.0****************` | ccb4.0 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `strip()` works for any character, not just spaces
- Always clean before processing
- Do not manually loop when Python already solved it

---

## **1️⃣6️⃣ Real-Life Application**

- Cleaning formatted input
- Removing markers from logs
- Preprocessing data

---

## **1️⃣7️⃣ Practice Questions**

1. Remove `#` from both ends
2. Remove `@` from both ends
3. Remove both `*` and `#` from both ends

---

## **1️⃣8️⃣ Result**

The program correctly removes **leading and trailing stars**.

---

## **1️⃣9️⃣ Conclusion**

Another core **input-cleaning pattern** mastered.

---
