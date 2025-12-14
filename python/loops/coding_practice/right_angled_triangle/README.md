# ✅ **Right Angled Triangle**

---

## **1️⃣ Question**

Given N, print a right-angled triangle of stars from 1 star up to N stars.

---

## **2️⃣ Outline**

- Read N
- Start with `count = 1`
- Print `count` stars using `"*" * count`
- Increase count until it reaches N

---

## **3️⃣ Objective**

To print a growing star pattern using a single loop.

---

## **4️⃣ Purpose**

Shows how string repetition replaces nested loops in patterns.

---

## **5️⃣ Theory**

If N = 4 → print:

```
*
**
***
****
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Start `count = 1`
3. While count ≤ N

   - print `"*" * count`
   - count = count + 1

---

## **7️⃣ Method**

- while loop
- string multiplication (`"*" * count`)

---

## **8️⃣ Constraints**

N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Not updating count
❌ Adding spaces (not required here)
❌ Printing fixed stars

---

## 🔟 Complexity

O(N)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

count = 1
while count <= N:
    print("*" * count)
    count = count + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
3
```

Output:

```
*
**
***
```

---

## **1️⃣3️⃣ Dry Run**

N = 3
count = 1 → "\*"
count = 2 → "**"
count = 3 → "\***"

---

## **1️⃣4️⃣ Test Cases**

| N   | Output Shape |
| --- | ------------ |
| 1   | \*           |
| 4   | 4 rows       |
| 6   | 6 rows       |

---

## **1️⃣5️⃣ Notes**

String repetition avoids nested loops.

---

## **1️⃣6️⃣ Result**

Triangle printed correctly with 1 loop.

---

## **1️⃣7️⃣ Conclusion**

A simple increasing-pattern task using basic loop logic.

---
