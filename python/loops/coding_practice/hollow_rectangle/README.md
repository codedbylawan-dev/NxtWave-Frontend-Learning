# ✅ **Hollow Rectangle**

---

## **1️⃣ Question**

Given two numbers **M** and **N**, print a **Hollow Rectangle** of:

- **M rows**
- **N columns**
- using stars (`*`)
- space after every star

---

## **2️⃣ Pattern Observation**

For **M = 4**, **N = 6**, output is:

```
* * * * * *
*         *
*         *
* * * * * *
```

---

## **3️⃣ Row-wise Logic (IMPORTANT)**

Each row falls into **one of two cases**:

### 🔹 Case 1: First row OR Last row

→ Print **N stars**

```
* * * * * *
```

### 🔹 Case 2: Middle rows

→ Print:

- one star at start
- spaces in between
- one star at end

```
*         *
```

---

## **4️⃣ What We Use (Only What You’ve Learned)**

- One `for` loop
- `if / else`
- String repetition
- No column loop ❌

---

## **5️⃣ Step-by-Step Explanation**

1. Read `M` and `N`
2. Loop from `row = 1` to `M`
3. If row is **first or last**

   - Print `* ` repeated `N` times

4. Else

   - Print `*`
   - Print spaces (`N - 2`)
   - Print `*`

---

## **6️⃣ Code (ONE LOOP ONLY – FINAL & CORRECT)**

```python
M = int(input())
N = int(input())

for row in range(1, M + 1):
    if row == 1 or row == M:
        print("* " * N)
    else:
        print("* " + "  " * (N - 2) + "* ")
```

---

## **7️⃣ Example**

### Input

```
4
6
```

### Output

```
* * * * * *
*         *
*         *
* * * * * *
```

---

## **8️⃣ Dry Run**

For `M = 3`, `N = 5`

- row 1 → `* * * * *`
- row 2 → `*       *`
- row 3 → `* * * * *`

---

## **9️⃣ Key Takeaways**

✔ Rectangle borders depend on **row number**
✔ Middle spacing = `N - 2`
✔ Same logic pattern as:

- Hollow Square
- Hollow Triangle
- Hollow Right Angled Triangle

✔ **Nested loops NOT required** ❌

---

## **🔟 Conclusion**

This solution is:

- ✅ Simple
- ✅ Beginner-friendly
- ✅ NxtWave-compliant
- ✅ Matches your learning level perfectly

---
