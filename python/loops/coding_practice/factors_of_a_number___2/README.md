# ✅ **Factors of a Number – 2**

---

## **1️⃣ Question**

Given a number **N**, print **all the factors of N separated by a space**.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditions → Factors

---

## **2️⃣ Outline**

- Read N
- Start from 1
- Check which numbers divide N
- Collect factors
- Print them in one line separated by space

---

## **3️⃣ Objective**

To find and print **all factors of a number** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- divisibility
- looping from 1 to N
- building output step by step

---

## **5️⃣ Theory**

A **factor** of a number is a number that divides it **exactly** (remainder 0).

Example:
For N = 15
Factors are → 1, 3, 5, 15

---

## **6️⃣ Step-by-Step Explanation**

1. Read the number N
2. Start a loop from 1 to N
3. Check if N % i == 0
4. If yes, add i to result string
5. After loop ends, print result

---

## **7️⃣ Method**

Use:

- for loop
- modulo operator (%)
- string concatenation

---

## **8️⃣ Constraints**

- N is a positive integer
- Output must be in **one line**
- Factors separated by **space**

---

## **9️⃣ Common Mistakes**

❌ Printing non-factors
❌ Printing each factor on new line
❌ Forgetting space between factors

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

result = ""

for i in range(1, N + 1):
    if N % i == 0:
        result = result + str(i) + " "

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
15
```

### Output

```
1 3 5 15
```

---

## **1️⃣3️⃣ Dry Run**

N = 9

- i = 1 → factor → add 1
- i = 3 → factor → add 3
- i = 9 → factor → add 9

Final output → `1 3 9`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output   |
| ----: | -------- |
|     9 | 1 3 9    |
|    15 | 1 3 5 15 |
|     7 | 1 7      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Factors always include **1 and the number itself**
- `%` operator is key for divisibility
- String building avoids advanced printing

---

## **1️⃣6️⃣ Real-Life Application**

- Number theory basics
- Mathematical validations
- Competitive programming foundations

---

## **1️⃣7️⃣ Practice Questions**

1. Print only even factors
2. Count number of factors
3. Find sum of factors

---

## **1️⃣8️⃣ Result**

The program correctly prints **all factors of N in one line**.

---

## **1️⃣9️⃣ Conclusion**

A fundamental problem that strengthens **loops, conditions, and logic**.

---
