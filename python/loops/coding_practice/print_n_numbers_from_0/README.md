# ✅ **Print N Numbers from 0**

---

## **1️⃣ Question**

Read a number **N** and print **N numbers starting from 0**, each on a new line.

---

## **2️⃣ Outline**

- Read N
- Start counter at 0
- Print counter N times
- Increase counter each time

---

## **3️⃣ Objective**

Print numbers from 0 to N-1 using a while loop.

---

## **4️⃣ Purpose**

Practice simple counting with loops.

---

## **5️⃣ Theory**

If N = 5 → numbers are:
0, 1, 2, 3, 4

---

## **6️⃣ Step-by-Step Explanation**

1. Set counter = 0
2. While counter < N → print counter
3. Increase counter
4. Repeat

---

## **7️⃣ Method**

Use one while loop.

---

## **8️⃣ Constraints**

N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Forgetting to increment counter
❌ Printing extra numbers

---

## 🔟 Complexity

O(N)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

counter = 0
while counter < N:
    print(counter)
    counter = counter + 1
```

---

## **1️⃣2️⃣ Example**

Input

```
2
```

Output

```
0
1
```

---

## **1️⃣3️⃣ Dry Run**

N = 3
counter = 0 → print 0
counter = 1 → print 1
counter = 2 → print 2
stop

---

## **1️⃣4️⃣ Test Cases**

| N   | Output    |
| --- | --------- |
| 1   | 0         |
| 3   | 0 1 2     |
| 5   | 0 1 2 3 4 |

---

## **1️⃣5️⃣ Result**

Correctly prints N numbers starting from 0.

---

## **1️⃣6️⃣ Conclusion**

A simple counting problem using a while loop.

---
