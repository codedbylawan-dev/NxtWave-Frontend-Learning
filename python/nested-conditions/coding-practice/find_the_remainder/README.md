# ✅ **Find the Remainder — Using Locked Format**

---

## **1️⃣ Question**

Given two integers **A** and **B**, print the **remainder** when A is divided by B.

---

## **1.5️⃣ Category**

Beginner → Arithmetic → Modulus Operator (%)

---

## **2️⃣ Outline**

- Read inputs A and B.
- Compute `A % B`.
- Print the result.

---

## **3️⃣ Objective**

To calculate the remainder of division using Python’s `%` operator.

---

## **4️⃣ Purpose**

This builds the foundation for solving problems involving divisibility, loops, digit extraction, encryption, and mathematical logic.

---

## **5️⃣ Theory**

- The modulus operator `%` gives the **remainder** after division.
- Formula:
  [
  \text{Remainder} = A % B
  ]
- Example: `10 % 3 = 1`

Python directly performs this using `%`.

---

## **6️⃣ Step-by-Step Explanation**

1. Take input A.
2. Take input B.
3. Use the modulus operator: `A % B`.
4. Store the result in a variable.
5. Print the result.

---

## **7️⃣ Method**

- Use `int(input())` to read integers.
- Apply `%` operator.
- Output the remainder.

---

## **8️⃣ Constraints**

- B must **not** be zero.
- Inputs are integers only.
- Output should be a single integer.

---

## **9️⃣ Common Mistakes**

❌ Using `/` instead of `%`.
❌ Forgetting to convert input to `int`.
❌ Printing extra text instead of only the remainder.
❌ Divider (B) being zero.

---

## 🔟 Complexity

- **Time:** O(1)
- **Space:** O(1)

---

## 1️⃣1️⃣ Code

```python
A = int(input())
B = int(input())

remainder = A % B
print(remainder)
```

---

## 1️⃣2️⃣ Example

### **Input**

```
10
3
```

### **Output**

```
1
```

---

## 1️⃣3️⃣ Dry Run

| Step | A            | B   | Expression | Result |
| ---- | ------------ | --- | ---------- | ------ |
| 1    | 10           | 3   | 10 % 3     | 1      |
| 2    | Print result |     |            | 1      |

---

## 1️⃣4️⃣ Test Cases Table

| A   | B   | A % B | Output |
| --- | --- | ----- | ------ |
| 10  | 3   | 1     | 1      |
| 24  | 5   | 4     | 4      |
| 7   | 2   | 1     | 1      |
| 9   | 4   | 1     | 1      |
| 100 | 10  | 0     | 0      |

---

## 1️⃣5️⃣ Notes/Key Takeaways

- `%` returns the remainder after division.
- Very important for even/odd checks, digit extraction, and looping patterns.
- Always ensure divisor ≠ 0.

---

## 1️⃣6️⃣ Real-Life Application

- Checking if a number is even (`num % 2 == 0`).
- Calculating leftover items in distribution.
- Time calculations (e.g., remaining minutes).
- Hashing algorithms.

---

## 1️⃣7️⃣ Practice Questions

1. Find remainder when **125** is divided by **8**.
2. Compute `(A * A) % B` for user inputs.
3. Check if a number ends with digit **7** using `% 10`.
4. Print the last digit of any number.

---

## 1️⃣8️⃣ Result

The program correctly computes and prints the remainder using the modulus operator.

---

## 1️⃣9️⃣ Conclusion

This is a foundational problem that helps you understand how Python handles division remainders. Mastering `%` prepares you for future logical, mathematical, and algorithmic problems.

---
