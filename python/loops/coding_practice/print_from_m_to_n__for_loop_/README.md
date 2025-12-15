# ✅ **Print from M to N**

---

## **1️⃣ Question**

Given two integers **M** and **N**, print all integers from **M to N**, each on a new line.

---

## **1.5️⃣ Category**

For Loop → Number Range → Iteration

---

## **2️⃣ Outline**

- Read M
- Read N
- Use a for loop starting from M to N
- Print each number

---

## **3️⃣ Objective**

To print a sequence of numbers between two given values using a **for loop**.

---

## **4️⃣ Purpose**

Helps understand:

- loop start and end values
- inclusive ranges
- printing sequences

---

## **5️⃣ Theory**

If M = 2 and N = 6

Numbers from 2 to 6 are:

```
2 3 4 5 6
```

The loop starts at M and stops at N.

---

## **6️⃣ Step-by-Step Explanation**

1. Read M
2. Read N
3. Start a loop from M to N
4. Print each value

---

## **7️⃣ Method**

Use:

- for loop
- range
- print

---

## **8️⃣ Constraints**

- M and N are integers
- M can be less than or equal to N

---

## **9️⃣ Common Mistakes**

❌ Forgetting to include N
❌ Printing all numbers on one line
❌ Wrong range end

---

## 🔟 Complexity

Time: **O(N − M + 1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

for i in range(M, N + 1):
    print(i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
2
6
```

### Output

```
2
3
4
5
6
```

---

## **1️⃣3️⃣ Dry Run**

M = -2, N = 2

Loop runs:
-2 → print
-1 → print
0 → print
1 → print
2 → print

---

## **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output Range |
| --- | --- | ------------ |
| 2   | 6   | 2 to 6       |
| -2  | 2   | -2 to 2      |
| 5   | 5   | 5            |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `range(start, end + 1)` includes end value
- Loop controls sequence
- Works for negative numbers too

---

## **1️⃣6️⃣ Real-Life Application**

- Page numbering
- Serial number printing
- Generating numeric ranges

---

## **1️⃣7️⃣ Practice Questions**

1. Print numbers from N to M
2. Print only even numbers from M to N
3. Print squares from M to N

---

## **1️⃣8️⃣ Result**

The program correctly prints numbers from M to N.

---

## **1️⃣9️⃣ Conclusion**

A fundamental loop-based range problem that strengthens control over **iteration limits**.

---
