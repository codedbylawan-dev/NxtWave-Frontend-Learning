# ✅ **10 Numbers After N**

---

## **1️⃣ Question**

Read N and print the next **10 numbers**, each on a new line.

---

## **2️⃣ Outline**

- Read N
- Start from N + 1
- Print 10 numbers using a while loop

---

## **3️⃣ Objective**

Practice using while loops to generate a sequence.

---

## **4️⃣ Purpose**

Strengthens loop control and counter usage.

---

## **5️⃣ Theory**

If N = 2, next 10 numbers are:
3, 4, 5, ..., 12

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set current = N + 1
3. Loop 10 times
4. Print current
5. Increase current by 1

---

## **7️⃣ Method**

Use while loop + increment.

---

## **8️⃣ Constraints**

- Always print exactly 10 numbers
- Each number on its own line

---

## **9️⃣ Common Mistakes**

❌ Forgetting to increment
❌ Printing extra numbers
❌ Starting from N instead of N+1

---

## 🔟 Complexity

O(10) → constant time
O(1) space

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

count = 0
current = N + 1

while count < 10:
    print(current)
    current = current + 1
    count = count + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
2
```

Output:

```
3
4
5
6
7
8
9
10
11
12
```

---

## **1️⃣3️⃣ Dry Run**

N = 11
current = 12
Loop prints 12 to 21

---

## **1️⃣4️⃣ Test Cases**

| Input | Output Start | Output End |
| ----- | ------------ | ---------- |
| 2     | 3            | 12         |
| 11    | 12           | 21         |
| 0     | 1            | 10         |

---

## **1️⃣5️⃣ Notes**

- Use N+1 as starting value
- Loop runs exactly 10 times

---

## **1️⃣6️⃣ Practice**

Print 20 numbers after N.

---

## **1️⃣7️⃣ Result**

Correctly prints next 10 numbers in sequence.

---

## **1️⃣8️⃣ Conclusion**

Simple loop problem to improve sequence printing.

---
