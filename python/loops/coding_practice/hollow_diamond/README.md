# ✅ **Hollow Diamond**

---

## **1️⃣ Question**

Given a number **N**, print a **Hollow Diamond** of
**(2 × N − 1)** rows using stars (`*`).

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from `1` to `2N − 1`
- Decide upper or lower half
- Print spaces and border stars

---

## **3️⃣ Objective**

To print a **hollow diamond shape** using stars with correct spacing.

---

## **4️⃣ Purpose**

This problem helps you understand:

- combining upper and lower pyramids
- hollow pattern borders
- symmetric spacing logic

---

## **5️⃣ Theory**

For a hollow diamond:

- Total rows = `2N − 1`
- Middle row is the widest
- Only **border stars** are printed
- Inner area is hollow (spaces)

For **N = 5**, output is:

```
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
```

---

## **6️⃣ Step-by-Step Explanation**

For each row `i` from `1` to `2N−1`:

- Find `current_row`

  - If `i ≤ N` → `current_row = i`
  - Else → `current_row = 2N - i`

- Left spaces = `N - current_row`
- If `current_row == 1`

  - Print one star

- Else

  - Print first star
  - Print hollow spaces
  - Print second star

---

## **7️⃣ Method**

- One `for` loop
- Conditional statements (mandatory here)
- String repetition

---

## **8️⃣ Constraints**

- `N ≥ 1`
- No trailing spaces
- Proper symmetry

---

## **9️⃣ Common Mistakes**

- Printing filled diamond instead of hollow
- Extra spaces at line end
- Wrong middle-row handling

---

## **🔟 Complexity**

- Time: **O(N²)**
- Space: **O(1)**

---

## **1️⃣1️⃣ Code (One Loop + Conditions – Correct)**

```python
N = int(input())

for i in range(1, 2 * N):
    if i <= N:
        current = i
    else:
        current = 2 * N - i

    spaces = " " * (N - current)

    if current == 1:
        print(spaces + "*")
    else:
        hollow_spaces = " " * (2 * current - 3)
        print(spaces + "*" + hollow_spaces + "*")
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
```

### Output

```
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
```

---

## **1️⃣3️⃣ Dry Run**

For `N = 3`

```
  *
 * *
*   *
 * *
  *
```

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output         |
| ----: | -------------- |
|     1 | `*`            |
|     3 | Hollow diamond |
|     5 | Matches sample |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Diamond = pyramid + inverted pyramid
- Border logic needs condition
- Inner spaces grow by `2` each row

---

## **1️⃣6️⃣ Real-Life Application**

- ASCII art
- UI alignment logic
- Symmetry-based problems

---

## **1️⃣7️⃣ Practice Questions**

1. Print solid diamond
2. Replace `*` with numbers
3. Print hollow diamond upside down

---

## **1️⃣8️⃣ Result**

The program prints the **exact hollow diamond** correctly.

---

## **1️⃣9️⃣ Conclusion**

This solution follows **your learning path**, uses **only necessary conditionals**, and produces the **correct pattern without extra spaces**.

---
