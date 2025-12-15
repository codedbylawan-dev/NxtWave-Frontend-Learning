# ✅ **Read N Inputs (For Loop)**

---

## **1️⃣ Question**

Given an integer **N**, read **N inputs** and print each input on a new line.

---

## **1.5️⃣ Category**

For Loop → Input & Output → Repetition

---

## **2️⃣ Outline**

- Read N
- Use a for loop N times
- Read one number in each iteration
- Print the number

---

## **3️⃣ Objective**

To practice reading multiple inputs using a **for loop**.

---

## **4️⃣ Purpose**

Helps understand repeated input reading and printing.

---

## **5️⃣ Theory**

A **for loop** runs a fixed number of times.
Here, it runs **N times** to read **N inputs**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the value of N
2. Start a loop that runs N times
3. In each loop iteration:

   - Read an integer
   - Print the integer

4. Stop after N inputs

---

## **7️⃣ Method**

Use:

- `for` loop
- `input()`
- `print()`

---

## **8️⃣ Constraints**

- N is a positive integer
- Exactly N inputs will be given

---

## **9️⃣ Common Mistakes**

❌ Reading fewer or more inputs
❌ Printing extra text
❌ Forgetting to convert input to integer

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(N):
    num = int(input())
    print(num)
```

---

## **1️⃣2️⃣ Example**

Input:

```
3
8
11
25
```

Output:

```
8
11
25
```

---

## **1️⃣3️⃣ Dry Run**

N = 2

- Loop 1 → read 7 → print 7
- Loop 2 → read 20 → print 20

---

## **1️⃣4️⃣ Test Cases Table**

| Input         | Output  |
| ------------- | ------- |
| 1 → 5         | 5       |
| 2 → 7, 20     | 7 20    |
| 3 → 8, 11, 25 | 8 11 25 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Loop count controls number of inputs
- Each input is handled one by one
- Output format must match exactly

---

## **1️⃣6️⃣ Real-Life Application**

- Reading scores of students
- Processing sensor values
- Handling multiple user inputs

---

## **1️⃣7️⃣ Practice Questions**

1. Read N inputs and print their sum
2. Read N inputs and print their product
3. Read N inputs and print only even numbers

---

## **1️⃣8️⃣ Result**

The program correctly reads and prints N inputs.

---

## **1️⃣9️⃣ Conclusion**

This problem builds confidence in using **for loops with input handling**.

---
