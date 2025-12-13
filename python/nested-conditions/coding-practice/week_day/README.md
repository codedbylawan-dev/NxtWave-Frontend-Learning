# ✅ **Week Day**

---

## **1️⃣ Question**

Given a day number **1 to 7**, determine whether it is:

- **Week Start** → Monday (1) or Tuesday (2)
- **Weekend** → Saturday (6) or Sunday (7)
- **Midweek** → Wednesday (3), Thursday (4), Friday (5)

---

## **1.5️⃣ Category**

Conditional Statements → Multi-condition Categorization

---

## **2️⃣ Outline**

- Read day number
- Check if it is 1 or 2 → Week Start
- Check if it is 6 or 7 → Weekend
- Otherwise → Midweek

---

## **3️⃣ Objective**

To classify the day number into a weekday category.

---

## **4️⃣ Purpose**

Helps understand grouped conditions with simple comparisons.

---

## **5️⃣ Theory**

Mapping:

| Day | Meaning   | Category   |
| --- | --------- | ---------- |
| 1   | Monday    | Week Start |
| 2   | Tuesday   | Week Start |
| 3   | Wednesday | Midweek    |
| 4   | Thursday  | Midweek    |
| 5   | Friday    | Midweek    |
| 6   | Saturday  | Weekend    |
| 7   | Sunday    | Weekend    |

---

## **6️⃣ Step-by-Step Explanation**

1. Read input day number
2. Compare with 1 and 2 → print Week Start
3. Compare with 6 and 7 → print Weekend
4. Else → print Midweek

---

## **7️⃣ Method**

Use:

- Simple equality checks
- if → elif → else

---

## **8️⃣ Constraints**

- Day number is always between 1 and 7
- Output must match exactly (capitalization matters)

---

## **9️⃣ Common Mistakes**

❌ Mixing Midweek and Week Start
❌ Using wrong day numbers
❌ Not matching exact output text

---

## 🔟 Complexity

**Time:** O(1)
**Space:** O(1)

---

## **1️⃣1️⃣ Code**

```python
day = int(input())

if day == 1 or day == 2:
    print("Week Start")
elif day == 6 or day == 7:
    print("Weekend")
else:
    print("Midweek")
```

---

## **1️⃣2️⃣ Example**

### Input

```
6
```

### Output

```
Weekend
```

---

## **1️⃣3️⃣ Dry Run**

| Input | Condition Check       | Output     |
| ----- | --------------------- | ---------- |
| 1     | day == 1 → Week Start | Week Start |
| 2     | day == 2 → Week Start | Week Start |
| 3     | else → Midweek        | Midweek    |
| 6     | day == 6 → Weekend    | Weekend    |
| 7     | day == 7 → Weekend    | Weekend    |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output     |
| ----- | ---------- |
| 1     | Week Start |
| 2     | Week Start |
| 3     | Midweek    |
| 5     | Midweek    |
| 6     | Weekend    |
| 7     | Weekend    |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Grouped conditions can be handled using multiple `or` checks
- order of conditions matters
- Very common structure in many real programs

---

## **1️⃣6️⃣ Real-Life Application**

- Scheduling systems
- Attendance or shift categorization
- Weekly reminders and notifications

---

## **1️⃣7️⃣ Practice Questions**

1. Print whether a day number is **Working Day** or **Holiday**.
2. Categorize months into **Quarter 1, 2, 3, 4**.
3. Print whether a number belongs to **Group A, B, C** based on ranges.

---

## **1️⃣8️⃣ Result**

The program correctly identifies whether the day is Week Start, Weekend, or Midweek.

---

## **1️⃣9️⃣ Conclusion**

A simple and practical classification exercise that reinforces grouped condition checks.

---
