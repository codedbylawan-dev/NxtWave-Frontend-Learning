# ✅ **Product of Numbers from M to N**

---

## **1️⃣ Question**

Given two numbers **M** and **N**, print the **product of all numbers from M to N** (including M and N).

---

## **1️⃣.5️⃣ Category**

For Loop → Range Iteration → Product Calculation

---

## **2️⃣ Outline**

- Read M
- Read N
- Initialize product as 1
- Traverse numbers from M to N
- Multiply each number with product
- Print the final product

---

## **3️⃣ Objective**

To calculate the **product of a range of numbers** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- looping through a range
- repeated multiplication
- accumulator variables

---

## **5️⃣ Theory**

Product means **multiplying numbers continuously**.

Example:
If M = 2 and N = 5

Numbers are: 2, 3, 4, 5

Product =
2 × 3 × 4 × 5 = **120**

We start with `1` and multiply each number.

---

## **6️⃣ Step-by-Step Explanation**

1. Read M and N
2. Set `product = 1`
3. Loop from M to N
4. Multiply product by the current number
5. After loop ends, print product

---

## **7️⃣ Method**

Use:

- for loop
- multiplication
- single accumulator variable

---

## **8️⃣ Constraints**

- N ≥ M
- M ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Starting product with 0
❌ Forgetting to include M or N
❌ Printing inside the loop

---

## **🔟 Complexity**

Time: **O(N − M + 1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

product = 1

for i in range(M, N + 1):
    product = product * i

print(product)
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
120
```

---

## **1️⃣3️⃣ Dry Run**

M = 1, N = 4

- product = 1
- 1 × 1 = 1
- 1 × 2 = 2
- 2 × 3 = 6
- 6 × 4 = 24

Output → **24**

---

## **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output |
| --- | --- | ------ |
| 2   | 5   | 120    |
| 1   | 4   | 24     |
| 3   | 3   | 3      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Product always starts from 1
- Loop range must include both M and N
- Multiplication happens step by step

---

## **1️⃣6️⃣ Real-Life Application**

- Factorial logic
- Mathematical series
- Computational calculations

---

## **1️⃣7️⃣ Practice Questions**

1. Product of even numbers from M to N
2. Product of odd numbers from M to N
3. Product of numbers divisible by 3

---

## **1️⃣8️⃣ Result**

The program correctly prints the **product of numbers from M to N**.

---

## **1️⃣9️⃣ Conclusion**

A key problem to master **range-based multiplication using for loops**.

---
