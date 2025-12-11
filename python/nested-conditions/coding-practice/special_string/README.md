# ✅ **Special String**

---

## **1️⃣ Question**

Given a string **S**, check whether the following conditions are satisfied:

1. The **first three characters** of S are **"NXT"**
2. The **remaining characters** form a **number** that is divisible by **2 or 7**

If both conditions are satisfied → print **"Special String"**
Otherwise → print **"Not a Special String"**.

---

## **1.5️⃣ Category**

Strings → Slicing → Conditions → Divisibility

---

## **2️⃣ Outline**

- Read S
- Extract first three characters
- Extract remaining substring
- Convert remaining substring into a number
- Check if first part equals "NXT"
- Check if number divisible by 2 or 7
- If both checks true → print Special String
- Else → print Not a Special String

---

## **3️⃣ Objective**

To verify a string pattern and check divisibility of the numeric portion.

---

## **4️⃣ Purpose**

To practice string slicing, number conversion, and condition checking.

---

## **5️⃣ Theory**

String slicing:

[
S[0:3] \text{ → first 3 characters}
]
[
S[3:] \text{ → remaining characters}
]

Conditions:

1.

[
S[0:3] = "NXT"
]

2.

[
\text{num} = \text{int}(S[3:])
]
[
\text{num} % 2 = 0 \quad \text{or} \quad \text{num} % 7 = 0
]

Final condition:

[
\text{Special String if both are true}
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read input string S
2. Extract first 3 characters
3. Extract remaining characters
4. Convert remaining characters to integer
5. Check if prefix equals "NXT"
6. Check if number divisible by 2 or 7
7. If both conditions true → print Special String
8. Else → print Not a Special String

---

## **7️⃣ Method**

- Use string indexing and slicing
- Convert substring using `int()`
- Use `%` for divisibility
- Combine conditions with AND and OR

---

## **8️⃣ Constraints**

- Remaining part must represent a valid number
- S length ≥ 4
- Output must match exactly

---

## **9️⃣ Common Mistakes**

❌ Forgetting to convert the substring to integer
❌ Using wrong slice positions
❌ Checking divisibility with AND instead of OR
❌ Mistyping “NXT”

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
S = input()

prefix = S[0:3]
remaining = int(S[3:])

cond1 = (prefix == "NXT")
cond2 = (remaining % 2 == 0 or remaining % 7 == 0)

if cond1 and cond2:
    print("Special String")
else:
    print("Not a Special String")
```

---

## **1️⃣2️⃣ Example**

### Input

```
NXT1234
```

### Output

```
Special String
```

---

## **1️⃣3️⃣ Dry Run**

| Step | S       | prefix | remaining | remaining % 2 | remaining % 7 | Conditions Result | Output               |
| ---- | ------- | ------ | --------- | ------------- | ------------- | ----------------- | -------------------- |
| 1    | NXT1234 | NXT    | 1234      | 0             | 2             | True AND True     | Special String       |
| 2    | PRA49   | PRA    | 49        | 1             | 0             | False AND True    | Not a Special String |

---

## **1️⃣4️⃣ Test Cases Table**

| S       | prefix | remaining | divisible? | Output               |
| ------- | ------ | --------- | ---------- | -------------------- |
| NXT1234 | NXT    | 1234      | Yes        | Special String       |
| PRA49   | PRA    | 49        | Yes        | Not a Special String |
| NXT14   | NXT    | 14        | Yes        | Special String       |
| NXT15   | NXT    | 15        | No         | Not a Special String |
| NXT7    | NXT    | 7         | Yes        | Special String       |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Slicing helps isolate parts of strings
- Use int() to convert numeric substrings
- Combined AND + OR conditions help check multi-step logic

---

## **1️⃣6️⃣ Real-Life Application**

- Validating formatted codes (prefix + number)
- Checking serial numbers
- Pattern matching in IDs
- Processing string-based numeric data

---

## **1️⃣7️⃣ Practice Questions**

1. Check if a string starts with “ABC” and remaining part divisible by 3.
2. Print “Valid” if string ends with a number divisible by 5.
3. Given “CODExxxx”, check if xxxx is divisible by 4.

---

## **1️⃣8️⃣ Result**

The program identifies whether the string meets both prefix and number-divisibility conditions.

---

## **1️⃣9️⃣ Conclusion**

This problem builds strong understanding of string slicing and numeric condition checks, essential for structured string processing tasks.

---
