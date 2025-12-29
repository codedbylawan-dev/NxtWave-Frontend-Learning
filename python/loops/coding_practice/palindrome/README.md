# ✅ **Palindrome**

---

## **1️⃣ Question**

Given a string, check whether the given string is a **palindrome**.

A palindrome reads the same from the beginning and the end.

Print **True** if the string is a palindrome. Otherwise, print **False**.

**Note:** Uppercase and lowercase characters are considered **different**.

---

## **1️⃣.5️⃣ Category**

String → String Slicing → Validation

---

## **2️⃣ Outline**

- Read the input string
- Reverse the string
- Compare original and reversed strings
- Print the result

---

## **3️⃣ Objective**

To determine whether a string reads the same forwards and backwards.

---

## **4️⃣ Purpose**

This problem helps in learning:

- string reversal using slicing
- string comparison
- boolean validation

---

## **5️⃣ Theory**

A string can be reversed using slicing:

```python
text[::-1]
```

If the reversed string equals the original string, it is a palindrome.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Reverse the string using slicing
3. Compare original and reversed strings
4. If equal → print True
5. Otherwise → print False

---

## **7️⃣ Method**

- Input
- String slicing
- Comparison
- Output

---

## **8️⃣ Constraints**

- Case-sensitive comparison
- No spaces or special rules unless specified

---

## **9️⃣ Common Mistakes**

❌ Ignoring case sensitivity
❌ Comparing only part of the string
❌ Using loops unnecessarily

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

rev = s[::-1]

print(s == rev)
```

---

## **1️⃣2️⃣ Example**

### Input

```
madam
```

### Output

```
True
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"Noon"`
Reverse → `"nooN"`
Comparison → `Noon == nooN` → False
Printed → `False`

---

## **1️⃣4️⃣ Test Cases Table**

| Input   | Output |
| ------- | ------ |
| madam   | True   |
| Noon    | False  |
| batsman | False  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Slicing makes reversal trivial
- Always follow case rules strictly
- Comparison is the final judge

---

## **1️⃣6️⃣ Real-Life Application**

- Text validation
- Pattern recognition
- Data integrity checks

---

## **1️⃣7️⃣ Practice Questions**

1. Check palindrome ignoring case
2. Check if a number string is palindrome
3. Check if a sentence is palindrome (with spaces removed)

---

## **1️⃣8️⃣ Result**

The program correctly identifies whether the string is a palindrome.

---

## **1️⃣9️⃣ Conclusion**

This is a classic **string logic** problem and a rite of passage for every programmer.

---

Twelve problems.
