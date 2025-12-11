# ✅ **Number or Remainder**

---

## **1️⃣ Question**

Read an integer **N** and check if **any** of these conditions is true:

1. **N is divisible by 5 AND N is divisible by 7**
2. **N is less than 7**

- If **any** condition is satisfied → print **N**
- Otherwise → print

  - remainder when N is divided by 5
  - remainder when N is divided by 7
    (each on a new line)

---

## **1.5️⃣ Category**

Arithmetic → Divisibility → Multi-condition OR

---

## **2️⃣ Outline**

- Read N
- Check if N divisible by both 5 and 7
- Check if N < 7
- If either is true → print N
- Else → print N % 5 and N % 7 on separate lines

---

## **3️⃣ Objective**

To choose between printing the number or printing two remainders based on given conditions.

---

## **4️⃣ Purpose**

To understand combining AND and OR logic together with modulus operations.

---

## **5️⃣ Theory**

Divisibility rules:

[
N % 5 = 0 \quad \text{and} \quad N % 7 = 0
]

Second condition:

[
N < 7
]

Decision:

[
\text{If (cond1 or cond2) → print N}
]
[
\text{Else → print N%5 then N%7}
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Compute `cond1 = (N%5 == 0) and (N%7 == 0)`
3. Compute `cond2 = (N < 7)`
4. If cond1 or cond2 is true → print N
5. Else → print remainders
6. End

---

## **7️⃣ Method**

- Use `%` to find remainders
- Use AND inside OR for nested condition logic
- Use if–else for final output

---

## **8️⃣ Constraints**

- N is an integer
- Exactly one or two lines must be printed
- Follow exact spacing and formatting

---

## **9️⃣ Common Mistakes**

❌ Using OR between divisibility conditions instead of AND
❌ Forgetting the second condition (N < 7)
❌ Printing both N and remainders
❌ Wrong newline formatting

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

cond1 = (N % 5 == 0) and (N % 7 == 0)
cond2 = (N < 7)

if cond1 or cond2:
    print(N)
else:
    print(N % 5)
    print(N % 7)
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
```

### Output

```
3
```

---

## **1️⃣3️⃣ Dry Run**

| N   | N%5 | N%7 | cond1 (5&7) | cond2 (<7) | Output           |
| --- | --- | --- | ----------- | ---------- | ---------------- |
| 3   | 3   | 3   | False       | True       | 3                |
| 9   | 4   | 2   | False       | False      | 4, 2 (new lines) |

---

## **1️⃣4️⃣ Test Cases Table**

| N   | Divisible by 5 & 7? | N < 7? | Output         |
| --- | ------------------- | ------ | -------------- |
| 3   | No                  | Yes    | 3              |
| 9   | No                  | No     | 4↵2            |
| 35  | Yes                 | No     | 35             |
| 2   | No                  | Yes    | 2              |
| 49  | No                  | No     | 49%5=4, 49%7=0 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- AND is used _inside_ one condition
- OR is used to combine the two major conditions
- Be careful with exact formatting for multiple outputs

---

## **1️⃣6️⃣ Real-Life Application**

- Input validation based on multi-rule checks
- Decision-making systems with fallback values
- Rule-based score or state calculations

---

## **1️⃣7️⃣ Practice Questions**

1. Print N if N divisible by 4 OR 6, else print N%4.
2. If N < 10 or N%3 == 0, print N; else print N%3.
3. Print digits of N if N > 99, else print N².

---

## **1️⃣8️⃣ Result**

The program correctly outputs either N or the required remainders based on the conditions.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens understanding of condition ordering and mixing AND/OR logic — essential tools in programming decision structures.

---

Say **Next** for the next problem.
