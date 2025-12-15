# ✅ **Product of the Numbers from M to N**

---

## **1️⃣ Question**

Given two numbers **M** and **N**, print the **product of all numbers from M to N** (both included).

---

## **1.5️⃣ Category**

For Loop → Range → Multiplication

---

## **2️⃣ Outline**

- Read M
- Read N
- Start product as 1
- Multiply numbers from M to N
- Print the final product

---

## **3️⃣ Objective**

To calculate the product of a sequence of numbers using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- loop iteration
- updating a variable step by step
- multiplication logic

---

## **5️⃣ Theory**

If numbers are from **M to N**, we multiply:

```
M × (M+1) × (M+2) × ... × N
```

Example:
M = 5, N = 7
→ 5 × 6 × 7 = 210

---

## **6️⃣ Step-by-Step Explanation**

1. Read M
2. Read N
3. Set `product = 1`
4. Loop from M to N
5. Multiply each number with `product`
6. Print `product`

---

## **7️⃣ Method**

Use:

- for loop
- multiplication
- single variable to store product

---

## **8️⃣ Constraints**

- M ≤ N
- M and N are integers

---

## **9️⃣ Common Mistakes**

❌ Starting product as 0
❌ Forgetting to include N in the loop
❌ Printing inside the loop

---

## 🔟 Complexity

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
5
7
```

### Output

```
210
```

---

## **1️⃣3️⃣ Dry Run**

M = 5, N = 7

- product = 1
- product = 1 × 5 = 5
- product = 5 × 6 = 30
- product = 30 × 7 = 210

---

## **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output  |
| --- | --- | ------- |
| 5   | 7   | 210     |
| 1   | 4   | 24      |
| 9   | 14  | 2162160 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always initialize product with 1
- Loop range must include N
- Multiply step-by-step

---

## **1️⃣6️⃣ Real-Life Application**

- Factorial calculation
- Series multiplication
- Mathematical computations

---

## **1️⃣7️⃣ Practice Questions**

1. Find product of numbers from 1 to N
2. Find product of even numbers in a range
3. Find factorial of a number

---

## **1️⃣8️⃣ Result**

The program correctly prints the product of numbers from M to N.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens **loop-based multiplication** and variable updates.

---
