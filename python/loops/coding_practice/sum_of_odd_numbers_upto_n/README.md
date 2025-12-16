# ✅ **Sum of Odd Numbers Up to N**

---

## **1️⃣ Question**

Given a number **N**, print the **sum of all odd numbers from 1 to N**.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Check → Summation

---

## **2️⃣ Outline**

- Read N
- Initialize sum as 0
- Loop from 1 to N
- Check if the number is odd
- Add odd numbers to sum
- Print the sum

---

## **3️⃣ Objective**

To calculate the **sum of odd numbers** within a given range using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you practice:

- looping through numbers
- identifying odd numbers
- accumulating a sum

---

## **5️⃣ Theory**

- An **odd number** is **not divisible by 2**
- Condition to check odd number:

  ```
  number % 2 != 0
  ```

Example:
N = 6
Numbers → 1 2 3 4 5 6
Odd numbers → 1 3 5
Sum → 9

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input value N
2. Create a variable `total` and set it to 0
3. Loop from 1 to N
4. If the number is odd, add it to `total`
5. After the loop, print `total`

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

- N is a positive integer

---

## **9️⃣ Common Mistakes**

❌ Adding even numbers
❌ Using `==` instead of `!=` in odd check
❌ Printing sum inside the loop

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

total = 0

for i in range(1, N + 1):
    if i % 2 != 0:
        total = total + i

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
6
```

### Output

```
9
```

---

## **1️⃣3️⃣ Dry Run**

N = 6

- i = 1 → odd → total = 1
- i = 2 → even → skip
- i = 3 → odd → total = 4
- i = 4 → skip
- i = 5 → odd → total = 9
- i = 6 → skip

Final Output → `9`

---

## **1️⃣4️⃣ Test Cases Table**

|   N | Output |
| --: | -----: |
|   6 |      9 |
|  15 |     64 |
|   1 |      1 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `% 2 != 0` is used to find odd numbers
- Initialize sum before loop
- Print result only once

---

## **1️⃣6️⃣ Real-Life Application**

- Filtering odd-numbered data
- Mathematical series calculations
- Conditional data processing

---

## **1️⃣7️⃣ Practice Questions**

1. Print odd numbers up to N
2. Count odd numbers up to N
3. Sum of numbers divisible by 3

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of odd numbers from 1 to N**.

---

## **1️⃣9️⃣ Conclusion**

A simple and important loop problem that reinforces **conditional checks** and **summation logic** using only learned concepts.
