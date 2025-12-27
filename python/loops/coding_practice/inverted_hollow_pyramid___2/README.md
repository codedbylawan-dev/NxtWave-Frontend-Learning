# ✅ **Inverted Hollow Pyramid – Numbers**

---

## **1️⃣ Question**

Given a number **N**, print an **Inverted Hollow Pyramid** of
**(2 × N − 1)** rows using numbers.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Calculate total rows
- Loop through rows
- Decide number and spaces
- Print hollow structure

---

## **3️⃣ Objective**

To print an **inverted hollow pyramid of numbers** using:

- one `for` loop
- conditional statements
- string repetition

---

## **4️⃣ Purpose**

This problem helps you understand:

- symmetric patterns
- inverted pyramid logic
- hollow pattern construction

---

## **5️⃣ Theory**

- Total rows = `2 × N − 1`
- Pattern increases till `N`, then decreases
- Each row contains:

  - left spaces
  - first number
  - hollow spaces (if needed)
  - last number

---

## **6️⃣ Step-by-Step Explanation**

1. Read input `N`
2. Compute `total_rows = 2 * N - 1`
3. Loop from `0` to `total_rows - 1`
4. Decide:

   - which number to print
   - how many left spaces

5. Print:

   - only number if `num == 1`
   - else hollow row with same number on both sides

---

## **7️⃣ Method**

- Use `for` loop
- Use `if-else`
- Use string repetition (`"  "`)

---

## **8️⃣ Constraints**

- `N ≥ 1`
- Use **double spaces** for alignment

---

## **9️⃣ Common Mistakes**

❌ Wrong left spacing
❌ Extra space after last number
❌ Printing inner spaces for `num = 1`

---

## **🔟 Complexity**

- Time: **O(N²)**
- Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
n = int(input())

total_rows = 2 * n - 1

for i in range(total_rows):
    if i < n:
        num = i + 1
        left_spaces = "  " * (n - i - 1)
    else:
        num = total_rows - i
        left_spaces = "  " * (i - n + 1)

    if num == 1:
        print(left_spaces + str(num))
    else:
        inner_spaces = "  " * (num - 2)
        print(left_spaces + str(num) + " " + inner_spaces + str(num))
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
```

### Output

```
    1
  2 2
3   3
  2 2
    1
```

---

## **1️⃣3️⃣ Dry Run**

For `N = 3`

- Top half → numbers increase
- Middle → widest row
- Bottom half → numbers decrease
- Hollow spaces increase then decrease

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Type                   |
| ----: | ----------------------------- |
|     1 | Single `1`                    |
|     3 | Symmetric hollow pyramid      |
|     5 | Wider inverted hollow pyramid |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Total rows = `2N - 1`
- Left spaces control alignment
- Hollow space = `num - 2`
- Print single number when `num == 1`

---

## **1️⃣6️⃣ Real-Life Application**

- Console pattern design
- Grid-based layouts
- Algorithmic thinking

---

## **1️⃣7️⃣ Practice Questions**

1. Replace numbers with `*`
2. Print same pattern left-aligned
3. Remove hollow and make it solid

---

## **1️⃣8️⃣ Result**

The program correctly prints an **Inverted Hollow Number Pyramid**.

---

## **1️⃣9️⃣ Conclusion**

This solution follows your **exact learning style**,
uses **one loop + conditions**,
and matches **NxtWave expectations** perfectly ✅

---
