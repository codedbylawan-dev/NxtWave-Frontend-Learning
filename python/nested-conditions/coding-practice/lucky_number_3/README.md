# ✅ **Lucky Number - 3**

---

## **1️⃣ Question**

Given a positive integer **N**, check whether it is divisible by **6**, **3**, or **2**, where priority (luckiest first) is:

1. 6
2. 3
3. 2

Print the result based on the highest-priority number that divides N.
If none divide N → print **"Number is not divisible by 2, 3 or 6"**.

---

## **1.5️⃣ Category**

Arithmetic → Divisibility → Conditional Logic (Priority Order)

---

## **2️⃣ Outline**

- Read N
- Check divisibility by 6
- Else check divisibility by 3
- Else check divisibility by 2
- If none → print not divisible message

---

## **3️⃣ Objective**

To determine which among 6, 3, or 2 divides N, following a priority order.

---

## **4️⃣ Purpose**

To apply ordered condition checking where the first true condition decides the answer.

---

## **5️⃣ Theory**

Divisibility:

[
N % 6 = 0 \quad \text{(highest priority)}
]
[
N % 3 = 0 \quad \text{(medium priority)}
]
[
N % 2 = 0 \quad \text{(lowest priority)}
]

Use **priority-based conditional evaluation**:

- First check 6
- If false, check 3
- If false, check 2
- If all false → remainder is non-zero for all

---

## **6️⃣ Step-by-Step Explanation**

1. Read integer N
2. Compute N % 6
3. If divisible → print message for 6
4. Otherwise compute N % 3
5. If divisible → print message for 3
6. Otherwise compute N % 2
7. If divisible → print message for 2
8. Else → print not divisible message

---

## **7️⃣ Method**

- Use remainder operator `%`
- Evaluate conditions in priority order
- Use chained if–elif–else

---

## **8️⃣ Constraints**

- N > 0
- Output text must match exactly
- Priority order must be followed strictly

---

## **9️⃣ Common Mistakes**

❌ Checking divisibility by 2 or 3 before 6
❌ Forgetting exact output format
❌ Misusing OR when priority is required
❌ Wrong ordering of conditions

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

if N % 6 == 0:
    print("Number is divisible by 6")
elif N % 3 == 0:
    print("Number is divisible by 3")
elif N % 2 == 0:
    print("Number is divisible by 2")
else:
    print("Number is not divisible by 2, 3 or 6")
```

---

## **1️⃣2️⃣ Example**

### Input

```
126
```

### Output

```
Number is divisible by 6
```

---

## **1️⃣3️⃣ Dry Run**

| Step | N   | N%6 | N%3 | N%2 | Condition Hit            | Output                               |
| ---- | --- | --- | --- | --- | ------------------------ | ------------------------------------ |
| 1    | 126 | 0   | 0   | 0   | Divisible by 6 (highest) | Number is divisible by 6             |
| 2    | 27  | 3   | 0   | 1   | Divisible by 3           | Number is divisible by 3             |
| 3    | 55  | 1   | 1   | 1   | None                     | Number is not divisible by 2, 3 or 6 |

---

## **1️⃣4️⃣ Test Cases Table**

| N   | N%6 | N%3 | N%2 | Output                               |
| --- | --- | --- | --- | ------------------------------------ |
| 126 | 0   | 0   | 0   | Number is divisible by 6             |
| 27  | 3   | 0   | 1   | Number is divisible by 3             |
| 14  | 2   | 2   | 0   | Number is divisible by 2             |
| 55  | 1   | 1   | 1   | Number is not divisible by 2, 3 or 6 |
| 18  | 0   | 0   | 0   | Number is divisible by 6             |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Priority-based condition checking is important in many problems
- 6 is luckiest → always check first
- A number divisible by 6 is automatically divisible by 2 and 3

---

## **1️⃣6️⃣ Real-Life Application**

- Handling priority rules in automation
- Determining best match in pattern checking
- Systems that choose highest priority valid condition

---

## **1️⃣7️⃣ Practice Questions**

1. Print according to priority: divisible by 10 → 5 → 2.
2. Check whether a number is divisible by 9, else 6, else 3.
3. Determine smallest divisor among 4, 6, 8 based on priority.

---

## **1️⃣8️⃣ Result**

Correct identification of the highest-priority divisor among 6, 3, and 2.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens condition ordering, divisibility checks, and logical flow control—essential skills for developing accurate and structured solutions.

---
