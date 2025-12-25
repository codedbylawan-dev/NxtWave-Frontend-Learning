# ✅ **Right Angled Triangle – 7**

---

## **1️⃣ Question**

Given a number **N**, print a **Right Angled Triangle of N rows** using stars (`*`) and hashes (`#`).

- The **first N − 1 rows** contain stars (`*`)
- The **last row** contains hashes (`#`)
- The triangle is **right-aligned**

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from 1 to N
- Print spaces first
- Print stars for first rows
- Print hashes for last row

---

## **3️⃣ Objective**

To print a **right-aligned right angled triangle** using **stars and hashes**, without using nested loops.

---

## **4️⃣ Purpose**

This problem helps you understand:

- conditional logic inside loops
- how to treat the **last row differently**
- right alignment using spaces

---

## **5️⃣ Theory**

For a right-aligned triangle:

- Total rows = **N**
- For each row:

  - Spaces = **N − row**
  - If it is **last row** → print `#`
  - Else → print `*`

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Start loop from 1 to N
3. For each row:

   - Print spaces using `" " * (N - row)`
   - If row equals N:

     - Print `#` repeated N times

   - Else:

     - Print `*` repeated row times

---

## **7️⃣ Method**

Use:

- for loop
- if condition
- string repetition
- single `print()` per row

---

## **8️⃣ Constraints**

- N ≥ 1
- Last row must contain only `#`

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Printing `#` in wrong rows
❌ Forgetting spaces before stars

---

## **🔟 Complexity**

Time: **O(N²)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code (NO nested loops – ONLY what you learned)**

```python
N = int(input())

for row in range(1, N + 1):
    spaces = " " * (N - row)

    if row == N:
        print(spaces + "#" * N)
    else:
        print(spaces + "*" * row)
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
```

### Output

```
    *
   **
  ***
 ****
#####
```

---

## **1️⃣3️⃣ Dry Run**

For **N = 3**

- row = 1 → `"  "` + `*` → `  *`
- row = 2 → `" "` + `**` → ` **`
- row = 3 → `""` + `###` → `###`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Pattern         |
| ----: | ---------------------- |
|     1 | `#`                    |
|     3 | `  *`, ` **`, `###`    |
|     5 | matches sample exactly |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Last row needs **special handling**
- Spaces control right alignment
- String repetition avoids nested loops
- Very beginner-friendly logic

---

## **1️⃣6️⃣ Real-Life Application**

- Console UI formatting
- Pattern-based problems
- Strengthening loop + condition skills

---

## **1️⃣7️⃣ Practice Questions**

1. Replace `*` with numbers
2. Print same pattern left-aligned
3. Print inverted version

---

## **1️⃣8️⃣ Result**

The program correctly prints a **right-aligned right angled triangle with stars and hashes**.

---

## **1️⃣9️⃣ Conclusion**

This solution is **simple, clean, and 100% aligned** with your current learning level and **NxtWave expectations** ✅

---
