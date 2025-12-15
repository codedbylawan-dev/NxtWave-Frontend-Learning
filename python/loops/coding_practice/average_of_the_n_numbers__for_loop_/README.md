# ✅ **Average of the N Numbers (For Loop)**

---

## **1️⃣ Question**

Given a number **N**, print the **average of numbers from 1 to N**.

---

## **1.5️⃣ Category**

For Loop → Natural Numbers → Average Calculation

---

## **2️⃣ Outline**

- Read N
- Initialize sum as 0
- Loop from 1 to N
- Add each number to sum
- Divide sum by N
- Print average

---

## **3️⃣ Objective**

To calculate the average of numbers from 1 to N using a **for loop**.

---

## **4️⃣ Purpose**

Helps understand how summation and division work together inside loops.

---

## **5️⃣ Theory**

Average formula:

```
Average = Sum of numbers / Count of numbers
```

For numbers from 1 to N:

- Count = N

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set `total = 0`
3. Loop from 1 to N
4. Add each number to total
5. Divide total by N
6. Print the result

---

## **7️⃣ Method**

Use:

- `for` loop
- `range()`
- Addition and division
- Float output

---

## **8️⃣ Constraints**

- N is a positive integer
- Output must be a float

---

## **9️⃣ Common Mistakes**

❌ Forgetting to divide by N
❌ Using wrong loop range
❌ Printing sum instead of average

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

average = total / N
print(average)
```

---

## **1️⃣2️⃣ Example**

Input:

```
8
```

Output:

```
4.5
```

---

## **1️⃣3️⃣ Dry Run**

N = 4

- total = 1 + 2 + 3 + 4 = 10
- average = 10 / 4 = 2.5

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----- | ------ |
| 1     | 1.0    |
| 8     | 4.5    |
| 15    | 8.0    |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Average needs sum and count
- Division gives float result
- Loop runs exactly N times

---

## **1️⃣6️⃣ Real-Life Application**

- Average marks
- Average temperature
- Performance analysis

---

## **1️⃣7️⃣ Practice Questions**

1. Find average of even numbers till N
2. Find average of numbers from M to N
3. Find average of first N odd numbers

---

## **1️⃣8️⃣ Result**

The program correctly prints the average of numbers from 1 to N.

---

## **1️⃣9️⃣ Conclusion**

A basic but important problem that combines loops, sum, and division.

---
