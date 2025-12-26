# ✅ **Rectangle – 4**

---

## **1️⃣ Question**

Given two numbers **M** (rows) and **N** (columns), print a **rectangle** such that:

- Borders contain stars (`*`)
- Inside contains zeros (`0`)
- Space after every symbol

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing → Conditional Rows

---

## **2️⃣ Key Observation (IMPORTANT)**

Rectangle rows fall into **3 types**:

1️⃣ **First row** → all stars
2️⃣ **Middle rows** → star + zeros + star
3️⃣ **Last row** → all stars

So again, **NO column loop needed**.

---

## **3️⃣ Objective**

To print a rectangle using:

- One `for` loop
- Row number checks
- String repetition

---

## **4️⃣ Theory (Row-wise Logic)**

For example, **M = 4, N = 8**

### First / Last row

```
* * * * * * * *
```

### Middle rows

```
* 0 0 0 0 0 0 *
```

---

## **5️⃣ Step-by-Step Explanation**

1. Read M and N
2. Loop from `1` to `M`
3. If row is **first or last**:

   - Print `"* "` repeated `N` times

4. Else:

   - Print:

     - `* `
     - `"0 "` repeated `N - 2` times
     - `* `

---

## **6️⃣ Method**

Use:

- One `for` loop
- `if / else`
- String repetition

---

## **7️⃣ Constraints**

- M ≥ 3
- N ≥ 3
- Space after every symbol

---

## **8️⃣ Common Mistakes**

❌ Using nested loops
❌ Printing zeros on border rows
❌ Forgetting space after symbols

---

## **9️⃣ Complexity**

- **Time:** O(M × N)
- **Space:** O(1)

---

## **🔟 Code (ONE LOOP ONLY – BEGINNER SAFE)**

```python
M = int(input())
N = int(input())

for row in range(1, M + 1):
    if row == 1 or row == M:
        print("* " * N)
    else:
        print("* " + "0 " * (N - 2) + "* ")
```

---

## **1️⃣1️⃣ Example**

### Input

```
4
8
```

### Output

```
* * * * * * * *
* 0 0 0 0 0 0 *
* 0 0 0 0 0 0 *
* * * * * * * *
```

---

## **1️⃣2️⃣ Dry Run (M = 3, N = 5)**

- row = 1 → `* * * * *`
- row = 2 → `* 0 0 0 *`
- row = 3 → `* * * * *`

---

## **1️⃣3️⃣ Notes / Key Takeaways**

✔ Rectangles = row logic
✔ Borders = first & last rows
✔ Middle rows = star + inside + star
✔ Nested loops are **not required**

---

## **1️⃣4️⃣ Conclusion**

This solution:

- ✅ Uses **only what you’ve learned**
- ✅ Matches NxtWave output
- ✅ Clean and scalable
- ✅ Same logic as Square–3

---
