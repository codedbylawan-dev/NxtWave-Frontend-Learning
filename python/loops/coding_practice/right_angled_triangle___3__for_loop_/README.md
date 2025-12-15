# ✅ **Right Angled Triangle – 3 (For Loop)**

---

## **1️⃣ Question**

Given a number **N**, print a **Right Angled Triangle** of **N rows** using **stars (`*`)** and **pluses (`+`)**.

- The **first N − 1 rows** should contain stars (`*`)
- The **Nth row** should contain pluses (`+`)

---

## **1.5️⃣ Category**

For Loop → Pattern Printing → Conditional Pattern

---

## **2️⃣ Outline**

- Read N
- Use a for loop from 1 to N
- If row number is less than N → print stars
- Else → print pluses

---

## **3️⃣ Objective**

To print a mixed-symbol right angled triangle using a **for loop** and **condition check**.

---

## **4️⃣ Purpose**

This problem helps understand:

- conditional logic inside loops
- pattern control using row numbers

---

## **5️⃣ Theory**

If **N = 4**, the output should be:

```
*
* *
* * *
+ + + +
```

- Rows 1 to 3 → stars
- Row 4 → pluses

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from 1 to N
3. If current row < N → print `*`
4. Else → print `+`

---

## **7️⃣ Method**

Use:

- for loop
- if–else condition
- string repetition

---

## **8️⃣ Constraints**

- N is a positive integer
- Space must be present after each symbol

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Printing pluses in wrong row
❌ Missing space after symbols

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(1, N + 1):
    if i < N:
        print("* " * i)
    else:
        print("+ " * N)
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
+ + + +
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

- i = 1 → `*`
- i = 2 → `* *`
- i = 3 → `+ + +`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output                           |
| ----- | -------------------------------- |
| 2     | `*` , `+ +`                      |
| 3     | `*`, `* *`, `+ + +`              |
| 5     | Stars for 4 rows, pluses in last |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- One loop + condition is enough
- Last row handled using `if i < N`
- String repetition simplifies printing

---

## **1️⃣6️⃣ Real-Life Application**

- Console pattern designs
- Conditional formatting
- Loop-based layout generation

---

## **1️⃣7️⃣ Practice Questions**

1. Print last row with `#` instead of `+`
2. Print first row with `+` and rest stars
3. Print reverse version of this pattern

---

## **1️⃣8️⃣ Result**

The program correctly prints the required mixed-symbol right angled triangle.

---

## **1️⃣9️⃣ Conclusion**

A simple and effective exercise to combine **for loop** and **if–else** for pattern control.

---
