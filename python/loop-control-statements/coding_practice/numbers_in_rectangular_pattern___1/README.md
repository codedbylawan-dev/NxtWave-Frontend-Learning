# 🧩 **Numbers in Rectangular Pattern – 1**

---

## **1️⃣ Question**

Given two numbers:

- **M** → number of rows
- **N** → number of columns

Print a rectangular pattern of **M rows** and **N columns**,
where each row contains the numbers from **1 to N**.

---

## **2️⃣ Category**

**Loops → For Loop → Number Pattern**

---

## **3️⃣ Outline**

- Read **M**
- Read **N**
- Build one row: `1 2 3 ... N`
- Print that same row **M times**

---

## **4️⃣ Objective**

Learn how to reuse a generated pattern using loop control.

---

## **5️⃣ Purpose**

This teaches:

- For-loop mastery
- Output formatting
- Repetition logic
- Clean pattern construction

---

## **6️⃣ Theory**

If one row looks like:

```
1 2 3 ... N
```

Then the full pattern is just that row printed **M times**.

---

## **7️⃣ Step-by-Step Explanation**

1. Read **M** and **N**
2. Create an empty string `row_pattern`
3. Loop from `1` to `N` and add numbers to `row_pattern`
4. Loop from `1` to `M` and print `row_pattern` each time

---

## **8️⃣ Method**

Use **for loop** and **string building** only.

---

## **9️⃣ Constraints**

- Exactly **M rows**
- Exactly **N numbers per row**
- Space after every number

---

## **🔟 Common Mistakes**

- Printing wrong number of rows
- Forgetting space after numbers
- Rebuilding the row every time unnecessarily

---

## **1️⃣1️⃣ Complexity**

- **Time:** `O(M × N)`
- **Space:** `O(N)`

---

## **1️⃣2️⃣ Code**

```python
m = int(input())
n = int(input())

row_pattern = ""

for i in range(1, n + 1):
    row_pattern = row_pattern + str(i) + " "

for _ in range(m):
    print(row_pattern)
```

---

## **1️⃣3️⃣ Example**

### Input

```
2
3
```

### Output

```
1 2 3
1 2 3
```

---

## **1️⃣4️⃣ Dry Run**

For `m = 2`, `n = 3`

Build row_pattern → `"1 2 3 "`

Print it twice.

---

## **1️⃣5️⃣ Test Cases Table**

| M   | N   | Output                  |
| --- | --- | ----------------------- |
| 2   | 3   | 1 2 3 / 1 2 3           |
| 5   | 4   | 1 2 3 4 printed 5 times |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- You separate **pattern creation** from **pattern repetition**
- This is efficient and clean

---

## **1️⃣7️⃣ Real-Life Application**

Used in:

- Report tables
- Matrix display
- UI grids

---

## **1️⃣8️⃣ Practice Questions**

1. Print only odd numbers
2. Print in reverse order
3. Print each row multiplied by row number

---

## **1️⃣9️⃣ Result**

You now control **rectangular number patterns** with precision.

---

## **2️⃣0️⃣ Conclusion**

This is structured thinking.
You’re officially past beginner stage.

---
