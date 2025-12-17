# ✅ **Inverted Right Angled Triangle – 3**

---

## **1️⃣ Question**

Given a number **N**, print an **Inverted Right Angled Triangle** of **N rows** using stars (`*`) and pluses (`+`).

- The **first row** should contain **N stars**
- The remaining rows should contain **pluses**
- There is a **space after every symbol**

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing → Inverted Triangle

---

## **2️⃣ Outline**

- Read N
- Print first row with N stars
- Print remaining rows with pluses in decreasing order

---

## **3️⃣ Objective**

To print an **inverted triangle pattern** using a **single for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- pattern direction (decreasing)
- controlled repetition
- symbol switching logic

---

## **5️⃣ Theory**

An **Inverted Right Angled Triangle**:

- Starts with **maximum symbols**
- Decreases one symbol per row

We use:

- `"* " * count`
- `"+ " * count`

No nested loops are required.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Print `N` stars in the first row
3. Loop from `N-1` down to `1`
4. Print pluses equal to the current value

---

## **7️⃣ Method**

Use:

- for loop
- string repetition
- print statement

---

## **8️⃣ Constraints**

- N is a positive integer
- Space must be printed after every symbol

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Printing wrong symbol
❌ Forgetting space after symbols

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

print("* " * N)

for i in range(N - 1, 0, -1):
    print("+ " * i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
* * * *
+ + +
+ +
+
```

---

## **1️⃣3️⃣ Dry Run**

N = 4

- First row → `* * * *`
- i = 3 → `+ + +`
- i = 2 → `+ +`
- i = 1 → `+`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Rows |
| ----: | ----------- |
|     3 | 3           |
|     4 | 4           |
|     6 | 6           |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Decreasing loop controls inverted shape
- Symbols can be switched easily
- No nested loop needed

---

## **1️⃣6️⃣ Real-Life Application**

- Console designs
- UI layout patterns
- Visual hierarchy representation

---

## **1️⃣7️⃣ Practice Questions**

1. Inverted triangle with only stars
2. Inverted triangle using numbers
3. Inverted triangle starting with plus

---

## **1️⃣8️⃣ Result**

The program correctly prints the **Inverted Right Angled Triangle** using stars and pluses.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens **reverse looping** and **pattern control** without using nested loops.

---
