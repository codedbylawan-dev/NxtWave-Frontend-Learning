# ✅ **Pyramid – 4**

---

## **1️⃣ Question**

Given a number **N**, print a **Pyramid of (2 × N − 1) rows** using numbers.

There should be a **space after every number**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from `1` to `(2 × N − 1)`
- Increase numbers till N
- Decrease numbers after N
- Print the same number repeatedly in each row

---

## **3️⃣ Objective**

To print a **number pyramid that increases and then decreases**
using **only one for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- symmetric patterns
- increasing + decreasing logic
- controlling values using row number

---

## **5️⃣ Theory**

Total rows = **2 × N − 1**

For each row:

- If `row ≤ N`
  → number = `row`
  → print it `row` times

- Else
  → number = `2 × N − row`
  → print it `(2 × N − row)` times

Each number must have a **space after it**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from `1` to `(2 × N − 1)`
3. Decide the number to print
4. Print that number repeated required times

---

## **7️⃣ Method**

Use:

- single `for` loop
- `if–else`
- string repetition

---

## **8️⃣ Constraints**

- N ≥ 1
- Space after every number

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Printing wrong number count
❌ Forgetting space after number

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
        print((str(row) + " ") * row)
    else:
        value = 2 * N - row
        print((str(value) + " ") * value)
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
4 4 4 4
3 3 3
2 2
1
```

---

## **1️⃣3️⃣ Dry Run (N = 3)**

| Row | Printed |
| --: | ------- |
|   1 | 1       |
|   2 | 2 2     |
|   3 | 3 3 3   |
|   4 | 2 2     |
|   5 | 1       |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Pattern  |
| ----: | --------------- |
|     1 | `1`             |
|     3 | correct pyramid |
|     6 | matches sample  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `2*N - row` is the key
- Same logic as Pyramid-3, just numbers
- One loop is enough

---

## **1️⃣6️⃣ Real-Life Application**

- Pattern logic in interviews
- Loop control mastery
- Symmetry understanding

---

## **1️⃣7️⃣ Practice Questions**

1. Print the same pyramid using `*`
2. Remove the space after numbers
3. Print only the top half

---

## **1️⃣8️⃣ Result**

The program correctly prints **Pyramid – 4** using only learned concepts.

---

## **1️⃣9️⃣ Conclusion**

This solution is:

✅ Simple
✅ Correct
✅ NxtWave-accurate
✅ No nested loops

---
