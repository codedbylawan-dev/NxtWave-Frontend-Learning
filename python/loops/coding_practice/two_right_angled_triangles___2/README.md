## **1️⃣ Question**

Given a number **N**, print:

- one **Right Angled Triangle**
- followed by one **Inverted Right Angled Triangle**

using stars (`*`).

There should be a **space after every star**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing → Triangle Patterns

---

## **2️⃣ Outline**

- Read N
- Print a Right Angled Triangle (increasing)
- Print an Inverted Right Angled Triangle (decreasing)

---

## **3️⃣ Objective**

To print **two different triangle patterns** one after another using **for loops**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- increasing patterns
- decreasing patterns
- reusing logic with different directions

---

## **5️⃣ Theory**

A **Right Angled Triangle**:

- Row 1 → 1 star
- Row 2 → 2 stars
- …
- Row N → N stars

An **Inverted Right Angled Triangle**:

- Row 1 → N stars
- Row 2 → N−1 stars
- …
- Row N → 1 star

We use **string repetition** to avoid nested loops.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from 1 to N and print stars
3. Loop from N to 1 and print stars
4. Each print creates one row

---

## **7️⃣ Method**

Use:

- for loop
- `"* " * number`
- print statement

---

## **8️⃣ Constraints**

- N is a positive integer
- Space must appear after every star

---

## **9️⃣ Common Mistakes**

❌ Printing only one triangle
❌ Wrong loop direction
❌ Missing space after star

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(1, N + 1):
    print("* " * i)

for i in range(N, 0, -1):
    print("* " * i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
```

### Output

```
*
* *
* * *
* * *
* *
*
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

First triangle:

- i = 1 → `*`
- i = 2 → `* *`
- i = 3 → `* * *`

Second triangle:

- i = 3 → `* * *`
- i = 2 → `* *`
- i = 1 → `*`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Rows |
| ----: | ----------- |
|     2 | 4           |
|     3 | 6           |
|     5 | 10          |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Same symbol, different directions
- Loop control decides pattern shape
- String repetition simplifies code

---

## **1️⃣6️⃣ Real-Life Application**

- Pattern-based UI layouts
- Console animations
- Learning structured output

---

## **1️⃣7️⃣ Practice Questions**

1. Print two triangles using `+`
2. Print three right angled triangles
3. Print triangle using numbers

---

## **1️⃣8️⃣ Result**

The program correctly prints **two right angled triangles** using stars.

---

## **1️⃣9️⃣ Conclusion**

This problem improves confidence in **pattern printing** using **simple for loops** without nesting.

---
