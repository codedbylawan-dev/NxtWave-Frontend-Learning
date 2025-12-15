# ✅ **Solid Rectangle (For Loop)**

---

## **1️⃣ Question**

Given two integers **M** and **N**, print a **solid rectangle** of **M rows** and **N columns** using the asterisk (`*`) character.

There must be a **space after each asterisk**.

---

## **1.5️⃣ Category**

For Loop → Pattern Printing → String Repetition

---

## **2️⃣ Outline**

- Read M (rows)
- Read N (columns)
- Create one row with N stars
- Print that row M times using a for loop

---

## **3️⃣ Objective**

To print a rectangle pattern using a **single for loop**.

---

## **4️⃣ Purpose**

Builds confidence in:

- for loop usage
- string repetition
- pattern printing without nested loops

---

## **5️⃣ Theory**

If `N = 3`, one row will be:

```
* * *
```

If `M = 2`, print that row **2 times**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read number of rows (M)
2. Read number of columns (N)
3. Create one row using string repetition
4. Use a for loop to print that row M times

---

## **7️⃣ Method**

Use:

- `for` loop
- string repetition (`* ` \* N)
- `print()`

---

## **8️⃣ Constraints**

- M ≥ 1
- N ≥ 1
- Space must be after every `*`

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Missing space after `*`
❌ Printing stars in one line only

---

## 🔟 Complexity

Time: **O(M)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

row = "* " * N

for i in range(M):
    print(row)
```

---

## **1️⃣2️⃣ Example**

### Input

```
2
3
```

### Output

```
* * *
* * *
```

---

## **1️⃣3️⃣ Dry Run**

M = 2, N = 3

row = "\* \* \* "

Loop runs 2 times → prints the same row twice

---

## **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output          |
| --- | --- | --------------- |
| 2   | 3   | 2 rows, 3 stars |
| 4   | 6   | 4 rows, 6 stars |
| 1   | 5   | 1 row, 5 stars  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- String repetition avoids nested loops
- One row can be reused
- for loop controls rows

---

## **1️⃣6️⃣ Real-Life Application**

- UI grid layouts
- Table formatting
- Pattern-based printing

---

## **1️⃣7️⃣ Practice Questions**

1. Print rectangle using `+` instead of `*`
2. Print square using numbers
3. Print rectangle with different symbols

---

## **1️⃣8️⃣ Result**

The rectangle is printed correctly using **only one for loop**.

---

## **1️⃣9️⃣ Conclusion**

A clean and beginner-friendly pattern problem solved **without nested loops**.

---
