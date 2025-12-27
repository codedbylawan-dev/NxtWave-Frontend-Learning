# ✅ **Solid Right Angled Triangle – 2**

---

## **1️⃣ Question**

Given an integer **N**, print a **right-aligned solid right angled triangle** of **N rows** using stars (`*`).

👉 There is a **space after every star**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Output Pattern**

For **N = 4**, the output should be:

```
      *
    * *
  * * *
* * * *
```

---

## **3️⃣ Outline**

- Read N
- Loop from `1` to `N`
- Print spaces first
- Print stars after spaces

---

## **4️⃣ Logic Explanation**

For each row:

- **Spaces** decrease from top to bottom
- **Stars** increase from top to bottom

### Formula:

- Spaces = `2 * (N - row)`
- Stars = `row`

(We use **double spaces** to match alignment)

---

## **5️⃣ Method**

- One `for` loop
- String repetition
- One `print()` per row

---

## **6️⃣ Code**

```python
n = int(input())

for row in range(1, n + 1):
    spaces = "  " * (n - row)
    stars = "* " * row
    print(spaces + stars)
```

---

## **7️⃣ Example**

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
```

---

## **8️⃣ Dry Run (N = 3)**

- row = 1 → spaces = 4, stars = 1 → `    *`
- row = 2 → spaces = 2, stars = 2 → `  * *`
- row = 3 → spaces = 0, stars = 3 → `* * *`

---

## **9️⃣ Notes / Key Takeaways**

- Right alignment comes from **spaces before stars**
- `"* "` keeps spacing clean
- One loop is enough
- Matches sample output exactly

---

## **🔟 Result**

The program correctly prints a **solid right-aligned right angled triangle**.

---

## **1️⃣1️⃣ Conclusion**

This solution is **simple**, **accurate**, and fully aligned with **your learning stage** and **problem expectations** ✅

---
