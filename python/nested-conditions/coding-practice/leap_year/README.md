# ✅ **Leap Year**

---

## **1️⃣ Question**

Read a year **Y** and determine whether it is a **leap year**.

A year is a leap year if **any** of these conditions is true:

1. **Y is divisible by 400**
2. **Y is divisible by 4 AND NOT divisible by 100**

Print:

- **True** → if Y is a leap year
- **False** → otherwise

---

## **1.5️⃣ Category**

Arithmetic → Divisibility → Multi-condition Logic

---

## **2️⃣ Outline**

- Read Y
- Check if divisible by 400
- Else check if divisible by 4 but not 100
- Print True or False

---

## **3️⃣ Objective**

To correctly determine leap years using mathematical divisibility rules.

---

## **4️⃣ Purpose**

Leap year logic is a classic programming problem used to practice combined logical conditions (AND + OR).

---

## **5️⃣ Theory**

A leap year must satisfy:

[
Y % 400 = 0
]

OR

[
(Y % 4 = 0) \And (Y % 100 \neq 0)
]

These rules match the real-world definition of leap years.

---

## **6️⃣ Step-by-Step Explanation**

1. Read Y
2. Compute `c1 = (Y % 400 == 0)`
3. Compute `c2 = (Y % 4 == 0)` and `(Y % 100 != 0)`
4. If either `c1` or (`c2` AND not divisible by 100) is true → print True
5. Else → print False

---

## **7️⃣ Method**

- Use modulus `%`
- Combine conditions using `and` + `or`
- Print boolean as a string

---

## **8️⃣ Constraints**

- Y is an integer
- Output must be **True** or **False** exactly
- No extra text allowed

---

## **9️⃣ Common Mistakes**

❌ Checking divisible by 4 only
❌ Forgetting the 100-rule exception
❌ Wrong logical grouping (parentheses matter!)
❌ Returning uppercase TRUE/FALSE incorrectly

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
Y = int(input())

cond1 = (Y % 400 == 0)
cond2 = (Y % 4 == 0) and (Y % 100 != 0)

if cond1 or cond2:
    print("True")
else:
    print("False")
```

---

## **1️⃣2️⃣ Example**

### Input

```
2016
```

### Output

```
True
```

---

## **1️⃣3️⃣ Dry Run**

| Y    | Y%400 | Y%4 | Y%100 | c1  | c2  | Output |
| ---- | ----- | --- | ----- | --- | --- | ------ |
| 2016 | 16    | 0   | 16    | No  | Yes | True   |
| 1800 | 200   | 0   | 0     | No  | No  | False  |
| 2000 | 0     | 0   | 0     | Yes | No  | True   |
| 1900 | 300   | 0   | 0     | No  | No  | False  |

---

## **1️⃣4️⃣ Test Cases Table**

| Year | Leap? |
| ---- | ----- |
| 2016 | True  |
| 1800 | False |
| 2000 | True  |
| 1996 | True  |
| 1900 | False |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Leap year rules rely on a combination of AND + OR
- Years divisible by 100 are NOT leap years unless divisible by 400
- Carefully use parentheses for correct logic

---

## **1️⃣6️⃣ Real-Life Application**

- Calendar date calculations
- Timekeeping algorithms
- Scheduling and validity checks in software systems

---

## **1️⃣7️⃣ Practice Questions**

1. Print the next leap year after a given year.
2. Print how many leap years exist between two given years.
3. Determine if a date (day, month, year) is valid considering leap years.

---

## **1️⃣8️⃣ Result**

The program correctly identifies leap years using standard conditions.

---

## **1️⃣9️⃣ Conclusion**

Leap year checking is a classic logic exercise that reinforces understanding of combined conditions. Mastering this prepares you for more complex validation problems.

---
