# ✅ **Quotient & Remainder — Using Locked Format**

---

## **1️⃣ Question**

Write a program that reads two integers **A** and **B**, and prints:

1. The **Quotient** when A is divided by B
2. The **Remainder** when A is divided by B

Each on a new line.

---

## **1.5️⃣ Category**

Beginner → Arithmetic → Division & Modulus

---

## **2️⃣ Outline**

- Read inputs A and B
- Compute quotient using integer division `A // B`
- Compute remainder using modulus `A % B`
- Print quotient
- Print remainder

---

## **3️⃣ Objective**

To calculate and display both the **integer quotient** and **remainder** of a division operation.

---

## **4️⃣ Purpose**

This problem teaches:

- Integer division (`//`)
- Remainder calculation (`%`)
- Multi-line output formatting
- How division results are split into quotient + remainder

---

## **5️⃣ Theory**

When you divide A by B:

[
A = (B \times \text{Quotient}) + \text{Remainder}
]

Python tools:

- **`A // B`** → integer quotient
- **`A % B`** → remainder

Example:
`5 // 2 = 2`
`5 % 2 = 1`

---

## **6️⃣ Step-by-Step Explanation**

1. Read integer **A**
2. Read integer **B**
3. Compute quotient using `A // B`
4. Compute remainder using `A % B`
5. Print quotient on first line
6. Print remainder on second line

---

## **7️⃣ Method**

- Use `int(input())` to read A and B
- Calculate quotient with integer division
- Calculate remainder with modulus
- Output results exactly as required

---

## **8️⃣ Constraints**

- **B ≠ 0** (cannot divide by zero)
- Output must be exactly 2 lines
- Inputs are integers

---

## **9️⃣ Common Mistakes**

❌ Using `/` instead of `//` for quotient
❌ Printing text instead of just numbers
❌ Reversing quotient and remainder
❌ Division by zero not considered

---

## 🔟 Complexity

- **Time:** O(1)
- **Space:** O(1)

---

## 1️⃣1️⃣ Code

```python
A = int(input())
B = int(input())

quotient = A // B
remainder = A % B

print(quotient)
print(remainder)
```

---

## 1️⃣2️⃣ Example

### **Input**

```
5
2
```

### **Output**

```
2
1
```

---

## 1️⃣3️⃣ Dry Run

| Step | A   | B   | Operation     | Result |
| ---- | --- | --- | ------------- | ------ |
| 1    | 5   | 2   | 5 // 2        | 2      |
| 2    | 5   | 2   | 5 % 2         | 1      |
| 3    |     |     | Print results | 2, 1   |

---

## 1️⃣4️⃣ Test Cases Table

| A   | B   | Quotient (A//B) | Remainder (A%B) |
| --- | --- | --------------- | --------------- |
| 5   | 2   | 2               | 1               |
| 30  | 10  | 3               | 0               |
| 9   | 4   | 2               | 1               |
| 100 | 7   | 14              | 2               |
| 11  | 3   | 3               | 2               |

---

## 1️⃣5️⃣ Notes/Key Takeaways

- `//` gives the **integer** part of division
- `%` gives the **remainder**
- Quotient & remainder always satisfy:
  **A = B × Quotient + Remainder**

---

## 1️⃣6️⃣ Real-Life Application

- Splitting items equally and knowing leftovers
- Packaging problems (boxes + remaining items)
- Time conversion (minutes → hours + leftover minutes)
- Banking & distribution systems

---

## 1️⃣7️⃣ Practice Questions

1. Print quotient and remainder when **A = 20**, **B = 6**
2. Input two numbers and check if remainder is even
3. Compute `(A // B) + (A % B)`
4. Print quotient only if remainder is 0

---

## 1️⃣8️⃣ Result

The program successfully prints both the quotient and the remainder using integer division and modulus.

---

## 1️⃣9️⃣ Conclusion

This exercise strengthens understanding of division mechanics and Python’s operators. Mastering these helps with problem-solving in mathematics, logic, and real-world distribution scenarios.

---
