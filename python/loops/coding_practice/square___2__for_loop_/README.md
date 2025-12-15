# ✅ **Square – 2 (For Loop)**

---

## **1️⃣ Question**

Given a number **M**, print a **square of M rows and M columns** using numbers.

Each row should contain the **same number**, starting from **1** up to **M**.

---

## **1.5️⃣ Category**

For Loop → Pattern Printing → Numbers

---

## **2️⃣ Outline**

- Read M
- Loop from 1 to M
- Print the current number repeated M times in one row

---

## **3️⃣ Objective**

To print a numeric square pattern using a **single for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- loop iteration
- number repetition using strings
- pattern printing without nested loops

---

## **5️⃣ Theory**

If M = 4

The output should be:

```
1111
2222
3333
4444
```

Each row number is printed **M times**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the value of M
2. Start a loop from 1 to M
3. Convert the number to string
4. Repeat it M times
5. Print the result

---

## **7️⃣ Method**

Use:

- for loop
- string repetition
- print statement

---

## **8️⃣ Constraints**

- M is a positive integer
- No spaces between numbers

---

## **9️⃣ Common Mistakes**

❌ Adding spaces between numbers
❌ Using nested loops
❌ Printing all numbers in one line

---

## 🔟 Complexity

Time: **O(M)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
M = int(input())

for i in range(1, M + 1):
    print(str(i) * M)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
1111
2222
3333
4444
```

---

## **1️⃣3️⃣ Dry Run**

M = 3

Loop runs with i = 1, 2, 3

Printed lines:

```
111
222
333
```

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output        |
| ----- | ------------- |
| 1     | 1             |
| 3     | 111 222 333   |
| 5     | 11111 … 55555 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Convert number to string before repetition
- One loop is enough
- Clean and beginner-friendly approach

---

## **1️⃣6️⃣ Real-Life Application**

- Number grids
- Console-based tables
- Learning pattern logic

---

## **1️⃣7️⃣ Practice Questions**

1. Print square using only `0`
2. Print square using `+`
3. Print rectangle using numbers

---

## **1️⃣8️⃣ Result**

The program prints a correct **number square pattern**.

---

## **1️⃣9️⃣ Conclusion**

A simple numeric pattern problem reinforcing **for loop** and **string repetition** concepts.

---
