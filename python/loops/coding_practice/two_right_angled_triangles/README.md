# ✅ **Two Right Angled Triangles**

---

## **1️⃣ Question**

Given a number **N**, print **two right-angled triangles**, each with **N rows**, using numbers starting from **1**.

Total rows printed = **2 × N**.

---

## **2️⃣ Outline**

- Read N
- First triangle: print 1, 2 2, 3 3 3, …
- Second triangle: same again
- Use loops for both triangles

---

## **3️⃣ Objective**

To print two identical number triangles one after another.

---

## **4️⃣ Purpose**

Practice repeating a pattern multiple times.

---

## **5️⃣ Theory**

If N = 3, each triangle is:

```
1
2 2
3 3 3
```

Total output:

```
1
2 2
3 3 3
1
2 2
3 3 3
```

---

## **6️⃣ Step-by-Step Explanation**

1. Loop from row = 1 to N → print row repeated row times
2. Repeat the same loop again

---

## **7️⃣ Method**

- while loop
- repetition using `("row " * row)`
- increment row

---

## **8️⃣ Constraints**

- N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Printing stars instead of numbers
❌ Missing the second triangle
❌ Wrong spacing

---

## 🔟 Complexity

O(N)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

# First Triangle
row = 1
while row <= N:
    print((str(row) + " ") * row)
    row = row + 1

# Second Triangle
row = 1
while row <= N:
    print((str(row) + " ") * row)
    row = row + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
3
```

Output:

```
1
2 2
3 3 3
1
2 2
3 3 3
```

---

## **1️⃣3️⃣ Dry Run**

For N = 2:

Triangle 1:

- row 1 → `1`
- row 2 → `2 2`

Triangle 2:

- row 1 → `1`
- row 2 → `2 2`

---

## **1️⃣4️⃣ Test Cases**

| Input | Output (short) |
| ----- | -------------- |
| 1     | 1 / 1          |
| 2     | 1, 2 2, 1, 2 2 |
| 4     | 8 total rows   |

---

## **1️⃣5️⃣ Notes**

Two triangles must always print back-to-back.

---

## **1️⃣6️⃣ Result**

Correctly prints two right-angled triangles of numbers.

---

## **1️⃣7️⃣ Conclusion**

Simple pattern repetition using loops.

---
