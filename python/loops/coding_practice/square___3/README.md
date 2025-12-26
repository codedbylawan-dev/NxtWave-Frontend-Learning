# ✅ **Square – 3**

---

## **1️⃣ Question**

Given a number **N**, print a **square of N rows** such that:

- Borders contain stars (`*`)
- Inside contains zeros (`0`)
- Space after every symbol

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing → Conditional Logic

---

## **2️⃣ Key Observation (IMPORTANT)**

In a square:

- **First row** → all `*`
- **Last row** → all `*`
- **Middle rows** →

  - First symbol `*`
  - Middle symbols `0`
  - Last symbol `*`

So we **don’t need columns** at all.
We just **print complete rows as strings**.

---

## **3️⃣ Objective**

To print a square pattern using:

- **Only one `for` loop**
- **String repetition**
- **Row-based logic**

---

## **4️⃣ Theory (Row-wise Thinking)**

Let `N = 5`

### Row types:

1️⃣ First row

```
* * * * *
```

2️⃣ Middle rows

```
* 0 0 0 *
```

3️⃣ Last row

```
* * * * *
```

---

## **5️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from `1` to `N`
3. If row is **first or last**:

   - Print `"* "` repeated `N` times

4. Else:

   - Print:

     - `* `
     - `"0 "` repeated `N-2` times
     - `* `

---

## **6️⃣ Method**

Use:

- One `for` loop
- `if-else`
- String repetition

---

## **7️⃣ Constraints**

- N ≥ 3
- Space after every symbol

---

## **8️⃣ Common Mistakes**

❌ Trying to use nested loops
❌ Printing zeros on borders
❌ Missing space after symbols

---

## **9️⃣ Complexity**

- **Time:** O(N²) (because strings are printed)
- **Space:** O(1)

---

## **🔟 Code (ONE LOOP ONLY – BEGINNER SAFE)**

```python
N = int(input())

for row in range(1, N + 1):
    if row == 1 or row == N:
        print("* " * N)
    else:
        print("* " + "0 " * (N - 2) + "* ")
```

---

## **1️⃣1️⃣ Example**

### Input

```
5
```

### Output

```
* * * * *
* 0 0 0 *
* 0 0 0 *
* 0 0 0 *
* * * * *
```

---

## **1️⃣2️⃣ Dry Run (N = 4)**

- row = 1 → `* * * *`
- row = 2 → `* 0 0 *`
- row = 3 → `* 0 0 *`
- row = 4 → `* * * *`

---

## **1️⃣3️⃣ Notes / Key Takeaways**

✔ Nested loops are **NOT mandatory**
✔ Think **row-by-row**, not grid
✔ Full lines can be built using strings
✔ This logic applies to MANY patterns

---

## **1️⃣4️⃣ Conclusion**

This solution is:

- ✅ 100% correct
- ✅ Uses **only what you’ve learned**
- ✅ NxtWave-friendly
- ✅ Pattern-thinking focused

---

If you want, next we can do:

- 🔲 Hollow Rectangle
- 🔺 Hollow Triangle
- ⭐ Border Number Square
