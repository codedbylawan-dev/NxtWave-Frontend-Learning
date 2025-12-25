# ✅ **Pyramid – 7**

---

## **1️⃣ Question**

Given a number **N**, print a **Pyramid of N rows** using numbers.

There should be **a space after every number**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from 1 to N
- Print leading spaces
- Print the row number repeatedly

---

## **3️⃣ Objective**

To print a **center-aligned number pyramid** using **only one for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- center alignment using spaces
- number repetition using strings
- building pyramids without nested loops

---

## **5️⃣ Theory**

For a number pyramid:

- Total rows = **N**
- For each row:

  - Leading spaces = `N − row`
  - Numbers printed = `row`

- Each number is followed by a space

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from `1` to `N`
3. In each row:

   - Print `" "` repeated `(N - row)`
   - Print the current number with space, repeated `row` times

4. Each loop prints one row

---

## **7️⃣ Method**

Use:

- one `for` loop
- string repetition
- one `print()` per row

---

## **8️⃣ Constraints**

- `N ≥ 1`
- Space after every number

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Forgetting spaces before numbers
❌ Printing numbers without space

---

## **🔟 Complexity**

- **Time:** `O(N²)`
- **Space:** `O(1)`

---

## **1️⃣1️⃣ Code (ONE LOOP – YOUR LEARNING STYLE)**

```python
N = int(input())

for row in range(1, N + 1):
    spaces = " " * (N - row)
    numbers = (str(row) + " ") * row
    print(spaces + numbers)
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
```

### Output

```
    1
   2 2
  3 3 3
 4 4 4 4
5 5 5 5 5
```

---

## **1️⃣3️⃣ Dry Run (N = 3)**

- row = 1 → `"  " + "1 "` → ` 1`
- row = 2 → `" " + "2 2 "` → `2 2`
- row = 3 → `"" + "3 3 3 "` → `3 3 3 `

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Pattern          |
| ----: | ----------------------- |
|     1 | `1`                     |
|     3 | centered number pyramid |
|     5 | matches sample          |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Center alignment = spaces before numbers
- `(str(row) + " ") * row` replaces nested loops
- Same logic as star pyramid, just numbers

---

## **1️⃣6️⃣ Real-Life Application**

- Formatting reports
- Console output alignment
- Understanding symmetry

---

## **1️⃣7️⃣ Practice Questions**

1. Print inverted number pyramid
2. Replace numbers with `*`
3. Print pyramid using even numbers

---

## **1️⃣8️⃣ Result**

The program correctly prints a **number pyramid** as required.

---

## **1️⃣9️⃣ Conclusion**

This solution is **100% aligned with your learning**,
uses **only one loop**, and **matches NxtWave output exactly** ✅

---
