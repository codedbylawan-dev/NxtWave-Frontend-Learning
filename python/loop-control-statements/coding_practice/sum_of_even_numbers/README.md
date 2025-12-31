# ✅ **Sum of Even Numbers**

---

## **1️⃣ Question**

Given an integer **N**, write a program to find the **sum of all even natural numbers up to N**.

---

## **1️⃣.5️⃣ Category**

Numbers → For Loop → Conditions

---

## **2️⃣ Outline**

- Read integer `N`
- Initialize `total` as `0`
- Loop from `1` to `N`
- Check if the number is even
- Add it to `total`
- Print `total`

---

## **3️⃣ Objective**

To calculate the sum of even numbers **from 1 to N** using basic looping and conditions.

---

## **4️⃣ Purpose**

This problem helps in learning:

- range control in loops
- conditional filtering
- accumulation pattern

---

## **5️⃣ Theory**

A number is **even** if:

```python
number % 2 == 0
```

We add only the numbers that satisfy this condition.

---

## **6️⃣ Step-by-Step Explanation**

1. Read input `N`
2. Set `total = 0`
3. Loop from `1` to `N`
4. If current number is even, add it to `total`
5. After loop ends, print `total`

---

## **7️⃣ Method**

- One `for` loop
- One `if` condition
- One accumulator variable

---

## **8️⃣ Constraints**

- `N` is a natural number
- Only even numbers are added
- Output is an integer

---

## **9️⃣ Common Mistakes**

❌ Using `range(1, n)` instead of `range(1, n+1)`
❌ Adding odd numbers
❌ Forgetting to initialize `total`

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
n = int(input())

total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total = total + i

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
```

### Output

```
6
```

---

## **1️⃣3️⃣ Dry Run**

Input → `5`

Numbers checked: `1, 2, 3, 4, 5`

- 2 is even → total = 2
- 4 is even → total = 6

Final Output → **6**

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----- | ------ |
| 5     | 6      |
| 4     | 6      |
| 1     | 0      |
| 10    | 30     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Correct loop boundary matters
- Accumulator pattern is a core concept
- Conditions filter the data cleanly

---

## **1️⃣6️⃣ Real-Life Application**

- Summing filtered datasets
- Billing & finance totals
- Statistical aggregation

---

## **1️⃣7️⃣ Practice Questions**

1. Sum of odd numbers up to N
2. Count of even numbers up to N
3. Sum of numbers divisible by 5 up to N

---

## **1️⃣8️⃣ Result**

The program correctly calculates the sum of even numbers from `1` to `N`.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens loop control, condition logic, and cumulative calculation using only foundational programming concepts.

---
