# ✅ **Butterfly Pattern**

---

## **1️⃣ Question**

Given a number **N**, print a **Butterfly pattern** of
`(2 × N − 1)` rows using stars (`*`).

There should be **a space after every star**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Total rows = `2 × N − 1`
- Use one loop from `1` to `total_rows`
- Decide:

  - number of stars on each side
  - number of spaces in the middle

---

## **3️⃣ Objective**

To print a **symmetric butterfly pattern** using:

- one `for` loop
- `if-else` conditions
- string repetition

---

## **4️⃣ Purpose**

This problem helps you understand:

- symmetry in patterns
- growing and shrinking logic
- controlling output using conditions

---

## **5️⃣ Theory**

For a Butterfly pattern:

- Total rows = `2N − 1`
- Pattern has:

  - left stars
  - middle spaces
  - right stars

### Star count logic:

- Upper half (row ≤ N): stars increase
- Lower half (row > N): stars decrease

### Space logic:

- Upper half: spaces decrease
- Lower half: spaces increase

---

## **6️⃣ Step-by-Step Explanation**

1. Read `N`
2. Calculate `total_rows = 2*N - 1`
3. Loop through each row:

   - If `row ≤ N`:

     - stars = row
     - spaces = `2 × (N − row)`

   - Else:

     - stars = `total_rows − row + 1`
     - spaces = `2 × (row − N)`

4. Print:

   - left stars
   - middle spaces
   - right stars

---

## **7️⃣ Method**

Use:

- one `for` loop
- `if-else`
- `"* "` and `"  "` string repetition

---

## **8️⃣ Constraints**

- `N ≥ 1`
- Space after every `*`

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Wrong middle spacing
❌ Printing extra stars
❌ Breaking symmetry

---

## **🔟 Complexity**

- **Time:** `O(N²)`
- **Space:** `O(1)`

---

## **1️⃣1️⃣ Code (ONE LOOP – AS PER YOUR LEARNING)**

```python
N = int(input())
total_rows = 2 * N - 1

for row in range(1, total_rows + 1):
    if row <= N:
        stars = row
        spaces = 2 * (N - row)
    else:
        stars = total_rows - row + 1
        spaces = 2 * (row - N)

    print("* " * stars + "  " * spaces + "* " * stars)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
*             *
* *         * *
* * *     * * *
* * * * * * * *
* * *     * * *
* *         * *
*             *
```

---

## **1️⃣3️⃣ Dry Run (N = 3)**

- Row 1 → `*       *`
- Row 2 → `* *   * *`
- Row 3 → `* * * * * *`
- Row 4 → `* *   * *`
- Row 5 → `*       *`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Pattern         |
| ----: | ---------------------- |
|     1 | `* *`                  |
|     3 | Butterfly shape        |
|     4 | Matches sample exactly |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Butterfly = **stars + spaces + stars**
- Middle spaces change by **2 units**
- One loop is enough with correct conditions

---

## **1️⃣6️⃣ Real-Life Application**

- UI symmetry layouts
- Console visual formatting
- Logical thinking for patterns

---

## **1️⃣7️⃣ Practice Questions**

1. Print butterfly using `#`
2. Remove middle space and observe
3. Print hollow butterfly

---

## **1️⃣8️⃣ Result**

The program prints a **perfect butterfly pattern** exactly as required.

---

## **1️⃣9️⃣ Conclusion**

This solution is:

- ✅ Correct
- ✅ Matches output exactly
- ✅ Uses only what you’ve learned
- ✅ NxtWave-friendly

---
