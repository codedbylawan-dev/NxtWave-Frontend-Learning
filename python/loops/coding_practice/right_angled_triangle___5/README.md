# ✅ **Right Angled Triangle – 5**

---

## **1️⃣ Question**

Given a number **N**, print a **Right Angled Triangle of N rows** using stars (`*`) such that the stars are **right-aligned**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from 1 to N
- Print spaces first
- Then print stars

---

## **3️⃣ Objective**

To print a **right-aligned triangle** using a **single for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- alignment using spaces
- combining spaces and stars
- building patterns row by row

---

## **5️⃣ Theory**

In a right-aligned triangle:

- Total width = N
- Each row has:

  - `(N − row)` spaces
  - `row` stars

Example for **N = 4**:

```
   *
  **
 ***
****
```

No grid checking is needed — only **row-based logic**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Start loop from 1 to N
3. For each row:

   - Print spaces = `N - row`
   - Print stars = `row`

4. Combine both in one print statement

---

## **7️⃣ Method**

Use:

- for loop
- string repetition for spaces
- string repetition for stars

---

## **8️⃣ Constraints**

- N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Printing stars before spaces
❌ Using row + column conditions

---

## **🔟 Complexity**

Time: **O(N²)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code (Correct – NO nested loops)**

```python
N = int(input())

for row in range(1, N + 1):
    print(" " * (N - row) + "*" * row)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
   *
  **
 ***
****
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

- row = 1 → `"  " + "*"` → `  *`
- row = 2 → `" " + "**"` → ` **`
- row = 3 → `"" + "***"` → `***`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output                 |
| ----: | ---------------------- |
|     1 | \*                     |
|     3 | ␠␠\*, ␠**, \***        |
|     5 | right-aligned triangle |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Right alignment = spaces before stars
- Spaces count decreases each row
- Stars count increases each row
- No nested loops needed

---

## **1️⃣6️⃣ Real-Life Application**

- Text alignment
- UI layouts
- Console formatting

---

## **1️⃣7️⃣ Practice Questions**

1. Print the same pattern using `#`
2. Print numbers instead of stars
3. Print an inverted right-aligned triangle

---

## **1️⃣8️⃣ Result**

The program correctly prints a **right-aligned right angled triangle**.

---

## **1️⃣9️⃣ Conclusion**

✔ This respects your **learning stage**
✔ This avoids **nested loops completely**

---
