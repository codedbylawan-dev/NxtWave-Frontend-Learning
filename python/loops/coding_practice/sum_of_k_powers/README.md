# ✅ **Sum of K Powers**

---

## **1️⃣ Question**

Given two numbers **N** and **K**, print the **sum of the Kth power of all numbers from 1 to N**.

---

## **1️⃣.5️⃣ Category**

For Loop → Power Calculation → Summation

---

## **2️⃣ Outline**

- Read N
- Read K
- Initialize sum as 0
- Traverse numbers from 1 to N
- Find Kth power of each number
- Add to sum
- Print sum

---

## **3️⃣ Objective**

To calculate the **sum of Kth powers** using a **single for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- power calculation
- accumulation using loop
- mathematical operations

---

## **5️⃣ Theory**

The **Kth power** of a number means:

- number raised to power K

Example:

- 2³ = 8
- 3² = 9

Python allows calculating power directly.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N and K
2. Set `total = 0`
3. Loop from 1 to N
4. Calculate Kth power of the number
5. Add it to total
6. Print total

---

## **7️⃣ Method**

Use:

- for loop
- power operator
- summation

---

## **8️⃣ Constraints**

- N ≥ 1
- K ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Forgetting to add to total
❌ Printing inside the loop
❌ Using nested loops unnecessarily

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())
K = int(input())

total = 0

for i in range(1, N + 1):
    total = total + (i ** K)

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
3
```

### Output

```
225
```

---

## **1️⃣3️⃣ Dry Run**

N = 5, K = 3

- 1³ = 1 → total = 1
- 2³ = 8 → total = 9
- 3³ = 27 → total = 36
- 4³ = 64 → total = 100
- 5³ = 125 → total = 225

---

## **1️⃣4️⃣ Test Cases Table**

| N   | K   | Output |
| --- | --- | ------ |
| 5   | 3   | 225    |
| 3   | 2   | 14     |
| 4   | 1   | 10     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Use **single loop only**
- Power calculation can be direct
- Accumulate values step by step

---

## **1️⃣6️⃣ Real-Life Application**

- Mathematical formulas
- Scientific calculations
- Data analysis

---

## **1️⃣7️⃣ Practice Questions**

1. Sum of squares from 1 to N
2. Sum of cubes from 1 to N
3. Sum of even powers from 1 to N

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of Kth powers** from 1 to N.

---

## **1️⃣9️⃣ Conclusion**

This solution follows **exactly what you’ve learned so far** and avoids nested loops completely.

---
