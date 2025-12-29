# ✅ **First Part or Last Part**

---

## **1️⃣ Question**

Given two strings **S1** and **S2**, check whether **S2** is present at the **beginning** or **ending** of **S1**.

Print **True** if **S2** is either at the start or end of **S1**.
Otherwise, print **False**.

---

## **1️⃣.5️⃣ Category**

String → Comparison → Conditional Checking

---

## **2️⃣ Outline**

- Read string `S1`
- Read string `S2`
- Check if `S1` starts with `S2`
- Check if `S1` ends with `S2`
- Print result

---

## **3️⃣ Objective**

To determine whether a substring appears at the **start** or **end** of a string.

---

## **4️⃣ Purpose**

This problem trains you in:

- string comparison
- prefix & suffix logic
- decision making

---

## **5️⃣ Theory**

A string:

- **starts with** a substring if its first characters match
- **ends with** a substring if its last characters match

Both checks must be performed.

---

## **6️⃣ Step-by-Step Explanation**

1. Take inputs `S1` and `S2`
2. Compare beginning of `S1` with `S2`
3. Compare ending of `S1` with `S2`
4. If any one is true, print `True`
5. Otherwise print `False`

---

## **7️⃣ Method**

- Input reading
- String slicing
- Conditional check

---

## **8️⃣ Constraints**

- Case-sensitive comparison
- No modification of strings allowed

---

## **9️⃣ Common Mistakes**

❌ Forgetting to check the ending
❌ Mixing uppercase and lowercase
❌ Printing strings instead of boolean values

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
s1 = input()
s2 = input()

if s1[:len(s2)] == s2 or s1[-len(s2):] == s2:
    print(True)
else:
    print(False)
```

---

## **1️⃣2️⃣ Example**

### Input

```
Manager
Man
```

### Output

```
True
```

---

## **1️⃣3️⃣ Dry Run**

`s1 = "helicopter"`
`s2 = "cop"`

Start check: `hel` ≠ `cop`
End check: `ter` ≠ `cop`

Result → **False**

---

## **1️⃣4️⃣ Test Cases Table**

| S1         | S2  | Output |
| ---------- | --- | ------ |
| Manager    | Man | True   |
| helicopter | cop | False  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- This logic appears in search engines, parsers, and validation systems
- Prefix and suffix checks are core string skills

---

## **1️⃣6️⃣ Real-Life Application**

- URL validation
- File extension checking
- Command parsing

---

## **1️⃣7️⃣ Practice Questions**

1. Check if `S2` appears **anywhere** in `S1`
2. Count how many times `S2` appears
3. Replace the prefix if it matches

---

## **1️⃣8️⃣ Result**

The program correctly identifies whether `S2` appears at the start or end of `S1`.

---

## **1️⃣9️⃣ Conclusion**

Mastering these comparisons makes you efficient at real-world text processing.

---
