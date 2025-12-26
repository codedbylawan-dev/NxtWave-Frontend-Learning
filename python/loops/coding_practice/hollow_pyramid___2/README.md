# ✅ **Hollow Pyramid – 2 (Numbers)**

---

## **1️⃣ Question**

Given a number **N**, print a **Hollow Pyramid** of
**(2 × N − 1) rows** using **numbers**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read `N`
- Total rows = `2*N - 1`
- Increase numbers till middle
- Decrease numbers after middle
- Print:

  - Single number at edges
  - Spaces in between

---

## **3️⃣ Objective**

To print a **hollow numeric pyramid** with correct spacing and symmetry.

---

## **4️⃣ Purpose**

This problem helps you understand:

- Upper and lower pyramid logic
- Middle row handling
- Space control between numbers

---

## **5️⃣ Theory**

For **N = 4**, total rows = **7**

### Row behavior:

- Row 1 → `1`
- Row 2 → `2 2`
- Middle row → widest hollow
- Then numbers decrease symmetrically

Spaces increase and decrease to form the hollow shape.

---

## **6️⃣ Step-by-Step Explanation**

1. Read input `N`
2. Loop from `1` to `2*N - 1`
3. Decide the number for the row:

   - If row ≤ N → number = row
   - Else → number = `2*N - row`

4. Print:

   - Single number if it’s the first or last occurrence
   - Otherwise, number + spaces + number

---

## **7️⃣ Method**

- Use one `for` loop
- Use `if-else` conditions
- Use string repetition for spacing

---

## **8️⃣ Constraints**

- `N ≥ 1`
- Space after every number

---

## **9️⃣ Common Mistakes**

- Printing extra spaces at the end
- Wrong middle row calculation
- Breaking symmetry

---

## **🔟 Complexity**

- **Time:** O(N)
- **Space:** O(1)

---

## **1️⃣1️⃣ Code**

```python
n = int(input())
total_rows = 2 * n - 1

for i in range(1, total_rows + 1):
    if i <= n:
        num = i
    else:
        num = total_rows - i + 1

    if num == 1:
        print("1")
    else:
        inner_spaces = "  " * (num - 2)
        print(str(num) + " " + inner_spaces + str(num))
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
1
2 2
3   3
4     4
3   3
2 2
1
```

---

## **1️⃣3️⃣ Dry Run (N = 3)**

```
1
2 2
3   3
2 2
1
```

---

## **1️⃣4️⃣ Notes / Key Takeaways**

- Middle row is the widest
- Numbers increase then decrease
- Inner spaces create the hollow effect
- One loop is enough with correct conditions

---

## **1️⃣5️⃣ Result**

The program prints a **perfect hollow numeric pyramid** with exact spacing.

---

## **1️⃣6️⃣ Conclusion**

This solution follows your **current learning level**, keeps logic **simple**, and produces the **exact required pattern** without confusion.

---
