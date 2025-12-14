# ✅ **Average of N Inputs**

---

## **1️⃣ Question**

Read a number **N**, then read **N integers**, and print their **average**.

---

## **2️⃣ Outline**

- Read N
- Repeat N times: read a number and add to sum
- Average = sum / N
- Print average

---

## **3️⃣ Objective**

To calculate the average using total sum ÷ count.

---

## **4️⃣ Purpose**

Practice reading multiple inputs and using loops.

---

## **5️⃣ Theory**

Average = (sum of numbers) / N

Example:
Inputs: 3, 6, 2, 8, 1 → sum = 20 → average = 20 / 5 = 4.0

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set sum = 0
3. Use a counter to read N numbers
4. Add each number to sum
5. After loop, divide sum by N
6. Print the result

---

## **7️⃣ Method**

Use a while loop and addition.

---

## **8️⃣ Constraints**

N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Not dividing by N
❌ Forgetting to update counter

---

## 🔟 Complexity

O(N)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

sum_values = 0
counter = 0

while counter < N:
    num = int(input())
    sum_values = sum_values + num
    counter = counter + 1

average = sum_values / N
print(average)
```

---

## **1️⃣2️⃣ Example**

Input

```
2
2
3
```

Output

```
2.5
```

---

## **1️⃣3️⃣ Dry Run**

N = 3
Inputs: 3, 6, 1
sum = 10
average = 10 / 3 = 3.3333333

---

## **1️⃣4️⃣ Test Cases**

| Inputs        | Output |
| ------------- | ------ |
| 5 → 3 6 2 8 1 | 4.0    |
| 2 → 2 3       | 2.5    |
| 3 → 1 1 1     | 1.0    |

---

## **1️⃣5️⃣ Result**

Program successfully prints the average of N inputs.

---

## **1️⃣6️⃣ Conclusion**

A clean loop-based calculation using sum and division.

---
