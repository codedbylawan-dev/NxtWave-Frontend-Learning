# ✅ **Right Angled Triangle – 4**

---

## **1️⃣ Question**

Given a number **N**, print **two Right Angled Triangles**, each with **N rows**, using stars (`*`).

---

## **1.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Print first Right Angled Triangle (N rows)
- Print second Right Angled Triangle (N rows)

---

## **3️⃣ Objective**

To print repeated patterns using **for loops**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- loop repetition
- pattern structure
- reusing logic

---

## **5️⃣ Theory**

A Right Angled Triangle of N rows prints:

- 1 star in row 1
- 2 stars in row 2
- …
- N stars in row N

This pattern is printed **twice**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the number N
2. Use a for loop from 1 to N
3. In each row, print stars equal to the row number
4. After first triangle, repeat the same logic
5. Total rows printed = `2 × N`

---

## **7️⃣ Method**

Use:

- for loop
- print statement
- string repetition

---

## **8️⃣ Constraints**

- N is a positive integer
- There is a space after every star

---

## **9️⃣ Common Mistakes**

❌ Printing only one triangle
❌ Missing space after `*`
❌ Wrong number of rows

---

## 🔟 Complexity

Time: **O(N²)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(1, N + 1):
    print("* " * i)

for i in range(1, N + 1):
    print("* " * i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
*
* *
* * *
* * * *
*
* *
* * *
* * * *
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

First triangle:

- Row 1 → `*`
- Row 2 → `* *`
- Row 3 → `* * *`

Second triangle:

- Same pattern again

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Rows |
| ----- | ----------- |
| 2     | 4           |
| 4     | 8           |
| 6     | 12          |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Same logic reused twice
- Pattern depends on row number
- String repetition simplifies printing

---

## **1️⃣6️⃣ Real-Life Application**

- UI pattern generation
- Console-based designs
- Learning structured output

---

## **1️⃣7️⃣ Practice Questions**

1. Print three Right Angled Triangles
2. Print triangle using numbers
3. Print inverted Right Angled Triangle

---

## **1️⃣8️⃣ Result**

The program prints **two Right Angled Triangles** correctly.

---

## **1️⃣9️⃣ Conclusion**

This problem reinforces **loop control** and **pattern repetition** using for loops.

---
