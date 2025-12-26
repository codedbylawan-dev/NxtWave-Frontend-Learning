# ✅ **Right Angled Triangle – 9**

---

## **1️⃣ Question**

Given a number **N**, print a **Right Angled Triangle** of **N rows** such that:

- Borders contain **dots (`.`)**
- Inside contains **zeros (`0`)**
- Space after every dot and zero

---

## **2️⃣ Pattern Observation (MOST IMPORTANT)**

For **N = 7**, output is:

```
.
. .
. 0 .
. 0 0 .
. 0 0 0 .
. 0 0 0 0 .
. . . . . . .
```

---

## **3️⃣ Row-wise Logic (KEY IDEA)**

Each row falls into **one of three cases**:

### 🔹 Case 1: First row

Only **one dot**

```
.
```

### 🔹 Case 2: Middle rows (2 to N−1)

- Start with dot
- Inside zeros
- End with dot

Example:

```
. 0 0 .
```

### 🔹 Case 3: Last row

All dots

```
. . . . . . .
```

---

## **4️⃣ What We Use (Only What You Learned)**

- One `for` loop
- `if / elif / else`
- String repetition

---

## **5️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from row = 1 to N
3. If row == 1
   → print single dot
4. Else if row == N
   → print dots N times
5. Else
   → print:

   - dot
   - zeros (row − 2 times)
   - dot

---

## **6️⃣ Code (ONE LOOP ONLY – BEGINNER SAFE)**

```python
N = int(input())

for row in range(1, N + 1):
    if row == 1:
        print(". ")
    elif row == N:
        print(". " * N)
    else:
        print(". " + "0 " * (row - 2) + ". ")
```

---

## **7️⃣ Example**

### Input

```
7
```

### Output

```
.
. .
. 0 .
. 0 0 .
. 0 0 0 .
. 0 0 0 0 .
. . . . . . .
```

---

## **8️⃣ Dry Run (N = 4)**

- row 1 → `.`
- row 2 → `. .`
- row 3 → `. 0 .`
- row 4 → `. . . .`

---

## **9️⃣ Key Takeaways**

✔ Borders decided by **row number**
✔ Inside values handled using string repetition
✔ Same logic style as **Square & Rectangle problems**
✔ Nested loops are **NOT mandatory**

---

## **🔟 Conclusion**

This solution is:

- ✅ Correct
- ✅ Simple
- ✅ Matches NxtWave output
- ✅ 100% within your learning scope

---

If you want, next we can do:

- **Hollow Right Angled Triangle**
- **Triangle with numbers**
- **Mixed symbol triangle**
