# ✅ **Product of N Inputs (For Loop)**

---

## **1️⃣ Question**

Given an integer **N**, read **N inputs** and print the **product** of the given inputs.

---

## **1.5️⃣ Category**

For Loop → Arithmetic Operations → Accumulation

---

## **2️⃣ Outline**

- Read N
- Initialize product as 1
- Use a for loop N times
- Multiply each input with product
- Print final product

---

## **3️⃣ Objective**

To calculate the product of multiple inputs using a **for loop**.

---

## **4️⃣ Purpose**

Strengthens understanding of loops and cumulative multiplication.

---

## **5️⃣ Theory**

Product starts from **1** because multiplying by 1 does not change the value.
Each input is multiplied with the previous product.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the value of N
2. Set `product = 1`
3. Run a loop N times
4. Read a number in each iteration
5. Multiply it with `product`
6. Print the final product

---

## **7️⃣ Method**

Use:

- `for` loop
- `input()`
- multiplication (`*`)
- `print()`

---

## **8️⃣ Constraints**

- N is a positive integer
- Inputs are integers

---

## **9️⃣ Common Mistakes**

❌ Initializing product as 0
❌ Forgetting to update product
❌ Printing inside the loop

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

product = 1
for i in range(N):
    num = int(input())
    product = product * num

print(product)
```

---

## **1️⃣2️⃣ Example**

Input:

```
3
2
3
7
```

Output:

```
42
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

- product = 1
- Read 2 → product = 2
- Read 3 → product = 6
- Read 7 → product = 42

---

## **1️⃣4️⃣ Test Cases Table**

| Inputs          | Output |
| --------------- | ------ |
| 3 → 2, 3, 7     | 42     |
| 4 → 11, 2, 4, 9 | 792    |
| 1 → 5           | 5      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Product must start from 1
- Loop controls number of inputs
- Final result printed after loop

---

## **1️⃣6️⃣ Real-Life Application**

- Calculating total multiplication factors
- Finding compound values
- Mathematical computations

---

## **1️⃣7️⃣ Practice Questions**

1. Find the product of even numbers only
2. Stop multiplication if input is 0
3. Find product of N numbers after a given number

---

## **1️⃣8️⃣ Result**

The program correctly computes the product of N inputs.

---

## **1️⃣9️⃣ Conclusion**

This problem reinforces **loop-based multiplication logic** and accumulator usage.

---
