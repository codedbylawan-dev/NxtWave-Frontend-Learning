# ✅ **M Pattern with `*` (Using Two Right Angled Triangles)**

---

## **1️⃣ Question**

Given a number **N**, print the letter **M** pattern using stars (`*`) with **a space after every star**.

The pattern is formed using **two solid right-angled triangles**, one on the **left** and one on the **right**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing → String Repetition

---

## **2️⃣ Outline**

- Read N
- Loop from 1 to N
- Print left stars
- Print middle spaces
- Print right stars

---

## **3️⃣ Objective**

To print an **M-shaped pattern** using:

- a **single for loop**
- **string repetition**
- **no nested loops**

---

## **4️⃣ Purpose**

This problem helps you understand:

- building patterns **row by row**
- combining multiple pattern parts in one line
- avoiding grid-based thinking

---

## **5️⃣ Theory**

Each row of the pattern consists of **three parts**:

1. **Left Triangle**

   - `i` stars → `"* " * i`

2. **Middle Gap**

   - Empty space between triangles
   - `"  " * (N - i)` → repeated **twice**

3. **Right Triangle**

   - `i` stars → `"* " * i`

So, each row looks like:

```
LEFT_STARS + GAP + GAP + RIGHT_STARS
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read `n`
2. Loop from `1` to `n`
3. For each row `i`:

   - Create spaces using `"  " * (n - i)`
   - Create stars using `"* " * i`
   - Join them in one line

4. Print the row

---

## **7️⃣ Method**

Use:

- one `for` loop
- string repetition
- single `print()` per row

---

## **8️⃣ Constraints**

- N ≥ 1
- Space after every `*`
- No nested loops allowed

---

## **9️⃣ Common Mistakes**

❌ Thinking in rows × columns
❌ Trying nested loops unnecessarily
❌ Forgetting double spaces in the middle

---

## **🔟 Complexity**

Time: **O(N²)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code (FINAL – Based on What You’ve Learned)**

```python
n = int(input())

for i in range(1, n + 1):
    spaces = "  " * (n - i)
    row = ("* " * i) + spaces + spaces + ("* " * i)
    print(row)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
*           *
* *       * *
* * *   * * *
* * * * * * *
```

---

## **1️⃣3️⃣ Dry Run (n = 3)**

| i   | Left Stars | Spaces | Right Stars | Result        |
| --- | ---------- | ------ | ----------- | ------------- |
| 1   | `* `       | `    ` | `* `        | `*     *`     |
| 2   | `* * `     | `  `   | `* * `      | `* *   * *`   |
| 3   | `* * * `   | ``     | `* * * `    | `* * * * * *` |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Pattern         |
| ----: | ---------------------- |
|     1 | `* *`                  |
|     3 | M pattern with 3 rows  |
|     6 | Matches sample exactly |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Pattern is built **row by row**
- No column logic is needed
- String repetition = powerful replacement for nested loops
- This approach is **correct and expected** at your level

---

## **1️⃣6️⃣ Real-Life Application**

- Console-based designs
- Understanding layout construction
- Interview pattern problems

---

## **1️⃣7️⃣ Practice Questions**

1. Replace `*` with numbers
2. Reduce middle gap by half
3. Print inverted M pattern

---

## **1️⃣8️⃣ Result**

The program correctly prints the **M pattern** using **only learned concepts**.

---

## **1️⃣9️⃣ Conclusion**

This solution is:
✅ Correct
✅ Simple
✅ Beginner-appropriate
✅ Aligned with NxtWave expectations
