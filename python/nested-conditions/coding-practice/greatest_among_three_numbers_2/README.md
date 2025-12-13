# Greatest Among Three Numbers - 2

Problem description: _Add the problem statement here._

## How to run

```
python index.py
```

## Notes

- Fill input/output format and examples.

# ✅ **Greatest Among Three Numbers – 2**

---

## **1️⃣ Question**

Read three integers **A**, **B**, and **C**, and print the **greatest** among them.

---

## **1.5️⃣ Category**

Arithmetic → Comparison → Maximum of Three Numbers

---

## **2️⃣ Outline**

- Read A
- Read B
- Read C
- Compare the three values
- Print the greatest number

---

## **3️⃣ Objective**

To determine the largest number among three given integers.

---

## **4️⃣ Purpose**

This problem develops comparison logic and helps build foundational decision-making skills used in many algorithms.

---

## **5️⃣ Theory**

We compare values using:

[
\text{Greatest} = \max(A, B, C)
]

Logic steps:

- Check if A is greatest
- Else check if B is greatest
- Else C is greatest

---

## **6️⃣ Step-by-Step Explanation**

1. Read A, B, C
2. Assume A is greatest
3. Compare B with current greatest and update if needed
4. Compare C with current greatest and update if needed
5. Print final greatest value

---

## **7️⃣ Method**

- Use simple comparison operators (`>` and `<`)
- Use if–elif–else to evaluate greatest

---

## **8️⃣ Constraints**

- A, B, C are integers
- Only one number must be printed
- No extra text should be printed

---

## **9️⃣ Common Mistakes**

❌ Missing comparison between all three numbers
❌ Printing all values instead of only the greatest
❌ Using incorrect logical operators
❌ Overcomplicating the solution

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
A = int(input())
B = int(input())
C = int(input())

if A >= B and A >= C:
    print(A)
elif B >= A and B >= C:
    print(B)
else:
    print(C)
```

---

## **1️⃣2️⃣ Example**

### Input

```
10
15
20
```

### Output

```
20
```

---

## **1️⃣3️⃣ Dry Run**

| A   | B   | C   | Greatest Logic                     | Output |
| --- | --- | --- | ---------------------------------- | ------ |
| 10  | 15  | 20  | 20 > 15 and 20 > 10                | 20     |
| -10 | 59  | 34  | 59 > -10 and 59 > 34               | 59     |
| 5   | 5   | 2   | A == B == 5 → first condition true | 5      |

---

## **1️⃣4️⃣ Test Cases Table**

| A   | B   | C   | Greatest |
| --- | --- | --- | -------- |
| 10  | 15  | 20  | 20       |
| -10 | 59  | 34  | 59       |
| 5   | 5   | 2   | 5        |
| 99  | 18  | 99  | 99       |
| -5  | -1  | -2  | -1       |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Compare values step-by-step
- Equal values should also be handled using `>=`
- Only one output line is required

---

## **1️⃣6️⃣ Real-Life Application**

- Ranking values in leaderboards
- Finding highest score, highest temperature
- Comparing performance metrics

---

## **1️⃣7️⃣ Practice Questions**

1. Print the smallest among three numbers.
2. Check if all three numbers are equal.
3. Print the median (middle) number among three.

---

## **1️⃣8️⃣ Result**

The program correctly prints the greatest number among A, B, and C.

---

## **1️⃣9️⃣ Conclusion**

This problem reinforces comparison logic — a building block for sorting, ranking, and decision-making systems.

---
