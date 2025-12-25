# ✅ **Sum of N Terms in Power Series**

---

## **1️⃣ Question**

Given two numbers **X** and **N**, print the **sum of N terms** in the following power series:

```
X¹, X³, X⁵, ...
```

---

## **1️⃣.5️⃣ Category**

For Loop → Power Series → Summation

---

## **2️⃣ Outline**

- Read X
- Read N
- Initialize sum as 0
- Start power from 1
- Loop N times
- Add X raised to current power
- Increase power by 2
- Print sum

---

## **3️⃣ Objective**

To calculate the **sum of odd powers** of a number using a **single for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- power patterns
- odd number progression
- summation using loops

---

## **5️⃣ Theory**

Odd powers increase like this:

```
1, 3, 5, 7, ...
```

Example for **X = 2, N = 4**:

```
2¹ = 2
2³ = 8
2⁵ = 32
2⁷ = 128
```

Sum = **170**

---

## **6️⃣ Step-by-Step Explanation**

1. Read X and N
2. Set `total = 0`
3. Set `power = 1`
4. Loop N times
5. Add `X ** power` to total
6. Increase power by 2
7. Print total

---

## **7️⃣ Method**

Use:

- for loop
- power operator (`**`)
- addition

---

## **8️⃣ Constraints**

- N ≥ 1
- X can be positive or negative

---

## **9️⃣ Common Mistakes**

❌ Using even powers
❌ Increasing power by 1
❌ Printing inside the loop

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code (NO nested loops)**

```python
X = int(input())
N = int(input())

total = 0
power = 1

for i in range(N):
    total = total + (X ** power)
    power = power + 2

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
2
6
```

### Output

```
2730
```

---

## **1️⃣3️⃣ Dry Run**

X = 2, N = 3

- power = 1 → 2¹ = 2 → total = 2
- power = 3 → 2³ = 8 → total = 10
- power = 5 → 2⁵ = 32 → total = 42

---

## **1️⃣4️⃣ Test Cases Table**

| X   | N   | Output |
| --- | --- | ------ |
| 2   | 6   | 2730   |
| 5   | 3   | 3255   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Only **one loop** is needed
- Power increases by **2**
- Clean and simple logic

---

## **1️⃣6️⃣ Real-Life Application**

- Mathematical sequences
- Pattern-based calculations

---

## **1️⃣7️⃣ Practice Questions**

1. Sum of even powers
2. Sum of first N squares
3. Sum of cubes

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of odd power terms**.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens **power handling and loop control** without nested loops.

---
