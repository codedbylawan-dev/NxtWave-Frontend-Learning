# ✅ **Diamond Pattern**

---

## **1️⃣ Question**

Given a number **N**, print a **Diamond pattern** of
**(2 × N − 1) rows** using stars (`*`).

There should be a **space after every star**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from `1` to `(2 × N − 1)`
- Decide:

  - spaces
  - stars

- Print row

---

## **3️⃣ Objective**

To print a **diamond shape** using **one loop and conditions only**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- combining upward + downward logic
- using `if-else` with loops
- pattern symmetry

---

## **5️⃣ Theory**

A diamond has **two parts**:

### 🔺 Upper part (including middle)

- Rows: `1 → N`
- Stars increase
- Spaces decrease

### 🔻 Lower part

- Rows: `N+1 → 2N−1`
- Stars decrease
- Spaces increase

We handle **both parts in ONE loop** using conditions.

---

## **6️⃣ Step-by-Step Explanation**

1. Total rows = `2 × N − 1`
2. Loop through each row
3. If row ≤ N:

   - spaces = `N - row`
   - stars = `row`

4. Else:

   - spaces = `row - N`
   - stars = `2N - row`

5. Print spaces + stars

---

## **7️⃣ Method**

Use:

- one `for` loop
- `if-else`
- string repetition

---

## **8️⃣ Constraints**

- `N ≥ 1`
- Space after every `*`

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Wrong star count in bottom half
❌ Forgetting symmetry

---

## **🔟 Complexity**

- **Time:** `O(N²)`
- **Space:** `O(1)`

---

## **1️⃣1️⃣ Code (ONE LOOP + CONDITION — YOUR STYLE)**

```python
N = int(input())

total_rows = 2 * N - 1

for row in range(1, total_rows + 1):
    if row <= N:
        spaces = " " * (N - row)
        stars = "* " * row
    else:
        spaces = " " * (row - N)
        stars = "* " * (total_rows - row + 1)

    print(spaces + stars)
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
```

### Output

```
  *
 * *
* * *
 * *
  *
```

---

## **1️⃣3️⃣ Dry Run (N = 3)**

| Row | Spaces | Stars |
| --: | ------ | ----- |
|   1 | 2      | 1     |
|   2 | 1      | 2     |
|   3 | 0      | 3     |
|   4 | 1      | 2     |
|   5 | 2      | 1     |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output          |
| ----: | --------------- |
|     1 | `*`             |
|     3 | perfect diamond |
|     5 | larger diamond  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Diamond = pyramid + inverted pyramid
- One loop is enough
- Conditions control direction

---

## **1️⃣6️⃣ Real-Life Application**

- UI symmetry
- ASCII art
- Logical thinking practice

---

## **1️⃣7️⃣ Practice Questions**

1. Print diamond using numbers
2. Replace `*` with `#`
3. Print hollow diamond

---

## **1️⃣8️⃣ Result**

The program prints a **correct diamond pattern** using **only basic concepts**.

---

## **1️⃣9️⃣ Conclusion**

You’re now **officially good at patterns**.
This solution is **correct**, **clean**, and **matches NxtWave expectations** ✅
