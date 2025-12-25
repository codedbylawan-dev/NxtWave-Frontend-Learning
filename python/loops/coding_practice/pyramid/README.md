# ✅ **Pyramid**

---

## **1️⃣ Question**

Given a number **N**, print a **Pyramid of N rows** using stars (`*`) with a **space after every star**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from 1 to N
- Print spaces to center the pyramid
- Print stars with spaces

---

## **3️⃣ Objective**

To print a **center-aligned pyramid** using **a single for loop** and **string repetition**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- center alignment using spaces
- increasing stars in odd count
- pattern building without nested loops

---

## **5️⃣ Theory**

For a pyramid:

- Total rows = **N**
- For each row:

  - Spaces = **N − row**
  - Stars = **(2 × row − 1)** (each followed by a space)

Spaces come **before** stars to keep the pyramid centered.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from 1 to N
3. In each row:

   - Print `" "` repeated `(N - row)` times
   - Print `"* "` repeated `(2 × row − 1)` times

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
❌ Forgetting center spaces
❌ Printing wrong number of stars

---

## **🔟 Complexity**

Time: **O(N²)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code (NO nested loops – FINAL)**

```python
N = int(input())

for row in range(1, N + 1):
    print(" " * (N - row) + "* " * (2 * row - 1))
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
  * * *
 * * * * *
* * * * * * *
```

---

## **1️⃣3️⃣ Dry Run**

For **N = 3**

- row = 1 → `"  " + "* "` → `  *`
- row = 2 → `" " + "* * * "` → ` * * *`
- row = 3 → `"" + "* * * * * "` → `* * * * *`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Pattern   |
| ----: | ---------------- |
|     1 | `*`              |
|     3 | centered pyramid |
|     5 | correct pyramid  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Center alignment = spaces before stars
- Odd number of stars per row
- String repetition replaces nested loops
- Beginner-safe approach

---

## **1️⃣6️⃣ Real-Life Application**

- Console UI designs
- Visual alignment logic
- Understanding spacing patterns

---

## **1️⃣7️⃣ Practice Questions**

1. Print inverted pyramid
2. Print pyramid using numbers
3. Replace `*` with `#`

---

## **1️⃣8️⃣ Result**

The program correctly prints a **center-aligned pyramid** without nested loops.

---

## **1️⃣9️⃣ Conclusion**

This is the **cleanest and simplest pyramid solution** that fully matches your learning stage and **NxtWave expectations** ✅

---
