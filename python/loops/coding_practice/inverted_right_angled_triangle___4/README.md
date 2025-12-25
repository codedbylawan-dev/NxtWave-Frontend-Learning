# ✅ **Inverted Right Angled Triangle – 4**

---

## **1️⃣ Question**

Given a number **N**, print an **Inverted Right Angled Triangle of N rows** using numbers, aligned to the **right**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read N
- Loop from N down to 1
- Print leading spaces
- Print numbers

---

## **3️⃣ Objective**

To print a **right-aligned inverted triangle** using **one loop** and **string repetition**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- right alignment using spaces
- inverted pattern logic
- combining spaces + numbers

---

## **5️⃣ Theory**

For each row:

- **Spaces before numbers** = `N - row`
- **Number printed** = `row`
- **Times printed** = `row`

Example for **N = 3**:

| Row | Spaces | Numbers |
| --: | -----: | ------- |
|   3 |      0 | 333     |
|   2 |      1 | 22      |
|   1 |      2 | 1       |

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from N down to 1
3. For each row:

   - Print `" "` repeated `(N - row)`
   - Print the number repeated `row` times

4. Print everything in one line

---

## **7️⃣ Method**

Use:

- reverse `for` loop
- string repetition
- single `print()`

---

## **8️⃣ Constraints**

- N ≥ 1
- One space indentation per row

---

## **9️⃣ Common Mistakes**

❌ Missing leading spaces
❌ Printing numbers before spaces
❌ Using nested loops

---

## **🔟 Complexity**

Time: **O(N²)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code (FINAL – CORRECT FORMAT)**

```python
N = int(input())

for row in range(N, 0, -1):
    spaces = " " * (N - row)
    numbers = str(row) * row
    print(spaces + numbers)
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
```

### Output

```
333
 22
  1
```

---

## **1️⃣3️⃣ Dry Run**

For **N = 3**

- row = 3 → `" " * 0 + "333"` → `333`
- row = 2 → `" " * 1 + "22"` → ` 22`
- row = 1 → `" " * 2 + "1"` → `  1`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output                          |
| ----: | ------------------------------- |
|     1 | `1`                             |
|     3 | right-aligned inverted triangle |
|     6 | correct indentation maintained  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Right alignment = **spaces before content**
- Inversion = **loop from N to 1**
- String repetition avoids nested loops

---

## **1️⃣6️⃣ Result**

The program now **perfectly matches your required output format** ✅

---

## **1️⃣7️⃣ Conclusion**

This is the **correct, final, and NxtWave-safe solution**, built **only from what you’ve learned**.

---
