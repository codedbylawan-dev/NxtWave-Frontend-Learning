# ✅ **Hollow Right Angled Triangle – 6**

---

## **1️⃣ Question**

Given a number **N**, print a **Hollow Inverted Right Angled Triangle** of **N rows** using stars (`*`).

There is a **space after every star**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read `N`
- Loop through rows
- Print left spaces
- Print stars only on borders
- Print single star in last row

---

## **3️⃣ Objective**

To print a **right-aligned hollow inverted right angled triangle** using **one loop** and **conditions**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- Inverted triangle structure
- Hollow border logic
- Space control before stars

---

## **5️⃣ Theory**

For **N = 4**:

- First row → all stars
- Middle rows → two stars (left & right border)
- Last row → single star
- Left spaces increase row by row

---

## **6️⃣ Step-by-Step Explanation**

1. Read `N`
2. Loop from `0` to `N-1`
3. For each row:

   - Print left spaces → `"  " * row`
   - If first row → print `"* " * N`
   - Else if last row → print `"*"`
   - Else → print `"* "` + inner spaces + `"*"`

---

## **7️⃣ Method**

- Single `for` loop
- `if / elif / else`
- String repetition

---

## **8️⃣ Constraints**

- `N ≥ 1`
- Space after every `*`

---

## **9️⃣ Common Mistakes**

- Printing extra stars in middle rows
- Wrong space count
- Misplacing the last star

---

## **🔟 Complexity**

- **Time:** O(N)
- **Space:** O(1)

---

## **1️⃣1️⃣ Code**

```python
n = int(input())

for i in range(n):
    left_spaces = "  " * i

    if i == 0:
        print("* " * n)
    elif i == n - 1:
        print(left_spaces + "*")
    else:
        inner_spaces = "  " * (n - i - 2)
        print(left_spaces + "* " + inner_spaces + "*")
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
  *   *
    * *
      *
```

---

## **1️⃣3️⃣ Notes / Key Takeaways**

- Inverted = stars reduce every row
- Hollow = only borders printed
- Left spaces increase gradually

---

## **1️⃣4️⃣ Result**

The program prints the **correct Hollow Right Angled Triangle – 6** exactly as required.

---

## **1️⃣5️⃣ Conclusion**

This solution follows **your learning flow**, **your formatting**, and **produces the exact output** ✅
