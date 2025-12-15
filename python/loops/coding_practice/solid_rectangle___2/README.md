# ✅ **Solid Rectangle – 2**

---

## **1️⃣ Question**

Print a rectangle pattern of **M rows** and **N columns** using the plus character (**+**).

There must be a **space after each +**.

---

## **1.5️⃣ Category**

For Loop → Pattern Printing → Rectangle

---

## **2️⃣ Outline**

- Read M (rows)
- Read N (columns)
- Create one row using string repetition
- Print that row M times

---

## **3️⃣ Objective**

To print a rectangle using a **single for loop**.

---

## **4️⃣ Purpose**

This problem helps you practice:

- for loop
- string repetition
- pattern printing without nesting

---

## **5️⃣ Theory**

- `"+ " * N` creates **one full row**
- Printing that row **M times** forms a rectangle

---

## **6️⃣ Step-by-Step Explanation**

1. Read M
2. Read N
3. Create one row using `"+ " * N`
4. Print the row inside a for loop M times

---

## **7️⃣ Method**

Use:

- for loop
- string repetition (`*`)
- print

---

## **8️⃣ Constraints**

- M and N are positive integers
- Space after each `+` is required

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Forgetting space after `+`
❌ Printing wrong number of rows

---

## 🔟 Complexity

Time: **O(M)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code (NO nested loop)**

```python
M = int(input())
N = int(input())

row = "+ " * N

for i in range(M):
    print(row)
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
5
```

### Output

```
+ + + + +
+ + + + +
+ + + + +
```

---

## **1️⃣3️⃣ Notes / Key Takeaways**

- String repetition replaces inner loop
- One loop is enough
- Cleaner and beginner-friendly

---

## **1️⃣4️⃣ Result**

The rectangle is printed correctly **without using nested loops**.

---
