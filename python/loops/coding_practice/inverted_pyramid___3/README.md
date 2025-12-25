# ✅ **Inverted Pyramid – 3**

---

## **1️⃣ Question**

Given a number **N**, print an **Inverted Pyramid of N rows** using:

- **Pluses (`+`) in the first row**
- **Stars (`*`) in the remaining rows**

There should be a **space after every symbol**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from 0 to N−1
- Print leading spaces
- Decide symbol (`+` or `*`)
- Print symbols

---

## **3️⃣ Objective**

To print an **inverted pyramid** using **one loop** and a **simple condition**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- conditional pattern changes
- inverted pyramids
- symbol switching using `if`

---

## **5️⃣ Theory**

For an inverted pyramid:

- Total rows = **N**
- For each row `i`:

  - Leading spaces = `i`
  - Symbols = `N - i`
  - First row → `+`
  - Remaining rows → `*`

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from `i = 0` to `N - 1`
3. Print `" "` repeated `i` times
4. If `i == 0`:

   - Print `"+ "` repeated `N` times

5. Else:

   - Print `"* "` repeated `(N - i)` times

---

## **7️⃣ Method**

Use:

- one `for` loop
- `if` condition
- string repetition

---

## **8️⃣ Constraints**

- `N ≥ 1`
- Space after every symbol

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Forgetting condition for first row
❌ Missing space after symbols

---

## **🔟 Complexity**

- **Time:** `O(N²)`
- **Space:** `O(1)`

---

## **1️⃣1️⃣ Code (ONE LOOP + CONDITION — YOUR LEARNING STYLE)**

```python
N = int(input())

for i in range(N):
    spaces = " " * i
    if i == 0:
        symbols = "+ " * N
    else:
        symbols = "* " * (N - i)
    print(spaces + symbols)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
+ + + +
 * * *
  * *
   *
```

---

## **1️⃣3️⃣ Dry Run (N = 3)**

- i = 0 → `"+ + + "`
- i = 1 → `" * * "`
- i = 2 → `"  * "`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Pattern   |
| ----: | ---------------- |
|     1 | `+`              |
|     3 | inverted pyramid |
|     4 | matches sample   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- First row handled using `if`
- Inverted shape from decreasing symbols
- One loop is enough

---

## **1️⃣6️⃣ Real-Life Application**

- Console formatting
- Conditional layouts
- Pattern logic mastery

---

## **1️⃣7️⃣ Practice Questions**

1. Replace `*` with `#`
2. Print last row as `+`
3. Print numbers instead of symbols

---

## **1️⃣8️⃣ Result**

The program correctly prints an **Inverted Pyramid with mixed symbols**.

---

## **1️⃣9️⃣ Conclusion**

This solution is **100% aligned with your learning**,
uses **only one loop**, and **matches the output exactly** ✅

---
