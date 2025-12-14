# ✅ **Rectangle - 2**

---

## **1️⃣ Question**

Given two numbers **M** (rows) and **N** (columns), print a rectangle using plus signs `+` with a space after each plus.

---

## **2️⃣ Outline**

- Read M
- Read N
- Create one row containing N pluses
- Print that row M times

---

## **3️⃣ Objective**

To print an M×N rectangle using simple repetition logic.

---

## **4️⃣ Purpose**

Helps understand pattern repetition without nested loops.

---

## **5️⃣ Theory**

If M = 3 and N = 5:
One row = `+ + + + + `
Repeat it 3 times.

---

## **6️⃣ Step-by-Step Explanation**

1. Build a string row using `"+"` repeated N times
2. Use a loop
3. Print that row M times

---

## **7️⃣ Method**

- String multiplication
- While loop
- Printing repeated rows

---

## **8️⃣ Constraints**

M ≥ 1
N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Missing space after each `+`
❌ Printing wrong number of rows

---

## 🔟 Complexity

O(M)

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

row = ("+ " * N)

count = 0
while count < M:
    print(row)
    count = count + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
3
5
```

Output:

```
+ + + + +
+ + + + +
+ + + + +
```

---

## **1️⃣3️⃣ Dry Run**

M = 2
N = 3
row = "+ + + "

Print row twice.

---

## **1️⃣4️⃣ Test Cases**

| M   | N   | Output              |
| --- | --- | ------------------- |
| 1   | 4   | One row of 4 pluses |
| 4   | 1   | 4 rows of one plus  |
| 2   | 6   | 2 rows of 6 pluses  |

---

## **1️⃣5️⃣ Result**

Correct rectangular pattern printed using simple loops.

---

## **1️⃣6️⃣ Conclusion**

Rectangle printed successfully without nested loops.

---
