# ✅ **Rectangle - 3**

---

## **1️⃣ Question**

Read two numbers **M** and **N**.
Print **M rows** and **N columns** using numbers starting from **1**.
Row 1 = print `1` N times
Row 2 = print `2` N times
…
Row M = print `M` N times

Each number must have a space after it.

---

## **2️⃣ Outline**

- Read M
- Read N
- Start number = 1
- Build a row string for each number
- Print M rows

---

## **3️⃣ Objective**

Print a repeating-number rectangle using simple loops.

---

## **4️⃣ Purpose**

To understand pattern printing using a single loop.

---

## **5️⃣ Theory**

If M = 5 and N = 4:
Row 1 → `1 1 1 1`
Row 2 → `2 2 2 2`
Row 3 → `3 3 3 3`
Row 4 → `4 4 4 4`
Row 5 → `5 5 5 5`

---

## **6️⃣ Step-by-Step Explanation**

1. Start with current number = 1
2. Build row = `"1 " * N`
3. Print row
4. Increase number
5. Repeat M times

---

## **7️⃣ Method**

Use:

- While loop
- String multiplication
- Reassign number each loop

---

## **8️⃣ Constraints**

M ≥ 1
N ≥ 1
Space after every number

---

## **9️⃣ Common Mistakes**

❌ Forgetting space after numbers
❌ Not incrementing the row number
❌ Printing wrong number of rows

---

## 🔟 Complexity

O(M)

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

row_num = 1
count = 0

while count < M:
    row = (str(row_num) + " ") * N
    print(row)
    row_num = row_num + 1
    count = count + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
5
4
```

Output:

```
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
5 5 5 5
```

---

## **1️⃣3️⃣ Dry Run**

M = 3, N = 2

Row 1 → `1 1`
Row 2 → `2 2`
Row 3 → `3 3`

---

## **1️⃣4️⃣ Test Cases**

| M   | N   | Output Example     |
| --- | --- | ------------------ |
| 1   | 4   | `1 1 1 1`          |
| 4   | 1   | `1`, `2`, `3`, `4` |
| 3   | 3   | 3×3 number square  |

---

## **1️⃣5️⃣ Result**

Correct rectangle printed with repeating row numbers.

---

## **1️⃣6️⃣ Conclusion**

A perfect pattern problem solved with a single loop and string repetition.

---
