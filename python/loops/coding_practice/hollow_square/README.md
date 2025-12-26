# ✅ **Hollow Square**

---

## **1️⃣ Question**

Given a number **N**, print a **Hollow Square** of **N rows** using stars (`*`).

- Borders contain stars
- Inside contains spaces
- Space after every star

---

## **2️⃣ Pattern Observation**

For **N = 4**, output is:

```
* * * *
*     *
*     *
* * * *
```

---

## **3️⃣ Row-wise Logic (IMPORTANT)**

Each row belongs to **one of three cases**:

### 🔹 Case 1: First row

All stars

```
* * * *
```

### 🔹 Case 2: Last row

All stars

```
* * * *
```

### 🔹 Case 3: Middle rows

- Star at start
- Spaces in middle
- Star at end

```
*     *
```

---

## **4️⃣ What We Use (Only What You Learned)**

- One `for` loop
- `if / elif / else`
- String repetition
- No column loop ❌

---

## **5️⃣ Step-by-Step Explanation**

1. Read `N`
2. Loop from `row = 1` to `N`
3. If row is **first or last**

   - Print `* ` repeated `N` times

4. Else

   - Print `*`
   - Print spaces (`N - 2`)
   - Print `*`

---

## **6️⃣ Code (ONE LOOP ONLY – BEGINNER SAFE)**

```python
N = int(input())

for row in range(1, N + 1):
    if row == 1 or row == N:
        print("* " * N)
    else:
        print("* " + "  " * (N - 2) + "* ")
```

---

## **7️⃣ Example**

### Input

```
4
```

### Output

```
* * * *
*     *
*     *
* * * *
```

---

## **8️⃣ Dry Run (N = 3)**

- row 1 → `* * *`
- row 2 → `*   *`
- row 3 → `* * *`

---

## **9️⃣ Key Takeaways**

✔ Borders decided using **row number**
✔ Middle spaces = `N - 2`
✔ Same logic style as:

- Hollow Triangle
- Square with zeros
- Rectangle borders

✔ Nested loops are **NOT required** ❌

---

## **🔟 Conclusion**

This solution is:

- ✅ Correct
- ✅ Simple
- ✅ NxtWave-style
- ✅ Matches your learning stage perfectly

---
