# ✅ **Right Angled Triangle – 8**

---

## **1️⃣ Question**

Given a number **N**, print **two Right Angled Triangles**, each of **N rows**, using stars (`*`).

- The **first N rows** form one Right Angled Triangle
- The **next N rows** form another Right Angled Triangle
- There is a **space after every star**

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Pattern Observation (MOST IMPORTANT)**

For **N = 4**, output is:

```
*
* *
* * *
* * * *
*
* *
* * *
* * * *
```

👉 It is **NOT side-by-side**
👉 It is **one triangle below another**

---

## **3️⃣ Objective**

To print **two identical right angled triangles** one after the other.

---

## **4️⃣ Logic Explanation (Very Simple)**

1. First, print **one right angled triangle** of N rows
2. Then, print **another right angled triangle reminder** of N rows
3. Each row prints stars equal to the row number

---

## **5️⃣ Step-by-Step Explanation**

### First Triangle

- Row 1 → `*`
- Row 2 → `* *`
- Row 3 → `* * *`
- …
- Row N → `* * * ...`

### Second Triangle

- Repeat the **same logic again**

---

## **6️⃣ Method**

Use:

- for loop
- string repetition (`"* "`)

---

## **7️⃣ Constraints**

- N ≥ 1
- Space after every `*`

---

## **8️⃣ Code (Correct & Beginner-Safe)**

```python
N = int(input())

# First Right Angled Triangle
for row in range(1, N + 1):
    print("* " * row)

# Second Right Angled Triangle
for row in range(1, N + 1):
    print("* " * row)
```

---

## **9️⃣ Example**

### Input

```
4
```

### Output

```
*
* *
* * *
* * * *
*
* *
* * *
* * * *
```

---

## **🔟 Dry Run (N = 3)**

### First Triangle

```
*
* *
* * *
```

### Second Triangle

```
*
* *
* * *
```

---

## **1️⃣1️⃣ Time & Space Complexity**

- **Time:** `O(N)`
- **Space:** `O(1)`

---

## **1️⃣2️⃣ Common Mistakes**

❌ Trying to print both triangles in one loop
❌ Adding extra blank lines
❌ Missing space after `*`

---

## **1️⃣3️⃣ Key Takeaways**

✔ Same pattern printed twice
✔ One triangle = one loop
✔ Very common interview pattern
✔ Clean and reminds loop flow

---

## **1️⃣4️⃣ Conclusion**

This problem is simply:

> **Right Angled Triangle + Right Angled Triangle**

Printed **one below the other**, using **basic for loops**.

---

If you want, next we can do:

- **Inverted two triangles**
- **Butterfly pattern**
- **Diamond pattern**
