# ✅ **Name of Month**

---

## **1️⃣ Question**

Given a number **N**, print the corresponding month name.
If N is not between 1 and 12, print **Invalid Month Number**.

---

## **1.5️⃣ Category**

Conditional Statements → Direct Mapping → Month Identification

---

## **2️⃣ Outline**

- Read N
- Check with if–elif chain
- Print the matching month name
- If not in range → print Invalid Month Number

---

## **3️⃣ Objective**

To convert a month number into a month name using conditional checks.

---

## **4️⃣ Purpose**

Strengthens your ability to map numbers to fixed outputs using if–elif–else.

---

## **5️⃣ Theory**

| Number | Month     |
| -----: | --------- |
|      1 | January   |
|      2 | February  |
|      3 | March     |
|      4 | April     |
|      5 | May       |
|      6 | June      |
|      7 | July      |
|      8 | August    |
|      9 | September |
|     10 | October   |
|     11 | November  |
|     12 | December  |

---

## **6️⃣ Step-by-Step Explanation**

1. Input N
2. If N matches 1 → print January
3. Continue checking all up to 12
4. If none match → Invalid Month Number

---

## **7️⃣ Method**

Use **if–elif–else** for direct mapping.

---

## **8️⃣ Constraints**

- N may be outside the range
- Only exact matching numbers produce month names

---

## **9️⃣ Common Mistakes**

❌ Forgetting to check out-of-range
❌ Misspelling month names
❌ Printing extra spaces or different text format

---

## 🔟 Complexity

Time: O(1)
Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

if N == 1:
    print("January")
elif N == 2:
    print("February")
elif N == 3:
    print("March")
elif N == 4:
    print("April")
elif N == 5:
    print("May")
elif N == 6:
    print("June")
elif N == 7:
    print("July")
elif N == 8:
    print("August")
elif N == 9:
    print("September")
elif N == 10:
    print("October")
elif N == 11:
    print("November")
elif N == 12:
    print("December")
else:
    print("Invalid Month Number")
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
April
```

---

## **1️⃣3️⃣ Dry Run**

For N = 10:

- Checks 1–9 → false
- N == 10 → true
- Output → **October**

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output               |
| ----- | -------------------- |
| 1     | January              |
| 6     | June                 |
| 12    | December             |
| 15    | Invalid Month Number |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- This is direct mapping using conditions
- Order of checks matters
- Out-of-range must be handled

---

## **1️⃣6️⃣ Real-Life Application**

- Calendar apps
- Date selection forms
- Generating month-based reports

---

## **1️⃣7️⃣ Practice Questions**

1. Print the season for a month number
2. Print the quarter of the year (Q1–Q4)
3. Print the number of days in a month

---

## **1️⃣8️⃣ Result**

The program correctly prints the month name or error message.

---

## **1️⃣9️⃣ Conclusion**

A straightforward month-mapping problem reinforcing conditional logic.

---
