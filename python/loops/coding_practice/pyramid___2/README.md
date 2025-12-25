# ✅ **Pyramid – 2**

---

## **1️⃣ Question**

Given a number **N**, print a **Pyramid of N rows** using numbers.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from 1 to N
- Print spaces for centering
- Print numbers with space

---

## **3️⃣ Objective**

To print a **number pyramid** using a **single for loop** and **string repetition**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- pyramid centering using spaces
- repeating numbers using strings
- building patterns without nested loops

---

## **5️⃣ Theory**

For a number pyramid:

- Total rows = **N**
- For each row **i**:

  - Leading spaces = **N − i**
  - Numbers printed = **2 × i − 1**
  - Each number has a space after it

Example for **N = 5**:

```
        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from 1 to N
3. For each row:

   - Print `"  "` (two spaces) `(N − row)` times
   - Print `row` followed by space `(2 × row − 1)` times

4. Print one line per row

---

## **7️⃣ Method**

Use:

- for loop
- string repetition
- single `print()` per row

---

## **8️⃣ Constraints**

- N ≥ 1
- Space after every number

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Missing spaces after numbers
❌ Wrong number of leading spaces

---

## **🔟 Complexity**

Time: **O(N²)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code (NO nested loops – FROM WHAT YOU’VE LEARNED)**

```python
N = int(input())

for row in range(1, N + 1):
    print("  " * (N - row) + (str(row) + " ") * (2 * row - 1))
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
```

### Output

```
        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
```

---

## **1️⃣3️⃣ Dry Run**

For **N = 3**

- row = 1 → `"  " * 2 + "1 " * 1`
- row = 2 → `"  " * 1 + "2 " * 3`
- row = 3 → `"  " * 0 + "3 " * 5`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output          |
| ----: | --------------- |
|     1 | `1`             |
|     3 | correct pyramid |
|     5 | matches sample  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Centering comes from **double spaces**
- `(2 × row − 1)` controls pyramid width
- String repetition replaces nested loops
- Fully beginner-safe ✅

---

## **1️⃣6️⃣ Result**

The program correctly prints a **number pyramid** exactly as shown in **NxtWave**.

---

## **1️⃣7️⃣ Conclusion**

This is the **cleanest, simplest, and correct solution** for **Pyramid – 2**,
written **strictly from what you’ve learned** 💯

---
