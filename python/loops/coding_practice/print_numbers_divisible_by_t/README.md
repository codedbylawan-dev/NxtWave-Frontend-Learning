# ✅ **Print Numbers Divisible by T**

---

## **1️⃣ Question**

Write a program that reads two numbers **N** and **T**, and prints all the numbers from **1 to N** that are divisible by **T**.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Check → Number Printing

---

## **2️⃣ Outline**

- Read N
- Read T
- Loop from 1 to N
- Check divisibility by T
- Print the number if divisible

---

## **3️⃣ Objective**

To practice using a **for loop** with a **condition** to filter numbers.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- iteration using for loop
- divisibility check using `%`
- conditional printing

---

## **5️⃣ Theory**

A number is divisible by **T** if:

```
number % T == 0
```

This means the remainder is **0**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the value of N
2. Read the value of T
3. Start a loop from 1 to N
4. For each number, check if it is divisible by T
5. If yes, print the number

---

## **7️⃣ Method**

Use:

- input()
- for loop
- if condition
- print statement

---

## **8️⃣ Constraints**

- N is a positive integer
- T is a positive integer
- T ≤ N

---

## **9️⃣ Common Mistakes**

❌ Forgetting `%` operator
❌ Printing all numbers without condition
❌ Using wrong loop range

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())
T = int(input())

for i in range(1, N + 1):
    if i % T == 0:
        print(i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
10
3
```

### Output

```
3
6
9
```

---

## **1️⃣3️⃣ Dry Run**

N = 10, T = 3

- i = 1 → not divisible
- i = 3 → divisible → print 3
- i = 6 → divisible → print 6
- i = 9 → divisible → print 9

---

## **1️⃣4️⃣ Test Cases Table**

| N   | T   | Output     |
| --- | --- | ---------- |
| 10  | 3   | 3 6 9      |
| 21  | 5   | 5 10 15 20 |
| 5   | 1   | 1 2 3 4 5  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `%` is used to check divisibility
- for loop helps scan a range of numbers
- Condition controls what gets printed

---

## **1️⃣6️⃣ Real-Life Application**

- Filtering multiples
- Scheduling intervals
- Mathematical validations

---

## **1️⃣7️⃣ Practice Questions**

1. Print numbers divisible by 4
2. Print numbers divisible by both 2 and 5
3. Count numbers divisible by T

---

## **1️⃣8️⃣ Result**

The program correctly prints all numbers from **1 to N** that are divisible by **T**.

---

## **1️⃣9️⃣ Conclusion**

A foundational problem that builds confidence in **loops + conditions**.

---
