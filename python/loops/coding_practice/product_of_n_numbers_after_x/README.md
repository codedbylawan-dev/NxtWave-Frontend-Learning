# ✅ **Product of N Numbers After X**

---

## **1️⃣ Question**

Given X and N, print the product of the next N numbers after X.

---

## **1.5️⃣ Category**

While Loop → Arithmetic → Sequence Product

---

## **2️⃣ Outline**

- Read X
- Read N
- Start from X + 1
- Multiply next N numbers
- Print final product

---

## **3️⃣ Objective**

To calculate the product of N consecutive numbers after X.

---

## **4️⃣ Purpose**

Strengthen understanding of loops and multiplication accumulation.

---

## **5️⃣ Theory**

If X = 4 and N = 2 → numbers are 5 and 6 → product = 30.

---

## **6️⃣ Step-by-Step Explanation**

1. Read X
2. Read N
3. Start number = X + 1
4. Product = 1
5. Multiply current number
6. Move to next number
7. Stop after N numbers

---

## **7️⃣ Method**

Use a while loop to repeat multiplication N times.

---

## **8️⃣ Constraints**

N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Starting from X instead of X+1
❌ Forgetting to update counter
❌ Forgetting initial product = 1

---

## 🔟 Complexity

Time: O(N)
Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
X = int(input())
N = int(input())

count = 0
product = 1
current = X + 1

while count < N:
    product = product * current
    current = current + 1
    count = count + 1

print(product)
```

---

## **1️⃣2️⃣ Example**

Input:

```
4
2
```

Output:

```
30
```

---

## **1️⃣3️⃣ Dry Run**

X = 4, N = 2
Numbers → 5, 6
Product → 5 × 6 = 30

---

## **1️⃣4️⃣ Test Cases Table**

| X   | N   | Numbers After X | Product |
| --- | --- | --------------- | ------- |
| 4   | 2   | 5, 6            | 30      |
| 10  | 5   | 11,12,13,14,15  | 360360  |
| 1   | 3   | 2,3,4           | 24      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Product accumulates values
- Start from X+1 always

---

## **1️⃣6️⃣ Real-Life Application**

- Calculating factorial-like sequences
- Mathematical progression problems

---

## **1️⃣7️⃣ Practice Questions**

1. Sum of N numbers after X
2. Product of numbers from 1 to N
3. Multiply every second number after X

---

## **1️⃣8️⃣ Result**

Correct product of N numbers after X is printed.

---

## **1️⃣9️⃣ Conclusion**

A simple loop-based multiplication problem reinforcing sequence handling.

---

s
