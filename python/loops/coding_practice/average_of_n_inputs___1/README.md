# ✅ **Average of N Inputs (For Loop)**

---

## **1️⃣ Question**

Given a number **N**, read **N inputs** and print the **average** of the given inputs.

---

## **1.5️⃣ Category**

For Loop → Input Handling → Arithmetic Operations

---

## **2️⃣ Outline**

- Read N
- Initialize sum as 0
- Read N numbers one by one
- Add each number to sum
- Divide sum by N
- Print the average

---

## **3️⃣ Objective**

To calculate the average of multiple inputs using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you practice:

- reading multiple inputs
- using a loop for accumulation
- calculating average

---

## **5️⃣ Theory**

Average formula:

```
Average = Sum of values / Number of values
```

If inputs are: 3, 4, 6, 7
Sum = 20
Count = 4
Average = 20 / 4 = 5.0

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set sum = 0
3. Use a for loop N times
4. Read a number each time
5. Add it to sum
6. Divide sum by N
7. Print the result

---

## **7️⃣ Method**

Use:

- integer input
- for loop
- arithmetic operators
- print statement

---

## **8️⃣ Constraints**

- N ≥ 1
- Inputs are integers
- Output must be a float

---

## **9️⃣ Common Mistakes**

❌ Forgetting to divide by N
❌ Using integer division accidentally
❌ Not reading all N inputs

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

total = 0
for i in range(N):
    number = int(input())
    total = total + number

average = total / N
print(average)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
3
4
6
7
```

### Output

```
5.0
```

---

## **1️⃣3️⃣ Dry Run**

N = 2
Inputs: 24, 15

- total = 0
- total = 0 + 24 = 24
- total = 24 + 15 = 39

Average = 39 / 2 = 19.5

---

## **1️⃣4️⃣ Test Cases Table**

| N   | Inputs     | Output |
| --- | ---------- | ------ |
| 1   | 10         | 10.0   |
| 2   | 24, 15     | 19.5   |
| 4   | 3, 4, 6, 7 | 5.0    |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Sum must start from 0
- Loop runs exactly N times
- Division gives float result

---

## **1️⃣6️⃣ Real-Life Application**

- Calculating average marks
- Finding average expenses
- Mean value calculations

---

## **1️⃣7️⃣ Practice Questions**

1. Find the average of N even numbers
2. Find the average of N numbers greater than 10
3. Print average only if it is greater than 5

---

## **1️⃣8️⃣ Result**

The program correctly calculates and prints the **average of N inputs**.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens loop-based input handling and basic arithmetic operations.

---
