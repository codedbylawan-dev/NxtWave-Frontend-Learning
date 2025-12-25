# ✅ **Pyramid – 6**

---

## **1️⃣ Question**

Given a number **N**, print a **Pyramid of N rows** using stars (`*`).

There should be **a space after every star**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from 1 to N
- Print leading spaces
- Print stars with space

---

## **3️⃣ Objective**

To print a **center-aligned pyramid** using:

- one `for` loop
- string repetition

---

## **4️⃣ Purpose**

This problem helps you understand:

- center alignment using spaces
- relation between row number and stars
- building pyramids without nested loops

---

## **5️⃣ Theory**

For a pyramid:

- Total rows = **N**
- For each row:

  - Leading spaces = `N − row`
  - Stars = `row`

- Each star is followed by a space (`"* "`)

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Start loop from `1` to `N`
3. For each row:

   - Print `" "` repeated `(N - row)`
   - Print `"* "` repeated `row`

4. Each iteration prints one row

---

## **7️⃣ Method**

Use:

- one `for` loop
- string repetition
- single `print()` per row

---

## **8️⃣ Constraints**

- `N ≥ 1`
- Space after every `*`

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Forgetting leading spaces
❌ Missing space after `*`

---

## **🔟 Complexity**

- **Time:** `O(N²)`
- **Space:** `O(1)`

---

## **1️⃣1️⃣ Code (ONE LOOP – AS PER YOUR LEARNING)**

```python
N = int(input())

for row in range(1, N + 1):
    spaces = " " * (N - row)
    stars = "* " * row
    print(spaces + stars)
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
 * * *
* * * *
```

---

## **1️⃣3️⃣ Dry Run (N = 3)**

- row = 1 → `"  " + "* "` → ` *`
- row = 2 → `" " + "* * "` → `* *`
- row = 3 → `"" + "* * * "` → `* * * `

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Pattern   |
| ----: | ---------------- |
|     1 | `*`              |
|     3 | centered pyramid |
|     4 | matches sample   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Center alignment comes from **spaces before stars**
- `"* "` controls star spacing
- One loop is enough for this pattern

---

## **1️⃣6️⃣ Real-Life Application**

- Console UI alignment
- Layout visualization
- Pattern logic practice

---

## **1️⃣7️⃣ Practice Questions**

1. Print inverted version of this pyramid
2. Replace `*` with numbers
3. Print pyramid using `#`

---

## **1️⃣8️⃣ Result**

The program correctly prints a **center-aligned pyramid** of stars.

---

## **1️⃣9️⃣ Conclusion**

This is the **cleanest and simplest solution** for **Pyramid – 6**,
written **exactly in your learning style**, with **no extra concepts** ✅

---
