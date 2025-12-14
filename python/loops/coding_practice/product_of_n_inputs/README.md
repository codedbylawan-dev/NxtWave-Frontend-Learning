# ✅ **Product of N Inputs**

---

## **1️⃣ Question**

Read N numbers and print the product of all N numbers.

---

## **2️⃣ Outline**

- Read N
- Start product at 1
- Loop N times
- Multiply each input into the product
- Print final product

---

## **3️⃣ Objective**

To calculate a running product using repeated inputs.

---

## **4️⃣ Purpose**

Builds understanding of loops + cumulative multiplication.

---

## **5️⃣ Theory**

Product starts at **1** because multiplying by 1 does not change the value.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set product = 1
3. While counter < N:

   - Read a number
   - product = product \* number
   - Increase counter

4. Print product

---

## **7️⃣ Method**

Use while loop and variable updates.

---

## **8️⃣ Constraints**

N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Starting product at 0 → result always becomes 0
❌ Forgetting to convert input to int
❌ Missing counter increment

---

## 🔟 Complexity

O(N)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

product = 1
counter = 0

while counter < N:
    num = int(input())
    product = product * num
    counter = counter + 1

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

product = 1
Read 2 → product = 2
Read 3 → product = 6
Read 7 → product = 42

---

## **1️⃣4️⃣ Test Cases**

| Inputs              | Result |
| ------------------- | ------ |
| 3, numbers 1 1 1    | 1      |
| 2, numbers 5 6      | 30     |
| 4, numbers 11 2 4 9 | 792    |

---

## **1️⃣5️⃣ Notes**

Always initialize product with 1, not 0.

---

## **1️⃣6️⃣ Practice**

Find the product of only the **even** numbers from N inputs.

---

## **1️⃣7️⃣ Result**

The program returns the correct product of N inputs.

---

## **1️⃣8️⃣ Conclusion**

A simple loop-based cumulative multiplication problem.

---
