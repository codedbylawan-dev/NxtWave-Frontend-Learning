# ✅ **Sum of Even Numbers Up to N**

---

## **1️⃣ Question**

Given a number **N**, print the **sum of all even numbers from 1 to N**.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Check → Summation

---

## **2️⃣ Outline**

- Read N
- Initialize sum as 0
- Loop from 1 to N
- Check if the number is even
- Add even numbers to sum
- Print the sum

---

## **3️⃣ Objective**

To calculate the **sum of even numbers** within a given range using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you practice:

- looping through numbers
- identifying even numbers
- accumulating a sum

---

## **5️⃣ Theory**

- An **even number** is divisible by 2
- Condition to check even number:

  ```
  number % 2 == 0
  ```

Example:
N = 6
Numbers → 1 2 3 4 5 6
Even numbers → 2 4 6
Sum → 12

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input value N
2. Create a variable `total` and set it to 0
3. Loop from 1 to N
4. If the number is even, add it to `total`
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

❌ Adding odd numbers
❌ Forgetting to initialize sum as 0
❌ Printing inside the loop

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
    if i % 2 == 0:
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
12
```

---

## **1️⃣3️⃣ Dry Run**

N = 6

- i = 1 → odd → skip
- i = 2 → even → total = 2
- i = 3 → skip
- i = 4 → total = 6
- i = 5 → skip
- i = 6 → total = 12

Final Output → `12`

---

## **1️⃣4️⃣ Test Cases Table**

|   N | Output |
| --: | -----: |
|   6 |     12 |
|  10 |     30 |
|   1 |      0 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `% 2 == 0` is used to find even numbers
- Always initialize sum before loop
- Print result after loop ends

---

## **1️⃣6️⃣ Real-Life Application**

- Summing even values in data
- Mathematical calculations
- Filtering numbers based on conditions

---

## **1️⃣7️⃣ Practice Questions**

1. Sum of odd numbers up to N
2. Count even numbers up to N
3. Sum of numbers divisible by 4

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of even numbers from 1 to N**.

---

## **1️⃣9️⃣ Conclusion**

A foundational loop problem that strengthens **conditions**, **iteration**, and **summation logic** using only learned concepts.
