# ✅ **Solid Rectangle**

---

## **1️⃣ Question**

Print a rectangle of **M rows** and **N columns** using `*`.

---

## **2️⃣ Outline**

- Read M
- Read N
- Create one row string: `"* " repeated N times`
- Print that row M times using a single loop

---

## **3️⃣ Objective**

Learn how to print repeated patterns using **one loop only**.

---

## **4️⃣ Purpose**

To avoid nested loops while still printing a rectangle.

---

## **5️⃣ Theory**

If N = 3 → one row looks like:

```
* * *
```

Then print this row **M times**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read M and N
2. Create a row like `"* " * N`
3. Use a while loop to print this row M times

---

## **7️⃣ Method**

- string repetition (`"* " * N`)
- while loop with counter

---

## **8️⃣ Constraints**

M ≥ 1
N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Forgetting space after `*`
❌ Not resetting string
❌ Printing extra blank lines

---

## 🔟 Complexity

Time: O(M)
Space: O(1)

---

## **1️⃣1️⃣ Code (NO nested loops)**

```python
M = int(input())
N = int(input())

row = "* " * N

counter = 0
while counter < M:
    print(row)
    counter = counter + 1
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
row = "\* \* \*"

Loop prints:
1st → `* * *`
2nd → `* * *`

---

## **1️⃣4️⃣ Test Cases**

| M   | N   | Output             |
| --- | --- | ------------------ |
| 1   | 5   | one row of 5 stars |
| 3   | 2   | 3 rows of 2 stars  |
| 4   | 6   | 4 rows of 6 stars  |

---

## **1️⃣5️⃣ Key Takeaway**

You can print patterns WITHOUT nested loops by repeating strings.

---

## **1️⃣6️⃣ Real Use**

- Printing menu layouts
- Banner generation
- Simple console UI blocks

---

## **1️⃣7️⃣ Practice**

1. Print a row of stars without loops
2. Print M lines of "Hello" using one loop
3. Print a rectangle using a custom symbol

---

## **1️⃣8️⃣ Result**

Rectangle printed using **one loop only**.

---

## **1️⃣9️⃣ Conclusion**

Pattern printing becomes easy once you know string repetition.

---
