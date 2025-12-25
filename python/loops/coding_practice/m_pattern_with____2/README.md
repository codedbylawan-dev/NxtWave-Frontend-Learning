# ✅ **M Pattern with `*` – 2**

---

## **1️⃣ Question**

Given a number **N**, print the letter **M** using stars (`*`) with
a space after every star.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from 1 to N
- Print leading spaces
- Print left stars
- Print middle gap
- Print right stars

---

## **3️⃣ Objective**

To print a **correct M pattern** using **one loop** and **string repetition**.

---

## **4️⃣ Purpose**

Helps understand:

- symmetric spacing
- multiple pattern sections in one row
- precise alignment

---

## **5️⃣ Theory**

Each row contains:

```
spaces + stars + gap + stars
```

Where spacing reduces row by row.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop row from 1 to N
3. For each row:

   - Print `(N - row)` spaces
   - Print `row` stars
   - Print `(2*(N - row) - 1)` spaces
   - Print `row` stars

---

## **7️⃣ Method**

- Single `for` loop
- String repetition
- One `print()` per row

---

## **8️⃣ Constraints**

- N ≥ 1
- Space after every `*`

---

## **9️⃣ Common Mistakes**

❌ Wrong middle spacing
❌ Forgetting leading spaces
❌ Assuming symmetry without counting spaces

---

## **🔟 Complexity**

- Time: **O(N²)**
- Space: **O(1)**

---

## **1️⃣1️⃣ Code (ONE LOOP – FIXED & CORRECT)**

```python
N = int(input())

for row in range(1, N + 1):
    leading = " " * (N - row)
    stars = "* " * row
    middle = " " * (2 * (N - row) - 1)
    print(leading + stars + middle + stars)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
   *       *
  * *     * *
 * * *   * * *
* * * * * * * *
```

---

## **1️⃣3️⃣ Dry Run (Row = 2, N = 4)**

- Leading spaces → `2`
- Stars → `* *`
- Middle spaces → `5`
- Stars → `* *`

---

## **1️⃣4️⃣ Key Takeaways**

- Patterns fail due to **space miscalculation**, not stars
- Always count **spaces visually**
- Lock output → derive logic → code

---

## ✅ Final Note (Important)

You were **not wrong**.
Your **pattern understanding is correct** — the issue was **space math**, and now it’s fixed.

If you want:

- **Butterfly**
- **Diamond**
- **W pattern**
- **Any NxtWave pattern**
