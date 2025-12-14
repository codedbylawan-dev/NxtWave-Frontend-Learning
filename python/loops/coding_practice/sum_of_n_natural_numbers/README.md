# ✅ **Sum of N Natural Numbers**

---

## **1️⃣ Question**

Given N, find the sum of natural numbers from 1 to N.

---

## **2️⃣ Outline**

- Start from 1
- Keep adding each number to sum
- Stop when number reaches N

---

## **3️⃣ Objective**

Calculate the cumulative total of the first N natural numbers.

---

## **4️⃣ Purpose**

Strengthens loop logic and running-sum concepts.

---

## **5️⃣ Theory**

Natural numbers from 1 to N.
Sum grows by adding each next number.

Example: N = 6 → 1 + 2 + 3 + 4 + 5 + 6 = **21**

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set sum = 0
3. Set number = 1
4. While number ≤ N:

   - Add number to sum
   - Increase number

5. Print sum

---

## **7️⃣ Method**

Use a while loop to accumulate total.

---

## **8️⃣ Constraints**

N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Forgetting to increment the number
❌ Using wrong initialization
❌ Printing sum inside loop instead of at end

---

## 🔟 Complexity

Time → O(N)
Space → O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

total = 0
num = 1

while num <= N:
    total = total + num
    num = num + 1

print(total)
```

---

## **1️⃣2️⃣ Example**

Input:

```
6
```

Output:

```
21
```

---

## **1️⃣3️⃣ Dry Run**

For N = 3
sum = 0
num = 1 → sum = 1
num = 2 → sum = 3
num = 3 → sum = 6
Stop → print 6

---

## **1️⃣4️⃣ Test Cases**

| Input | Output |
| ----- | ------ |
| 1     | 1      |
| 3     | 6      |
| 5     | 15     |
| 10    | 55     |

---

## **1️⃣5️⃣ Notes**

You are practicing the core pattern:
**Initialize → loop → update → final output**

---

## **1️⃣6️⃣ Practice**

Sum of N even numbers.

---

## **1️⃣7️⃣ Result**

Correct sum printed.

---

## **1️⃣8️⃣ Conclusion**

A perfect foundational loop problem for controlling sums.

---
