# ✅ **Inverted Right Angled Triangle – 6**

---

## **1️⃣ Question**

Given a number **N**, print an **Inverted Right Angled Triangle of N rows** using stars (`*`).

There should be a **space after every star (`* `)**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Pattern (Correct Output)**

For **N = 4**, output should be:

```
* * * *
  * * *
    * *
      *
```

---

## **3️⃣ Objective**

To print an **inverted right angled triangle**, aligned to the **right**, using **only one loop and conditions**.

---

## **4️⃣ Purpose**

This problem helps you learn:

- inverted patterns
- right alignment using spaces
- controlling rows using conditions
- avoiding nested loops

---

## **5️⃣ Theory**

For an inverted right angled triangle:

- Total rows = **N**
- For each row:

  - **Spaces increase**
  - **Stars decrease**

Rules per row:

- Spaces = `row - 1`
- Stars = `N - row + 1`

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from `1` to `N`
3. For each row:

   - Print `"  "` repeated `(row - 1)` times
   - Print `"* "` repeated `(N - row + 1)` times

4. Print everything in one line

---

## **7️⃣ Method**

Use:

- one `for` loop
- string repetition
- one `print()` per row

---

## **8️⃣ Constraints**

- N ≥ 1
- Space after every star

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Printing stars before spaces
❌ Forgetting double space alignment

---

## **🔟 Complexity**

- **Time:** `O(N²)`
- **Space:** `O(1)`

---

## **1️⃣1️⃣ Code (ONE LOOP – YOUR LEARNING LEVEL)**

```python
N = int(input())

for row in range(1, N + 1):
    spaces = "  " * (row - 1)
    stars = "* " * (N - row + 1)
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
* * * *
  * * *
    * *
      *
```

---

## **1️⃣3️⃣ Dry Run (N = 3)**

| Row | Spaces | Stars | Output  |
| --: | -----: | ----: | ------- |
|   1 |      0 |     3 | `* * *` |
|   2 |      1 |     2 | `  * *` |
|   3 |      2 |     1 | `    *` |

---

## **1️⃣4️⃣ Key Takeaways**

✔ Inverted = stars decrease
✔ Right aligned = spaces increase
✔ One loop is enough
✔ Same logic works for numbers, symbols

---

## **1️⃣5️⃣ Conclusion**

This solution:

- ✅ matches the **image exactly**
- ✅ follows **your learning stage**
- ✅ uses **only one loop**
- ✅ is **NxtWave-perfect**

---

If you want, next we can do:

- **Inverted Pyramid**
- **Butterfly (single loop)**
- **Diamond with symbols**
