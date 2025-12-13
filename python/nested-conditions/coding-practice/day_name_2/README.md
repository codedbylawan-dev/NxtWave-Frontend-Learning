# ✅ **Day Name – 2**

---

## **1️⃣ Question**

You are given:

- **D** → Day name of the **1st day** of the month
- **N** → A date (like 16th)

You must find which weekday falls on date **N** of that month.

---

## **1.5️⃣ Category**

Date Arithmetic → Day Cycles → Conditional Logic

---

## **2️⃣ Outline**

- Convert day name to a number (Monday → 1, Tuesday → 2, … Sunday → 7)
- Calculate how many days pass from day 1 to day N
- Apply `(N – 1)` days forward
- Wrap around after 7
- Convert the final number back to a day name

---

## **3️⃣ Objective**

To determine the weekday after adding `(N - 1)` days to the starting weekday.

---

## **4️⃣ Purpose**

This teaches:

- rotating through cycles
- arithmetic with modulo
- converting between names ↔ numbers

---

## **5️⃣ Theory**

### Step 1: Assign numbers

| Day       | Number |
| --------- | ------ |
| Monday    | 1      |
| Tuesday   | 2      |
| Wednesday | 3      |
| Thursday  | 4      |
| Friday    | 5      |
| Saturday  | 6      |
| Sunday    | 7      |

### Step 2: Move forward

The day on date **N** is:

```
final_day = (start_day_number + (N - 1)) % 7
```

Special case:
If result is **0**, it means **Sunday**.

---

## **6️⃣ Step-by-Step Explanation**

For **Monday**, N = 16:

- Monday = 1
- N – 1 = 15
- final = (1 + 15) % 7 = 16 % 7 = 2
- 2 → Tuesday
  → Correct.

---

## **7️⃣ Method**

- Map day name → number using if–elif
- Use modulo
- Map number → day name using if–elif

---

## **8️⃣ Constraints**

- Day will always be valid
- N will always be positive
- Use only basic arithmetic

---

## **9️⃣ Common Mistakes**

❌ Forgetting to subtract 1
❌ Not handling modulo 0 → Sunday
❌ Case mismatch

---

## 🔟 Complexity

O(1) time
O(1) space

---

## **1️⃣1️⃣ Code (BEGINNER SAFE — ONLY if/elif + arithmetic)**

```python
D = input()
N = int(input())

# Convert day name to number
if D == "Monday":
    start = 1
elif D == "Tuesday":
    start = 2
elif D == "Wednesday":
    start = 3
elif D == "Thursday":
    start = 4
elif D == "Friday":
    start = 5
elif D == "Saturday":
    start = 6
else:
    start = 7   # Sunday

# Calculate final day number
final = (start + (N - 1)) % 7

# Special handling: if modulo result is 0 → Sunday
if final == 0:
    final = 7

# Convert number back to day name
if final == 1:
    print("Monday")
elif final == 2:
    print("Tuesday")
elif final == 3:
    print("Wednesday")
elif final == 4:
    print("Thursday")
elif final == 5:
    print("Friday")
elif final == 6:
    print("Saturday")
else:
    print("Sunday")
```

---

## **1️⃣2️⃣ Example**

### Input

```
Monday
16
```

### Output

```
Tuesday
```

---

## **1️⃣3️⃣ Dry Run**

Start = Monday → 1
N = 16 → move 15 days
(1 + 15) % 7 = 16 % 7 = 2 → Tuesday

---

## **1️⃣4️⃣ Test Cases Table**

| Input        | Output    |
| ------------ | --------- |
| Monday, 1    | Monday    |
| Monday, 7    | Sunday    |
| Monday, 8    | Monday    |
| Tuesday, 17  | Thursday  |
| Sunday, 2    | Monday    |
| Thursday, 14 | Wednesday |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Dates move in cycles of 7
- Modulo helps wrap the cycle
- Convert names ⇄ numbers for easy math

---

## **1️⃣6️⃣ Real-Life Application**

- Calendar apps
- Scheduling systems
- Billing cycles
- Attendance software

---

## **1️⃣7️⃣ Practice Questions**

1. Find the day after X days from today.
2. Given weekday and date, find previous weekday.
3. Find weekday of the last day of the month.

---

## **1️⃣8️⃣ Result**

You can now compute weekday of any date using only simple logic.

---

## **1️⃣9️⃣ Conclusion**

A tough-looking problem but simple once you convert days into numbers.

---
