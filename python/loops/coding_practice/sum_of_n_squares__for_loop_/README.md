# ✅ **Sum of N Squares**

---

## **1️⃣ Question**

Given a number **N**, print the **sum of the squares of the first N natural numbers**.

---

## **1.5️⃣ Category**

For Loop → Arithmetic → Accumulation

---

## **2️⃣ Outline**

- Read N
- Start sum as 0
- Loop from 1 to N
- Add square of each number
- Print the final sum

---

## **3️⃣ Objective**

To calculate the sum of squares using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you practice:

- looping from 1 to N
- squaring numbers
- updating a running total

---

## **5️⃣ Theory**

The **square** of a number is:

```
number × number
```

The sum of squares from 1 to N is:

```
1² + 2² + 3² + ... + N²
```

Example:
N = 3
→ 1 + 4 + 9 = 14

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set `total = 0`
3. Loop from 1 to N
4. Square the number
5. Add it to `total`
6. Print `total`

---

## **7️⃣ Method**

Use:

- for loop
- multiplication
- addition

---

## **8️⃣ Constraints**

- N is a positive integer

---

## **9️⃣ Common Mistakes**

❌ Forgetting to square the number
❌ Starting sum with a non-zero value
❌ Printing inside the loop

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

total = 0

for i in range(1, N + 1):
    total = total + (i * i)

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
6
```

### Output

```
91
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

- total = 0
- i = 1 → total = 1
- i = 2 → total = 5
- i = 3 → total = 14

---

## **1️⃣4️⃣ Test Cases Table**

| N   | Output |
| --- | ------ |
| 3   | 14     |
| 4   | 30     |
| 6   | 91     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Square = number × number
- Loop runs from 1 to N
- Add each square to total

---

## **1️⃣6️⃣ Real-Life Application**

- Mathematical formulas
- Statistical calculations
- Problem-solving foundations

---

## **1️⃣7️⃣ Practice Questions**

1. Sum of cubes of first N numbers
2. Sum of squares of even numbers till N
3. Print squares instead of summing

---

## **1️⃣8️⃣ Result**

The program correctly prints the sum of squares of the first N natural numbers.

---

## **1️⃣9️⃣ Conclusion**

A fundamental loop-based problem that strengthens **math + iteration** skills.

---
