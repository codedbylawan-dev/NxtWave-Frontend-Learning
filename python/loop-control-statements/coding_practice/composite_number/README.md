# ✅ **Composite Number**

---

## **1️⃣ Question**

Given an integer **N**, write a program to check whether the number is a **composite number** or not.

- Print **True** if it is composite
- Otherwise, print **False**

---

## **1️⃣.5️⃣ Category**

Numbers → For Loop → Conditions

---

## **2️⃣ Outline**

- Read integer `N`
- Initialize `count` as `0`
- Loop from `1` to `N`
- Count how many numbers divide `N`
- If count > 2 → composite
- Print result

---

## **3️⃣ Objective**

To determine whether a number has **more than two factors**.

---

## **4️⃣ Purpose**

This problem strengthens:

- divisor checking
- condition control
- counting logic

---

## **5️⃣ Theory**

A **composite number** is a number that has **more than two factors**.

For example, `12` has factors: `1, 2, 3, 4, 6, 12`
Total factors = `6` → composite

---

## **6️⃣ Step-by-Step Explanation**

1. Read input `N`
2. Set `count = 0`
3. Loop from `1` to `N`
4. If `N % i == 0`, increase `count`
5. After loop, if `count > 2`, print `True`, else print `False`

---

## **7️⃣ Method**

- One `for` loop
- One `if` condition
- Factor counting

---

## **8️⃣ Constraints**

- `N` is a positive integer
- Output must be `True` or `False`

---

## **9️⃣ Common Mistakes**

❌ Forgetting that 1 is not composite
❌ Incorrect divisor count
❌ Breaking loop early (not allowed in your scope)

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
n = int(input())

count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count > 2:
    print(True)
else:
    print(False)
```

---

## **1️⃣2️⃣ Example**

### Input

```
12
```

### Output

```
True
```

---

## **1️⃣3️⃣ Dry Run**

Input → `12`

Divisors found: `1, 2, 3, 4, 6, 12`
`count = 6`
Since `count > 2` → **True**

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----- | ------ |
| 12    | True   |
| 3     | False  |
| 1     | False  |
| 9     | True   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Composite = more than two factors
- Counting divisors is the safest method
- No advanced tricks required

---

## **1️⃣6️⃣ Real-Life Application**

- Cryptography fundamentals
- Mathematical validations
- Number classification systems

---

## **1️⃣7️⃣ Practice Questions**

1. Check if a number is prime
2. Count the number of factors
3. Find all composite numbers between 1 and N

---

## **1️⃣8️⃣ Result**

The program correctly identifies whether the given number is composite.

---

## **1️⃣9️⃣ Conclusion**

This problem builds strong understanding of number properties using only basic loops and conditions.

---
