# ✅ **Hollow Right Angled Triangle – 5**

---

## **1️⃣ Question**

Given a number **N**, print a **Hollow Right Angled Triangle** of **N rows** using stars (`*`).

There is a **space after every star**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read `N`
- Loop through rows
- Print left spaces first
- Print stars only on borders
- Print full stars on last row

---

## **3️⃣ Objective**

To print a **right-aligned hollow right angled triangle** using **one for loop** and **conditions**.

---

## **4️⃣ Purpose**

This pattern teaches:

- Right alignment using spaces
- Hollow pattern logic
- Border-based star placement

---

## **5️⃣ Theory**

For **N = 4**:

- First row → one star at the right
- Middle rows → two stars (border)
- Last row → fully filled with stars
- Spaces decrease row by row

---

## **6️⃣ Step-by-Step Explanation**

1. Read `N`
2. Loop from `1` to `N`
3. For each row:

   - Print left spaces → `"  " * (N - row)`
   - If last row → print `"* " * row`
   - Else if row is 1 → print `"*"`
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

- Extra stars in middle
- Wrong space count
- Missing right alignment

---

## **🔟 Complexity**

- **Time:** O(N)
- **Space:** O(1)

---

## **1️⃣1️⃣ Code**

```python
n = int(input())

for row in range(1, n + 1):
    left_spaces = "  " * (n - row)

    if row == 1:
        print(left_spaces + "*")
    elif row == n:
        print("* " * n)
    else:
        inner_spaces = "  " * (row - 2)
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
      *
    * *
  *   *
* * * *
```

---

## **1️⃣3️⃣ Notes / Key Takeaways**

- Right alignment = spaces before stars
- Hollow = only borders have stars
- One loop + conditions is enough

---

## **1️⃣4️⃣ Result**

The program prints the **correct Hollow Right Angled Triangle – 5** exactly as required.

---

## **1️⃣5️⃣ Conclusion**

This solution is **100% aligned with your learning**, **clean**, and **pattern-accurate**.
