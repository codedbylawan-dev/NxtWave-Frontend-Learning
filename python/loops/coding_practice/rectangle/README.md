# ✅ **Rectangle**

---

## **1️⃣ Question**

Given M and N, print a rectangle with **M rows** and **N stars** in each row.

---

## **2️⃣ Outline**

- Read M
- Read N
- Create one row: `"*" * N`
- Print that row M times using a while loop

---

## **3️⃣ Objective**

To print a rectangle pattern using only one loop and string multiplication.

---

## **4️⃣ Purpose**

Shows how repetition of a full row replaces nested loops.

---

## **5️⃣ Theory**

If M = 4 and N = 5 → print:

```
*****
*****
*****
*****
```

Row = `"*" repeated N times`.

---

## **6️⃣ Step-by-Step Explanation**

1. Read M
2. Read N
3. Make `row = "*" * N`
4. Loop M times and print row

---

## **7️⃣ Method**

- while loop
- string repetition using `*`

---

## **8️⃣ Constraints**

M ≥ 1, N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Using spaces (not required here)
❌ Forgotten conversion (not needed; `*` works on strings)
❌ Loop not incremented

---

## 🔟 Complexity

O(M)

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

row = "*" * N

count = 0
while count < M:
    print(row)
    count = count + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
4
5
```

Output:

```
*****
*****
*****
*****
```

---

## **1️⃣3️⃣ Dry Run**

M = 3, N = 2
row = "\*\*"

Loop:
1 → print **
2 → print **
3 → print \*\*

---

## **1️⃣4️⃣ Test Cases**

| M   | N   | Output Shape |
| --- | --- | ------------ |
| 3   | 3   | 3×3 stars    |
| 2   | 6   | 2×6 stars    |
| 1   | 5   | 1 row of 5   |

---

## **1️⃣5️⃣ Notes**

`"*" * N` replaces the need for nested loops.

---

## **1️⃣6️⃣ Result**

Prints an M × N rectangle correctly.

---

## **1️⃣7️⃣ Conclusion**

A simple shape problem solved efficiently without nested loops.

---
