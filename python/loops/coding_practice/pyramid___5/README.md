# ✅ **Pyramid – 5**

---

## **1️⃣ Question**

Given a number **N**, print a **Pyramid of `2*N - 1` rows** using:

- **Pluses (`+`)**
- **Hashes (`#`)**

👉 The **last column** of every row contains `#`
👉 The remaining positions contain `+`
👉 There is a **space after every symbol**

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing → Conditional Logic

---

## **2️⃣ Outline**

- Read N
- Loop from `1` to `2*N - 1`
- Use condition to decide:

  - Top half
  - Bottom half

- Print spaces + symbols

---

## **3️⃣ Objective**

To print a **full pyramid** using **only one loop** and **conditions**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- Using **conditions inside a loop**
- Handling **increasing and decreasing patterns**
- Building complex patterns without nested loops

---

## **5️⃣ Theory**

Total rows in Pyramid – 5:

```
rows = 2*N - 1
```

We split rows logically:

### 🔼 Top half (including middle)

```
row <= N
```

### 🔽 Bottom half

```
row > N
```

For every row:

- Print **spaces first**
- Print **`+` symbols**
- Print **`#` at the end**

---

## **6️⃣ Step-by-Step Explanation**

1. Read `N`
2. Loop from `1` to `2*N - 1`
3. If `row <= N`:

   - Increasing pattern

4. Else:

   - Decreasing pattern

5. Print the row

---

## **7️⃣ Method**

Use:

- One `for` loop
- `if / else` condition
- String repetition

---

## **8️⃣ Constraints**

- N ≥ 1
- Space after every `+` and `#`

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Forgetting `#` at the end
❌ Wrong space calculation

---

## **🔟 Complexity**

- **Time:** `O(N²)`
- **Space:** `O(1)`

---

## **1️⃣1️⃣ Code (ONE LOOP + CONDITION – FINAL)**

```python
N = int(input())

total_rows = 2 * N - 1

for row in range(1, total_rows + 1):
    if row <= N:
        spaces = "  " * (N - row)
        plus = "+ " * (row - 1) + "#"
    else:
        spaces = "  " * (row - N)
        plus = "+ " * (total_rows - row) + "#"

    print(spaces + plus)
```

---

## **1️⃣2️⃣ Example**

### **Input**

```
5
```

### **Output**

```
        #
      + #
    + + #
  + + + #
+ + + + #
  + + + #
    + + #
      + #
        #
```

---

## **1️⃣3️⃣ Dry Run (N = 3)**

Total rows = `5`

| Row | Condition | Output  |
| --: | --------- | ------- |
|   1 | row ≤ N   | `    #` |
|   2 | row ≤ N   | `  + #` |
|   3 | row ≤ N   | `+ + #` |
|   4 | row > N   | `  + #` |
|   5 | row > N   | `    #` |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Rows | Pattern      |
| ----: | ---- | ------------ |
|     1 | 1    | `#`          |
|     3 | 5    | Pyramid      |
|     5 | 9    | Full pyramid |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- One loop **CAN** handle two directions using conditions
- `row <= N` and `row > N` is the key idea
- No nested loops needed
- This is **NxtWave-valid**

---

## **1️⃣6️⃣ Real-Life Application**

- UI layout control
- Symmetric designs
- Conditional rendering logic

---

## **1️⃣7️⃣ Practice Questions**

1. Replace `+` with `*`
2. Replace `#` with numbers
3. Print the same pyramid inverted

---

## **1️⃣8️⃣ Result**

The program correctly prints **Pyramid – 5** using **one loop + conditions**.

---

## **1️⃣9️⃣ Conclusion**

✅ This is the **best possible solution**
✅ Uses **only what you’ve learned**
✅ No nested loops
✅ Fully matches **NxtWave expectations**

---
