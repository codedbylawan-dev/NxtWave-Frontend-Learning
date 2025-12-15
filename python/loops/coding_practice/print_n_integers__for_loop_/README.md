# ✅ **Print N Integers (For Loop)**

---

## **1️⃣ Question**

Given a number **N**, print all integers from **1 to N**, each on a new line.

---

## **1.5️⃣ Category**

For Loop → Numbers → Sequential Printing

---

## **2️⃣ Outline**

- Read N
- Loop from 1 to N
- Print each number

---

## **3️⃣ Objective**

To print numbers in order using a **for loop**.

---

## **4️⃣ Purpose**

Helps understand looping through a range of numbers.

---

## **5️⃣ Theory**

A `for` loop with `range(1, N+1)` generates numbers starting from 1 up to N.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the value of N
2. Start a loop from 1
3. Print the current number
4. Continue until N

---

## **7️⃣ Method**

Use:

- `for` loop
- `range()`
- `print()`

---

## **8️⃣ Constraints**

- N is a positive integer
- Each number must be printed on a new line

---

## **9️⃣ Common Mistakes**

❌ Using `range(N)` instead of `range(1, N+1)`
❌ Printing numbers on the same line

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(1, N + 1):
    print(i)
```

---

## **1️⃣2️⃣ Example**

Input:

```
3
```

Output:

```
1
2
3
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

Loop runs:

- i = 1 → print 1
- i = 2 → print 2
- i = 3 → print 3

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output    |
| ----- | --------- |
| 1     | 1         |
| 3     | 1 2 3     |
| 5     | 1 2 3 4 5 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `range(start, end)` does not include end
- Use `N + 1` to include N

---

## **1️⃣6️⃣ Real-Life Application**

- Counting systems
- Generating serial numbers
- Loop-based calculations

---

## **1️⃣7️⃣ Practice Questions**

1. Print numbers from 1 to N in reverse
2. Print only even numbers from 1 to N
3. Print squares of numbers from 1 to N

---

## **1️⃣8️⃣ Result**

The program prints numbers from 1 to N correctly.

---

## **1️⃣9️⃣ Conclusion**

A basic loop problem to practice number sequences using a for loop.

---
