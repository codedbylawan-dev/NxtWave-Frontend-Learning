# ✅ **First N Natural Numbers (For Loop)**

---

## **1️⃣ Question**

Given a number **N**, print the **first N natural numbers** starting from **1**, each on a new line.

---

## **1.5️⃣ Category**

For Loop → Natural Numbers → Sequential Printing

---

## **2️⃣ Outline**

- Read N
- Loop from 1 to N
- Print each number

---

## **3️⃣ Objective**

To print natural numbers using a **for loop**.

---

## **4️⃣ Purpose**

Helps understand looping and number sequences starting from 1.

---

## **5️⃣ Theory**

Natural numbers start from **1** and increase by **1**.
`range(1, N + 1)` generates numbers from 1 to N.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the value of N
2. Start a loop from 1
3. Print the current number
4. Stop after reaching N

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
❌ Starting from 0 instead of 1

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
7
```

Output:

```
1
2
3
4
5
6
7
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
| 2     | 1 2       |
| 5     | 1 2 3 4 5 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Natural numbers always start from 1
- Use `N + 1` to include N

---

## **1️⃣6️⃣ Real-Life Application**

- Counting items
- Numbering lists
- Iteration basics

---

## **1️⃣7️⃣ Practice Questions**

1. Print first N even numbers
2. Print first N odd numbers
3. Print natural numbers in reverse

---

## **1️⃣8️⃣ Result**

The program prints natural numbers from 1 to N correctly.

---

## **1️⃣9️⃣ Conclusion**

A foundational loop problem for practicing natural number sequences.

---
