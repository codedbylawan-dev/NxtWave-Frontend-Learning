# ✅ **Divisible by Seven — Using Locked Format**

---

## **1️⃣ Question**

Given an integer **N**, check whether it is **divisible by 7**.
If yes, print **"Divisible by Seven"**, otherwise print **"Not Divisible by Seven"**.

---

## **1.5️⃣ Category**

Beginner → Conditions → Modulus Operator

---

## **2️⃣ Outline**

- Read input N.
- Compute `N % 7`.
- If remainder is 0 → print “Divisible by Seven”.
- Else → print “Not Divisible by Seven”.

---

## **3️⃣ Objective**

To determine if a number is divisible by 7 using the modulus operator and conditional statements.

---

## **4️⃣ Purpose**

This problem strengthens understanding of conditional logic, divisibility checks, and the `%` operator — all essential for beginner Python programming.

---

## **5️⃣ Theory**

- A number **N** is divisible by 7 if:

[
N % 7 = 0
]

- The modulus operator `%` returns the remainder when dividing N by 7.
- If the remainder is **0**, the number is perfectly divisible.

Example:
`35 % 7 = 0` → divisible
`8 % 7 = 1` → not divisible

---

## **6️⃣ Step-by-Step Explanation**

1. Read integer N from user.
2. Compute remainder using `N % 7`.
3. If the remainder equals 0:

   - Print `"Divisible by Seven"`.

4. Otherwise:

   - Print `"Not Divisible by Seven"`.

---

## **7️⃣ Method**

- Use `int(input())` for reading N.
- Use `%` to check divisibility.
- Apply if–else condition to print the correct message.

---

## **8️⃣ Constraints**

- N is an integer (positive or negative allowed).
- Output must match **exact text** — case-sensitive.
- Only one print statement must appear based on condition.

---

## **9️⃣ Common Mistakes**

❌ Forgetting to use `%` correctly.
❌ Checking for `N / 7 == 0` instead of `N % 7 == 0`.
❌ Misspelling output text (must match exactly).
❌ Adding extra spaces or lines in output.

---

## 🔟 Complexity

- **Time:** O(1)
- **Space:** O(1)

---

## 1️⃣1️⃣ Code

```python
N = int(input())

if N % 7 == 0:
    print("Divisible by Seven")
else:
    print("Not Divisible by Seven")
```

---

## 1️⃣2️⃣ Example

### **Input**

```
35
```

### **Output**

```
Divisible by Seven
```

---

## 1️⃣3️⃣ Dry Run

| Step | N   | Expression | Result | Output                 |
| ---- | --- | ---------- | ------ | ---------------------- |
| 1    | 35  | 35 % 7     | 0      | Divisible by Seven     |
| 2    | 8   | 8 % 7      | 1      | Not Divisible by Seven |

---

## 1️⃣4️⃣ Test Cases Table

| N   | N % 7 | Output                 |
| --- | ----- | ---------------------- |
| 35  | 0     | Divisible by Seven     |
| 8   | 1     | Not Divisible by Seven |
| 0   | 0     | Divisible by Seven     |
| 14  | 0     | Divisible by Seven     |
| 21  | 0     | Divisible by Seven     |
| 22  | 1     | Not Divisible by Seven |

---

## 1️⃣5️⃣ Notes/Key Takeaways

- `%` is the easiest way to check divisibility.
- Only a remainder of **0** means divisible.
- Negative numbers also work: `-14 % 7 = 0`.

---

## 1️⃣6️⃣ Real-Life Application

- Scheduling tasks every 7 days.
- Weekly recurring events.
- Checking day-based intervals like reminders or billing cycles.

---

## 1️⃣7️⃣ Practice Questions

1. Check if a number is divisible by **5**.
2. Print “Even” or “Odd” using `% 2`.
3. Check if a number is divisible by **3 and 7**.
4. Print “Multiple of 10” if divisible by 10.

---

## 1️⃣8️⃣ Result

You successfully determined whether a number is divisible by 7 using modulus and conditional statements.

---

## 1️⃣9️⃣ Conclusion

This problem reinforces the core Python concepts of modulus and conditional branching. Mastering such basics prepares you for more complex logical and mathematical operations in programming.

---
