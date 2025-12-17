# ✅ **Sum of Numbers Divisible by T**

---

## **1️⃣ Question**

Given three integers **T**, **M**, and **N**, print the **sum of numbers divisible by T** from **M to N**.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Check → Summation

---

## **2️⃣ Outline**

- Read T
- Read M
- Read N
- Loop from M to N
- Check divisibility by T
- Add to sum
- Print the sum

---

## **3️⃣ Objective**

To calculate a **conditional sum** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- looping over a range
- checking divisibility
- accumulating values

---

## **5️⃣ Theory**

A number is divisible by **T** if:

```
number % T == 0
```

Only such numbers are added to the sum.

---

## **6️⃣ Step-by-Step Explanation**

1. Read T, M, and N
2. Initialize `total = 0`
3. Loop from M to N
4. If the number is divisible by T, add it to `total`
5. After the loop, print `total`

---

## **7️⃣ Method**

Use:

- input()
- for loop
- if condition
- addition assignment

---

## **8️⃣ Constraints**

- M ≤ N
- T is a positive integer

---

## **9️⃣ Common Mistakes**

❌ Forgetting to initialize sum
❌ Adding all numbers instead of divisible ones
❌ Wrong loop range

---

## **🔟 Complexity**

Time: **O(N − M + 1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
T = int(input())
M = int(input())
N = int(input())

total = 0

for i in range(M, N + 1):
    if i % T == 0:
        total = total + i

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
2
5
9
```

### Output

```
14
```

---

## **1️⃣3️⃣ Dry Run**

T = 2, M = 5, N = 9

- 6 → divisible → sum = 6
- 8 → divisible → sum = 14

Final Output → **14**

---

## **1️⃣4️⃣ Test Cases Table**

| T   | M   | N   | Output |
| --- | --- | --- | ------ |
| 2   | 5   | 9   | 14     |
| 3   | 1   | 10  | 18     |
| 5   | 5   | 5   | 5      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Initialize sum before loop
- `%` controls which numbers are added
- Loop boundaries matter

---

## **1️⃣6️⃣ Real-Life Application**

- Calculating totals with conditions
- Filtering and aggregating data

---

## **1️⃣7️⃣ Practice Questions**

1. Sum numbers divisible by 3 from 1 to 50
2. Sum even numbers between two values
3. Sum numbers divisible by both 2 and 3

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of numbers divisible by T** in the given range.

---

## **1️⃣9️⃣ Conclusion**

A strong practice problem for **loop-based summation with conditions**.

---
