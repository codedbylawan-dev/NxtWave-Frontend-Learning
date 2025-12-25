# ✅ **Inverted Pyramid – 2**

---

## **1️⃣ Question**

Given a number **N**, print an **Inverted Pyramid of N rows** using stars (`*`).

There should be **a space after every star**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from 0 to N−1
- Print leading spaces
- Print stars

---

## **3️⃣ Objective**

To print an **inverted pyramid** using **one for loop** and **string repetition**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- inverted patterns
- controlling spaces before stars
- reducing stars row by row

---

## **5️⃣ Theory**

For an inverted pyramid:

- Total rows = **N**
- For each row `i` (starting from 0):

  - Leading spaces = `i`
  - Stars = `N − i`
  - Each star has a space after it

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from `i = 0` to `N - 1`
3. In each row:

   - Print `" "` repeated `i` times
   - Print `"* "` repeated `(N - i)` times

4. Print one row per iteration

---

## **7️⃣ Method**

Use:

- one `for` loop
- string repetition
- one `print()` per row

---

## **8️⃣ Constraints**

- `N ≥ 1`
- Space after every `*`

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Forgetting spaces before stars
❌ Printing stars without space

---

## **🔟 Complexity**

- **Time:** `O(N²)`
- **Space:** `O(1)`

---

## **1️⃣1️⃣ Code (ONE LOOP – YOUR LEARNING STYLE)**

```python
N = int(input())

for i in range(N):
    spaces = " " * i
    stars = "* " * (N - i)
    print(spaces + stars)
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
```

### Output

```
* * * * *
 * * * *
  * * *
   * *
    *
```

---

## **1️⃣3️⃣ Dry Run (N = 3)**

- i = 0 → `" " * 0 + "* " * 3` → `* * * `
- i = 1 → `" " * 1 + "* " * 2` → `* *`
- i = 2 → `" " * 2 + "* " * 1` → ` *`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Pattern   |
| ----: | ---------------- |
|     1 | `*`              |
|     3 | inverted pyramid |
|     5 | matches sample   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Inverted pattern = stars decrease
- Spaces increase each row
- String repetition avoids nested loops

---

## **1️⃣6️⃣ Real-Life Application**

- Console formatting
- UI alignment logic
- Pattern problem solving

---

## **1️⃣7️⃣ Practice Questions**

1. Print inverted pyramid using numbers
2. Replace `*` with `#`
3. Print inverted pyramid without spaces

---

## **1️⃣8️⃣ Result**

The program correctly prints an **inverted pyramid**.

---

## **1️⃣9️⃣ Conclusion**

This solution is **100% based on your learning**,
uses **one loop only**, and **matches the required output exactly** ✅

---
