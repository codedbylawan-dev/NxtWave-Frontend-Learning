# ✅ **Hollow Right Angled Triangle – 2**

---

## **1️⃣ Question**

Given a number **N**, print a **Hollow Right Angled Triangle** of **N rows** using:

- underscore `_`
- pipe `|`
- forward slash `/`

---

## **2️⃣ Required Output Pattern**

For **N = 5**, output must be **exactly**:

```
______
|    /
|   /
|  /
| /
|/
```

---

## **3️⃣ Pattern Understanding (VERY IMPORTANT)**

### 🔹 Total rows = **N + 1**

(Top row + N triangle rows)

### 🔹 Row-wise logic

#### ▶ First row (row = 0)

- Print **underscores**
- Count = `N + 1`

```
______
```

#### ▶ Remaining rows (row = 1 to N)

Each row has:

- One `|`
- Some spaces
- One `/`

Spaces **decrease** row by row.

---

## **4️⃣ Allowed Concepts (What YOU have learned)**

✔ One `for` loop
✔ `if / else`
✔ String repetition
❌ No nested loops
❌ No column loops

---

## **5️⃣ Row-wise Logic Table**

| Row | Pipe | Spaces | Slash |     |
| --: | ---: | -----: | ----: | --- |
|   1 |    ` |      ` |     4 | `/` |
|   2 |    ` |      ` |     3 | `/` |
|   3 |    ` |      ` |     2 | `/` |
|   4 |    ` |      ` |     1 | `/` |
|   5 |    ` |      ` |     0 | `/` |

Spaces = `N - row`

---

## **6️⃣ Final Code (ONE LOOP ONLY – CORRECT)**

```python
N = int(input())

for row in range(0, N + 1):
    if row == 0:
        print("_" * (N + 1))
    else:
        print("|" + " " * (N - row) + "/")
```

---

## **7️⃣ Example**

### Input

```
5
```

### Output

```
______
|    /
|   /
|  /
| /
|/
```

---

## **8️⃣ Dry Run (N = 3)**

- row 0 → `____`
- row 1 → `|  /`
- row 2 → `| /`
- row 3 → `|/`

---

## **9️⃣ Key Takeaways**

✔ First row is **special case**
✔ Remaining rows use **decreasing spaces**
✔ One loop + conditions is **enough**
✔ This logic is reusable for many hollow patterns

---

## **🔟 Conclusion**

This solution is:

- ✅ 100% matches the required output
- ✅ Uses **ONLY what you learned**
- ✅ No nested loops
- ✅ Clean, readable, and NxtWave-friendly

---
