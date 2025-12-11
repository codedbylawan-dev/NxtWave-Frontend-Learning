# ✅ **Calculate Double or Triple**

---

## **1️⃣ Question**

Read a number **N** and decide:

- If **N is divisible by 3**, print **3 × N**
- Otherwise, print **2 × N**

---

## **1.5️⃣ Category**

Arithmetic → Divisibility → Conditional Output

---

## **2️⃣ Outline**

- Read N
- Check divisibility by 3
- If divisible → compute and print triple
- Else → compute and print double

---

## **3️⃣ Objective**

To practice using conditions to choose between two arithmetic operations.

---

## **4️⃣ Purpose**

This problem reinforces basic divisibility checking and applying different formulas based on conditions.

---

## **5️⃣ Theory**

Divisibility check:

[
N % 3 = 0
]

If true →
[
\text{result} = 3 \times N
]

Else →
[
\text{result} = 2 \times N
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read the integer N
2. Use modulus to check if N % 3 == 0
3. If divisible → calculate 3N
4. If not divisible → calculate 2N
5. Print the result

---

## **7️⃣ Method**

- Use `%` to test divisibility
- Use `if–else`
- Perform multiplication

---

## **8️⃣ Constraints**

- N is an integer
- Output must be a single integer
- Must not print extra words

---

## **9️⃣ Common Mistakes**

❌ Forgetting to multiply correctly
❌ Forgetting parentheses
❌ Checking divisibility of 2 instead of 3
❌ Printing extra spaces or text

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣11️⃣ Code**

```python
N = int(input())

if N % 3 == 0:
    print(3 * N)
else:
    print(2 * N)
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
```

### Output

```
9
```

---

## **1️⃣3️⃣ Dry Run**

| N   | N % 3 | Condition          | Output |
| --- | ----- | ------------------ | ------ |
| 3   | 0     | divisible by 3     | 9      |
| 4   | 1     | not divisible by 3 | 8      |

---

## **1️⃣4️⃣ Test Cases Table**

| N   | Divisible by 3? | Output |
| --- | --------------- | ------ |
| 3   | Yes             | 9      |
| 4   | No              | 8      |
| 6   | Yes             | 18     |
| 10  | No              | 20     |
| 12  | Yes             | 36     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `% 3` checks whether a number is divisible by 3
- Use if–else when only one of two outcomes is needed
- Multiplication patterns reinforce simple algebra in programming

---

## **1️⃣6️⃣ Real-Life Application**

- Discount rules (apply bigger multiplier under certain conditions)
- Scaling factors in animations or physics
- Financial adjustments based on thresholds

---

## **1️⃣7️⃣ Practice Questions**

1. Print double if N is divisible by 4, else print triple.
2. Print N×N if N is even, else print N×3.
3. Print half of N if divisible by 5, else print N+5.

---

## **1️⃣8️⃣ Result**

The program correctly outputs triple when divisible by 3 and double otherwise.

---

## **1️⃣9️⃣ Conclusion**

This task reinforces condition-based arithmetic decisions — one of the core building blocks for solving real programming problems.

---
