# ✅ **Allowed to Exam**

---

## **1️⃣ Question**

Read two strings **H** (Hall ticket) and **I** (Identification card) and check:

1. If **H == "Y"**, print
   **"Allowed to Exam - Has Hall ticket"**

2. Else if **I == "Y"**, print
   **"Allowed to Exam - Has Identification Card"**

---

## **1.5️⃣ Category**

Conditional Statements → String Comparison → Eligibility Check

---

## **2️⃣ Outline**

- Read H
- Read I
- If H is "Y" → print hall-ticket message
- Else if I is "Y" → print ID-card message

---

## **3️⃣ Objective**

To determine exam eligibility based on possession of either a hall ticket or an identification card.

---

## **4️⃣ Purpose**

This problem strengthens:

- string comparison using `==`
- ordered conditional logic

---

## **5️⃣ Theory**

Conditions:

[
H == "Y"
]

Else:

[
I == "Y"
]

Each condition leads to a different message.

---

## **6️⃣ Step-by-Step Explanation**

1. Read H
2. Read I
3. If H equals "Y" → print hall-ticket message
4. Else if I equals "Y" → print ID-card message
5. End

---

## **7️⃣ Method**

- Use string input
- Compare using `==`
- Use if + elif

---

## **8️⃣ Constraints**

- Input must be exactly "Y" or "N"
- Output should match exactly (case-sensitive)
- Only one line must be printed

---

## **9️⃣ Common Mistakes**

❌ Using lowercase "y" instead of uppercase "Y"
❌ Printing both messages
❌ Checking ID card before hall ticket
❌ Adding extra spaces or punctuation

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
H = input()
I = input()

if H == "Y":
    print("Allowed to Exam - Has Hall ticket")
elif I == "Y":
    print("Allowed to Exam - Has Identification Card")
```

---

## **1️⃣2️⃣ Example**

### Input

```
Y
N
```

### Output

```
Allowed to Exam - Has Hall ticket
```

---

## **1️⃣3️⃣ Dry Run**

| H   | I   | H == "Y"? | I == "Y"? | Output                                    |
| --- | --- | --------- | --------- | ----------------------------------------- |
| Y   | N   | Yes       | —         | Allowed to Exam - Has Hall ticket         |
| N   | Y   | No        | Yes       | Allowed to Exam - Has Identification Card |
| N   | N   | No        | No        | _(no output in this problem)_             |

---

## **1️⃣4️⃣ Test Cases Table**

| H   | I   | Output                                    |
| --- | --- | ----------------------------------------- |
| Y   | N   | Allowed to Exam - Has Hall ticket         |
| Y   | Y   | Allowed to Exam - Has Hall ticket         |
| N   | Y   | Allowed to Exam - Has Identification Card |
| N   | N   | _(no output required)_                    |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Hall ticket has first priority
- Only one output line is printed
- String comparisons are exact and case-sensitive

---

## **1️⃣6️⃣ Real-Life Application**

- Access permission logic
- Login fallback options
- Multi-level verification systems

---

## **1️⃣7️⃣ Practice Questions**

1. Check login with password OR OTP.
2. Print Allowed if student has ID OR fee receipt.
3. Check if user has email verification OR phone verification.

---

## **1️⃣8️⃣ Result**

The code correctly determines exam eligibility based on the provided documents.

---

## **1️⃣9️⃣ Conclusion**

A clean, practical example of sequential condition checking using strings — essential for validation logic in real applications.

---
