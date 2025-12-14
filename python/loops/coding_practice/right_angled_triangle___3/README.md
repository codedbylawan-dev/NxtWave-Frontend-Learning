# ✅ **Right Angled Triangle – 3**

---

## **1️⃣ Question**

Given a number **N**, print a right-angled triangle of **N rows** where:

- Rows **1 to N-1** contain stars `*`
- Row **N** contains pluses `+`

---

## **2️⃣ Outline**

- Read N
- Use a loop from 1 to N
- If row < N → print row number of stars
- If row = N → print N pluses

---

## **3️⃣ Objective**

To practice pattern creation with conditions inside a loop.

---

## **4️⃣ Purpose**

Helps understand how to change the pattern on the last row.

---

## **5️⃣ Theory**

If N = 4, the pattern is:

```
*
* *
* * *
+ + + +
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Start count at 1
3. If count < N → print stars
4. If count == N → print pluses
5. Increase count

---

## **7️⃣ Method**

- while loop
- if condition
- string repetition

---

## **8️⃣ Constraints**

- N ≥ 1

---

## **9️⃣ Common Mistakes**

- Using stars on last row
- Wrong spacing
- Wrong number of symbols

---

## 🔟 Complexity

O(N)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

row = 1
while row <= N:
    if row < N:
        print(("* ")*row)
    else:
        print(("+ ")*N)
    row = row + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
4
```

Output:

```
*
* *
* * *
+ + + +
```

---

## **1️⃣3️⃣ Dry Run**

For N = 3:

- row = 1 → `*`
- row = 2 → `* *`
- row = 3 → `+ + +`

---

## **1️⃣4️⃣ Test Cases**

| Input | Output Pattern     |
| ----- | ------------------ |
| 1     | +                  |
| 2     | \* / + +           |
| 5     | last row + + + + + |

---

## **1️⃣5️⃣ Notes**

Last row must always be pluses.

---

## **1️⃣6️⃣ Result**

Prints a triangle of stars and pluses correctly.

---

## **1️⃣7️⃣ Conclusion**

Simple loop + condition pattern problem.

---
