# ✅ **Sum of Odd Numbers from M to N**

---

## **1️⃣ Question**

Given two integers **M** and **N**, print the **sum of all odd numbers from M to N**.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Check → Range Sum

---

## **2️⃣ Outline**

- Read M
- Read N
- Initialize sum as 0
- Loop from M to N
- Check if the number is odd
- Add odd numbers to sum
- Print the final sum

---

## **3️⃣ Objective**

To calculate the **sum of odd numbers** in a given range using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you practice:

- looping through a range
- identifying odd numbers
- accumulating values using sum

---

## **5️⃣ Theory**

- An **odd number** gives remainder **1** when divided by 2
- Condition to check odd number:

  ```
  number % 2 == 1
  ```

Example:
M = 5, N = 13
Odd numbers → 5, 7, 9, 11, 13
Sum → 45

---

## **6️⃣ Step-by-Step Explanation**

1. Read the value of M
2. Read the value of N
3. Create a variable `total` and set it to 0
4. Loop from M to N
5. If the number is odd, add it to `total`
6. After the loop, print `total`

---

## **7️⃣ Method**

Use:

- `input()`
- `int()`
- `for` loop
- `if` condition
- addition operator

---

## **8️⃣ Constraints**

- M and N are integers
- M ≤ N

---

## **9️⃣ Common Mistakes**

❌ Including even numbers
❌ Forgetting to initialize sum as 0
❌ Printing sum inside the loop

---

## **🔟 Complexity**

Time: **O(N − M + 1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

total = 0

for i in range(M, N + 1):
    if i % 2 == 1:
        total = total + i

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
13
```

### Output

```
45
```

---

## **1️⃣3️⃣ Dry Run**

M = 5, N = 13

- i = 5 → odd → total = 5
- i = 7 → odd → total = 12
- i = 9 → odd → total = 21
- i = 11 → odd → total = 32
- i = 13 → odd → total = 45

Final Output → `45`

---

## **1️⃣4️⃣ Test Cases Table**

|   M |   N | Output |
| --: | --: | -----: |
|   5 |  13 |     45 |
|  10 |  20 |     75 |
|   1 |   1 |      1 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Initialize sum as **0**
- `% 2 == 1` checks odd numbers
- Loop must include N

---

## **1️⃣6️⃣ Real-Life Application**

- Filtering and summing values
- Mathematical series
- Conditional data processing

---

## **1️⃣7️⃣ Practice Questions**

1. Sum of even numbers from M to N
2. Sum of numbers divisible by 3
3. Sum of odd numbers from 1 to N

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of odd numbers from M to N**.

---

## **1️⃣9️⃣ Conclusion**

A clean and simple problem that strengthens **for loops**, **odd number checking**, and **sum accumulation** using only learned concepts.
