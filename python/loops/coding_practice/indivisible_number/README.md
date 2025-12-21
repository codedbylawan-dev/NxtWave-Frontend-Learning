# ✅ **Indivisible Number**

---

## **1️⃣ Question**

Given a number **N**, check whether **N is divisible by any number from 2 to 9**.

- If **N is divisible by at least one number from 2 to 9**, print
  **`Divisible Number`**
- Otherwise, print
  **`Indivisible Number`**

---

## **1️⃣.5️⃣ Category**

For Loop → Divisibility Check → Conditional Logic

---

## **2️⃣ Outline**

- Read N
- Assume number is indivisible
- Check divisibility from 2 to 9
- If divisible → update status
- Print result

---

## **3️⃣ Objective**

To check **divisibility within a range** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- modulo operator `%`
- checking conditions inside a loop
- using flags (True / False logic)

---

## **5️⃣ Theory**

A number **N is divisible by another number X** if:

```
N % X == 0
```

We test N with all numbers from **2 to 9**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the number N
2. Set a variable `is_divisible = False`
3. Loop from 2 to 9
4. If N is divisible by any number

   - set `is_divisible = True`

5. After loop

   - if divisible → print message
   - else → print message

---

## **7️⃣ Method**

Use:

- for loop
- modulo operator
- if condition

---

## **8️⃣ Constraints**

- N is a positive integer

---

## **9️⃣ Common Mistakes**

❌ Checking only one divisor
❌ Forgetting `%` operator
❌ Printing result inside loop

---

## **🔟 Complexity**

Time: **O(1)** (fixed range from 2 to 9)
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

is_divisible = False

for i in range(2, 10):
    if N % i == 0:
        is_divisible = True

if is_divisible:
    print("Divisible Number")
else:
    print("Indivisible Number")
```

---

## **1️⃣2️⃣ Example**

### Input

```
15
```

### Output

```
Divisible Number
```

---

## **1️⃣3️⃣ Dry Run**

Input → `103`

Check:

- 103 % 2 ≠ 0
- 103 % 3 ≠ 0
- 103 % 4 ≠ 0
- …
- 103 % 9 ≠ 0

No divisor found
→ print **Indivisible Number**

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output             |
| ----- | ------------------ |
| 15    | Divisible Number   |
| 103   | Indivisible Number |
| 18    | Divisible Number   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `%` is used to test divisibility
- Flag variables help track conditions
- Loop range is fixed (2–9)

---

## **1️⃣6️⃣ Real-Life Application**

- Prime number checks (basic idea)
- Validation logic
- Number filtering

---

## **1️⃣7️⃣ Practice Questions**

1. Check divisibility from 2 to 5
2. Print all divisors from 2 to 9
3. Count how many numbers divide N

---

## **1️⃣8️⃣ Result**

The program correctly identifies whether a number is **divisible or indivisible**.

---

## **1️⃣9️⃣ Conclusion**

A clean problem that strengthens **modulo logic and loop-based condition checking**.

---
