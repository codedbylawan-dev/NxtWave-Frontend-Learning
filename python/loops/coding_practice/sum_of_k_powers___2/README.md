# ✅ **Sum of K Powers – 2**

---

## **1️⃣ Question**

Given a number **N**, print the **sum of the Kth power of all digits** of the number, where **K is the number of digits in N**.

---

## **1️⃣.5️⃣ Category**

For Loop → Digits → Power & Sum

---

## **2️⃣ Outline**

- Read number N
- Convert N to string
- Find number of digits (K)
- Traverse each digit
- Raise digit to power K
- Add to sum
- Print the sum

---

## **3️⃣ Objective**

To calculate the **sum of powers of digits** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- digits processing
- power calculation
- accumulation using loop

---

## **5️⃣ Theory**

If a number has **K digits**,
each digit is raised to the **power K**.

Example:
N = 24753
Digits = 2, 4, 7, 5, 3
K = 5

Sum =
2⁵ + 4⁵ + 7⁵ + 5⁵ + 3⁵

---

## **6️⃣ Step-by-Step Explanation**

1. Read input as string
2. Find length of string → K
3. Initialize sum as 0
4. Loop through each digit
5. Convert digit to number
6. Add digit⁽ᴷ⁾ to sum
7. Print the sum

---

## **7️⃣ Method**

Use:

- input()
- len()
- for loop
- power operator

---

## **8️⃣ Constraints**

- Input is a positive integer
- Output should be a single integer

---

## **9️⃣ Common Mistakes**

❌ Forgetting to convert digit to integer
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

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
24753
```

### Output

```
21231
```

---

## **1️⃣3️⃣ Dry Run**

N = "17"
K = 2

Digits:

- 1² = 1
- 7² = 49

Sum = 1 + 49 = **50**

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----: | -----: |
| 24753 |  21231 |
|    17 |     50 |
|     5 |      5 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Length of number decides power
- Digits must be converted to integers
- Loop handles digit processing easily

---

## **1️⃣6️⃣ Real-Life Application**

- Armstrong number checking
- Digit-based validations
- Mathematical digit analysis

---

## **1️⃣7️⃣ Practice Questions**

1. Sum of squares of digits
2. Product of digits
3. Count digits greater than 5

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of Kth powers of digits**.

---

## **1️⃣9️⃣ Conclusion**

A key problem that connects **digits, loops, and power calculations**.

---
