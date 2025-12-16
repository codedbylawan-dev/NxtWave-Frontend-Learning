# ✅ **Product of Odd Numbers from M to N**

---

## **1️⃣ Question**

Given two numbers **M** and **N**, print the **product of all odd numbers from M to N**.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Check → Range Product

---

## **2️⃣ Outline**

- Read M
- Read N
- Initialize product as 1
- Loop from M to N
- Check if the number is odd
- Multiply odd numbers
- Print the final product

---

## **3️⃣ Objective**

To calculate the **product of odd numbers** within a given range using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you practice:

- looping through a range
- identifying odd numbers
- multiplying values step by step

---

## **5️⃣ Theory**

- An **odd number** gives remainder **1** when divided by 2
- Condition to check odd number:

  ```
  number % 2 == 1
  ```

Example:
M = 2, N = 7
Numbers → 2 3 4 5 6 7
Odd numbers → 3 5 7
Product → 105

---

## **6️⃣ Step-by-Step Explanation**

1. Read the value of M
2. Read the value of N
3. Create a variable `product` and set it to 1
4. Loop from M to N
5. If the number is odd, multiply it with `product`
6. After the loop, print `product`

---

## **7️⃣ Method**

Use:

- `input()`
- `int()`
- `for` loop
- `if` condition
- multiplication operator

---

## **8️⃣ Constraints**

- M and N are integers
- M ≤ N

---

## **9️⃣ Common Mistakes**

❌ Forgetting to initialize product as 1
❌ Including even numbers
❌ Printing product inside the loop

---

## **🔟 Complexity**

Time: **O(N − M + 1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

product = 1

for i in range(M, N + 1):
    if i % 2 == 1:
        product = product * i

print(product)
```

---

## **1️⃣2️⃣ Example**

### Input

```
2
7
```

### Output

```
105
```

---

## **1️⃣3️⃣ Dry Run**

M = 2, N = 7

- i = 2 → even → skip
- i = 3 → odd → product = 3
- i = 4 → even → skip
- i = 5 → odd → product = 15
- i = 6 → even → skip
- i = 7 → odd → product = 105

Final Output → `105`

---

## **1️⃣4️⃣ Test Cases Table**

|   M |   N | Output |
| --: | --: | -----: |
|   2 |   7 |    105 |
|   4 |   8 |     35 |
|   1 |   1 |      1 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Initialize product as **1**, not 0
- `% 2 == 1` checks odd numbers
- Loop must include N

---

## **1️⃣6️⃣ Real-Life Application**

- Multiplying filtered values
- Mathematical sequences
- Problem-solving with conditions

---

## **1️⃣7️⃣ Practice Questions**

1. Product of even numbers from M to N
2. Product of numbers divisible by 3
3. Product of odd numbers from 1 to N

---

## **1️⃣8️⃣ Result**

The program correctly prints the **product of odd numbers from M to N**.

---

## **1️⃣9️⃣ Conclusion**

A solid range-based problem that reinforces **for loops**, **odd number checking**, and **multiplication logic** using only learned concepts.
