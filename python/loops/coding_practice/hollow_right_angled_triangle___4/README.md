# ✅ **Hollow Right Angled Triangle – 4**

---

## **1️⃣ Question**

Given a number **N**, print a **Hollow Right Angled Triangle** of **N rows** using:

- Hashes (`#`) in the **first row**
- Pluses (`+`) in the remaining rows

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read the number `N`
- Loop from `0` to `N - 1`
- Print:

  - Hashes in the first row
  - Pluses on the left and diagonal in middle rows
  - A single plus in the last row

---

## **3️⃣ Objective**

To print a **hollow right angled triangle** with correct alignment and no extra spaces.

---

## **4️⃣ Purpose**

This problem helps you understand:

- Row-based pattern control
- How spaces shift the diagonal
- How different rows need different outputs

---

## **5️⃣ Theory**

- Total rows = **N**
- Each row has a different structure:

### Row-wise rules

1. **First row**

   - Contains `N` hashes
   - Each hash followed by a space

2. **Middle rows**

   - Start with `+ `
   - Spaces decrease as row number increases
   - End with another `+`

3. **Last row**

   - Contains only one `+`

---

## **6️⃣ Step-by-Step Explanation**

1. Take input `N`
2. Loop through rows using `i`
3. Check:

   - If `i == 0` → print hashes
   - If `i == N - 1` → print single plus
   - Otherwise:

     - Print `+`
     - Add required inner spaces
     - Print another `+`

---

## **7️⃣ Method**

- Use a single `for` loop
- Use string repetition for spaces
- Use conditions to decide row content

---

## **8️⃣ Constraints**

- `N ≥ 2`
- No trailing spaces after the last symbol

---

## **9️⃣ Common Mistakes**

- Printing extra spaces after the diagonal
- Miscounting inner spaces
- Treating all rows the same

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
        print("# " * n)
    elif i == n - 1:
        print("+")
    else:
        inner_spaces = "  " * (n - i - 2)
        print("+ " + inner_spaces + "+")
```

---

## **1️⃣2️⃣ Example**

### Input

```
6
```

### Output

```
# # # # # #
+       +
+     +
+   +
+ +
+
```

---

## **1️⃣3️⃣ Dry Run (N = 5)**

| Row | Output      |
| --: | ----------- |
|   0 | `# # # # #` |
|   1 | `+     +`   |
|   2 | `+   +`     |
|   3 | `+ +`       |
|   4 | `+`         |

---

## **1️⃣4️⃣ Notes / Key Takeaways**

- First row is always full
- Middle rows shrink inward
- Last row ends the triangle cleanly
- Pattern width reduces naturally

---

## **1️⃣5️⃣ Result**

The program prints a **perfect hollow right angled triangle** with correct alignment.

---

## **1️⃣6️⃣ Conclusion**

This solution follows a **clear row-based pattern**, matches the expected output exactly, and fits perfectly with your current learning level.

---
