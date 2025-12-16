# ✅ **Sum of Digits**

---

## **1️⃣ Question**

Given a **positive number**, print the **sum of all its digits**.

---

## **1️⃣.5️⃣ Category**

For Loop → String Processing → Digit Calculation

---

## **2️⃣ Outline**

- Read the number as input
- Treat the number as a string
- Traverse each digit
- Convert digit to number and add to sum
- Print the final sum

---

## **3️⃣ Objective**

To calculate the **sum of digits** of a number using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- digit-by-digit processing
- converting characters to integers
- accumulating values using a loop

---

## **5️⃣ Theory**

When a number is read as a **string**, each character represents one digit.
By converting each digit into an integer, we can add them to get the total sum.

Example:
Number = `151893`
Digits = `1, 5, 1, 8, 9, 3`
Sum = `27`

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input number
2. Store it as a string
3. Initialize a variable `total` with value 0
4. Use a for loop to go through each digit
5. Convert digit to integer and add to `total`
6. Print `total`

---

## **7️⃣ Method**

Use:

- input()
- for loop
- int() for conversion
- addition operator

---

## **8️⃣ Constraints**

- Input is a positive integer
- Output should be a single integer

---

## **9️⃣ Common Mistakes**

❌ Forgetting to convert digit to integer
❌ Initializing sum incorrectly
❌ Printing intermediate results instead of final sum

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
number = input()

total = 0
for digit in number:
    total = total + int(digit)

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
151893
```

### Output

```
27
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"692"`

- total = 0
- digit = '6' → total = 6
- digit = '9' → total = 15
- digit = '2' → total = 17

Final Output → `17`

---

## **1️⃣4️⃣ Test Cases Table**

|  Input | Output |
| -----: | ------ |
| 151893 | 27     |
|    692 | 17     |
|      5 | 5      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Strings help process digits easily
- Always convert digit characters to integers
- for loop is ideal for digit traversal

---

## **1️⃣6️⃣ Real-Life Application**

- Digital sum calculations
- Checksum validation
- Number analysis tasks

---

## **1️⃣7️⃣ Practice Questions**

1. Find the product of digits
2. Count even digits in a number
3. Find the largest digit in a number

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of all digits** in the given number.

---

## **1️⃣9️⃣ Conclusion**

This problem builds a strong foundation in **digit processing** and **loop-based calculations** using Python.
