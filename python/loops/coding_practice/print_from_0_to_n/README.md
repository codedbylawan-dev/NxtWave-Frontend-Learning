# ✅ **Print from 0 to N (For Loop)**

---

## **1️⃣ Question**

Given a number **N**, print all the numbers from **0 to N**, each on a new line.

---

## **1.5️⃣ Category**

For Loop → Number Printing → Sequence

---

## **2️⃣ Outline**

- Read N
- Start from 0
- Print numbers up to N (inclusive)

---

## **3️⃣ Objective**

To print a sequence of numbers starting from 0 using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- loop starting values
- inclusive ranges
- basic sequence printing

---

## **5️⃣ Theory**

If **N = 4**, the numbers from 0 to 4 are:

```
0
1
2
3
4
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read the value of N
2. Use a for loop starting from 0
3. Print each number till N

---

## **7️⃣ Method**

Use:

- integer input
- for loop
- print statement

---

## **8️⃣ Constraints**

- N ≥ 0
- Each number should be printed on a new line

---

## **9️⃣ Common Mistakes**

❌ Starting loop from 1 instead of 0
❌ Missing the last number N
❌ Printing numbers in one line

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(0, N + 1):
    print(i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
0
1
2
3
4
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

Loop runs from 0 to 3:

- i = 0 → print 0
- i = 1 → print 1
- i = 2 → print 2
- i = 3 → print 3

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output      |
| ----- | ----------- |
| 0     | 0           |
| 2     | 0 1 2       |
| 5     | 0 1 2 3 4 5 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `range(0, N+1)` includes N
- Loop start value matters
- One print per line is default

---

## **1️⃣6️⃣ Real-Life Application**

- Counting systems
- Index-based operations
- Step-by-step counters

---

## **1️⃣7️⃣ Practice Questions**

1. Print numbers from 0 to N in reverse
2. Print only even numbers from 0 to N
3. Print numbers from 1 to N

---

## **1️⃣8️⃣ Result**

The program correctly prints all numbers from **0 to N**.

---

## **1️⃣9️⃣ Conclusion**

A simple for-loop problem that strengthens understanding of **loop ranges and sequence printing**.

---
