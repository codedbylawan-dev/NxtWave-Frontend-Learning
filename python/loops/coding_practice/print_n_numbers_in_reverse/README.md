# ✅ **Print N Numbers in Reverse**

---

## **1️⃣ Question**

Given a number **N**, print the numbers from **N to 1**, each on a new line.

---

## **1️⃣.5️⃣ Category**

For Loop → Reverse Order → Printing

---

## **2️⃣ Outline**

- Read N
- Start a loop from N
- Decrease the number by 1 each time
- Print each number

---

## **3️⃣ Objective**

To print numbers in **reverse order** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- reverse iteration
- loop control
- printing numbers step-by-step

---

## **5️⃣ Theory**

A **for loop** can move backwards by using a **negative step value**.

We start from **N** and go down to **1**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input number N
2. Use a for loop starting from N
3. Print the current value
4. Decrease the value by 1
5. Stop when the value reaches 1

---

## **7️⃣ Method**

Use:

- input()
- for loop
- range()
- print()

---

## **8️⃣ Constraints**

- N is a positive integer
- Output must be printed line by line

---

## **9️⃣ Common Mistakes**

❌ Using a positive step instead of negative
❌ Stopping the loop before reaching 1
❌ Printing values on the same line

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(N, 0, -1):
    print(i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
```

### Output

```
5
4
3
2
1
```

---

## **1️⃣3️⃣ Dry Run**

Input → `3`

- i = 3 → print 3
- i = 2 → print 2
- i = 1 → print 1

Loop ends.

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output    |
| ----: | --------- |
|     1 | 1         |
|     3 | 3 2 1     |
|     5 | 5 4 3 2 1 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Negative step is used for reverse order
- `range()` end value is not included
- One print per loop gives one line

---

## **1️⃣6️⃣ Real-Life Application**

- Countdown timers
- Reverse processing
- Backward navigation

---

## **1️⃣7️⃣ Practice Questions**

1. Print numbers from N to 0
2. Print only even numbers from N to 1
3. Print numbers from 10 to 1

---

## **1️⃣8️⃣ Result**

The program correctly prints numbers from **N to 1**.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens understanding of **reverse looping using for loops**.

---
