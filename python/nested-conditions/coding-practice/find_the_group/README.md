# ✅ **Find the Group**

---

## **1️⃣ Question**

Given a number **N** (1 to 10), find whether it belongs to **Group A** or **Group B**.

- Numbers with **remainder 1 when divided by 2** → **Group A**
- Numbers with **remainder 0 when divided by 2** → **Group B**

---

## **1.5️⃣ Category**

Arithmetic → Modulus Check → Odd/Even Based Grouping

---

## **2️⃣ Outline**

- Read N
- Compute `N % 2`
- If remainder is **1**, print Group A
- If remainder is **0**, print Group B

---

## **3️⃣ Objective**

To determine a group by checking the remainder when dividing by 2.

---

## **4️⃣ Purpose**

You learn how modulus helps categorize values into logical groups.

---

## **5️⃣ Theory**

- `N % 2 == 1` → N is odd → Group A
- `N % 2 == 0` → N is even → Group B

This matches the pattern 1–10 grouping.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Divide N by 2 and check remainder
3. If remainder is 1 → print Group A
4. Else → print Group B

---

## **7️⃣ Method**

Use:

- `%` operator
- Simple `if / else`

---

## **8️⃣ Constraints**

- N is between 1 and 10
- Output must match exactly “Group A” or “Group B”

---

## **9️⃣ Common Mistakes**

❌ Using > or < instead of `%`
❌ Reversing the groups
❌ Printing lowercase or extra spaces

---

## 🔟 Complexity

- **Time:** O(1)
- **Space:** O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

if N % 2 == 1:
    print("Group A")
else:
    print("Group B")
```

---

## **1️⃣2️⃣ Example**

### Input

```
6
```

### Output

```
Group B
```

---

## **1️⃣3️⃣ Dry Run**

| N   | N % 2 | Group   |
| --- | ----- | ------- |
| 3   | 1     | Group A |
| 6   | 0     | Group B |
| 9   | 1     | Group A |
| 10  | 0     | Group B |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output  |
| ----- | ------- |
| 1     | Group A |
| 2     | Group B |
| 5     | Group A |
| 8     | Group B |
| 9     | Group A |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `%` helps divide values into categories, not just find remainders
- Odd → Group A
- Even → Group B

---

## **1️⃣6️⃣ Real-Life Application**

Grouping based on remainder is used in:

- Team formation
- Allocation of roll numbers
- Alternating scheduling (odd/even days)

---

## **1️⃣7️⃣ Practice Questions**

1. Print "Odd" or "Even" using `%`.
2. Divide numbers 1–20 into 3 groups using `% 3`.
3. Check if a number ends with digit 5 using `% 10`.

---

## **1️⃣8️⃣ Result**

The program correctly identifies the group of N using remainder logic.

---

## **1️⃣9️⃣ Conclusion**

A simple but powerful example of how `%` helps classify data into groups.

---
