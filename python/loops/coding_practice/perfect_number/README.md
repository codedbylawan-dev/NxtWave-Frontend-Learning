# ✅ **Perfect Number**

---

## **1️⃣ Question**

Given a number **N**, check whether it is a **Perfect Number**.

A number is called a **Perfect Number** if the **sum of its factors excluding itself** is equal to the number.

---

## **1️⃣.5️⃣ Category**

For Loop → Factors → Conditional Check

---

## **2️⃣ Outline**

- Read N
- Initialize sum as 0
- Find factors of N (excluding N)
- Add factors to sum
- Compare sum with N
- Print result

---

## **3️⃣ Objective**

To determine whether a number is a **Perfect Number** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- factor calculation
- conditional comparison
- summation logic

---

## **5️⃣ Theory**

A **factor** of a number is a number that divides it exactly.

Perfect Number condition:

```
Sum of factors (excluding N) = N
```

Example:
N = 6
Factors excluding 6 → 1, 2, 3
Sum → 1 + 2 + 3 = 6 → Perfect Number

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set `total = 0`
3. Loop from 1 to N-1
4. If number divides N, add it to total
5. After loop, compare total with N
6. Print result

---

## **7️⃣ Method**

Use:

- for loop
- modulo operator `%`
- if condition

---

## **8️⃣ Constraints**

- N is a positive integer

---

## **9️⃣ Common Mistakes**

❌ Including the number itself as a factor
❌ Looping till N instead of N-1
❌ Printing result inside loop

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

total = 0

for i in range(1, N):
    if N % i == 0:
        total = total + i

if total == N:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
```

---

## **1️⃣2️⃣ Example**

### Input

```
6
```

### Output

```
Perfect Number
```

---

## **1️⃣3️⃣ Dry Run**

N = 6

- i = 1 → factor → total = 1
- i = 2 → factor → total = 3
- i = 3 → factor → total = 6
- i = 4 → no
- i = 5 → no

total == N → Perfect Number

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output               |
| ----: | -------------------- |
|     6 | Perfect Number       |
|    21 | Not a Perfect Number |
|    28 | Perfect Number       |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Exclude the number itself
- Sum only proper factors
- Comparison decides the result

---

## **1️⃣6️⃣ Real-Life Application**

- Mathematical analysis
- Number classification problems
- Competitive programming basics

---

## **1️⃣7️⃣ Practice Questions**

1. Print all perfect numbers up to N
2. Check if a number is abundant
3. Check if a number is deficient

---

## **1️⃣8️⃣ Result**

The program correctly identifies whether a number is a **Perfect Number**.

---

## **1️⃣9️⃣ Conclusion**

A classic problem that strengthens **looping, factor logic, and condition checking**.

---
