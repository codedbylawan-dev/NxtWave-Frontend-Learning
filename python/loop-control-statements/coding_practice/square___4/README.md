# 🧩 **Square – 4**

---

## **1️⃣ Question**

Given a number **N**, print a square of **N rows** and **N columns** using numbers starting from **0**.

Each row must contain the same number printed **N times**.

---

## **2️⃣ Category**

**Loops → Pattern Printing**

---

## **3️⃣ Outline**

- Read integer **N**
- Initialize a number `num = 0`
- Repeat the following **N times**:

  - Print `num` **N times** in one line
  - Increase `num` by 1

---

## **4️⃣ Objective**

Generate a square pattern using only basic looping and repetition.

---

## **5️⃣ Purpose**

This problem teaches how to control repeated output and structure without complex loop logic.

---

## **6️⃣ Theory**

A square pattern needs:

- **N lines**
- **N values in each line**

Instead of multiple loops, we use **string repetition** to print each row.

---

## **7️⃣ Step-by-Step Explanation**

1. Read **N**
2. Set `num = 0`
3. Run a loop **N times**
4. On each iteration:

   - Print `(str(num) + " ")` repeated **N times**
   - Move to the next line
   - Increase `num`

---

## **8️⃣ Method**

One `for` loop + string repetition.

---

## **9️⃣ Constraints**

- Exactly **N lines**
- Exactly **N numbers in each line**
- A space after every number

---

## **🔟 Common Mistakes**

- Forgetting to increase `num`
- Printing all rows on the same line
- Missing spaces between numbers

---

## **1️⃣1️⃣ Complexity**

- **Time:** `O(N²)`
- **Space:** `O(1)`

---

## **1️⃣2️⃣ Code**

```python
n = int(input())

num = 0
for i in range(n):
    print((str(num) + " ") * n)
    num = num + 1
```

---

## **1️⃣3️⃣ Example**

### Input

```
3
```

### Output

```
0 0 0
1 1 1
2 2 2
```

---

## **1️⃣4️⃣ Dry Run**

| Iteration | num | Printed Line |
| --------- | --- | ------------ |
| 1         | 0   | 0 0 0        |
| 2         | 1   | 1 1 1        |
| 3         | 2   | 2 2 2        |

---

## **1️⃣5️⃣ Test Cases Table**

| Input | Output                                |
| ----- | ------------------------------------- |
| 2     | 0 0 / 1 1                             |
| 4     | 0 0 0 0 / 1 1 1 1 / 2 2 2 2 / 3 3 3 3 |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- You created a 2D pattern using a single loop
- String repetition is extremely powerful
- No advanced logic required

---

## **1️⃣7️⃣ Real-Life Application**

Used in building tables, grids, UI layouts, and display systems.

---

## **1️⃣8️⃣ Practice Questions**

1. Print the same square with decreasing numbers.
2. Print the square using stars.
3. Print the square with alternating 0 and 1 rows.

---

## **1️⃣9️⃣ Result**

The square pattern is generated correctly using only learned concepts.

---

## **2️⃣0️⃣ Conclusion**

You just solved a 2D pattern problem **without nested loops**.
That’s clean thinking.

---
