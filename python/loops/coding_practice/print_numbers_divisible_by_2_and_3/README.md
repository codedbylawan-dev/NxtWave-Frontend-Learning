# ✅ **Print Numbers Divisible by 2 and 3**

---

## **1️⃣ Question**

Given a number **N**, print all the numbers from **1 to N** that are divisible by **both 2 and 3**, each on a new line.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Check → Divisibility

---

## **2️⃣ Outline**

- Read N
- Loop from 1 to N
- Check divisibility by 2 and 3
- Print the number if condition is satisfied

---

## **3️⃣ Objective**

To print numbers that satisfy **multiple conditions** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- checking more than one condition
- using logical operators
- filtering numbers in a loop

---

## **5️⃣ Theory**

A number is divisible by **both 2 and 3** if:

```
number % 2 == 0 and number % 3 == 0
```

Such numbers are multiples of **6**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the number N
2. Start a loop from 1 to N
3. For each number, check:

   - divisible by 2
   - divisible by 3

4. If both are true, print the number

---

## **7️⃣ Method**

Use:

- input()
- for loop
- if condition with `and`
- print statement

---

## **8️⃣ Constraints**

- N is a positive integer

---

## **9️⃣ Common Mistakes**

❌ Using `or` instead of `and`
❌ Forgetting one of the divisibility checks
❌ Printing all numbers instead of filtered ones

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(1, N + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
15
```

### Output

```
6
12
```

---

## **1️⃣3️⃣ Dry Run**

N = 15

Numbers divisible by both 2 and 3:

- 6 → printed
- 12 → printed

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output      |
| ----: | ----------- |
|     6 | 6           |
|    12 | 6 12        |
|     5 | (no output) |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Use `and` when **all conditions must be true**
- `%` helps check divisibility
- Loop filters required values

---

## **1️⃣6️⃣ Real-Life Application**

- Filtering valid records
- Eligibility checks
- Rule-based data selection

---

## **1️⃣7️⃣ Practice Questions**

1. Print numbers divisible by 4 and 5
2. Print numbers divisible by 2, 3, and 5
3. Print multiples of 6 up to N

---

## **1️⃣8️⃣ Result**

The program prints **only numbers divisible by both 2 and 3**.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens **conditional logic inside loops** using multiple checks.

---
