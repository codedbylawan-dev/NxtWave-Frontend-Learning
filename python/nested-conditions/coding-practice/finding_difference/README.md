# ✅ **Finding Difference**

---

## **1️⃣ Question**

Given two integers **N1** and **N2**, print their **absolute difference** (difference without negative sign).

---

## **1.5️⃣ Category**

Arithmetic → Difference → Absolute Value (Manual)

---

## **2️⃣ Outline**

- Read N1
- Read N2
- Compute difference
- Convert negative difference to positive
- Print result

---

## **3️⃣ Objective**

To calculate the absolute difference between two integers using basic arithmetic.

---

## **4️⃣ Purpose**

Strengthens understanding of subtraction and conditional handling of negative values.

---

## **5️⃣ Theory**

Difference = **N1 – N2**

Absolute difference =

- If difference ≥ 0 → use it
- If difference < 0 → multiply by -1

Example:
N1 = 200, N2 = 500
Difference = -300
Absolute difference = 300

---

## **6️⃣ Step-by-Step Explanation**

1. Read N1
2. Read N2
3. Compute `diff = N1 - N2`
4. If diff is negative → convert to positive
5. Print the result

---

## **7️⃣ Method**

Use:

- subtraction
- if–else
- manual absolute value logic

---

## **8️⃣ Constraints**

- N1 and N2 are integers
- Result must always be non-negative

---

## **9️⃣ Common Mistakes**

❌ Printing negative numbers
❌ Forgetting to multiply negative difference by -1
❌ Using `/` instead of `-`

---

## 🔟 Complexity

Time: **O(1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N1 = int(input())
N2 = int(input())

diff = N1 - N2

if diff < 0:
    diff = -diff

print(diff)
```

---

## **1️⃣2️⃣ Example**

### Input

```
200
500
```

### Output

```
300
```

---

## **1️⃣3️⃣ Dry Run**

For **N1 = -12**, **N2 = -1**:

- diff = -12 - (-1) = -11
- diff < 0 → convert to positive → 11
- Print **11**

---

## **1️⃣4️⃣ Test Cases Table**

| N1  | N2  | diff | Absolute | Output |
| --- | --- | ---- | -------- | ------ |
| 200 | 500 | -300 | 300      | 300    |
| -12 | -1  | -11  | 11       | 11     |
| 10  | 3   | 7    | 7        | 7      |
| 5   | 5   | 0    | 0        | 0      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Absolute difference is always non-negative
- You can implement absolute value using simple if-else logic

---

## **1️⃣6️⃣ Real-Life Application**

- Distance between two values
- Price difference calculation
- Score comparison

---

## **1️⃣7️⃣ Practice Questions**

1. Print the absolute difference between the last digits of two numbers.
2. Print |A² – B²|.
3. Given three numbers, print the absolute difference between largest and smallest.

---

## **1️⃣8️⃣ Result**

Correctly prints the absolute difference between the two input numbers.

---

## **1️⃣9️⃣ Conclusion**

A simple but fundamental arithmetic problem that strengthens conditional logic and number handling.

---
