# ✅ **Print Odd Numbers from M to N**

---

## **1️⃣ Question**

Given two numbers **M** and **N**, print **all odd numbers from M to N** in a **single line**, separated by a space.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Check → Number Printing

---

## **2️⃣ Outline**

- Read M
- Read N
- Loop from M to N
- Check if a number is odd
- Add odd numbers to a result string
- Print the result

---

## **3️⃣ Objective**

To print **odd numbers within a given range** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you practice:

- looping through a range
- identifying odd numbers
- building output step by step

---

## **5️⃣ Theory**

- An **odd number** leaves remainder **1** when divided by 2
- Condition to check odd number:

  ```
  number % 2 != 0
  ```

Example:
M = 5, N = 10
Numbers → 5 6 7 8 9 10
Odd numbers → 5 7 9

---

## **6️⃣ Step-by-Step Explanation**

1. Read M and N
2. Create an empty string to store output
3. Loop from M to N
4. Check if the number is odd
5. Add the number and a space to the string
6. Print the final string

---

## **7️⃣ Method**

Use:

- `input()`
- `int()`
- `for` loop
- `if` condition
- string concatenation

---

## **8️⃣ Constraints**

- M ≤ N
- M and N are integers

---

## **9️⃣ Common Mistakes**

❌ Printing even numbers
❌ Printing each number on a new line
❌ Missing spaces between numbers

---

## **🔟 Complexity**

Time: **O(N − M + 1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

result = ""

for i in range(M, N + 1):
    if i % 2 != 0:
        result = result + str(i) + " "

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
10
```

### Output

```
5 7 9
```

---

## **1️⃣3️⃣ Dry Run**

M = 9, N = 13

- i = 9 → odd → add "9 "
- i = 10 → even → skip
- i = 11 → odd → add "11 "
- i = 12 → even → skip
- i = 13 → odd → add "13 "

Final output → `9 11 13`

---

## **1️⃣4️⃣ Test Cases Table**

|   M |   N | Output              |
| --: | --: | ------------------- |
|   5 |  10 | 5 7 9               |
|   9 |  21 | 9 11 13 15 17 19 21 |
|   2 |   6 | 3 5                 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `% 2 != 0` identifies odd numbers
- Output can be built using strings
- Print once for single-line output

---

## **1️⃣6️⃣ Real-Life Application**

- Filtering odd values
- Number pattern problems
- Data validation

---

## **1️⃣7️⃣ Practice Questions**

1. Print even numbers from M to N
2. Count odd numbers in a range
3. Print odd numbers in reverse order

---

## **1️⃣8️⃣ Result**

The program correctly prints **odd numbers from M to N in one line**.

---

## **1️⃣9️⃣ Conclusion**

A clean and simple problem that strengthens **looping**, **conditions**, and **string building** using only learned concepts.
