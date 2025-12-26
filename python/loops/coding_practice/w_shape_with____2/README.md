# ✅ **W Shape with \* – 2**

---

## **1️⃣ Question**

Given a number **N**, print the letter **W** of **N rows** using stars (`*`).

There should be a **space after every star (`* `)**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Pattern (Correct Output)**

For **N = 5**

```
* * * * * * * * *
 * * * * * * * *
  * * *   * * *
   * *     * *
    *       *
```

---

## **3️⃣ Objective**

To print the **W shape** using **one loop and conditions**, without nested loops.

---

## **4️⃣ Purpose**

This problem helps you understand:

- combining **two inverted triangles**
- spacing control using string repetition
- using **conditions inside a single loop**
- pattern symmetry

---

## **5️⃣ Theory**

For each row:

- Left side stars **decrease**
- Middle space **increases**
- Right side stars **decrease**
- Left indentation **increases**

Rules:

- Left spaces = `row - 1`
- Left stars = `N - row + 1`
- Middle spaces = `2 * (row - 1) + 1`
- Right stars = `N - row + 1`

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from `1` to `N`
3. For each row:

   - Print left spaces
   - Print left stars
   - Print middle spaces
   - Print right stars

4. Print everything in **one line**

---

## **7️⃣ Method**

Use:

- one `for` loop
- string repetition
- one `print()` per row

---

## **8️⃣ Constraints**

- N ≥ 2
- Space after every `*`

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Forgetting middle spacing
❌ Wrong alignment

---

## **🔟 Complexity**

- **Time:** `O(N²)`
- **Space:** `O(1)`

---

## **1️⃣1️⃣ Code (ONE LOOP – YOUR LEARNING FORMAT)**

```python
N = int(input())

for row in range(1, N + 1):
    left_spaces = " " * (row - 1)
    left_stars = "* " * (N - row + 1)
    middle_spaces = "  " * (row - 1)
    right_stars = "* " * (N - row + 1)

    print(left_spaces + left_stars + middle_spaces + right_stars)
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
```

### Output

```
* * * * * * * * *
 * * * * * * * *
  * * *   * * *
   * *     * *
    *       *
```

---

## **1️⃣3️⃣ Key Takeaways**

✔ W = two inverted triangles
✔ Spacing creates shape
✔ One loop + condition logic is enough
✔ Same logic works for **M / Butterfly / X**

---

## **1️⃣4️⃣ Conclusion**

This solution is:

- ✅ **Pattern-accurate**
- ✅ **Beginner-safe**
- ✅ **One-loop only**
- ✅ **Exactly what NxtWave expects**

---
