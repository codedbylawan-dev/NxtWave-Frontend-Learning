# 🧩 **Shuffle String**

---

## **1️⃣ Question**

Given a string **S** and **N indices** (where `N = len(S)`),
print a new string formed by taking characters of **S** in the order of the given indices.

---

## **2️⃣ Category**

**Strings → Indexing → Rebuilding Strings**

---

## **3️⃣ Outline**

- Read string **S**
- Find its length **N**
- Initialize empty string `result`
- Read **N indices**
- For each index:

  - Append `S[index]` to `result`

- Print `result`

---

## **4️⃣ Objective**

Learn how to **reconstruct a string** using index control.

---

## **5️⃣ Purpose**

This builds:

- Index manipulation
- Dynamic string building
- Input-driven transformation

---

## **6️⃣ Theory**

A string can be **rebuilt** by selecting characters in any order using indices.

---

## **7️⃣ Step-by-Step Explanation**

1. Read **S**
2. Compute **N = len(S)**
3. Set `result = ""`
4. Repeat **N times**:

   - Read an integer `idx`
   - Append `S[idx]` to `result`

5. Print `result`

---

## **8️⃣ Method**

Single loop + string concatenation.

---

## **9️⃣ Constraints**

- Number of indices = length of string
- All indices are valid

---

## **🔟 Common Mistakes**

- Forgetting to initialize `result`
- Reading fewer or extra indices
- Printing inside the loop instead of after building

---

## **1️⃣1️⃣ Complexity**

- **Time:** `O(N)`
- **Space:** `O(N)`

---

## **1️⃣2️⃣ Code**

```python
s = input()
n = len(s)

result = ""

for i in range(n):
    idx = int(input())
    result = result + s[idx]

print(result)
```

---

## **1️⃣3️⃣ Example**

### Input

```
goindc
5
1
4
2
3
0
```

### Output

```
coding
```

---

## **1️⃣4️⃣ Dry Run**

| Step | Index | Character | Result |
| ---- | ----- | --------- | ------ |
| 1    | 5     | c         | c      |
| 2    | 1     | o         | co     |
| 3    | 4     | d         | cod    |
| 4    | 2     | i         | codi   |
| 5    | 3     | n         | codin  |
| 6    | 0     | g         | coding |

---

## **1️⃣5️⃣ Test Cases Table**

| Input            | Output |
| ---------------- | ------ |
| goindc + indices | coding |
| eimag + indices  | image  |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- Indices can completely reorder data
- You control structure using simple tools
- This is core algorithm thinking

---

## **1️⃣7️⃣ Real-Life Application**

Used in:

- Encryption
- Data transformation
- Shuffling algorithms

---

## **1️⃣8️⃣ Practice Questions**

1. Reverse the shuffle.
2. Validate if given shuffle is correct.
3. Shuffle only vowels.

---

## **1️⃣9️⃣ Result**

You successfully rebuilt a string using index logic.

---

## **2️⃣0️⃣ Conclusion**

This problem is a foundation for **data rearrangement algorithms**.

---
