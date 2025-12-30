# 🧩 **Word Triangle**

---

## **1️⃣ Question**

Given a word **S**, print the letters of the word on **N lines**,
where **N = length of the word**, forming a growing pattern.

---

## **2️⃣ Category**

**Strings → Slicing → Pattern Printing**

---

## **3️⃣ Outline**

- Read word **S**
- For each position `i` from `1` to `len(S)`:

  - Print first `i` characters of the word

---

## **4️⃣ Objective**

Understand how to build patterns using **string slicing**.

---

## **5️⃣ Purpose**

This teaches:

- Progressive string building
- Controlled pattern generation
- Using loop index as a slicing boundary

---

## **6️⃣ Theory**

A string slice:

```
S[:i]
```

means:
start from index `0` and go up to `i-1`.

So when `i` increases, the printed part grows.

---

## **7️⃣ Step-by-Step Explanation**

1. Read the word.
2. Loop from `1` to `length of word`.
3. On each loop:

   - Print the slice `S[:i]`.

---

## **8️⃣ Method**

Use **for loop + slicing**.

---

## **9️⃣ Constraints**

- The word contains only characters.
- Print exactly **N** lines.

---

## **🔟 Common Mistakes**

- Starting loop from `0` (prints empty line first)
- Using `S[i]` instead of `S[:i]`
- Forgetting newline after each print

---

## **1️⃣1️⃣ Complexity**

- **Time:** `O(N²)`
- **Space:** `O(1)`

---

## **1️⃣2️⃣ Code**

```python
s = input()

for i in range(1, len(s) + 1):
    print(s[:i])
```

---

## **1️⃣3️⃣ Example**

### **Input**

```
Rahul
```

### **Output**

```
R
Ra
Rah
Rahu
Rahul
```

---

## **1️⃣4️⃣ Dry Run**

Word: `Rahul`

| i   | s[:i] |
| --- | ----- |
| 1   | R     |
| 2   | Ra    |
| 3   | Rah   |
| 4   | Rahu  |
| 5   | Rahul |

---

## **1️⃣5️⃣ Test Cases Table**

| Input     | Output                                                |
| --------- | ----------------------------------------------------- |
| Rahul     | R Ra Rah Rahu Rahul                                   |
| Workbench | W Wo Wor Work Workb Workbe Workben Workbenc Workbench |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- Slicing is more powerful than indexing for pattern problems.
- This problem blends **strings + loops + slicing**.
- Core skill for UI text rendering and formatting logic.

---

## **1️⃣7️⃣ Real-Life Application**

Used in:

- Typing animations
- Progressive loaders
- Visual text effects
- Teaching tools

---

## **1️⃣8️⃣ Practice Questions**

1. Print the triangle in reverse.
2. Print only odd-length lines.
3. Print the triangle using a while loop.

---

## **1️⃣9️⃣ Result**

You now create **structured string patterns** using clean logic.

---

## **2️⃣0️⃣ Conclusion**

This is where basic string knowledge becomes **visual programming skill**.

---
