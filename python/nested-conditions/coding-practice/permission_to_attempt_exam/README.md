# ✅ **Permission to Attempt Exam**

---

## **1️⃣ Question**

You are given:

- **A** → attendance percentage in string format (example: `"80%"`)
- **M** → medical report status (`"Y"` or `"N"`)

You must check:

- If **attendance ≥ 75**, OR
- If **medical report = "Y"**

Print:

- **Allowed to write exam** → if any condition is true
- **Cannot write exam** → otherwise

---

## **1.5️⃣ Category**

String Handling → Type Conversion → Logical OR Conditions

---

## **2️⃣ Outline**

- Read inputs A and M
- Extract the numeric value from A (remove `%`)
- Convert to integer
- Check attendance ≥ 75 OR medical report is "Y"
- Print appropriate result

---

## **3️⃣ Objective**

To apply logical **OR** conditions and string-to-number conversion in a real scenario.

---

## **4️⃣ Purpose**

Helps understand condition combinations where satisfying _any_ rule is enough.

---

## **5️⃣ Theory**

1. Attendance is given as `"80%"` → need to remove `%`:
   `"80%" → "80" → 80`
2. Logical condition:

[
(A \ge 75) \quad \text{or} \quad (M == "Y")
]

If any one of them is **True**, student is allowed.

---

## **6️⃣ Step-by-Step Explanation**

1. Read attendance string A
2. Remove the `%` symbol
3. Convert to integer
4. Read medical report M
5. If attendance ≥ 75 → allowed
6. Else if M == "Y" → allowed
7. Else → cannot write exam

---

## **7️⃣ Method**

- Use string slicing to remove `%`
- Convert to integer
- Use `if`, `elif`, `else`
- Use `or` for checking multiple conditions

---

## **8️⃣ Constraints**

- A always includes `%`
- M is always `"Y"` or `"N"`
- Output must match exactly

---

## **9️⃣ Common Mistakes**

❌ Forgetting to remove `%` before converting to int
❌ Comparing string `"80%"` directly with `75`
❌ Confusing OR and AND
❌ Case mismatch like `"y"` instead of `"Y"`

---

## 🔟 Complexity

- Time: **O(1)**
- Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
A = input()
M = input()

attendance = int(A[:-1])  # remove '%' and convert

if attendance >= 75 or M == "Y":
    print("Allowed to write exam")
else:
    print("Cannot write exam")
```

---

## **1️⃣2️⃣ Example**

### Input

```
80%
Y
```

### Output

```
Allowed to write exam
```

---

## **1️⃣3️⃣ Dry Run**

| A   | M   | attendance | Condition True?        | Result                |
| --- | --- | ---------- | ---------------------- | --------------------- |
| 80% | Y   | 80         | 80 ≥ 75                | Allowed to write exam |
| 70% | Y   | 70         | M == "Y"               | Allowed to write exam |
| 72% | N   | 72         | Neither condition true | Cannot write exam     |

---

## **1️⃣4️⃣ Test Cases Table**

| A   | M   | Output                |
| --- | --- | --------------------- |
| 80% | Y   | Allowed to write exam |
| 90% | N   | Allowed to write exam |
| 70% | Y   | Allowed to write exam |
| 60% | N   | Cannot write exam     |
| 75% | N   | Allowed to write exam |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Remove `%` before converting to number
- OR means only one condition needs to be true
- Very common pattern in eligibility checking

---

## **1️⃣6️⃣ Real-Life Application**

- Exam eligibility systems
- Attendance-based access control
- Gym membership check-in rules
- Medical exemption validations

---

## **1️⃣7️⃣ Practice Questions**

1. Check if a student passes based on marks ≥ 40 or grace marks = "Y".
2. Check if entry is permitted if age ≥ 18 or with parent permission.
3. Check employee promotion eligibility based on experience or certification.

---

## **1️⃣8️⃣ Result**

The program correctly determines exam eligibility using attendance and medical status.

---

## **1️⃣9️⃣ Conclusion**

A practical example of combining string processing with logical conditions to make real-world decisions.

---
