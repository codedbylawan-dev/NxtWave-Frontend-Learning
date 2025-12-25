# ✅ **Pyramid – 3**

---

## **1️⃣ Question**

Given a number **N**, print a **Pyramid of (2 × N − 1) rows** using stars (`*`).

There should be a **space after every star**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from 1 to `(2 × N − 1)`
- Increase stars till N
- Decrease stars after N

---

## **3️⃣ Objective**

To print a **vertical pyramid pattern** using a **single for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- growing and shrinking patterns
- controlling logic using row number
- avoiding nested loops completely

---

## **5️⃣ Theory**

Total rows = **2 × N − 1**

- From row `1` to `N` → stars **increase**
- From row `N+1` to end → stars **decrease**

Star count logic:

- If `row ≤ N` → stars = `row`
- Else → stars = `2N − row`

Each star has a **space after it**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from `1` to `(2 × N − 1)`
3. Decide star count based on row
4. Print `"* "` repeated that many times

---

## **7️⃣ Method**

Use:

- one `for` loop
- `if-else`
- string repetition

---

## **8️⃣ Constraints**

- N ≥ 1
- Space after every `*`

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Printing extra stars
❌ Forgetting the middle row logic

---

## **🔟 Complexity**

Time: **O(N²)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code (ONLY WHAT YOU LEARNED)**

```python
N = int(input())

for row in range(1, 2 * N):
    if row <= N:
        print("* " * row)
    else:
        print("* " * (2 * N - row))
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
```

### Output

```
*
* *
* * *
* *
*
```

---

## **1️⃣3️⃣ Dry Run (N = 3)**

| Row | Stars |
| --: | ----- |
|   1 | 1     |
|   2 | 2     |
|   3 | 3     |
|   4 | 2     |
|   5 | 1     |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Pattern  |
| ----: | --------------- |
|     1 | `*`             |
|     3 | matches sample  |
|     6 | correct pyramid |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- One loop is enough
- `2*N - row` is the key logic
- Clean, readable, and beginner-safe

---

## **1️⃣6️⃣ Real-Life Application**

- Pattern logic for interviews
- Understanding symmetry
- Loop control mastery

---

## **1️⃣7️⃣ Practice Questions**

1. Print the same pattern using numbers
2. Remove spaces after stars
3. Print inverted version

---

## **1️⃣8️⃣ Result**

The program correctly prints **Pyramid – 3** using only learned concepts.

---

## **1️⃣9️⃣ Conclusion**

This solution is:

✅ Correct
✅ Simple
✅ Matches NxtWave exactly
✅ No nested loops

---
