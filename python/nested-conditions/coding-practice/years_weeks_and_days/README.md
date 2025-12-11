# ✅ **Years, Weeks & Days**

---

## **1️⃣ Question**

Given **N** days, convert it into:

- **Years (Y)**
- **Weeks (W)**
- **Days (D)**

Where:

- 1 year = 365 days
- 1 week = 7 days

---

## **1.5️⃣ Category**

Arithmetic → Time Conversion → Integer Division & Modulo

---

## **2️⃣ Outline**

- Read N
- Compute years = N // 365
- Reduce remaining days
- Compute weeks = remaining // 7
- Compute final leftover days
- Print years, weeks, days

---

## **3️⃣ Objective**

To convert a total number of days into meaningful time components using integer division and remainders.

---

## **4️⃣ Purpose**

To practice decomposition of a total quantity using:

- division
- modulo
- multi-step conversion logic

---

## **5️⃣ Theory**

1. Years:

[
Y = \left\lfloor \frac{N}{365} \right\rfloor
]

2. Remaining after years:

[
R_1 = N % 365
]

3. Weeks:

[
W = \left\lfloor \frac{R_1}{7} \right\rfloor
]

4. Remaining days:

[
D = R_1 % 7
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Compute years using integer division
3. Compute days left after extracting years
4. Compute weeks from remaining days
5. Compute final leftover days
6. Print results in required order

---

## **7️⃣ Method**

- Use `//` for integer division
- Use `%` for remainder
- Print values line by line

---

## **8️⃣ Constraints**

- N ≥ 0
- Outputs must be printed exactly on separate lines
- No additional formatting

---

## **9️⃣ Common Mistakes**

❌ Forgetting integer division (using `/` instead of `//`)
❌ Not updating the remaining days properly
❌ Mixing order of output lines
❌ Incorrectly assuming 1 year = 360 days

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

Y = N // 365
remaining = N % 365

W = remaining // 7
D = remaining % 7

print(Y)
print(W)
print(D)
```

---

## **1️⃣2️⃣ Example**

### Input

```
1329
```

### Output

```
3
33
3
```

---

## **1️⃣3️⃣ Dry Run**

| Step      | Calculation | Result |
| --------- | ----------- | ------ |
| N         | 1329        |        |
| Years     | 1329 // 365 | 3      |
| Remaining | 1329 % 365  | 234    |
| Weeks     | 234 // 7    | 33     |
| Days      | 234 % 7     | 3      |
| Output    | 3, 33, 3    | ✔      |

---

## **1️⃣4️⃣ Test Cases Table**

| N    | Years | Weeks | Days |
| ---- | ----- | ----- | ---- |
| 1329 | 3     | 33    | 3    |
| 0    | 0     | 0     | 0    |
| 365  | 1     | 0     | 0    |
| 400  | 1     | 5     | 5    |
| 800  | 2     | 10    | 5    |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always extract larger units first (years → weeks → days)
- Integer division is essential for correct splitting
- Remaining after each step must be handled properly

---

## **1️⃣6️⃣ Real-Life Application**

- Calendar conversions
- Age calculations
- Converting total hours/days for work logs
- Time breakdown in simulations

---

## **1️⃣7️⃣ Practice Questions**

1. Convert hours → days → hours.
2. Convert minutes → hours → minutes.
3. Convert seconds → hours → minutes → seconds.

---

## **1️⃣8️⃣ Result**

The program correctly converts total days into years, weeks, and remaining days.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens your understanding of unit conversion using integer math—an important skill for real-world systems and time calculations.

---
