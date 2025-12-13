# ✅ **Simple Calculator**

---

## **1️⃣ Question**

You are given:

- An operator **O** (`+`, `-`, `*`, `/`, `%`)
- Two integers **A** and **B**

You must perform the correct arithmetic operation:

| Operator | Meaning                 | Expression |
| -------- | ----------------------- | ---------- |
| `+`      | Addition                | A + B      |
| `-`      | Subtraction (A − B)     | A - B      |
| `*`      | Multiplication          | A \* B     |
| `/`      | Division (float result) | A / B      |
| `%`      | Remainder               | A % B      |

---

## **1.5️⃣ Category**

Arithmetic Operations → Conditional Logic → Operator Handling

---

## **2️⃣ Outline**

- Read operator
- Read A
- Read B
- Use the correct condition to perform the matching arithmetic
- Print result

---

## **3️⃣ Objective**

To implement a simple calculator using conditional statements based on user input.

---

## **4️⃣ Purpose**

This problem teaches branching logic where different actions occur depending on the operator.

---

## **5️⃣ Theory**

Since the operator is a **string**, use equality checks:

```
if O == "+"
elif O == "-"
elif O == "*"
elif O == "/"
elif O == "%"
```

Division must produce **float**, others produce **int**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read operator O
2. Convert A and B to integers
3. Check O
4. If `+`, print A + B
5. If `-`, print A - B
6. If `*`, print A \* B
7. If `/`, print A / B (float)
8. If `%`, print A % B

---

## **7️⃣ Method**

Use **if–elif–else** for operator matching.

---

## **8️⃣ Constraints**

- O is guaranteed to be one of: `+`, `-`, `*`, `/`, `%`
- B will not be zero if operator is `/` or `%`
- Integer outputs for all except division

---

## **9️⃣ Common Mistakes**

❌ Forgetting to convert input strings to integers
❌ Accidentally printing integer for division
❌ Using wrong order of A and B in subtraction
❌ Mistyping operator strings

---

## 🔟 Complexity

⭐ **Time:** O(1)
⭐ **Space:** O(1)

---

## **1️⃣1️⃣ Code**

```python
O = input()
A = int(input())
B = int(input())

if O == "+":
    print(A + B)
elif O == "-":
    print(A - B)
elif O == "*":
    print(A * B)
elif O == "/":
    print(A / B)
else:
    print(A % B)
```

---

## **1️⃣2️⃣ Example**

### Input

```
+
3
5
```

### Output

```
8
```

---

## **1️⃣3️⃣ Dry Run**

| O   | A   | B   | Operation | Result |
| --- | --- | --- | --------- | ------ |
| +   | 3   | 5   | 3 + 5     | 8      |
| \*  | 2   | 5   | 2 \* 5    | 10     |
| -   | 10  | 9   | 10 - 9    | 1      |
| /   | 8   | 2   | 8 / 2     | 4.0    |
| %   | 9   | 4   | 9 % 4     | 1      |

---

## **1️⃣4️⃣ Test Cases Table**

| O   | A   | B   | Output |
| --- | --- | --- | ------ |
| +   | 3   | 5   | 8      |
| \*  | 2   | 5   | 10     |
| -   | 10  | 9   | 1      |
| /   | 7   | 2   | 3.5    |
| %   | 20  | 6   | 2      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Operator decides the action
- Division must always produce float
- All other operations produce integers

---

## **1️⃣6️⃣ Real-Life Application**

- Basic calculators
- Invoice generation
- Billing systems
- Mathematical expression evaluation

---

## **1️⃣7️⃣ Practice Questions**

1. Build a calculator supporting exponent (`A^B`)
2. Build a calculator supporting floor division (`A//B`)
3. Print operation name along with result

---

## **1️⃣8️⃣ Result**

The program successfully acts as a mini-calculator based on operator input.

---

## **1️⃣9️⃣ Conclusion**

A great exercise to combine arithmetic operations with conditional logic—solidifying how programs make decisions based on user input.

---
