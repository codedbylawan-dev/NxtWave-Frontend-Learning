# ✅ **Sum of Even Numbers from M to N**

---

## **1️⃣ Question**

Given two numbers **M** and **N**, print the **sum of all even numbers from M to N**.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Check → Range Summation

---

## **2️⃣ Outline**

- Read M
- Read N
- Initialize sum as 0
- Loop from M to N
- Check if the number is even
- Add even numbers to sum
- Print the sum

---

## **3️⃣ Objective**

To calculate the **sum of even numbers** within a given range using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you practice:

- looping through a range
- checking even numbers
- accumulating values

---

## **5️⃣ Theory**

- An **even number** is divisible by 2
- Condition to check even number:

  ```
  number % 2 == 0
  ```

Example:
M = 2, N = 6
Numbers → 2 3 4 5 6
Even numbers → 2 4 6
Sum → 12

---

## **6️⃣ Step-by-Step Explanation**

1. Read the value of M
2. Read the value of N
3. Create a variable `total` and set it to 0
4. Loop from M to N
5. If the number is even, add it to `total`
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

❌ Adding odd numbers by mistake
❌ Forgetting to check `% 2 == 0`
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
    if i % 2 == 0:
        total = total + i

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
2
6
```

### Output

```
12
```

---

## **1️⃣3️⃣ Dry Run**

M = 2, N = 6

- i = 2 → even → total = 2
- i = 3 → odd → skip
- i = 4 → even → total = 6
- i = 5 → odd → skip
- i = 6 → even → total = 12

Final Output → `12`

---

## **1️⃣4️⃣ Test Cases Table**

|   M |   N | Output |
| --: | --: | -----: |
|   2 |   6 |     12 |
|  10 |  20 |     90 |
|   1 |   1 |      0 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `% 2 == 0` identifies even numbers
- Loop range must include N
- Print the result after loop ends

---

## **1️⃣6️⃣ Real-Life Application**

- Summing even-indexed data
- Filtering values based on conditions
- Mathematical series calculations

---

## **1️⃣7️⃣ Practice Questions**

1. Print even numbers from M to N
2. Count even numbers from M to N
3. Sum of numbers divisible by 4 in a range

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of even numbers from M to N**.

---

## **1️⃣9️⃣ Conclusion**

A clear range-based problem that strengthens **for loop usage**, **conditional checks**, and **accumulation logic** using only learned concepts.
