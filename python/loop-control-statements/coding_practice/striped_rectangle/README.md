# ✅ **Striped Rectangle**

---

## **1️⃣ Question**

Given two integers **M** and **N**, print a **striped rectangle pattern** of **M rows** and **N columns** using `+` and `-` characters.

- Odd rows contain `+`
- Even rows contain `-`

---

## **1️⃣.5️⃣ Category**

Pattern Printing → For Loop → Conditions

---

## **2️⃣ Outline**

- Read integer `M` (rows)
- Read integer `N` (columns)
- Loop through rows
- For each row:

  - If row number is odd, print `+`
  - If row number is even, print `-`

- Print each row with spaces

---

## **3️⃣ Objective**

To print a rectangular pattern with alternating rows of symbols.

---

## **4️⃣ Purpose**

This problem helps in learning:

- row-based pattern control
- use of conditions inside loops
- alignment and formatting

---

## **5️⃣ Theory**

For each row:

- Row 1 → `+`
- Row 2 → `-`
- Row 3 → `+`
- Row 4 → `-`
- …

Each row contains **N symbols** separated by spaces.

---

## **6️⃣ Step-by-Step Explanation**

1. Read `M` and `N`
2. Loop from `1` to `M`
3. If row number is odd, choose symbol `+`
4. Otherwise choose `-`
5. Print the chosen symbol `N` times with spaces

---

## **7️⃣ Method**

- One outer loop
- One `if` condition
- String repetition

---

## **8️⃣ Constraints**

- Must follow exact row pattern
- Must print spaces between symbols

---

## **9️⃣ Common Mistakes**

❌ Mixing symbol order
❌ Forgetting spaces
❌ Wrong number of rows or columns

---

## **🔟 Complexity**

- Time Complexity: **O(M × N)**
- Space Complexity: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
m = int(input())
n = int(input())

for row in range(1, m + 1):
    if row % 2 != 0:
        print("+ " * n)
    else:
        print("- " * n)
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
7
```

### Output

```
+ + + + + + +
- - - - - - -
+ + + + + + +
- - - - - - -
+ + + + + + +
```

---

## **1️⃣3️⃣ Dry Run**

For `m = 3`, `n = 4`

Rows printed:

1 → `+ + + +`
2 → `- - - -`
3 → `+ + + +`

---

## **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output                        |
| --- | --- | ----------------------------- |
| 3   | 3   | +++ / --- / +++               |
| 4   | 5   | +++++ / ----- / +++++ / ----- |
| 1   | 4   | ++++                          |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Row number controls the pattern
- Conditions are the brain of pattern logic
- String repetition makes printing clean

---

## **1️⃣6️⃣ Real-Life Application**

- UI grid rendering
- Terminal visualization
- Console-based layouts

---

## **1️⃣7️⃣ Practice Questions**

1. Start with `-` instead of `+`
2. Make the rectangle vertical stripes
3. Use numbers instead of symbols

---

## **1️⃣8️⃣ Result**

The program prints the correct striped rectangle pattern.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens loop control, conditional logic, and structured pattern construction.

---
