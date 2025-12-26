# ✅ **Hollow Right Angled Triangle – 3**

---

## **1️⃣ Question**

Given a number **N**, print a **Hollow Right Angled Triangle** of **N rows** using stars (`*`).

There is a **space after every star**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read `N`
- Loop from `0` to `N-1`
- First row → all stars
- Last column → one star
- Diagonal → star
- Remaining places → spaces

---

## **3️⃣ Objective**

To print a **hollow right angled triangle** using **one for loop** and **conditions**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- Border logic
- Diagonal positioning
- Controlling spaces inside a pattern

---

## **5️⃣ Theory**

For **N = 5**:

- **Row 0** → full stars
- **Middle rows** → first star + inner star
- **Last row** → single star

Spaces reduce as rows go down.

---

## **6️⃣ Step-by-Step Explanation**

1. Read `N`
2. Loop row from `0` to `N-1`
3. For each row:

   - If first row → print `* ` N times
   - Else if last row → print `*`
   - Else:

     - Print `* `
     - Print spaces
     - Print `*`

---

## **7️⃣ Method**

- One `for` loop
- `if / elif / else`
- String repetition

---

## **8️⃣ Constraints**

- `N ≥ 1`
- Space after every `*`

---

## **9️⃣ Common Mistakes**

- Printing extra stars
- Wrong inner spacing
- Missing diagonal star

---

## **🔟 Complexity**

- **Time:** O(N)
- **Space:** O(1)

---

## **1️⃣1️⃣ Code**

```python
n = int(input())

for i in range(n):
    if i == 0:
        print("* " * n)
    elif i == n - 1:
        print("* ")
    else:
        inner_spaces = "  " * (n - i - 2)
        print("* " + inner_spaces + "* ")
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
```

### Output

```
* * * * *
*     *
*   *
* *
*
```

---

## **1️⃣3️⃣ Notes / Key Takeaways**

- First row decides the width
- Inner spaces shrink each row
- One loop is enough
- Conditions control the shape

---

## **1️⃣4️⃣ Result**

The program prints the **correct Hollow Right Angled Triangle** exactly as required.

---

## **1️⃣5️⃣ Conclusion**

This solution matches your **current learning**, keeps logic **simple**, and produces the **exact output** without confusion.

---
