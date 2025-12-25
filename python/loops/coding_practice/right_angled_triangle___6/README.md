# ✅ **Right Angled Triangle – 6**

---

## **1️⃣ Question**

Given a number **N**, print a **Right Angled Triangle of N rows** using stars (`*`),
aligned to the **right side**, with a **space after every star**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from 1 to N
- Print spaces first
- Print stars with a space

---

## **3️⃣ Objective**

To print a **right-aligned right angled triangle** using **one for loop** and **string repetition**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- right alignment using spaces
- star spacing using `"* "`
- building patterns without nested loops

---

## **5️⃣ Theory**

For a right-aligned triangle:

- Total rows = **N**
- For each row:

  - Spaces = **N − row**
  - Stars = **row**

Spaces come **before** stars to push the triangle to the right.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Start loop from 1 to N
3. In each row:

   - Print `"  "` repeated `(N - row)` times
   - Print `"* "` repeated `row` times

4. Print everything in **one line per row**

---

## **7️⃣ Method**

Use:

- for loop
- string repetition
- single `print()` per row

---

## **8️⃣ Constraints**

- N ≥ 1
- Space after every `*`

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Printing stars before spaces
❌ Missing space after `*`

---

## **🔟 Complexity**

Time: **O(N²)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code (NO nested loops – FINAL & CORRECT)**

```python
N = int(input())

for row in range(1, N + 1):
    print("  " * (N - row) + "* " * row)
```

---

## **1️⃣2️⃣ Example**

### Input

```
6
```

### Output

```
          *
        * *
      * * *
    * * * *
  * * * * *
* * * * * *
```

---

## **1️⃣3️⃣ Dry Run**

For **N = 3**

- row = 1 → `"  " * 2 + "* "` → `   *`
- row = 2 → `"  " * 1 + "* * "` → ` * *`
- row = 3 → `"  " * 0 + "* * * "` → `* * * `

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Pattern         |
| ----: | ---------------------- |
|     1 | `*`                    |
|     3 | right-aligned triangle |
|     6 | matches sample exactly |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Right alignment = **spaces before stars**
- `"  "` (two spaces) keeps alignment clean
- String repetition replaces nested loops
- Beginner-safe and NxtWave-friendly

---

## **1️⃣6️⃣ Real-Life Application**

- Console UI layouts
- Formatting reports
- Visual logic building

---

## **1️⃣7️⃣ Practice Questions**

1. Print the inverted version of this pattern
2. Replace `*` with numbers
3. Print the same pattern using `#`

---

## **1️⃣8️⃣ Result**

The program correctly prints a **right-aligned right angled triangle** without nested loops.

---

## **1️⃣9️⃣ Conclusion**

This is the **simplest, cleanest, and correct solution** for **Right Angled Triangle – 6**,
fully aligned with **your learning stage** and **NxtWave expectations** ✅

---
