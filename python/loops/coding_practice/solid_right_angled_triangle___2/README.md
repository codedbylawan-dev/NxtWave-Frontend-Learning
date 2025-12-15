# ✅ **Solid Right Angled Triangle – 2**

---

## **1️⃣ Question**

Given a number **N**, print a **double Right Angled Triangle** pattern using stars (`*`).
Each triangle should have **N rows**, and both triangles should be printed **one after the other**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Print the first Right Angled Triangle (N rows)
- Print the second Right Angled Triangle (N rows)

---

## **3️⃣ Objective**

To print **two identical triangular patterns** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you practice:

- repeating patterns
- controlling output using loops
- understanding triangle structures

---

## **5️⃣ Theory**

A Right Angled Triangle pattern works like this:

- Row 1 → 1 star
- Row 2 → 2 stars
- Row 3 → 3 stars
- …
- Row N → N stars

This same pattern is printed **twice**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the number N
2. Use a for loop from 1 to N
3. Print stars equal to the current row number
4. After completing the first triangle, repeat the same loop
5. Total rows printed = `2 × N`

---

## **7️⃣ Method**

Use:

- for loop
- string repetition (`"* " * i`)
- print statement

---

## **8️⃣ Constraints**

- N is a positive integer
- There is a space after every star (`* `)

---

## **9️⃣ Common Mistakes**

❌ Printing only one triangle
❌ Missing space after `*`
❌ Printing more or fewer rows

---

## **🔟 Complexity**

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

- i = 1 → `*`
- i = 2 → `* *`
- i = 3 → `* * *`

Second triangle:

- Same pattern printed again

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Total Rows Printed |
| ----: | ------------------ |
|     2 | 4                  |
|     4 | 8                  |
|     5 | 10                 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Patterns depend on row count
- Same logic can be reused multiple times
- No nested loops are used

---

## **1️⃣6️⃣ Real-Life Application**

- Console-based designs
- Learning structured output
- Pattern-based logic building

---

## **1️⃣7️⃣ Practice Questions**

1. Print three Right Angled Triangles
2. Print the same pattern using numbers
3. Print only the second triangle

---

## **1️⃣8️⃣ Result**

The program correctly prints **two Right Angled Triangles**, each with **N rows**.

---

## **1️⃣9️⃣ Conclusion**

This problem reinforces **for loop usage** and **pattern repetition** using only learned concepts.
