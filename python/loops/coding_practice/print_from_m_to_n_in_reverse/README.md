# ✅ **Print from M to N in Reverse**

---

## **1️⃣ Question**

Given two integers **M** and **N**, print the numbers from **N to M**, each on a new line.

_(Given that N ≥ M)_

---

## **1️⃣.5️⃣ Category**

For Loop → Reverse Iteration → Printing

---

## **2️⃣ Outline**

- Read M
- Read N
- Start a loop from N
- Decrease the value until M
- Print each number

---

## **3️⃣ Objective**

To print numbers in **reverse order** between two given values using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you practice:

- reverse looping
- handling two inputs
- controlled range traversal

---

## **5️⃣ Theory**

Using a **for loop with a negative step**, we can move backwards from a higher number to a lower number.

---

## **6️⃣ Step-by-Step Explanation**

1. Read M
2. Read N
3. Start loop from N
4. Print the current number
5. Decrease by 1
6. Stop when M is reached

---

## **7️⃣ Method**

Use:

- input()
- for loop
- range() with negative step
- print()

---

## **8️⃣ Constraints**

- N is greater than or equal to M
- One number should be printed per line

---

## **9️⃣ Common Mistakes**

❌ Using positive step
❌ Ending the loop before reaching M
❌ Printing numbers in the wrong order

---

## **🔟 Complexity**

Time: **O(N − M)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

for i in range(N, M - 1, -1):
    print(i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
2
5
```

### Output

```
5
4
3
2
```

---

## **1️⃣3️⃣ Dry Run**

M = 2, N = 4

- i = 4 → print 4
- i = 3 → print 3
- i = 2 → print 2

Loop stops.

---

## **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output  |
| --- | --- | ------- |
| 1   | 1   | 1       |
| 2   | 5   | 5 4 3 2 |
| 4   | 7   | 7 6 5 4 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Use `M - 1` to include M in output
- Negative step is required for reverse order
- Order matters in range(start, end, step)

---

## **1️⃣6️⃣ Real-Life Application**

- Reverse indexing
- Countdown ranges
- Backward traversal

---

## **1️⃣7️⃣ Practice Questions**

1. Print from N to 0
2. Print only odd numbers from N to M
3. Print numbers from 100 to 50

---

## **1️⃣8️⃣ Result**

The program correctly prints numbers from **N down to M**.

---

## **1️⃣9️⃣ Conclusion**

This problem reinforces **reverse looping with two limits** using a **for loop**.

---
