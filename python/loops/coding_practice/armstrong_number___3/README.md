# ✅ **Armstrong Number – 3**

---

## **1️⃣ Question**

Given a number **N**, check whether it is an **Armstrong Number**.
Print **“Armstrong Number”** if it is, otherwise print **“Not an Armstrong Number”**.

---

## **1️⃣.5️⃣ Category**

For Loop → Digits → Power → Condition Checking

---

## **2️⃣ Outline**

- Read number N
- Convert N to string
- Find number of digits (K)
- Initialize sum as 0
- Traverse each digit
- Raise digit to power K
- Add to sum
- Compare sum with N
- Print result

---

## **3️⃣ Objective**

To determine whether a number satisfies the **Armstrong condition**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- digit extraction
- power calculation
- comparison logic

---

## **5️⃣ Theory**

A number is an **Armstrong Number** if:

> Sum of each digit raised to the power of total digits
> is equal to the number itself.

Example:
54748 has **5 digits**

5⁵ + 4⁵ + 7⁵ + 4⁵ + 8⁵ = **54748**

So it is an Armstrong Number.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input number as string
2. Count digits → K
3. Set total = 0
4. Loop through each digit
5. Convert digit to integer
6. Add digit⁽ᴷ⁾ to total
7. Compare total with original number
8. Print result

---

## **7️⃣ Method**

Use:

- input()
- len()
- for loop
- power operator
- if condition

---

## **8️⃣ Constraints**

- Input is a positive integer
- Output must be exact text

---

## **9️⃣ Common Mistakes**

❌ Comparing string with integer
❌ Using wrong power value
❌ Printing inside loop

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = input()
K = len(N)

total = 0

for digit in N:
    number = int(digit)
    total = total + (number ** K)

if total == int(N):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
```

---

## **1️⃣2️⃣ Example**

### Input

```
54748
```

### Output

```
Armstrong Number
```

---

## **1️⃣3️⃣ Dry Run**

N = "24"
K = 2

Digits:

- 2² = 4
- 4² = 16

Sum = 20 ≠ 24
So → Not an Armstrong Number

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output                  |
| ----: | ----------------------- |
| 54748 | Armstrong Number        |
|   153 | Armstrong Number        |
|    24 | Not an Armstrong Number |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Power depends on digit count
- Convert digits properly
- Final comparison decides result

---

## **1️⃣6️⃣ Real-Life Application**

- Number property checks
- Mathematical validations
- Coding logic practice

---

## **1️⃣7️⃣ Practice Questions**

1. Find Armstrong numbers between 1 and 1000
2. Count Armstrong numbers in a range
3. Print all Armstrong numbers up to N

---

## **1️⃣8️⃣ Result**

The program correctly identifies whether a number is an **Armstrong Number**.

---

## **1️⃣9️⃣ Conclusion**

This problem combines **digits, powers, loops, and conditions** in a clean way.

---
