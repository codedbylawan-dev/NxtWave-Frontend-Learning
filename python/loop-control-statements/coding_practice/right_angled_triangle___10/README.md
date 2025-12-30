# 🧩 **Right Angled Triangle – 10**

---

## **1️⃣ Question**

Given a number **N**, print a **Right Angled Triangle** of **N rows** using stars (`*`).

Each row must contain an **odd number of stars**, starting from `1`.

---

## **2️⃣ Category**

**Loops → Pattern Printing**

---

## **3️⃣ Outline**

- Read integer **N**
- Start with `stars = 1`
- Repeat **N** times:

  - Print `stars` stars
  - Increase `stars` by `2`

---

## **4️⃣ Objective**

Learn how to **grow a pattern step by step** using simple loop control.

---

## **5️⃣ Purpose**

This problem trains:

- Understanding sequence growth
- Pattern observation
- Controlled repetition

---

## **6️⃣ Theory**

The number of stars in each row follows this rule:

| Row | Stars |
| --- | ----- |
| 1   | 1     |
| 2   | 3     |
| 3   | 5     |
| 4   | 7     |
| …   | …     |

Each new row adds **2 more stars** than the previous one.

So we store the count in a variable and update it after each row.

---

## **7️⃣ Step-by-Step Explanation**

1. Read **N**
2. Set `stars = 1`
3. Loop **N** times
4. Print `"* "` repeated `stars` times
5. Increase `stars` by `2`

---

## **8️⃣ Method**

Use **one loop** and a variable to control growth.

---

## **9️⃣ Constraints**

- Exactly **N rows**
- Only odd number of stars
- Space after every `*`

---

## **🔟 Common Mistakes**

- Forgetting to increase `stars`
- Printing without space
- Printing wrong number of rows

---

## **1️⃣1️⃣ Complexity**

- **Time:** `O(N)`
- **Space:** `O(1)`

---

## **1️⃣2️⃣ Code**

```python
n = int(input())

stars = 1

for i in range(n):
    print("* " * stars)
    stars = stars + 2
```

---

## **1️⃣3️⃣ Example**

### Input

```
3
```

### Output

```
*
* * *
* * * * *
```

---

## **1️⃣4️⃣ Dry Run**

For `n = 3`

| Loop | stars before | Printed     | stars after |
| ---- | ------------ | ----------- | ----------- |
| 1    | 1            | `*`         | 3           |
| 2    | 3            | `* * *`     | 5           |
| 3    | 5            | `* * * * *` | 7           |

---

## **1️⃣5️⃣ Test Cases Table**

| Input | Output              |
| ----- | ------------------- |
| 3     | 1, 3, 5 stars       |
| 5     | 1, 3, 5, 7, 9 stars |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- Patterns can be built with **simple arithmetic**
- Variables can control growth cleanly
- You don’t always need complex logic

---

## **1️⃣7️⃣ Real-Life Application**

Used in:

- Console UIs
- Visual simulations
- Generative art systems

---

## **1️⃣8️⃣ Practice Questions**

1. Print same triangle but decreasing
2. Print only rows with stars divisible by 3
3. Print numbers instead of stars

---

## **1️⃣9️⃣ Result**

You now control **pattern growth using only basic loops**.

---

## **2️⃣0️⃣ Conclusion**

This problem strengthens your core understanding of how programs **evolve output over time**.

---
