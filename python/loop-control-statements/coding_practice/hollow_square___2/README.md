# 🧩 **Hollow Square – 2**

---

## **1️⃣ Question**

Given a number **N**, print a **Hollow Square** of **N + 2 rows** using:

- `+` at corners
- `-` on top and bottom
- `|` on left and right
- spaces inside

There is a space after every character.

---

## **2️⃣ Category**

**Loops → Pattern Printing**

---

## **3️⃣ Outline**

- Read **N**
- Build **top border**
- Build **middle line**
- Print middle line **N times**
- Build **bottom border**

---

## **4️⃣ Objective**

Learn how to construct a full shape by **assembling rows** instead of drawing cell-by-cell.

---

## **5️⃣ Purpose**

This trains:

- thinking in **rows**
- string building
- controlled repetition
- pattern design without complexity

---

## **6️⃣ Theory**

The shape has only **three unique rows**:

1. **Top row**
2. **Middle row**
3. **Bottom row**

If we can build these as strings, we can print the full square.

---

## **7️⃣ Step-by-Step Explanation**

1. Build top row
2. Build middle row
3. Print top row once
4. Print middle row **N times**
5. Print top row again as bottom row

---

## **8️⃣ Method**

Use **single for loop + string repetition**.

---

## **9️⃣ Constraints**

- Exactly **N + 2 rows**
- Space after every symbol
- Must stay hollow

---

## **🔟 Common Mistakes**

- Forgetting spaces
- Printing too many rows
- Filling inside accidentally

---

## **1️⃣1️⃣ Complexity**

- **Time:** `O(N)`
- **Space:** `O(1)`

---

## **1️⃣2️⃣ Code**

_(using only what you’ve learned)_

```python
n = int(input())

top = "+ " + "- " * n + "+"
middle = "| " + "  " * n + "|"

print(top)

for i in range(n):
    print(middle)

print(top)
```

---

## **1️⃣3️⃣ Example**

### Input

```
5
```

### Output

```
+ - - - - - +
|           |
|           |
|           |
|           |
|           |
+ - - - - - +
```

---

## **1️⃣4️⃣ Dry Run**

For `n = 3`:

- `top` → `+ - - - +`
- `middle` → `|       |`

Print order:

1. top
2. middle
3. middle
4. middle
5. top

---

## **1️⃣5️⃣ Test Cases Table**

| Input | Rows Printed |
| ----- | ------------ |
| 2     | 4 rows       |
| 5     | 7 rows       |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- Patterns can be built by **reusing prepared rows**
- No need for complicated logic
- Thinking in **rows first** makes everything easier

---

## **1️⃣7️⃣ Real-Life Application**

- UI boxes
- Console panels
- ASCII layouts

---

## **1️⃣8️⃣ Practice Questions**

1. Make hollow rectangle
2. Make double border square
3. Make hollow triangle

---

## **1️⃣9️⃣ Result**

You just built a complex structure using **only beginner tools**.

---

## **2️⃣0️⃣ Conclusion**

This is real programming discipline.
You didn’t skip steps.
You **earned** the solution.

---
