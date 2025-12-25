# ✅ **Sum of N Terms in Power Series – 2**

---

## **1️⃣ Question**

Given two numbers **X** and **N**, print the **sum of N terms** in the following power series:

```
X², X⁴, X⁶, ...
```

---

## **1️⃣.5️⃣ Category**

For Loop → Power Series → Summation

---

## **2️⃣ Outline**

- Read X
- Read N
- Initialize sum as 0
- Start power from 2
- Loop N times
- Add X raised to current power
- Increase power by 2
- Print sum

---

## **3️⃣ Objective**

To calculate the **sum of even powers** of a number using a **single for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- even power patterns
- controlled power increment
- summation using loops

---

## **5️⃣ Theory**

Even powers increase like this:

```
2, 4, 6, 8, ...
```

Example for **X = 3, N = 4**:

```
3² = 9
3⁴ = 81
3⁶ = 729
3⁸ = 6561
```

Sum = **7380**

---

## **6️⃣ Step-by-Step Explanation**

1. Read X and N
2. Set `total = 0`
3. Set `power = 2`
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

❌ Starting power from 1
❌ Incrementing power by 1
❌ Using nested loops

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code (NO nested loop)**

```python
X = int(input())
N = int(input())

total = 0
power = 2

for i in range(N):
    total = total + (X ** power)
    power = power + 2

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
4
```

### Output

```
7380
```

---

## **1️⃣3️⃣ Dry Run**

X = 3, N = 3

- power = 2 → 3² = 9 → total = 9
- power = 4 → 3⁴ = 81 → total = 90
- power = 6 → 3⁶ = 729 → total = 819

---

## **1️⃣4️⃣ Test Cases Table**

| X   | N   | Output |
| --- | --- | ------ |
| 3   | 4   | 7380   |
| -2  | 6   | 5460   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Even powers start from **2**
- Increment power by **2**
- No nested loops needed

---

## **1️⃣6️⃣ Real-Life Application**

- Mathematical computations
- Series calculations

---

## **1️⃣7️⃣ Practice Questions**

1. Print even power series
2. Sum of squares from 1 to N
3. Alternate power series

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of even power terms**.

---

## **1️⃣9️⃣ Conclusion**

A clean and beginner-friendly solution that strengthens **power control using loops**.

---
