# ✅ **Sum of N Natural Numbers (For Loop)**

---

## **1️⃣ Question**

Given a number **N**, print the **sum of natural numbers from 1 to N**.

---

## **1.5️⃣ Category**

For Loop → Natural Numbers → Accumulation (Sum)

---

## **2️⃣ Outline**

- Read N
- Initialize sum as 0
- Loop from 1 to N
- Add each number to sum
- Print sum

---

## **3️⃣ Objective**

To calculate the sum of natural numbers using a **for loop**.

---

## **4️⃣ Purpose**

Builds understanding of how values are accumulated step-by-step inside a loop.

---

## **5️⃣ Theory**

Natural numbers start from **1**.
The sum is obtained by adding each number one by one.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the value of N
2. Set `total = 0`
3. Start loop from 1 to N
4. Add current number to total
5. After loop ends, print total

---

## **7️⃣ Method**

Use:

- `for` loop
- `range()`
- Addition (`+`)
- Variable to store sum

---

## **8️⃣ Constraints**

- N is a positive integer
- Output must be a single integer

---

## **9️⃣ Common Mistakes**

❌ Forgetting to initialize sum variable
❌ Printing inside the loop instead of after loop
❌ Using wrong range

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

total = 0
for i in range(1, N + 1):
    total = total + i

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

N = 3

- i = 1 → total = 0 + 1 = 1
- i = 2 → total = 1 + 2 = 3
- i = 3 → total = 3 + 3 = 6

Printed output → `6`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----- | ------ |
| 1     | 1      |
| 3     | 6      |
| 6     | 21     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always initialize sum before loop
- Add numbers inside the loop
- Print result after loop

---

## **1️⃣6️⃣ Real-Life Application**

- Total marks calculation
- Summing expenses
- Counting totals

---

## **1️⃣7️⃣ Practice Questions**

1. Find sum of first N even numbers
2. Find sum of numbers from M to N
3. Find sum of squares from 1 to N

---

## **1️⃣8️⃣ Result**

The program correctly prints the sum of natural numbers from 1 to N.

---

## **1️⃣9️⃣ Conclusion**

A fundamental loop problem that teaches accumulation using a counter.

---
