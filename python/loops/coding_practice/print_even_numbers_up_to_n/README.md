# ✅ **Print Even Numbers up to N**

---

## **1️⃣ Question**

Given a number **N**, print **all even numbers from 1 to N**, each on a new line.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Check → Number Printing

---

## **2️⃣ Outline**

- Read N
- Loop from 1 to N
- Check if a number is even
- Print the number if it is even

---

## **3️⃣ Objective**

To identify and print **even numbers** within a given range using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- looping through a range
- checking conditions using `%` (modulus)
- selective printing

---

## **5️⃣ Theory**

- An **even number** is divisible by 2
- Condition to check even number:

  ```
  number % 2 == 0
  ```

Example:
For N = 7
Numbers → 1 2 3 4 5 6 7
Even numbers → 2 4 6

---

## **6️⃣ Step-by-Step Explanation**

1. Read the number N
2. Start a loop from 1 to N
3. For each number, check if it is divisible by 2
4. If yes, print the number
5. Continue until the loop ends

---

## **7️⃣ Method**

Use:

- `input()`
- `int()`
- `for` loop
- `if` condition

---

## **8️⃣ Constraints**

- N is a positive integer

---

## **9️⃣ Common Mistakes**

❌ Printing odd numbers
❌ Forgetting the condition
❌ Looping beyond N

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(1, N + 1):
    if i % 2 == 0:
        print(i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
7
```

### Output

```
2
4
6
```

---

## **1️⃣3️⃣ Dry Run**

N = 5

- i = 1 → odd → skip
- i = 2 → even → print 2
- i = 3 → odd → skip
- i = 4 → even → print 4
- i = 5 → odd → skip

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output      |
| ----: | ----------- |
|     5 | 2 4         |
|    10 | 2 4 6 8 10  |
|     1 | (no output) |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `%` operator is used to check divisibility
- Even numbers are divisible by 2
- Loop range must include N

---

## **1️⃣6️⃣ Real-Life Application**

- Filtering even values
- Number-based validations
- Mathematical computations

---

## **1️⃣7️⃣ Practice Questions**

1. Print odd numbers up to N
2. Print even numbers from M to N
3. Count how many even numbers are there

---

## **1️⃣8️⃣ Result**

The program correctly prints **all even numbers from 1 to N**.

---

## **1️⃣9️⃣ Conclusion**

A simple conditional looping problem that strengthens **basic logic**, **for loops**, and **number checking** using learned concepts only.
