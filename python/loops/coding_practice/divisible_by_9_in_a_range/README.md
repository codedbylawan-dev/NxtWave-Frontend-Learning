# ✅ **Divisible by 9 in a Range**

---

## **1️⃣ Question**

Given two numbers **M** and **N**, print all the numbers from **M to N** that are **divisible by 9**.
If no such numbers are found, print **`No Numbers found`**.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Checking → Number Divisibility

---

## **2️⃣ Outline**

- Read M
- Read N
- Initialize a flag (count)
- Traverse from M to N
- Check divisibility by 9
- Print numbers if found
- Otherwise print message

---

## **3️⃣ Objective**

To identify and print numbers divisible by **9** within a given range.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- range-based iteration
- modulo operator `%`
- condition checking inside loops

---

## **5️⃣ Theory**

A number is divisible by **9** if:

```
number % 9 == 0
```

We check each number from **M to N** and print only those that satisfy the condition.

---

## **6️⃣ Step-by-Step Explanation**

1. Read M and N
2. Set `count = 0`
3. Loop from M to N
4. If the number is divisible by 9

   - print the number
   - increase count

5. After loop

   - if count is 0, print `No Numbers found`

---

## **7️⃣ Method**

Use:

- for loop
- if condition
- modulo operator `%`

---

## **8️⃣ Constraints**

- N ≥ M
- M and N can be any integers

---

## **9️⃣ Common Mistakes**

❌ Forgetting `% 9` condition
❌ Printing message inside loop
❌ Not handling the “no numbers” case

---

## **🔟 Complexity**

Time: **O(N − M + 1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

count = 0

for i in range(M, N + 1):
    if i % 9 == 0:
        print(i)
        count = count + 1

if count == 0:
    print("No Numbers found")
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
25
```

### Output

```
9
18
```

---

## **1️⃣3️⃣ Dry Run**

M = 3, N = 8

Numbers checked: 3, 4, 5, 6, 7, 8
No number divisible by 9

Output → `No Numbers found`

---

## **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output           |
| --- | --- | ---------------- |
| 5   | 25  | 9 18             |
| 3   | 8   | No Numbers found |
| 9   | 9   | 9                |

---
