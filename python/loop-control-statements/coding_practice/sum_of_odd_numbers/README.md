# ✅ **Sum of Odd Numbers**

---

## **1️⃣ Question**

Given an integer **N**, write a program to find the **sum of all odd natural numbers up to N**.

---

## **1️⃣.5️⃣ Category**

Numbers → For Loop → Conditions

---

## **2️⃣ Outline**

- Read integer `N`
- Initialize `total` as `0`
- Loop from `1` to `N`
- Check if the number is odd
- Add it to `total`
- Print `total`

---

## **3️⃣ Objective**

To calculate the sum of odd numbers **from 1 to N** using only basic loops and conditions.

---

## **4️⃣ Purpose**

This problem helps in learning:

- loop boundaries
- identifying odd numbers
- accumulation logic

---

## **5️⃣ Theory**

A number is **odd** if:

```python
number % 2 != 0
```

We add only numbers that satisfy this condition.

---

## **6️⃣ Step-by-Step Explanation**

1. Read input `N`
2. Set `total = 0`
3. Loop from `1` to `N`
4. If the current number is odd, add it to `total`
5. After the loop, print `total`

---

## **7️⃣ Method**

- One `for` loop
- One `if` condition
- One accumulator variable

---

## **8️⃣ Constraints**

- `N` is a natural number
- Only odd numbers up to `N` are added
- Output is an integer

---

## **9️⃣ Common Mistakes**

❌ Using `range(1, n)` instead of `range(1, n + 1)`
❌ Wrong condition for odd check
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
    if i % 2 != 0:
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
9
```

---

## **1️⃣3️⃣ Dry Run**

Input → `5`

Numbers checked: `1, 2, 3, 4, 5`

Odd numbers added:
`1 + 3 + 5 = 9`

Final Output → **9**

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----- | ------ |
| 10    | 25     |
| 5     | 9      |
| 1     | 1      |
| 7     | 16     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Loop range must match the problem exactly
- Condition determines which numbers contribute
- Accumulator pattern is fundamental

---

## **1️⃣6️⃣ Real-Life Application**

- Data filtering
- Finance & billing totals
- Statistical processing

---

## **1️⃣7️⃣ Practice Questions**

1. Sum of even numbers up to N
2. Count of odd numbers up to N
3. Sum of numbers divisible by 5 up to N

---

## **1️⃣8️⃣ Result**

The program correctly calculates the sum of odd numbers from `1` to `N`.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens careful problem reading, loop control, and condition-based accumulation.

---
