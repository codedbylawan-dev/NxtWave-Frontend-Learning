# ✅ **Special Eleven**

---

## **1️⃣ Question**

Given an integer **N**, check if the **remainder** when N is divided by **11** is **0 or 1**.
If yes, print **"Special Eleven"**, otherwise print **"Normal Number"**.

---

## **1.5️⃣ Category**

Beginner → Conditions → Modulus Operator

---

## **2️⃣ Outline**

- Read number N
- Compute `N % 11`
- If remainder is 0 or 1 → print "Special Eleven"
- Otherwise → print "Normal Number"

---

## **3️⃣ Objective**

To check if a number meets the special condition: remainder equals **0** or **1** when divided by **11**.

---

## **4️⃣ Purpose**

This problem teaches:

- Multiple condition checking
- Modulus operator behavior
- Using logical OR (`or`)

Everything is within your learned concepts.

---

## **5️⃣ Theory**

To check divisibility behavior:

[
\text{rem} = N % 11
]

A number is considered **Special Eleven** if:

[
\text{rem} = 0 \quad \text{or} \quad \text{rem} = 1
]

Examples:

- `22 % 11 = 0` → Special
- `23 % 11 = 1` → Special
- `15 % 11 = 4` → Not Special

---

## **6️⃣ Step-by-Step Explanation**

1. Read input N
2. Calculate remainder using `N % 11`
3. Check if remainder is **0** or **1**
4. If true → print `"Special Eleven"`
5. Otherwise → print `"Normal Number"`

---

## **7️⃣ Method**

- Use `%` to compute remainder
- Use if–else
- Use logical OR (`or`) to check two conditions

---

## **8️⃣ Constraints**

- Input is an integer
- Output text must match exactly
- No advanced methods allowed

---

## **9️⃣ Common Mistakes**

❌ Incorrect condition: using `== 0 or 1` instead of `(== 0) or (== 1)`
❌ Printing wrong text
❌ Forgetting integer conversion
❌ Misunderstanding OR logic

---

## 🔟 Complexity

- **Time:** O(1)
- **Space:** O(1)

---

## 1️⃣1️⃣ Code

```python
N = int(input())

remainder = N % 11

if remainder == 0 or remainder == 1:
    print("Special Eleven")
else:
    print("Normal Number")
```

---

## 1️⃣2️⃣ Example

### **Input**

```
22
```

### **Output**

```
Special Eleven
```

---

## 1️⃣3️⃣ Dry Run

| Step | N   | N % 11 | Condition (0 or 1) | Output         |
| ---- | --- | ------ | ------------------ | -------------- |
| 1    | 22  | 0      | True               | Special Eleven |
| 2    | 23  | 1      | True               | Special Eleven |
| 3    | 15  | 4      | False              | Normal Number  |

---

## 1️⃣4️⃣ Test Cases Table

| N   | N % 11 | Output         |
| --- | ------ | -------------- |
| 22  | 0      | Special Eleven |
| 23  | 1      | Special Eleven |
| 15  | 4      | Normal Number  |
| 44  | 0      | Special Eleven |
| 57  | 2      | Normal Number  |
| 101 | 2      | Normal Number  |
| 112 | 2      | Normal Number  |
| 121 | 0      | Special Eleven |

---

## 1️⃣5️⃣ Notes/Key Takeaways

- Logical OR allows checking multiple conditions
- `%` helps determine remainder-based patterns
- Special cases often rely on remainder values

---

## 1️⃣6️⃣ Real-Life Application

- Special pattern detection in sequences
- Remainder logic used in digital systems
- Coding challenges involving modular arithmetic

---

## 1️⃣7️⃣ Practice Questions

1. Print “Special Five” if `N % 5` is **0 or 2**, else print “Normal”.
2. Check if a number’s remainder when divided by 6 is **1 or 3**.
3. Print “Lucky Number” if `N % 9` equals 0, 1, or 8.

---

## 1️⃣8️⃣ Result

You applied modulus and OR condition to detect whether N satisfies the rule for a **Special Eleven** number.

---

## 1️⃣9️⃣ Conclusion

This problem strengthens your understanding of remainder-based logic and multi-condition checking — essential for more advanced numerical pattern problems.

---
