# ✅ **Average of the N Numbers**

---

## **1️⃣ Question**

Given **N**, print the **average of the numbers from 1 to N**.

---

## **1.5️⃣ Category**

While Loop → Summation → Arithmetic

---

## **2️⃣ Outline**

- Read N
- Add numbers from 1 to N
- Compute average = sum / N
- Print the result

---

## **3️⃣ Objective**

To calculate the average of the first N natural numbers.

---

## **4️⃣ Purpose**

Strengthens understanding of loops and arithmetic operations.

---

## **5️⃣ Theory**

If N = 4
Numbers → 1, 2, 3, 4
Sum = 10
Average = 10 / 4 = **2.5**

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Start counter = 1
3. Start sum = 0
4. Add counter to sum
5. Increase counter
6. Stop when counter > N
7. Divide sum by N
8. Print average

---

## **7️⃣ Method**

Use a while loop to accumulate sum.

---

## **8️⃣ Constraints**

N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Using division inside loop
❌ Forgetting to increment counter
❌ Printing integer instead of float

---

## 🔟 Complexity

Time: O(N)
Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

sum_value = 0
count = 1

while count <= N:
    sum_value = sum_value + count
    count = count + 1

average = sum_value / N
print(average)
```

---

## **1️⃣2️⃣ Example**

Input:

```
4
```

Output:

```
2.5
```

---

## **1️⃣3️⃣ Dry Run**

N = 3
sum = 1 + 2 + 3 = 6
average = 6 / 3 = 2.0

---

## **1️⃣4️⃣ Test Cases Table**

| N   | Sum | Average |
| --- | --- | ------- |
| 3   | 6   | 2.0     |
| 5   | 15  | 3.0     |
| 7   | 28  | 4.0     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Natural numbers start at 1
- Always compute average after loop

---

## **1️⃣6️⃣ Real-Life Application**

- Average marks
- Average speed calculations

---

## **1️⃣7️⃣ Practice Questions**

1. Average of N even numbers
2. Average of numbers from M to N

---

## **1️⃣8️⃣ Result**

Program correctly prints the average of numbers from 1 to N.

---

## **1️⃣9️⃣ Conclusion**

A simple summation and division problem using a basic while loop.

---
