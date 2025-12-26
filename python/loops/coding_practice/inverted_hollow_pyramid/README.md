# ✅ **Inverted Hollow Pyramid**

---

## **1️⃣ Question**

Given a number **N**, print an **Inverted Hollow Pyramid** of **N rows** using stars (`*`).

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from `0` to `N-1`
- Print leading spaces
- Print border stars

---

## **3️⃣ Objective**

To print an **inverted hollow pyramid** with correct alignment and hollow space.

---

## **4️⃣ Purpose**

This problem helps you understand:

- inverted pyramid logic
- hollow pattern borders
- controlled spacing

---

## **5️⃣ Pattern**

For **N = 5**, output is:

```
* * * * *
 *     *
  *   *
   * *
    *
```

---

## **6️⃣ Step-by-Step Explanation**

For each row `i`:

- Leading spaces = `i`
- If `i == 0`

  - Print `N` stars

- Else if `i == N-1`

  - Print one star

- Else

  - Print two border stars with hollow space in between

---

## **7️⃣ Method**

- One `for` loop
- Conditional statements (mandatory)
- String repetition

---

## **8️⃣ Constraints**

- `N ≥ 1`
- No extra stars
- No trailing spaces

---

## **9️⃣ Common Mistakes**

- Printing filled pyramid instead of hollow
- Wrong inner space calculation
- Missing last row single star

---

## **🔟 Complexity**

- Time: **O(N²)**
- Space: **O(1)**

---

## **1️⃣1️⃣ Code (Correct & Working)**

```python
n = int(input())

for i in range(n):
    spaces = " " * i

    if i == 0:
        print("* " * n)
    elif i == n - 1:
        print(spaces + "*")
    else:
        inner_spaces = "  " * ((n - i) - 2)
        print(spaces + "* " + inner_spaces + "*")
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

## **1️⃣3️⃣ Dry Run (N = 4)**

```
* * * *
 *   *
  * *
   *
```

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output                  |
| ----: | ----------------------- |
|     1 | `*`                     |
|     3 | Inverted hollow pyramid |
|     5 | Matches sample          |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- First row is always **full stars**
- Last row is always **one star**
- Middle rows need **two stars only**
- Inner hollow spaces decrease each row

---

## **1️⃣6️⃣ Result**

The program prints the **correct inverted hollow pyramid**.

---

## **1️⃣7️⃣ Conclusion**

This solution is **fully correct**, **fits your learning level**, and uses **only one loop with necessary conditions**.

---
