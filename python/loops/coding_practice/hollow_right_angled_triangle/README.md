# ✅ **Hollow Right Angled Triangle**

---

## **1️⃣ Question**

Given a number **N**, print a **Hollow Right Angled Triangle** of **N rows** using stars (`*`).

---

## **2️⃣ Pattern (VERY IMPORTANT)**

For **N = 5**, output is:

```
*
* *
*   *
*     *
* * * * *
```

---

## **3️⃣ Observation (Row-wise Logic)**

Each row behaves differently:

### 🔹 Row 1

- Only **one star**

```
*
```

### 🔹 Middle Rows (2 to N−1)

- One star at **start**
- One star at **end**
- Spaces in between

```
*   *
```

### 🔹 Last Row

- All stars

```
* * * * *
```

---

## **4️⃣ Allowed Concepts (What You’ve Learned)**

✔ One `for` loop
✔ `if / elif / else`
✔ String repetition
❌ No column loop
❌ No nested loop

---

## **5️⃣ Step-by-Step Explanation**

1. Read `N`
2. Loop from `row = 1` to `N`
3. Apply conditions:

   - If `row == 1` → print `*`
   - Else if `row == N` → print `* ` repeated `N` times
   - Else → print:

     - `*`
     - spaces `(row - 2)`
     - `*`

---

## **6️⃣ Code (ONE LOOP – FINAL & CORRECT)**

```python
N = int(input())

for row in range(1, N + 1):
    if row == 1:
        print("* ")
    elif row == N:
        print("* " * N)
    else:
        print("* " + "  " * (row - 2) + "* ")
```

---

## **7️⃣ Example**

### Input

```
5
```

### Output

```
*
* *
*   *
*     *
* * * * *
```

---

## **8️⃣ Dry Run (N = 4)**

- row 1 → `*`
- row 2 → `* *`
- row 3 → `*   *`
- row 4 → `* * * *`

---

## **9️⃣ Key Takeaways**

✔ Hollow patterns = **row-based logic**
✔ Inside space = `row - 2`
✔ Border rows handled with conditions
✔ **Nested loops NOT required** ❌

---

## **🔟 Conclusion**

This solution is:

- ✅ Exactly matches the problem
- ✅ Matches NxtWave output
- ✅ Uses **only what you’ve learned**
- ✅ Clean & reusable for other hollow patterns

---
