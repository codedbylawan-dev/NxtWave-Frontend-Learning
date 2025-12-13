# ✅ **Days Conversion**

---

## **1️⃣ Question**

Convert a given number of days **N** into:

- **Years (Y)** → 1 year = **365 days**
- **Weeks (W)** → 1 week = **7 days**
- **Days (D)** → remaining days

Output must be:

```
Y years W weeks D days
```

---

## **1.5️⃣ Category**

Arithmetic → Division & Modulus → Time Conversion

---

## **2️⃣ Outline**

- Read N
- Find number of years (`N // 365`)
- Subtract year-days
- Find weeks from remaining (`remaining // 7`)
- Remaining after weeks → days
- Print result

---

## **3️⃣ Objective**

To convert total days into a structured time breakdown.

---

## **4️⃣ Purpose**

Teaches multi-step arithmetic conversion using integer division and modulus.

---

## **5️⃣ Theory**

1 Year = 365 days
1 Week = 7 days

Steps:

```
years = N // 365
remaining = N % 365

weeks = remaining // 7
days = remaining % 7
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read **N**
2. Compute full years
3. Compute remaining days after removing years
4. Compute full weeks
5. Compute final leftover days
6. Print in the required format

---

## **7️⃣ Method**

Use:

- `//` integer division
- `%` remainder
- simple arithmetic

---

## **8️⃣ Constraints**

- N ≥ 0
- Output format must match exactly
- No negative values

---

## **9️⃣ Common Mistakes**

❌ Using `/` (float division) instead of `//`
❌ Incorrect subtraction of remaining days
❌ Printing extra text or wrong spacing

---

## 🔟 Complexity

Time: **O(1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

years = N // 365
remaining = N % 365

weeks = remaining // 7
days = remaining % 7

print(years, "years", weeks, "weeks", days, "days")
```

---

## **1️⃣2️⃣ Example**

### Input

```
1329
```

### Output

```
3 years 33 weeks 3 days
```

---

## **1️⃣3️⃣ Dry Run**

For **N = 1329**:

- years = 1329 // 365 = 3
- remaining = 1329 % 365 = 234
- weeks = 234 // 7 = 33
- days = 234 % 7 = 3

Output → `3 years 33 weeks 3 days`

---

## **1️⃣4️⃣ Test Cases Table**

| N    | Years | Weeks | Days | Output                  |
| ---- | ----- | ----- | ---- | ----------------------- |
| 1329 | 3     | 33    | 3    | 3 years 33 weeks 3 days |
| 960  | 2     | 32    | 6    | 2 years 32 weeks 6 days |
| 0    | 0     | 0     | 0    | 0 years 0 weeks 0 days  |
| 400  | 1     | 5     | 5    | 1 years 5 weeks 5 days  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `//` gives whole units
- `%` gives remaining units
- Perfect use-case of multi-step arithmetic

---

## **1️⃣6️⃣ Real-Life Application**

- Converting days into calendar format
- Time management systems
- Travel duration breakdown

---

## **1️⃣7️⃣ Practice Questions**

1. Convert hours into days, hours, minutes.
2. Convert minutes into hours and minutes.
3. Convert seconds into hours, minutes, seconds.

---

## **1️⃣8️⃣ Result**

Program successfully converts total days into years, weeks, and days.

---

## **1️⃣9️⃣ Conclusion**

A clean conversion problem applying integer division and remainder to break down a total into structured units.

---
