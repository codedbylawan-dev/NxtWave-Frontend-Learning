# ✅ **Inverted Right Angled Triangle**

---

## **1️⃣ Question**

Given a number **N**, print an **Inverted Right Angled Triangle** of **N rows** using stars (`*`).

> There is a **space after every star (`*`)**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing → Reverse Order

---

## **2️⃣ Outline**

- Read N
- Start from N stars in the first row
- Reduce stars by 1 in each next row
- Continue until 1 star

---

## **3️⃣ Objective**

To print an **inverted triangle pattern** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- reverse order looping
- pattern size control
- printing decreasing output

---

## **5️⃣ Theory**

In an inverted right angled triangle:

- Row 1 → N stars
- Row 2 → N − 1 stars
- …
- Last row → 1 star

Example for **N = 5**:

```
* * * * *
* * * *
* * *
* *
*
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Start a loop from N to 1
3. In each iteration:

   - Print stars equal to the current value

4. Reduce stars row by row

---

## **7️⃣ Method**

Use:

- input()
- for loop
- string repetition
- print()

---

## **8️⃣ Constraints**

- N is a positive integer
- Each star must have a space after it
- Exactly N rows must be printed

---

## **9️⃣ Common Mistakes**

❌ Printing increasing stars
❌ Missing space after `*`
❌ Looping in the wrong direction

---

## **🔟 Complexity**

Time: **O(N²)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(N, 0, -1):
    print("* " * i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
```

### Output

```
* * * * *
* * * *
* * *
* *
*
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

Loop values: 3 → 1

- i = 3 → print `* * *`
- i = 2 → print `* *`
- i = 1 → print `*`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Rows |
| ----- | ----------- |
| 1     | `*`         |
| 3     | 3 rows      |
| 5     | 5 rows      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Reverse looping controls pattern reduction
- String repetition avoids nested loops
- Output depends on loop variable

---

## **1️⃣6️⃣ Real-Life Application**

- Console pattern design
- Visual representation of decreasing data
- Learning reverse iteration

---

## **1️⃣7️⃣ Practice Questions**

1. Print inverted triangle using numbers
2. Print inverted triangle using `+`
3. Print triangle from N to 2

---

## **1️⃣8️⃣ Result**

The program correctly prints an **Inverted Right Angled Triangle**.

---

## **1️⃣9️⃣ Conclusion**

A clean pattern problem that strengthens **reverse for-loop control** without using nested loops.

---
