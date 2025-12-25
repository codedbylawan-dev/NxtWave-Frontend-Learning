# ✅ **Inverted Pyramid**

---

## **1️⃣ Question**

Given a number **N**, print an **Inverted Pyramid of N rows** using stars (`*`).

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from N to 1
- Print leading spaces
- Print stars

---

## **3️⃣ Objective**

To print an **inverted pyramid pattern** using **one for loop** and **string repetition**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- inverted pattern logic
- center alignment using spaces
- reducing stars row by row

---

## **5️⃣ Theory**

For an **Inverted Pyramid**:

- Total rows = **N**
- For each row:

  - **Leading spaces** = `N - row`
  - **Stars** = `2 × row - 1`

Example for **N = 4**:

```
*******
 *****
  ***
   *
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from `N` down to `1`
3. For each row:

   - Print `" "` repeated `(N - row)` times
   - Print `"*"` repeated `(2 × row - 1)` times

4. Print one row at a time

---

## **7️⃣ Method**

Use:

- reverse `for` loop
- string repetition
- single `print()` per row

---

## **8️⃣ Constraints**

- N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Printing wrong number of stars
❌ Missing center alignment

---

## **🔟 Complexity**

Time: **O(N²)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code (NO nested loops – FINAL)**

```python
N = int(input())

for row in range(N, 0, -1):
    spaces = " " * (N - row)
    stars = "*" * (2 * row - 1)
    print(spaces + stars)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
*******
 *****
  ***
   *
```

---

## **1️⃣3️⃣ Dry Run**

For **N = 3**

- row = 3 → spaces = 0, stars = 5 → `*****`
- row = 2 → spaces = 1, stars = 3 → ` ***`
- row = 1 → spaces = 2, stars = 1 → `  *`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Pattern           |
| ----: | ------------------------ |
|     1 | `*`                      |
|     4 | matches sample           |
|     9 | correct inverted pyramid |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Inverted pyramid shrinks stars every row
- Alignment comes from **leading spaces**
- `2 × row − 1` controls pyramid width

---

## **1️⃣6️⃣ Result**

The program prints the **exact inverted pyramid** shown in NxtWave ✅

---

## **1️⃣7️⃣ Conclusion**

This is the **cleanest, simplest, and correct solution** for **Inverted Pyramid**, fully aligned with **your current learning stage** 💯

---
