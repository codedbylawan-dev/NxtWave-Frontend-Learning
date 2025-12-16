# ✅ **Sum and Average of the 10 Inputs**

---

## **1️⃣ Question**

Read **10 integers** and print

- the **sum** of the inputs
- the **average** of the inputs

---

## **1️⃣.5️⃣ Category**

For Loop → Input Handling → Sum & Average

---

## **2️⃣ Outline**

- Initialize sum as 0
- Read 10 numbers one by one
- Add each number to sum
- Calculate average = sum / 10
- Print sum
- Print average

---

## **3️⃣ Objective**

To calculate **sum and average** using a **for loop** with fixed number of inputs.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- repeated input reading
- accumulation using a variable
- average calculation

---

## **5️⃣ Theory**

- **Sum** = addition of all numbers
- **Average** = sum ÷ count

Here, count is always **10**.

---

## **6️⃣ Step-by-Step Explanation**

1. Create a variable `total` and set it to 0
2. Run a loop 10 times
3. Read one number in each iteration
4. Add the number to `total`
5. After loop ends, calculate average
6. Print sum and average

---

## **7️⃣ Method**

Use:

- `input()`
- `int()`
- `for` loop
- arithmetic operators

---

## **8️⃣ Constraints**

- Exactly 10 inputs
- Inputs can be positive or negative integers

---

## **9️⃣ Common Mistakes**

❌ Forgetting to convert input to integer
❌ Dividing by wrong number
❌ Printing inside the loop

---

## **🔟 Complexity**

Time: **O(10)** → constant time
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
total = 0

for i in range(10):
    number = int(input())
    total = total + number

average = total / 10

print(total)
print(average)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
7
14
25
1
8
24
38
99
10
```

### Output

```
230
23.0
```

---

## **1️⃣3️⃣ Dry Run**

Inputs: 4, 7, 14, 25, 1, 8, 24, 38, 99, 10

- total after loop = 230
- average = 230 / 10 = 23.0

---

## **1️⃣4️⃣ Test Cases Table**

| Inputs (10 numbers)           | Sum | Average |
| ----------------------------- | --- | ------- |
| 4,7,14,25,1,8,24,38,99,10     | 230 | 23.0    |
| 20,35,99,-84,-93,2,7,53,23,11 | 73  | 7.3     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Loop count controls number of inputs
- Average is always float
- Sum must be calculated before average

---

## **1️⃣6️⃣ Real-Life Application**

- Exam score average
- Daily expense tracking
- Data analysis basics

---

## **1️⃣7️⃣ Practice Questions**

1. Find sum and average of 5 inputs
2. Find average of only positive numbers
3. Count how many inputs are negative

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum and average of 10 inputs**.

---

## **1️⃣9️⃣ Conclusion**

A foundational problem that strengthens **loop-based input handling**, **accumulation**, and **average calculation** using only learned concepts.
