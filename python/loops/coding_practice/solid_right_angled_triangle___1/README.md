# ✅ **Solid Right Angled Triangle (For Loop)**

---

## **1️⃣ Question**

Given an integer **N**, print a **right-angled triangle** of **N rows** using the asterisk (`*`) character.

There must be a **space after each asterisk**.

---

## **1.5️⃣ Category**

For Loop → Pattern Printing → String Repetition

---

## **2️⃣ Outline**

- Read N
- Start from row 1
- Increase number of stars in each row
- Print rows one by one

---

## **3️⃣ Objective**

To print a right-angled triangle pattern using a **for loop**.

---

## **4️⃣ Purpose**

Helps understand:

- loop counting
- gradual increase of output
- pattern building without nested loops

---

## **5️⃣ Theory**

If N = 4, rows will be:

```
*
* *
* * *
* * * *
```

Row number = number of stars in that row.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Start loop from 1 to N
3. In each loop, print `* ` repeated current row number
4. Move to next line

---

## **7️⃣ Method**

Use:

- `for` loop
- string repetition (`"* " * i`)
- `print()`

---

## **8️⃣ Constraints**

- N ≥ 1
- Each star must have a space after it

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Forgetting space after `*`
❌ Printing all stars in one line

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

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
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

i = 1 → `* `
i = 2 → `* * `
i = 3 → `* * * `

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output         |
| ----- | -------------- |
| 1     | \*             |
| 2     | _<br>_ \*      |
| 4     | 4-row triangle |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Loop variable controls pattern size
- String repetition avoids nested loops
- Clean and beginner-friendly approach

---

## **1️⃣6️⃣ Real-Life Application**

- UI shapes
- Text-based designs
- Learning loop flow

---

## **1️⃣7️⃣ Practice Questions**

1. Print triangle using `+`
2. Print triangle using numbers
3. Print triangle in reverse order

---

## **1️⃣8️⃣ Result**

The right-angled triangle is printed correctly.

---

## **1️⃣9️⃣ Conclusion**

A simple pattern problem that strengthens **for loop** and **string repetition** concepts.

---
