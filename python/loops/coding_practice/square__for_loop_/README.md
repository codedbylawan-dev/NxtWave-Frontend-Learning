# ✅ **Square (For Loop)**

---

## **1️⃣ Question**

Given a number **N**, print a **square pattern** of **N rows and N columns** using stars (`*`).

---

## **1.5️⃣ Category**

For Loop → Pattern Printing → Repetition

---

## **2️⃣ Outline**

- Read N
- Create one row containing N stars
- Print that row N times

---

## **3️⃣ Objective**

To print a square pattern using a **single for loop**.

---

## **4️⃣ Purpose**

This problem helps understand:

- repetition using loops
- string repetition using `*`
- pattern printing without nested loops

---

## **5️⃣ Theory**

If N = 4

One row:

```
* * * *
```

Print the same row **4 times**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Create a row using `* ` repeated N times
3. Use a for loop to print the row N times

---

## **7️⃣ Method**

Use:

- for loop
- string repetition
- print statement

---

## **8️⃣ Constraints**

- N is a positive integer
- Space must be present after every `*`

---

## **9️⃣ Common Mistakes**

❌ Missing space after `*`
❌ Printing all stars in one line
❌ Using nested loops unnecessarily

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

row = "* " * N
for i in range(N):
    print(row)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
* * * *
* * * *
* * * *
* * * *
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

row = `"* * * "`

Loop runs 3 times → prints row each time

---

## **1️⃣4️⃣ Test Cases Table**

| N   | Output     |
| --- | ---------- |
| 2   | 2×2 square |
| 4   | 4×4 square |
| 1   | \*         |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- String repetition avoids nested loops
- One row reused multiple times
- Clean and beginner-friendly solution

---

## **1️⃣6️⃣ Real-Life Application**

- UI grids
- Console pattern layouts
- Table formatting

---

## **1️⃣7️⃣ Practice Questions**

1. Print a square using `+`
2. Print a square using numbers
3. Print a rectangle using stars

---

## **1️⃣8️⃣ Result**

The program correctly prints an **N × N square** using stars.

---

## **1️⃣9️⃣ Conclusion**

A simple and efficient pattern problem using only basic loop concepts.

---
