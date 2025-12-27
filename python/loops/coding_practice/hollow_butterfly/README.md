# 🦋 **Hollow Butterfly Pattern**

---

## **1️⃣ Question**

Given a number **N**, write a program to print a **Hollow Butterfly** of **2 × N rows** using stars (`*`).

---

## **2️⃣ Category**

Pattern Printing → Hollow Patterns

---

## **3️⃣ Outline**

- Total rows = `2 × N`
- Each row contains **two hollow right-angled triangles**
- Upper half grows
- Lower half shrinks
- Borders only, middle hollow

---

## **4️⃣ Objective**

To print a **symmetric hollow butterfly pattern** using:

- single `for` loop
- string repetition
- minimal conditional logic

---

## **5️⃣ Purpose**

This pattern trains you to:

- split patterns into **upper + lower halves**
- mirror logic correctly
- control **double spaces (`"  "`)**
- handle hollow structures cleanly

---

## **6️⃣ Theory**

For each row:

- Left wing → hollow right triangle
- Middle gap → spaces
- Right wing → mirror of left wing

Rules:

- First & last rows → only border stars
- Middle rows → hollow stars
- Stars printed as `"* "`
- Spaces printed as `"  "`

---

## **7️⃣ Step-by-Step Explanation**

1. Read `N`
2. Loop from `0` to `2*N - 1`
3. Decide:

   - current row size
   - left wing stars
   - hollow spacing
   - middle gap

4. Print left wing + middle spaces + right wing

---

## **8️⃣ Method**

We calculate:

- `stars` → how many stars per wing
- `gap` → middle spacing
- Borders → first and last column stars only

---

## **9️⃣ Constraints**

- `N ≥ 2`
- Space after every star is mandatory
- No trailing spaces

---

## **🔟 Common Mistakes**

❌ Wrong middle gap
❌ Extra spaces at line end
❌ Using nested loops unnecessarily

---

## **1️⃣1️⃣ Complexity**

- **Time:** `O(N²)`
- **Space:** `O(1)`

---

## **1️⃣2️⃣ Code (FINAL & CORRECT)**

```python
n = int(input())
total_rows = 2 * n

for i in range(total_rows):

    if i < n:
        stars = i + 1
    else:
        stars = total_rows - i

    middle_spaces = "  " * (2 * (n - stars))

    if stars == 1:
        print("* " + middle_spaces + "*")
    else:
        inner_spaces = "  " * (stars - 2)
        print(
            "* " +
            inner_spaces +
            "* " +
            middle_spaces +
            "* " +
            inner_spaces +
            "*"
        )
```

---

## **1️⃣3️⃣ Example**

### **Input**

```
4
```

### **Output**

```
*             *
* *         * *
*   *     *   *
*     * *     *
*     * *     *
*   *     *   *
* *         * *
*             *
```

---

## **1️⃣4️⃣ Dry Run (N = 4)**

- Rows 1–4 → increasing wings
- Rows 5–8 → decreasing wings
- Middle gap shrinks then expands
- Borders maintained throughout

---

## **1️⃣5️⃣ Test Cases**

| Input | Rows | Output             |
| ----: | ---: | ------------------ |
|     2 |    4 | smallest butterfly |
|     4 |    8 | matches sample     |
|     6 |   12 | wider butterfly    |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- Butterfly = **two mirrored hollow triangles**
- Middle spacing is the key
- One loop is sufficient
- Clean math > nested loops

---

## **1️⃣7️⃣ Real-Life Application**

- ASCII art
- UI pattern rendering
- Logical symmetry problems

---

## **1️⃣8️⃣ Practice Questions**

1. Filled butterfly
2. Number butterfly
3. Inverted hollow butterfly

---

## **1️⃣9️⃣ Result**

The program prints a **perfect hollow butterfly** with correct alignment and spacing.

---

## **2️⃣0️⃣ Conclusion**

This solution follows **your exact learning discipline**
✔ clean
✔ minimal conditions
✔ fully correct
