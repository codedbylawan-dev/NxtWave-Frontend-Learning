# ✅ **Get Season**

---

## **1️⃣ Question**

Given a month number (1–12), print the season it belongs to:

- Winter → 11, 12, 1
- Spring → 2, 3
- Summer → 4, 5, 6
- Rainy → 7, 8
- Autumn → 9, 10

---

## **1.5️⃣ Category**

Conditions → Relational Operators → Logical Operators

---

## **2️⃣ Outline**

- Read month
- Check all winter values using OR
- Check spring values
- Check summer values
- Check rainy values
- Else → autumn

---

## **3️⃣ Objective**

To classify a month into its correct season using only basic conditional logic.

---

## **4️⃣ Purpose**

Strengthens multi-condition checking using logical operators (`or`).

---

## **5️⃣ Theory**

You can check multiple matching values using:

```
if month == 11 or month == 12 or month == 1
```

Because you **have learned OR** but not lists.

---

## **6️⃣ Step-by-Step Explanation**

1. Read month
2. Check if month is 11 OR 12 OR 1
3. Else check if month is 2 OR 3
4. Else check if month is 4,5,6
5. Else check if month is 7 OR 8
6. Else print Autumn

---

## **7️⃣ Method**

Use:

- `==`
- `or`
- `if–elif–else`

No lists, no `in`.

---

## **8️⃣ Constraints**

- Month is between 1 and 12
- Only one valid season output

---

## **9️⃣ Common Mistakes**

❌ Using `<` or `>` instead of checking exact months
❌ Using lists (not learned yet)
❌ Using `in` operator (not learned yet)

---

## 🔟 Complexity

Time: **O(1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

(100% based on concepts you learned)

```python
month = int(input())

if month == 11 or month == 12 or month == 1:
    print("Winter")
elif month == 2 or month == 3:
    print("Spring")
elif month == 4 or month == 5 or month == 6:
    print("Summer")
elif month == 7 or month == 8:
    print("Rainy")
else:
    print("Autumn")
```

---

## **1️⃣2️⃣ Example**

### Input

```
1
```

### Output

```
Winter
```

---

## **1️⃣3️⃣ Dry Run**

| Input | Condition True | Output |
| ----- | -------------- | ------ |
| 1     | Winter group   | Winter |
| 4     | Summer group   | Summer |
| 7     | Rainy group    | Rainy  |
| 10    | Autumn group   | Autumn |

---

## **1️⃣4️⃣ Test Cases Table**

| Month | Output |
| ----- | ------ |
| 12    | Winter |
| 2     | Spring |
| 5     | Summer |
| 7     | Rainy  |
| 10    | Autumn |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Multiple equality checks can be combined using **OR**
- You don’t need lists for grouped conditions
- Logical operators help simplify complex decisions

---

## **1️⃣6️⃣ Real-Life Application**

- Seasonal adjustments in apps
- Weather-based alerts
- Calendar systems

---

## **1️⃣7️⃣ Practice Questions**

1. Check if a number is 2, 4, or 6 (even list using OR).
2. Print the quarter of the year using OR conditions.
3. Map months to number of days (28/30/31).

---

## **1️⃣8️⃣ Result**

The program prints the correct season using only learned concepts.

---

## **1️⃣9️⃣ Conclusion**

A solid example of how to handle grouped conditions without using advanced data structures.

---
