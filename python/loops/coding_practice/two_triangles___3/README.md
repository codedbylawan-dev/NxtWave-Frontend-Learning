# ✅ **Two Right Angled Triangles – Hollow**

---

## **1️⃣ Question**

Given a number **N**, print **two hollow Right Angled Triangles** of **N rows** using stars (`*`).

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from `0` to `N-1`
- Print:

  - first row (two stars at ends)
  - middle hollow rows
  - last row (fully filled)

---

## **3️⃣ Objective**

To print **two hollow right-angled triangles** side by side using **a single loop** and **string repetition**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- symmetric patterns
- hollow structures
- spacing control using `"  "` (double spaces)
- combining two patterns in one row

---

## **5️⃣ Theory**

For **N rows**:

- Total stars in last row = `2 × N`
- Each star is printed as `"* "`
- Each empty space is printed as `"  "` (double space)

Row behavior:

- **First row** → only border stars
- **Middle rows** → hollow triangles
- **Last row** → fully filled stars

---

## **6️⃣ Step-by-Step Explanation**

1. Take input `N`
2. Loop from `i = 0` to `N - 1`
3. For each row:

   - If `i == 0` → print first border row
   - If `i == N - 1` → print full row
   - Else → print hollow row with inner spaces

---

## **7️⃣ Method**

Use:

- one `for` loop
- `if / elif / else`
- string repetition for spaces and stars

---

## **8️⃣ Constraints**

- `N ≥ 2`
- Space after every star is mandatory
- Use double spaces for alignment

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Using single spaces instead of `"  "`
❌ Printing extra spaces at the end

---

## **🔟 Complexity**

- **Time Complexity:** `O(N²)`
- **Space Complexity:** `O(1)`

---

## **1️⃣1️⃣ Code (FINAL & CORRECT)**

```python
n = int(input())

for i in range(n):
    if i == 0:
        spaces = "  " * (2 * n - 2)
        print("* " + spaces + "*")

    elif i == n - 1:
        print("* " * (2 * n))

    else:
        left_hollow = "  " * (i - 1)
        middle_spaces = "  " * (2 * (n - i) - 2)

        print(
            "* " +
            left_hollow +
            "* " +
            middle_spaces +
            "* " +
            left_hollow +
            "*"
        )
```

---

## **1️⃣2️⃣ Example**

### Input

```
6
```

### Output

```
*                     *
* *                 * *
*   *             *   *
*     *         *     *
*       *     *       *
* * * * * * * * * * * *
```

---

## **1️⃣3️⃣ Dry Run**

For `N = 4`

- Row 0 → border stars
- Row 1 → hollow with 1 inner space
- Row 2 → hollow with 2 inner spaces
- Row 3 → full stars

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output                         |
| ----: | ------------------------------ |
|     2 | Two border stars               |
|     4 | Correct hollow double triangle |
|     6 | Matches sample exactly         |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always think in **rows**
- Borders first, hollow middle, solid last
- `"  "` spacing is the backbone
- One loop is enough

---

## **1️⃣6️⃣ Real-Life Application**

- Console UI layouts
- ASCII art
- Logical pattern thinking

---

## **1️⃣7️⃣ Practice Questions**

1. Print the inverted version
2. Replace `*` with numbers
3. Make only one triangle hollow

---

## **1️⃣8️⃣ Result**

The program prints **two perfectly aligned hollow right-angled triangles** using a **single loop**.

---

## **1️⃣9️⃣ Conclusion**

This solution is **correct, clean, beginner-safe**, and fully aligned with **your learning style and pattern rules** ✅
