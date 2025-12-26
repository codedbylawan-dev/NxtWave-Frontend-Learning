# ✅ **Hollow Pyramid**

---

## **1️⃣ Question**

Given a number **N**, print a **Hollow Pyramid** of **N rows** using stars (`*`).

---

## **2️⃣ Output Pattern (Correct & Final)**

For **N = 5**, the output must be **exactly**:

```
    *
   * *
  *   *
 *     *
* * * * *
```

---

## **3️⃣ Category**

For Loop → Pattern Printing (Hollow Patterns)

---

## **4️⃣ Objective**

To print a **hollow pyramid** using:

- **one `for` loop**
- **if / elif / else conditions**
- **string repetition**
- ❌ **no nested loops**

---

## **5️⃣ Important Notes (Spacing Rules)**

- Each **space** = `" "` (single space)
- Each **star** = `"*"`
- Left alignment is achieved using **leading spaces**
- Middle is hollow (spaces only)

---

## **6️⃣ Pattern Logic (Very Clear)**

### Total Rows = `N`

### For each row `i` (starting from `1` to `N`):

#### 🔹 Left Spaces

```
N - i
```

#### 🔹 Stars Logic

- **First row (`i == 1`)**

  - Print **only one star**

- **Last row (`i == N`)**

  - Print **N stars separated by space**

- **Middle rows**

  - Print:

    - one star
    - hollow spaces
    - one star

---

## **7️⃣ Row-wise Breakdown (N = 5)**

| Row | Spaces | Content     |
| --: | -----: | ----------- |
|   1 |      4 | `*`         |
|   2 |      3 | `* *`       |
|   3 |      2 | `*   *`     |
|   4 |      1 | `*     *`   |
|   5 |      0 | `* * * * *` |

---

## **8️⃣ Final Code (ONE LOOP – NO NESTED LOOP)**

```python
N = int(input())

for i in range(1, N + 1):
    spaces = " " * (N - i)

    if i == 1:
        print(spaces + "*")
    elif i == N:
        print("* " * N)
    else:
        hollow_spaces = " " * (2 * i - 3)
        print(spaces + "*" + hollow_spaces + "*")
```

---

## **9️⃣ Dry Run (N = 4)**

```
   *
  * *
 *   *
* * * *
```

---

## **🔟 Common Mistakes (You avoided them 👍)**

❌ Using nested loops
❌ Printing stars before spaces
❌ Wrong hollow space calculation

---

## **1️⃣1️⃣ Key Takeaways**

- Hollow patterns = **edges only**
- First & last rows are **special cases**
- One loop + condition = enough for many patterns
- This logic is reusable for **diamond, hollow triangle, hollow pyramid**

---

## **1️⃣2️⃣ Conclusion**

This solution is:

✅ Correct
✅ Beginner-safe
✅ Uses **only what you learned**
✅ Matches **NxtWave expectations**
✅ Clean & scalable

---
