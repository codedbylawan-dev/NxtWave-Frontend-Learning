# ✅ **Rectangle – 3 (For Loop)**

---

## **1️⃣ Question**

Given two numbers **M** and **N**, print a **Rectangle of M rows and N columns** using numbers.

---

## **1.5️⃣ Category**

For Loop → Pattern Printing → Number Patterns

---

## **2️⃣ Outline**

- Read M
- Read N
- Print numbers from 1 to M
- Each number should appear **N times in a row**

---

## **3️⃣ Objective**

To print a rectangular number pattern using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- row-wise printing
- string repetition
- formatted output using loops

---

## **5️⃣ Theory**

If **M = 2** and **N = 3**, output is:

```
1 1 1
2 2 2
```

Each row:

- uses the row number
- repeated N times

---

## **6️⃣ Step-by-Step Explanation**

1. Read M and N
2. Loop from 1 to M
3. In each iteration, print the current number **N times**

---

## **7️⃣ Method**

Use:

- for loop
- string conversion
- string repetition

---

## **8️⃣ Constraints**

- M ≥ 1
- N ≥ 1
- There must be a space after every number

---

## **9️⃣ Common Mistakes**

❌ Using nested loops unnecessarily
❌ Missing spaces between numbers
❌ Printing wrong number of rows

---

## 🔟 Complexity

Time: **O(M)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

for i in range(1, M + 1):
    print((str(i) + " ") * N)
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
1 1 1
2 2 2
```

---

## **1️⃣3️⃣ Dry Run**

M = 3, N = 4

Loop runs 3 times:

- i = 1 → `1 1 1 1`
- i = 2 → `2 2 2 2`
- i = 3 → `3 3 3 3`

---

## **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output Rows   |
| --- | --- | ------------- |
| 1   | 3   | 1 1 1         |
| 2   | 2   | 1 1 / 2 2     |
| 4   | 1   | 1 / 2 / 3 / 4 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- String repetition avoids nested loops
- Convert number to string before repetition
- One loop is enough for this pattern

---

## **1️⃣6️⃣ Real-Life Application**

- Table generation
- Grid-based displays
- Pattern formatting

---

## **1️⃣7️⃣ Practice Questions**

1. Print rectangle using stars
2. Print rectangle with fixed number
3. Print rectangle in reverse order

---

## **1️⃣8️⃣ Result**

The program correctly prints a **number rectangle of M rows and N columns**.

---

## **1️⃣9️⃣ Conclusion**

A simple and efficient rectangle pattern using **for loop and string repetition**.

---
