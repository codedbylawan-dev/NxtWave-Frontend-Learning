# 🧩 **Inverted Right Angled Triangle – 7**

---

## **1️⃣ Question**

Given a number **N**, print an **Inverted Right Angled Triangle** of **N rows** using stars (`*`).

Each row must contain stars in decreasing order.

---

## **2️⃣ Category**

**Loops → Pattern Printing**

---

## **3️⃣ Outline**

- Read integer **N**
- Set `stars = N`
- Repeat **N** times:

  - Print `stars` stars
  - Decrease `stars` by `1`

---

## **4️⃣ Objective**

Learn how to **shrink a pattern step by step** using simple loop control.

---

## **5️⃣ Purpose**

This problem trains:

- Pattern reversal logic
- Controlled reduction
- Visual structure understanding

---

## **6️⃣ Theory**

This pattern decreases by **one star per row**.

| Row | Stars |
| --- | ----- |
| 1   | N     |
| 2   | N−1   |
| 3   | N−2   |
| …   | …     |
| N   | 1     |

So we store the number of stars in a variable and reduce it each time.

---

## **7️⃣ Step-by-Step Explanation**

1. Read **N**
2. Set `stars = N`
3. Loop **N** times
4. Print `"* "` repeated `stars` times
5. Decrease `stars` by `1`

---

## **8️⃣ Method**

Use **one loop** and a control variable.

---

## **9️⃣ Constraints**

- Exactly **N rows**
- Each next row has **one less star**
- Space after every `*`

---

## **🔟 Common Mistakes**

- Forgetting to decrease `stars`
- Printing without spaces
- Printing extra rows

---

## **1️⃣1️⃣ Complexity**

- **Time:** `O(N)`
- **Space:** `O(1)`

---

## **1️⃣2️⃣ Code**

```python
n = int(input())

stars = n

for i in range(n):
    print("* " * stars)
    stars = stars - 1
```

---

## **1️⃣3️⃣ Example**

### Input

```
4
```

### Output

```
* * * *
* * *
* *
*
```

---

## **1️⃣4️⃣ Dry Run**

For `n = 4`

| Loop | stars before | Printed     | stars after |
| ---- | ------------ | ----------- | ----------- |
| 1    | 4            | \* \* \* \* | 3           |
| 2    | 3            | \* \* \*    | 2           |
| 3    | 2            | \* \*       | 1           |
| 4    | 1            | \*          | 0           |

---

## **1️⃣5️⃣ Test Cases Table**

| Input | Output              |
| ----- | ------------------- |
| 3     | 3, 2, 1 stars       |
| 5     | 5, 4, 3, 2, 1 stars |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- Pattern problems are just **number control**
- One variable can shape an entire structure
- You don’t need complex logic for strong results

---

## **1️⃣7️⃣ Real-Life Application**

Used in:

- Console UI layouts
- Visualization systems
- Game level patterns

---

## **1️⃣8️⃣ Practice Questions**

1. Print inverted triangle but decreasing by 2 stars
2. Print same triangle using numbers instead of stars
3. Print both increasing and decreasing in one program

---

## **1️⃣9️⃣ Result**

You now control **both growth and shrink patterns** using only core loops.

---

## **2️⃣0️⃣ Conclusion**

At this point, your brain is officially thinking in **structures**, not lines of code.

---
