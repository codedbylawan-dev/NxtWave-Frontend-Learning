# ✅ **Diamond – 2 (Numbers)**

---

## **1️⃣ Question**

Given a number **N**, print a **Diamond of `2 × N − 1` rows** using numbers.

There should be a **space after every number**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Pattern (Final Output Shape)**

For **N = 4**, output is:

```
   1
  2 2
 3 3 3
4 4 4 4
 3 3 3
  2 2
   1
```

---

## **3️⃣ Objective**

To print a **diamond-shaped number pattern** using:

- **one loop**
- **conditions**
- **string repetition**

---

## **4️⃣ Key Observation (IMPORTANT)**

Total rows = **2 × N − 1**

Row-wise behavior:

- Numbers **increase** till middle
- Then **decrease**
- Spaces **decrease**, then **increase**

---

## **5️⃣ Core Logic (Your Level)**

For each row:

- Find the **current number** to print
- Print:

  - leading spaces
  - the same number repeated

👉 The trick:

```
current = row (top half)
current = 2*N - row (bottom half)
```

---

## **6️⃣ Step-by-Step Explanation**

1. Loop from `1` to `2*N - 1`
2. Decide which number to print:

   - If `row <= N` → use `row`
   - Else → use `2*N - row`

3. Print:

   - `" "` repeated `(N - current)`
   - `number + space` repeated `current`

---

## **7️⃣ Method**

Use:

- one `for` loop
- `if-else`
- string repetition

---

## **8️⃣ Constraints**

- N ≥ 1
- Space after every number

---

## **9️⃣ Code (ONE LOOP + CONDITION, CLEAN)**

```python
N = int(input())

for row in range(1, 2 * N):
    if row <= N:
        current = row
    else:
        current = 2 * N - row

    spaces = " " * (N - current)
    numbers = (str(current) + " ") * current
    print(spaces + numbers)
```

---

## **🔟 Example**

### Input

```
4
```

### Output

```
   1
  2 2
 3 3 3
4 4 4 4
 3 3 3
  2 2
   1
```

---

## **1️⃣1️⃣ Dry Run (N = 3)**

Rows = `2*3 - 1 = 5`

| Row | current | Output  |
| --: | ------: | ------- |
|   1 |       1 | `  1`   |
|   2 |       2 | ` 2 2`  |
|   3 |       3 | `3 3 3` |
|   4 |       2 | ` 2 2`  |
|   5 |       1 | `  1`   |

---

## **1️⃣2️⃣ Time & Space Complexity**

- **Time:** `O(N²)`
- **Space:** `O(1)`

---

## **1️⃣3️⃣ Common Mistakes**

❌ Using two separate loops
❌ Forgetting space after number
❌ Printing wrong middle row

---

## **1️⃣4️⃣ Key Takeaways**

✔ Diamond = grow + shrink
✔ One loop is enough
✔ Conditions control shape
✔ Same logic applies to `*`, `+`, `#`

---

## **1️⃣5️⃣ Conclusion**

This solution:

- matches **NxtWave output exactly**
- uses **only what you learned**
- is **interview-safe and beginner-clean**

---

If you want, next we can do:

- **Diamond with `*`**
- **Diamond with mixed symbols**
- **Butterfly using one loop**
