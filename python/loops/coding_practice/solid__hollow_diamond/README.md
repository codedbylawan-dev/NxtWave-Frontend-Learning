# ✅ **Solid & Hollow Diamond**

---

## **1️⃣ Question**

Given a number **N**, print a pattern of **(2 × N − 1) rows** using stars (`*`) such that:

- The **top part** forms a **solid pyramid**
- The **bottom part** forms a **hollow inverted pyramid**
- There is a **space after every star**

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Output Pattern**

For **N = 6**, the output should be:

```
     *
    * *
   * * *
  * * * *
 * * * * *
* * * * * *
 *       *
  *     *
   *   *
    * *
     *
```

---

## **3️⃣ Outline**

- Read N
- Calculate total rows as `2 × N − 1`
- First N rows → solid pyramid
- Remaining rows → hollow inverted pyramid

---

## **4️⃣ Logic Explanation**

### 🔹 Total Rows

```
total_rows = 2 * N - 1
```

---

### 🔹 Top Half (Solid Pyramid)

For rows from `0` to `N-1`:

- Left spaces → `N - row - 1`
- Stars → `row + 1`

---

### 🔹 Bottom Half (Hollow Inverted Pyramid)

For remaining rows:

- Left spaces increase each row
- Print:

  - First star
  - Inner spaces
  - Last star

- Final row prints **only one star**

---

## **5️⃣ Method**

- One `for` loop
- `if / else` conditions
- String repetition for spaces and stars

---

## **6️⃣ Code**

```python
n = int(input())

total_rows = 2 * n - 1

for i in range(total_rows):

    if i < n:
        left_spaces = " " * (n - i - 1)
        stars = "* " * (i + 1)
        print(left_spaces + stars)

    else:
        row = i - n + 1
        left_spaces = " " * row

        if row == n - 1:
            print(left_spaces + "*")
        else:
            inner_spaces = " " * (2 * (n - row - 1) - 2)
            print(left_spaces + "* " + inner_spaces + "*")
```

---

## **7️⃣ Dry Run (N = 4)**

Top:

```
   *
  * *
 * * *
* * * *
```

Bottom:

```
 *   *
  * *
   *
```

---

## **8️⃣ Notes / Key Takeaways**

- Solid pyramid → stars only
- Hollow pyramid → first and last star only
- Spaces control alignment
- Output matches pattern exactly

---

## **9️⃣ Result**

The program correctly prints a **solid + hollow diamond pattern** using the learned concepts.

---

## **🔟 Conclusion**

This solution is **accurate**, **clean**, and fully aligned with your **current learning level** and **pattern expectations**.

---
