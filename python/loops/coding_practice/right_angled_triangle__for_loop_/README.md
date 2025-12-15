# ✅ **Right Angled Triangle (For Loop)**

---

## **1️⃣ Question**

Given a number **N**, print a **right angled triangle** of **N rows** using stars (`*`).

---

## **1.5️⃣ Category**

For Loop → Pattern Printing → Triangle

---

## **2️⃣ Outline**

- Read N
- Use a for loop from 1 to N
- Print stars equal to the current row number

---

## **3️⃣ Objective**

To print a right angled triangle pattern using a **single for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- increasing patterns
- loop control
- string repetition

---

## **5️⃣ Theory**

If N = 4

The output should be:

```
*
**
***
****
```

Each row prints stars equal to the row number.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Start a loop from 1 to N
3. In each iteration, print `*` repeated current count

---

## **7️⃣ Method**

Use:

- for loop
- string repetition (`"*" * i`)
- print statement

---

## **8️⃣ Constraints**

- N is a positive integer
- Output must have exactly N rows
- No extra spaces

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Printing all stars in one line
❌ Printing extra spaces

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(1, N + 1):
    print("*" * i)
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
**
***
****
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

Loop iterations:

- i = 1 → `*`
- i = 2 → `**`
- i = 3 → `***`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output                     |
| ----- | -------------------------- |
| 1     | \*                         |
| 3     | \*, **, \***               |
| 5     | 5 rows of increasing stars |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- One loop is enough for simple patterns
- String repetition avoids nested loops
- Row number controls star count

---

## **1️⃣6️⃣ Real-Life Application**

- Visual progress indicators
- Console pattern designs
- Learning structured output

---

## **1️⃣7️⃣ Practice Questions**

1. Print triangle using `+`
2. Print numbers in triangle form
3. Print reverse right angled triangle

---

## **1️⃣8️⃣ Result**

The program correctly prints a right angled triangle of stars.

---

## **1️⃣9️⃣ Conclusion**

A beginner-friendly pattern problem that strengthens **for loop** and **string repetition** skills.

---
