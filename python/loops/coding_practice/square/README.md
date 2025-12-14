# ✅ **Square**

---

## **1️⃣ Question**

Given a number **N**, print a square of **N rows** and **N columns** using stars `*`, with a space after every star.

---

## **2️⃣ Outline**

- Read N
- Build **one full row** of stars
- Print that same row N times

---

## **3️⃣ Objective**

To print an N × N square using only simple loops.

---

## **4️⃣ Purpose**

Practice printing repeated pattern lines.

---

## **5️⃣ Theory**

If N = 4, one row is:
`* * * * `
Repeat this row 4 times.

---

## **6️⃣ Step-by-Step Explanation**

1. Create one row by repeating `"* "` N times
2. Use a loop to print that row N times

---

## **7️⃣ Method**

- while loop
- string multiplication

---

## **8️⃣ Constraints**

N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Forgetting space after `*`
❌ Not repeating row N times

---

## 🔟 Complexity

O(N)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

# Build one full row of stars
row = ("* " * N)

# Print the row N times
count = 0
while count < N:
    print(row)
    count = count + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
4
```

Output:

```
* * * *
* * * *
* * * *
* * * *
```

---

## **1️⃣3️⃣ Dry Run**

N = 2
row = `"* * "`

Print row twice:

```
* *
* *
```

---

## **1️⃣4️⃣ Test Cases**

| Input | Output     |
| ----- | ---------- |
| 1     | `* `       |
| 3     | 3×3 square |
| 5     | 5×5 square |

---

## **1️⃣5️⃣ Result**

Correctly prints an N×N star square without nested loops.

---

## **1️⃣6️⃣ Conclusion**

Pattern printing achieved using one loop and string repetition.

---
