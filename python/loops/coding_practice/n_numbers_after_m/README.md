# ✅ **N Numbers After M**

---

## **1️⃣ Question**

Read two integers **M** and **N**, then print **N numbers after M**, each on a new line.

---

## **2️⃣ Outline**

- Read M
- Read N
- Start from M + 1
- Print N numbers

---

## **3️⃣ Objective**

Use a while loop to generate a sequence starting after M.

---

## **4️⃣ Purpose**

Strengthen control of counters and loop logic.

---

## **5️⃣ Theory**

If:
M = 3
N = 5

Numbers after 3 → **4, 5, 6, 7, 8**

---

## **6️⃣ Step-by-Step Explanation**

1. Read M
2. Read N
3. Let `current = M + 1`
4. Loop N times
5. Print `current`
6. Increment `current`

---

## **7️⃣ Method**

Use while loop and increment by 1 each time.

---

## **8️⃣ Constraints**

- Print exactly N numbers
- Each number on its own line

---

## **9️⃣ Common Mistakes**

❌ Looping incorrectly
❌ Starting from M instead of M+1
❌ Printing extra numbers

---

## 🔟 Complexity

Time → O(N)
Space → O(1)

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

count = 0
current = M + 1

while count < N:
    print(current)
    current = current + 1
    count = count + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
3
5
```

Output:

```
4
5
6
7
8
```

---

## **1️⃣3️⃣ Dry Run**

M = 11
N = 2
Start → 12
Print → 12, 13

---

## **1️⃣4️⃣ Test Cases**

| M   | N   | Output Start | Output End |
| --- | --- | ------------ | ---------- |
| 3   | 5   | 4            | 8          |
| 11  | 2   | 12           | 13         |
| 0   | 4   | 1            | 4          |

---

## **1️⃣5️⃣ Notes**

- Always begin from M + 1
- Loop count must be exactly N

---

## **1️⃣6️⃣ Practice**

Print numbers from M to M + N (including M itself).

---

## **1️⃣7️⃣ Result**

Program prints N numbers after M correctly.

---

## **1️⃣8️⃣ Conclusion**

A direct and simple while-loop based sequence problem.

---
