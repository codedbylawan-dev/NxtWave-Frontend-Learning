# ✅ **Inverted Right Angled Triangle – 5**

---

## **1️⃣ Question**

Given a number **N**, print an **Inverted Right Angled Triangle of N rows** using numbers.
There should be a **space after every number**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from N down to 1
- Print leading spaces
- Print numbers with a space

---

## **3️⃣ Objective**

To print a **right-aligned inverted triangle** using **numbers**, with **space after every number**, without nested loops.

---

## **4️⃣ Purpose**

This problem helps you understand:

- inverted pattern logic
- right alignment using spaces
- number repetition with spacing

---

## **5️⃣ Theory**

For each row:

- **Leading spaces** = `N - row` (each space is **two spaces** as per grid)
- **Number printed** = `row`
- **Count of numbers** = `row`
- **Each number followed by a space**

Example for **N = 4**:

```
4 4 4 4
  3 3 3
    2 2
      1
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from `N` to `1`
3. For each row:

   - Print `"  "` repeated `(N - row)` times
   - Print `"<row> "` repeated `row` times

4. Print in a single line

---

## **7️⃣ Method**

Use:

- reverse `for` loop
- string repetition
- single `print()`

---

## **8️⃣ Constraints**

- N ≥ 1
- Space after every number

---

## **9️⃣ Common Mistakes**

❌ Missing space after number
❌ Wrong number of leading spaces
❌ Using nested loops

---

## **🔟 Complexity**

Time: **O(N²)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code (FINAL – CORRECT FORMAT)**

```python
N = int(input())

for row in range(N, 0, -1):
    spaces = "  " * (N - row)
    numbers = (str(row) + " ") * row
    print(spaces + numbers)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
4 4 4 4
  3 3 3
    2 2
      1
```

---

## **1️⃣3️⃣ Dry Run**

For **N = 3**

- row = 3 → `"  "*0 + "3 3 3 "` → `3 3 3`
- row = 2 → `"  "*1 + "2 2 "` → `  2 2`
- row = 1 → `"  "*2 + "1 "` → `    1`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Pattern           |
| ----: | ------------------------ |
|     1 | `1`                      |
|     4 | matches sample           |
|     7 | correct inverted pyramid |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Two spaces `"  "` are used for alignment
- Space after every number is **mandatory**
- Reverse loop creates inversion

---

## **1️⃣6️⃣ Result**

The program prints the **exact pattern shown in NxtWave** ✅

---

## **1️⃣7️⃣ Conclusion**

This is the **correct, simple, beginner-safe solution**, fully aligned with **your learning stage** and **NxtWave expectations** 💯

---
