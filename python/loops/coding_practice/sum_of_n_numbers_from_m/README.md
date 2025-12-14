# ✅ **Sum of N Numbers from M**

---

## **1️⃣ Question**

Read **M** and **N**, then compute the **sum of N numbers starting from M**.

---

## **2️⃣ Outline**

- Read M
- Read N
- Add numbers: M, M+1, M+2, … for N terms
- Print the total sum

---

## **3️⃣ Objective**

To practice generating a sequence and accumulating a running total.

---

## **4️⃣ Purpose**

Strengthens understanding of loops and sum calculation.

---

## **5️⃣ Theory**

Example: M = 7, N = 3
Numbers: 7, 8, 9
Sum = 24

---

## **6️⃣ Step-by-Step Explanation**

1. Read M
2. Read N
3. Start sum at 0
4. Start number at M
5. Add number to sum
6. Increase number
7. Repeat N times

---

## **7️⃣ Method**

Use while loop + running sum.

---

## **8️⃣ Constraints**

- Must add exactly N numbers
- No extra printing

---

## **9️⃣ Common Mistakes**

❌ Starting from M+1 instead of M
❌ Forgetting to increment number
❌ Forgetting to update sum

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
total = 0
current = M

while count < N:
    total = total + current
    current = current + 1
    count = count + 1

print(total)
```

---

## **1️⃣2️⃣ Example**

Input:

```
7
3
```

Output:

```
24
```

---

## **1️⃣3️⃣ Dry Run**

M = 2, N = 4
Numbers: 2, 3, 4, 5

Sum steps:
0 + 2 = 2
2 + 3 = 5
5 + 4 = 9
9 + 5 = 14

Output → **14**

---

## **1️⃣4️⃣ Test Cases**

| M   | N   | Expected Sum |
| --- | --- | ------------ |
| 7   | 3   | 24           |
| 2   | 10  | 65           |
| 5   | 1   | 5            |
| 0   | 5   | 10           |

---

## **1️⃣5️⃣ Notes**

- Sequence always begins at M
- Loop runs exactly N times

---

## **1️⃣6️⃣ Practice**

Find the **average** of N numbers from M.

---

## **1️⃣7️⃣ Result**

Program correctly computes the sum of N consecutive numbers starting from M.

---

## **1️⃣8️⃣ Conclusion**

A simple loop-based sum problem—great for strengthening fundamentals.

---
