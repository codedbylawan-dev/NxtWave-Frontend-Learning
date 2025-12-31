# ✅ **Inverted Right Angled Triangle – 8**

---

## **1️⃣ Question**

Given an integer **N**, print an inverted right-angled triangle of stars with increasing left spaces as shown.

---

## **1️⃣.5️⃣ Category**

Pattern Printing → For Loop → Spacing

---

## **2️⃣ Outline**

- Read integer `N`
- Use one `for` loop for rows
- Use string multiplication for spaces
- Use string multiplication for stars
- Print each row

---

## **3️⃣ Objective**

To print a shifted inverted triangle using only **basic loops and strings**.

---

## **4️⃣ Purpose**

This strengthens:

- pattern thinking
- spacing control
- string building using repetition

---

## **5️⃣ Theory**

We control the pattern using two parts in each row:

- **Spaces** increase every row
- **Stars** decrease every row

---

## **6️⃣ Step-by-Step Explanation**

1. Read `N`
2. For each row from `0` to `N-1`:

   - Build spaces using `" " * (row * 4)`
   - Build stars using `"* " * (2*(N-row)-1)`

3. Print the combined line

---

## **7️⃣ Method**

- One `for` loop
- String repetition
- Basic arithmetic

---

## **8️⃣ Constraints**

- Must match the exact visual pattern
- Use only learned features

---

## **9️⃣ Common Mistakes**

❌ Printing stars before spaces
❌ Wrong space count
❌ Extra spaces at line end

---

## **🔟 Complexity**

- Time: **O(N²)**
- Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
n = int(input())

for row in range(n):
    spaces = " " * (row * 4)
    stars = "* " * (2 * (n - row) - 1)
    print(spaces + stars)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
* * * * * * *
    * * * * *
        * * *
            *
```

---

## **1️⃣3️⃣ Dry Run**

For `n = 4`:

| Row | Spaces | Stars |
| --- | ------ | ----- |
| 0   | 0      | 7     |
| 1   | 4      | 5     |
| 2   | 8      | 3     |
| 3   | 12     | 1     |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output              |
| ----- | ------------------- |
| 1     | `*`                 |
| 3     | 5 → 3 → 1 stars     |
| 4     | 7 → 5 → 3 → 1 stars |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Pattern = spaces + stars
- String repetition is powerful and simple
- No advanced concepts needed

---

## **1️⃣6️⃣ Real-Life Application**

- Console UI layout
- ASCII visualization

---

## **1️⃣7️⃣ Practice Questions**

1. Reverse this pattern
2. Change stars to numbers
3. Make it hollow

---

## **1️⃣8️⃣ Result**

The program prints the correct shifted inverted triangle using only learned concepts.

---

## **1️⃣9️⃣ Conclusion**

This problem fits perfectly within your current learning scope and strengthens pattern control using basic tools.

---
