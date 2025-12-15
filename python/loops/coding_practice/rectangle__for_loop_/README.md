# ✅ **Rectangle (For Loop)**

---

## **1️⃣ Question**

Given two numbers **M** and **N**, print a **rectangle of M rows and N columns** using stars (`*`).

---

## **1.5️⃣ Category**

For Loop → Pattern Printing → Rectangle

---

## **2️⃣ Outline**

- Read M (rows)
- Read N (columns)
- Use a loop that runs M times
- Print `*` repeated N times in each row

---

## **3️⃣ Objective**

To print a rectangle pattern using a **single for loop**.

---

## **4️⃣ Purpose**

This problem helps understand:

- fixed repetition using loops
- pattern printing without nested loops

---

## **5️⃣ Theory**

If M = 3 and N = 4

The output should be:

```
****
****
****
```

Each row contains **N stars**, and there are **M rows**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the number of rows (M)
2. Read the number of columns (N)
3. Run a loop M times
4. In each iteration, print `*` repeated N times

---

## **7️⃣ Method**

Use:

- for loop
- string repetition (`"*" * N`)
- print statement

---

## **8️⃣ Constraints**

- M and N are positive integers
- No extra spaces
- Exactly M lines must be printed

---

## **9️⃣ Common Mistakes**

❌ Using nested loops unnecessarily
❌ Printing stars on a single line
❌ Adding spaces between stars

---

## 🔟 Complexity

Time: **O(M)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

for i in range(M):
    print("*" * N)
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
4
```

### Output

```
****
****
****
```

---

## **1️⃣3️⃣ Dry Run**

M = 2, N = 5

Loop runs 2 times:

1st time → print `*****`
2nd time → print `*****`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output                     |
| ----- | -------------------------- |
| 1 1   | \*                         |
| 2 3   | **\* \***                  |
| 5 7   | 7 stars printed on 5 lines |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- One loop is enough
- String repetition simplifies pattern problems
- Clean and beginner-friendly solution

---

## **1️⃣6️⃣ Real-Life Application**

- Grid layouts
- Console UI blocks
- Table-like displays

---

## **1️⃣7️⃣ Practice Questions**

1. Print rectangle using `+`
2. Print rectangle using numbers
3. Print hollow rectangle (later)

---

## **1️⃣8️⃣ Result**

The program correctly prints a rectangle of stars.

---

## **1️⃣9️⃣ Conclusion**

A basic rectangle pattern problem that strengthens **for loop** and **string repetition** concepts.

---
