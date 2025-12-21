# ✅ **Divisible by 6**

---

## **1️⃣ Question**

Given two numbers **M** and **N**, print the numbers from **M to N** that are **divisible by 6**.
If **no such numbers exist**, print **`No Numbers Found`**.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Checking → Counting & Printing

---

## **2️⃣ Outline**

- Read M
- Read N
- Initialize a flag (or count)
- Traverse numbers from M to N
- Check divisibility by 6
- Print valid numbers
- If none found, print message

---

## **3️⃣ Objective**

To identify and print numbers divisible by **6** within a range.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- modulus operator `%`
- conditional statements inside loops
- handling “no result” cases

---

## **5️⃣ Theory**

A number is **divisible by 6** if:

```
number % 6 == 0
```

We check each number from **M to N** and print only those that satisfy this condition.

---

## **6️⃣ Step-by-Step Explanation**

1. Read M and N
2. Set `found = False`
3. Loop from M to N
4. If number is divisible by 6

   - print the number
   - set `found = True`

5. After loop, if `found` is False

   - print `No Numbers Found`

---

## **7️⃣ Method**

Use:

- for loop
- if condition
- modulus operator

---

## **8️⃣ Constraints**

- N ≥ M
- M and N are integers

---

## **9️⃣ Common Mistakes**

❌ Forgetting `% 6` condition
❌ Printing message even when numbers exist
❌ Not handling “no numbers” case

---

## **🔟 Complexity**

Time: **O(N − M + 1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

found = False

for i in range(M, N + 1):
    if i % 6 == 0:
        print(i, end=" ")
        found = True

if not found:
    print("No Numbers Found")
```

---

## **1️⃣2️⃣ Example**

### Input

```
6
23
```

### Output

```
6 12 18
```

---

## **1️⃣3️⃣ Dry Run**

M = 2, N = 5

- 2 % 6 ≠ 0
- 3 % 6 ≠ 0
- 4 % 6 ≠ 0
- 5 % 6 ≠ 0

No number printed → Output: `No Numbers Found`

---

## **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output           |
| --- | --- | ---------------- |
| 6   | 23  | 6 12 18          |
| 2   | 5   | No Numbers Found |
| 12  | 12  | 12               |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `%` helps check divisibility
- Use a flag to detect empty output
- Loop + condition is a powerful combo

---

## **1️⃣6️⃣ Real-Life Application**

- Filtering valid values
- Rule-based number selection
- Data validation

---

## **1️⃣7️⃣ Practice Questions**

1. Print numbers divisible by 5
2. Print numbers divisible by both 3 and 4
3. Count numbers divisible by 6

---

## **1️⃣8️⃣ Result**

The program correctly prints numbers divisible by **6** or displays **No Numbers Found**.

---

## **1️⃣9️⃣ Conclusion**

A clean loop-based filtering problem that improves **condition checking skills**.

---
