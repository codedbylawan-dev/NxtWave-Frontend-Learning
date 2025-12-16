# ✅ **Factorial**

---

## **1️⃣ Question**

Given a positive integer **N**, print the **factorial of N**.

---

## **1️⃣.5️⃣ Category**

For Loop → Mathematical Computation

---

## **2️⃣ Outline**

- Read N
- Initialize a variable for result
- Multiply numbers from 1 to N
- Print the final result

---

## **3️⃣ Objective**

To compute the **factorial** of a number using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- repeated multiplication
- accumulation using loops
- basic mathematical logic

---

## **5️⃣ Theory**

**Factorial** of a number N is the product of all positive integers from 1 to N.

Example:
Factorial of 4
= 4 × 3 × 2 × 1
= 24

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input number N
2. Initialize `fact` with value 1
3. Use a for loop from 1 to N
4. Multiply `fact` by the current number
5. After loop ends, print `fact`

---

## **7️⃣ Method**

Use:

- input()
- for loop
- multiplication operator

---

## **8️⃣ Constraints**

- N is a positive integer
- Output is a single integer

---

## **9️⃣ Common Mistakes**

❌ Initializing factorial as 0
❌ Forgetting multiplication
❌ Printing inside the loop

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

fact = 1
for i in range(1, N + 1):
    fact = fact * i

print(fact)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
24
```

---

## **1️⃣3️⃣ Dry Run**

Input → `5`

- fact = 1
- i = 1 → fact = 1
- i = 2 → fact = 2
- i = 3 → fact = 6
- i = 4 → fact = 24
- i = 5 → fact = 120

Final Output → `120`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----: | -----: |
|     1 |      1 |
|     4 |     24 |
|     7 |   5040 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Factorial starts with 1, not 0
- Loop multiplies values step by step
- Very common interview problem

---

## **1️⃣6️⃣ Real-Life Application**

- Combinations and permutations
- Probability calculations
- Mathematical modeling

---

## **1️⃣7️⃣ Practice Questions**

1. Print factorial of numbers from 1 to N
2. Find factorial using while loop
3. Find factorial of even numbers only

---

## **1️⃣8️⃣ Result**

The program correctly prints the **factorial of N**.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens understanding of **loops**, **multiplication**, and **step-by-step accumulation** in Python.
