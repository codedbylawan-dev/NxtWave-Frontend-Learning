# ✅ **Sum of Numbers from M to N**

---

## **1️⃣ Question**

Given two integers **M** and **N**, print the **sum of all numbers from M to N**.

---

## **1.5️⃣ Category**

For Loop → Summation → Iteration

---

## **2️⃣ Outline**

- Read M
- Read N
- Initialize sum = 0
- Loop from M to N
- Add each number to sum
- Print sum

---

## **3️⃣ Objective**

To calculate the sum of a range of numbers using a **for loop**.

---

## **4️⃣ Purpose**

This problem builds understanding of:

- accumulating values
- loop-based addition
- range handling

---

## **5️⃣ Theory**

If M = 2 and N = 6

Numbers are:

```
2, 3, 4, 5, 6
```

Sum:

```
2 + 3 + 4 + 5 + 6 = 20
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read M
2. Read N
3. Set sum = 0
4. Loop from M to N
5. Add current number to sum
6. Print final sum

---

## **7️⃣ Method**

Use:

- for loop
- addition
- variable to store sum

---

## **8️⃣ Constraints**

- M and N are integers
- M ≤ N

---

## **9️⃣ Common Mistakes**

❌ Forgetting to initialize sum
❌ Printing sum inside loop
❌ Incorrect range end

---

## 🔟 Complexity

Time: **O(N − M + 1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

total = 0
for i in range(M, N + 1):
    total = total + i

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
2
6
```

### Output

```
20
```

---

## **1️⃣3️⃣ Dry Run**

M = 2, N = 6

total = 0
+2 → 2
+3 → 5
+4 → 9
+5 → 14
+6 → 20

---

## **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output |
| --- | --- | ------ |
| 2   | 6   | 20     |
| 10  | 20  | 165    |
| 5   | 5   | 5      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always initialize accumulator variables
- Add inside loop, print after loop
- `range(M, N+1)` includes N

---

## **1️⃣6️⃣ Real-Life Application**

- Total score calculation
- Summing daily expenses
- Range-based totals

---

## **1️⃣7️⃣ Practice Questions**

1. Find sum of even numbers from M to N
2. Find sum of odd numbers from M to N
3. Find sum of squares from M to N

---

## **1️⃣8️⃣ Result**

The program correctly prints the sum from M to N.

---

## **1️⃣9️⃣ Conclusion**

A core loop-based summation problem that strengthens accumulator logic.

---
