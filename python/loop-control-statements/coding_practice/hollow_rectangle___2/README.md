# ✅ **Hollow Rectangle – 2**

---

## **1️⃣ Question**

Given two integers **M** and **N**, print a **hollow rectangle** such that:

- Total rows = `M + 2`
- Total columns = `N + 2`

The rectangle must use:

- `+` for the four corners
- `-` for the top and bottom borders
- `|` for the left and right borders
- Spaces inside the rectangle

---

## **1️⃣.5️⃣ Category**

Pattern Printing → For Loop → Conditions

---

## **2️⃣ Outline**

- Read `M` and `N`
- Calculate total rows = `M + 2`
- Calculate total columns = `N + 2`
- Loop through each row
- Print borders on first and last row
- Print side borders with spaces on middle rows

---

## **3️⃣ Objective**

To draw a hollow rectangle **around** the given dimensions.

---

## **4️⃣ Purpose**

This problem strengthens:

- careful reading of problem constraints
- border vs inside logic
- accurate pattern sizing

---

## **5️⃣ Theory**

If input is:

```
M = 5
N = 10
```

Then actual pattern size is:

```
7 rows × 12 columns
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read `M` and `N`
2. Set `rows = M + 2`, `cols = N + 2`
3. Loop from `1` to `rows`
4. If current row is first or last:

   - Print `+`, then `cols - 2` dashes, then `+`

5. Else:

   - Print `|`, then `cols - 2` spaces, then `|`

---

## **7️⃣ Method**

- One `for` loop
- `if` condition
- String repetition

---

## **8️⃣ Constraints**

- `M ≥ 1`, `N ≥ 1`
- Must exactly follow border symbols and spacing

---

## **9️⃣ Common Mistakes**

❌ Forgetting to add `2` to dimensions
❌ Incorrect number of dashes or spaces
❌ Mixing border symbols

---

## **🔟 Complexity**

- Time Complexity: **O(M × N)**
- Space Complexity: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
m = int(input())
n = int(input())

rows = m + 2
cols = n + 2

for r in range(1, rows + 1):
    if r == 1 or r == rows:
        print("+" + "-" * (cols - 2) + "+")
    else:
        print("|" + " " * (cols - 2) + "|")
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
10
```

### Output

```
+----------+
|          |
|          |
|          |
|          |
|          |
+----------+
```

(7 rows × 12 columns)

---

## **1️⃣3️⃣ Dry Run**

For `M = 3`, `N = 4`

```
Rows = 5, Columns = 6

+----+
|    |
|    |
|    |
+----+
```

---

## **1️⃣4️⃣ Test Cases Table**

| M   | N   | Rows × Cols |
| --- | --- | ----------- |
| 1   | 1   | 3 × 3       |
| 3   | 4   | 5 × 6       |
| 5   | 10  | 7 × 12      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Input dimensions are **inner space only**
- Borders are built around the input
- Always translate problem statement to real size before coding

---

## **1️⃣6️⃣ Real-Life Application**

- UI frame layout
- Console dashboards
- Grid-based designs

---

## **1️⃣7️⃣ Practice Questions**

1. Make this rectangle double-bordered
2. Replace symbols with numbers
3. Create a hollow square with same rule

---

## **1️⃣8️⃣ Result**

The program now correctly prints the hollow rectangle according to the problem’s real constraints.

---

## **1️⃣9️⃣ Conclusion**

This corrected version respects the problem statement and builds the required rectangle precisely using only fundamental concepts.

---
