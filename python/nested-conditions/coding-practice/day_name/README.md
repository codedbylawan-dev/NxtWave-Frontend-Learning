# ✅ **Day Name**

---

## **1️⃣ Question**

Given a day number (1–7), print the corresponding **day name**:

| Number | Day Name  |
| ------ | --------- |
| 1      | Monday    |
| 2      | Tuesday   |
| 3      | Wednesday |
| 4      | Thursday  |
| 5      | Friday    |
| 6      | Saturday  |
| 7      | Sunday    |

---

## **1.5️⃣ Category**

Conditional Statements → Equality Checking → Basic Mapping

---

## **2️⃣ Outline**

- Read day number
- Compare with values 1 to 7
- Print the matching day name

---

## **3️⃣ Objective**

To map a numeric value to a specific string output using simple conditions.

---

## **4️⃣ Purpose**

Understanding how to create direct mappings using `if–elif–else`.

---

## **5️⃣ Theory**

Each number corresponds to exactly one day; therefore simple equality checks are enough:

```
if day == 1 → Monday
elif day == 2 → Tuesday
...
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read input number
2. Check if it equals 1 → print Monday
3. Else if equals 2 → print Tuesday
4. Continue until 7
5. No need for “else” because constraint says number is always 1–7

---

## **7️⃣ Method**

Use chained equality comparisons with `==` and `elif`.

---

## **8️⃣ Constraints**

- Day number is always between 1 and 7
- Output must match exactly (case-sensitive)

---

## **9️⃣ Common Mistakes**

❌ Printing extra spaces
❌ Misspelled day names
❌ Using invalid ranges (like day < 3)

---

## 🔟 Complexity

- Time: **O(1)**
- Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
day = int(input())

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
else:
    print("Sunday")
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
```

### Output

```
Wednesday
```

---

## **1️⃣3️⃣ Dry Run**

| Input | Condition True | Output    |
| ----- | -------------- | --------- |
| 1     | day == 1       | Monday    |
| 2     | day == 2       | Tuesday   |
| 3     | day == 3       | Wednesday |
| 7     | else           | Sunday    |

---

## **1️⃣4️⃣ Test Cases Table**

| Day Number | Expected Output |
| ---------- | --------------- |
| 1          | Monday          |
| 2          | Tuesday         |
| 5          | Friday          |
| 7          | Sunday          |
| 6          | Saturday        |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Straight equality checks are perfect for fixed mappings.
- Output text must match exactly as given.

---

## **1️⃣6️⃣ Real-Life Application**

- Scheduling apps
- Timetable generation
- Calendar-based reminders

---

## **1️⃣7️⃣ Practice Questions**

1. Map month number (1–12) to month name.
2. Print grade letter based on marks.
3. Print season based on month (again with equality checks).

---

## **1️⃣8️⃣ Result**

The program correctly prints the name of the day according to the day number.

---

## **1️⃣9️⃣ Conclusion**

A simple and effective use of chained conditions to perform direct mapping.

---
