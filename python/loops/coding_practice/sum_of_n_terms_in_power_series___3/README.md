# ✅ **Sum of N Terms in Power Series – 3 (Alternating)**

---

## **1️⃣ Question**

Given two numbers **X** and **N**, print the **sum of N terms** in the following power series with alternating signs:

```
X², -X⁴, X⁶, -X⁸, ...
```

---

## **1️⃣.5️⃣ Category**

For Loop → Power Series → Alternating Sum

---

## **2️⃣ Outline**

- Read X
- Read N
- Initialize sum as 0
- Start power from 2
- Use a sign variable
- Loop N times
- Add signed power value
- Change sign each time
- Print sum

---

## **3️⃣ Objective**

To calculate an **alternating power series** using a **single for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- alternating signs
- even power progression
- controlled summation

---

## **5️⃣ Theory**

The powers increase by **2**, and the **sign alternates**:

```
+X², -X⁴, +X⁶, -X⁸, ...
```

Example (X = 2, N = 4):

```
+2² = 4
-2⁴ = -16
+2⁶ = 64
-2⁸ = -256
```

Sum = **-204**

---

## **6️⃣ Step-by-Step Explanation**

1. Read X and N
2. Set `total = 0`
3. Set `power = 2`
4. Set `sign = 1`
5. Loop N times
6. Add `sign × (X ** power)` to total
7. Increase power by 2
8. Change sign
9. Print total

---

## **7️⃣ Method**

Use:

- for loop
- power operator (`**`)
- sign control using `1` and `-1`

---

## **8️⃣ Constraints**

- N ≥ 1
- X can be positive or negative

---

## **9️⃣ Common Mistakes**

❌ Forgetting to change sign
❌ Increasing power by 1
❌ Using nested loops

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code (NO nested loop)**

```python
X = int(input())
N = int(input())

total = 0
power = 2
sign = 1

for i in range(N):
    total = total + (sign * (X ** power))
    power = power + 2
    sign = sign * -1

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
2
6
```

### Output

```
-3276
```

---

## **1️⃣3️⃣ Dry Run**

X = 2, N = 3

- +2² = 4 → total = 4
- -2⁴ = -16 → total = -12
- +2⁶ = 64 → total = 52

---

## **1️⃣4️⃣ Test Cases Table**

| X   | N   | Output |
| --- | --- | ------ |
| 2   | 6   | -3276  |
| -7  | 3   | 115297 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Sign alternates using `1` and `-1`
- Power increases by 2
- One loop is enough

---

## **1️⃣6️⃣ Real-Life Application**

- Mathematical series
- Signal processing
- Pattern-based calculations

---

## **1️⃣7️⃣ Practice Questions**

1. Start with negative sign
2. Alternate after every two terms
3. Use odd powers instead

---

## **1️⃣8️⃣ Result**

The program correctly prints the **alternating power series sum**.

---

## **1️⃣9️⃣ Conclusion**

A clean problem that strengthens **loop control + sign handling**, without any nested logic.

---
