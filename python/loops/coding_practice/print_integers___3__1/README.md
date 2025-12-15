# ✅ **Print Integers – 3**

---

## **1️⃣ Question**

Given an integer **N**, print the integers from **N to 1**, each on a new line.

---

## **1.5️⃣ Category**

For Loop → Iteration → Printing Numbers

---

## **2️⃣ Outline**

- Read N
- Use a for loop that runs N times
- Print numbers by decreasing from N to 1

---

## **3️⃣ Objective**

To print numbers in **reverse order** using a **for loop** and simple arithmetic.

---

## **4️⃣ Purpose**

This problem helps you understand:

- for loop execution
- using loop counter
- controlling output using subtraction

---

## **5️⃣ Theory**

A **for loop** repeats a block of code a fixed number of times.

By subtracting the loop variable from **N**, we can print numbers in reverse order **without using advanced syntax**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the value of N
2. Start a loop that runs from 0 to N−1
3. Subtract the loop value from N
4. Print the result
5. Continue until all numbers are printed

---

## **7️⃣ Method**

Use:

- for loop
- range(N)
- subtraction
- print statement

---

## **8️⃣ Constraints**

- N is a positive integer

---

## **9️⃣ Common Mistakes**

❌ Printing `i` directly instead of `N - i`
❌ Printing in the wrong order
❌ Printing numbers on the same line

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
n = int(input())

for i in range(n):
    print(n - i)
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

Input: `N = 3`

- i = 0 → print 3
- i = 1 → print 2
- i = 2 → print 1

Loop ends.

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output    |
| ----- | --------- |
| 1     | 1         |
| 3     | 3 2 1     |
| 5     | 5 4 3 2 1 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Reverse printing can be done using subtraction
- No need for advanced range usage
- for loop runs a fixed number of times

---

## **1️⃣6️⃣ Result**

The program prints integers from **N to 1** correctly.

---

## **1️⃣7️⃣ Conclusion**

A beginner-friendly reverse printing problem using **only basic for loop logic**.

---
