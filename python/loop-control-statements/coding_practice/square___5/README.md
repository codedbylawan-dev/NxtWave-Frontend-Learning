# 🧩 **Square – 5**

---

## **1️⃣ Question**

Given a starting number **S** and a number **N**,
print a square of **N rows** and **N columns** using numbers starting from **S**.

Example for `S = 3`, `N = 4`:

```
3 4 5 6
3 4 5 6
3 4 5 6
3 4 5 6
```

---

## **2️⃣ Category**

**Loops → Pattern Printing → Row Construction**

---

## **3️⃣ Outline**

- Read **S**
- Read **N**
- Build one row as a string:

  - from `S` to `S + N - 1`

- Print that row **N times**

---

## **4️⃣ Objective**

Learn how to **generate a row once** and **reuse it** to form a square.

---

## **5️⃣ Purpose**

This builds:

- Pattern logic without nested loops
- String construction control
- Repetition using a single loop

---

## **6️⃣ Theory**

If every row is the same,
we only need to **construct one row** correctly,
then print it again and again.

---

## **7️⃣ Step-by-Step Explanation**

1. Read **S**
2. Read **N**
3. Create empty string `row`
4. Use a loop from `0` to `N-1`

   - Append `S + i` and a space to `row`

5. Print `row` exactly **N times**

---

## **8️⃣ Method**

Single loop for row creation
Single loop for row printing

---

## **9️⃣ Constraints**

- Exactly **N numbers per row**
- Exactly **N rows**
- Space after every number

---

## **🔟 Common Mistakes**

- Forgetting space after each number
- Printing while building the row
- Off-by-one error in range

---

## **1️⃣1️⃣ Complexity**

- **Time:** `O(N²)`
- **Space:** `O(N)`

---

## **1️⃣2️⃣ Code**

```python
s = int(input())
n = int(input())

row = ""

for i in range(n):
    row = row + str(s + i) + " "

for i in range(n):
    print(row.strip())
```

---

## **1️⃣3️⃣ Example**

### Input

```
3
4
```

### Output

```
3 4 5 6
3 4 5 6
3 4 5 6
3 4 5 6
```

---

## **1️⃣4️⃣ Dry Run**

For `S = 3`, `N = 4`

Row built once → `"3 4 5 6 "`

Printed 4 times → square formed.

---

## **1️⃣5️⃣ Test Cases Table**

| S   | N   | Output         |
| --- | --- | -------------- |
| 1   | 3   | 1 2 3 (3 rows) |
| 5   | 2   | 5 6 (2 rows)   |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- You can simulate nested behavior using smart construction
- Build once, reuse many times
- Patterns are about **structure**, not syntax

---

## **1️⃣7️⃣ Real-Life Application**

Used in:

- Table generation
- Grid displays
- Matrix formatting

---

## **1️⃣8️⃣ Practice Questions**

1. Reverse each row.
2. Start from the last number.
3. Print square using decreasing numbers.

---

## **1️⃣9️⃣ Result**

You created a 2D pattern **without nested loops**.

---

## **2️⃣0️⃣ Conclusion**

You’re now controlling **multi-line structures** with simple tools.
This is how real problem solvers think.

---
