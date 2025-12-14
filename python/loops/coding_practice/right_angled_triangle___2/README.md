# ✅ **Right Angled Triangle – 2**

---

## **1️⃣ Question**

Write a program that reads a number **N** and prints a right-angled triangle using numbers from **1 to N**.

---

## **2️⃣ Outline**

- Read N
- Start count at 1
- Print the number repeated count times
- Increase count until N

---

## **3️⃣ Objective**

To practice creating patterns using a while loop.

---

## **4️⃣ Purpose**

Helps understand repetition using loops.

---

## **5️⃣ Theory**

If N = 5, the triangle is:

```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set count = 1
3. While count <= N:

   - Print count repeated count times
   - Increase count

---

## **7️⃣ Method**

- integer input
- while loop
- string multiplication

---

## **8️⃣ Constraints**

- N ≥ 1

---

## **9️⃣ Common Mistakes**

- Not increasing count
- Wrong spacing
- Printing extra rows

---

## 🔟 Complexity

O(N)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

count = 1
while count <= N:
    print((str(count) + " ") * count)
    count = count + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
5
```

Output:

```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
```

---

## **1️⃣3️⃣ Dry Run**

For N = 3:

- count = 1 → print `1`
- count = 2 → print `2 2`
- count = 3 → print `3 3 3`

---

## **1️⃣4️⃣ Test Cases**

| Input | Output          |
| ----- | --------------- |
| 1     | 1               |
| 3     | 1 / 2 2 / 3 3 3 |
| 5     | 5 rows          |

---

## **1️⃣5️⃣ Notes**

Patterns repeat based on row number.

---

## **1️⃣6️⃣ Result**

Correct right-angled number triangle is printed.

---

## **1️⃣7️⃣ Conclusion**

Simple pattern using while loop and string multiplication.

---
