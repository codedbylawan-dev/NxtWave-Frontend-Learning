# 🧩 **Print Characters**

---

## **1️⃣ Question**

Given a string **S** and **N indices**, where **N = length of the string**,
print the character of the string present at each given index.

---

## **2️⃣ Category**

**Strings → Indexing → Input Processing**

---

## **3️⃣ Outline**

- Read string **S**
- Read **N = len(S)**
- Read **N indices (one per line)**
- For each index:

  - Print `S[index]`

---

## **4️⃣ Objective**

Learn how to access characters of a string using **index positions** from user input.

---

## **5️⃣ Purpose**

This builds mastery over:

- String indexing
- Dynamic input handling
- Mapping inputs to string positions

---

## **6️⃣ Theory**

A string is an ordered sequence of characters.
Each character has a position called an **index**.

Indexing starts from **0**.

Example:
`tarc`

| Index | 0   | 1   | 2   | 3   |
| ----- | --- | --- | --- | --- |
| Char  | t   | a   | r   | c   |

Access using:
`S[index]`

---

## **7️⃣ Step-by-Step Explanation**

1. Take the input string.
2. Its length tells how many indices will follow.
3. For each index:

   - Extract the character from the string.
   - Print it on a new line.

---

## **8️⃣ Method**

Use **string indexing** inside a loop.

---

## **9️⃣ Constraints**

- Index values are always valid.
- Exactly **N** indices are provided.

---

## **🔟 Common Mistakes**

- Forgetting that indexing starts at **0**
- Printing the index instead of the character
- Taking all indices in one line instead of separate lines

---

## **1️⃣1️⃣ Complexity**

- **Time:** `O(N)`
- **Space:** `O(1)`

---

## **1️⃣2️⃣ Code**

```python
s = input()
n = len(s)

for i in range(n):
    index = int(input())
    print(s[index])
```

---

## **1️⃣3️⃣ Example**

### **Input**

```
tarc
3
1
2
0
```

### **Output**

```
c
a
r
t
```

---

## **1️⃣4️⃣ Dry Run**

String: `tarc`

Indices: `3, 1, 2, 0`

| Index | Character |
| ----- | --------- |
| 3     | c         |
| 1     | a         |
| 2     | r         |
| 0     | t         |

Printed in order.

---

## **1️⃣5️⃣ Test Cases Table**

| Input             | Output      |
| ----------------- | ----------- |
| `tarc 3 1 2 0`    | `c a r t`   |
| `eesnv 2 0 4 1 3` | `s e v e n` |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- Indexing gives **direct access** to characters.
- User input can dynamically control what part of the string you use.
- This problem trains **precision thinking**.

---

## **1️⃣7️⃣ Real-Life Application**

Used in:

- Password rules
- Data extraction
- Encryption systems
- Parsing user commands

---

## **1️⃣8️⃣ Practice Questions**

1. Print characters in reverse order of given indices.
2. Print only the characters whose indices are even.
3. Replace characters at given indices with `*`.

---

## **1️⃣9️⃣ Result**

You now control string positions using external input.

That’s a serious backend skill.

---

## **2️⃣0️⃣ Conclusion**

This problem upgrades you from “I know strings” to
“I control data using position logic.”

Exactly what real programs do.

---
