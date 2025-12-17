# ✅ **Product of Numbers divisible by 3 from M to N**

---

## **1️⃣ Question**

Given two numbers **M** and **N**, find the **product of all numbers from M to N that are divisible by 3**.
If **no number is divisible by 3**, print **1**.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Logic → Product Calculation

---

## **2️⃣ Outline**

- Read M
- Read N
- Start product as 1
- Traverse from M to N
- Multiply numbers divisible by 3
- Print product

---

## **3️⃣ Objective**

To calculate the **product of selected numbers** in a range using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- range-based looping
- divisibility check
- cumulative product

---

## **5️⃣ Theory**

A number is divisible by **3** if:

```
number % 3 == 0
```

We multiply **only those numbers** that satisfy this condition.
If none satisfy, product remains **1**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read M and N
2. Initialize `product = 1`
3. Loop from M to N
4. If number divisible by 3 → multiply to product
5. After loop, print product

---

## **7️⃣ Method**

Use:

- for loop
- if condition
- multiplication

---

## **8️⃣ Constraints**

- N ≥ M
- Integers only

---

## **9️⃣ Common Mistakes**

❌ Forgetting to initialize product as 1
❌ Using addition instead of multiplication
❌ Wrong divisibility condition

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
    if i % 3 == 0:
        product = product * i

print(product)
```

---

## **1️⃣2️⃣ Example**

### Input

```
2
7
```

### Output

```
18
```

---

## **1️⃣3️⃣ Dry Run**

M = 2, N = 7

Divisible by 3 → 3, 6

- product = 1 × 3 = 3
- product = 3 × 6 = 18

Final Output → **18**

---

## **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output |
| --- | --- | ------ |
| 2   | 7   | 18     |
| 12  | 14  | 12     |
| 1   | 2   | 1      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Initialize product properly
- Condition controls which values are used
- Loop range must include N

---

## **1️⃣6️⃣ Real-Life Application**

- Filtering data before calculation
- Batch product computations
- Mathematical validations

---

## **1️⃣7️⃣ Practice Questions**

1. Product of numbers divisible by 5
2. Product of even numbers in a range
3. Product of odd numbers in a range

---

## **1️⃣8️⃣ Result**

The program correctly prints the **product of numbers divisible by 3** from M to N.

---

## **1️⃣9️⃣ Conclusion**

A clean loop-and-condition problem that strengthens **range processing and product logic**.

---
