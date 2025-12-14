# ✅ **Square – 2**

---

## **1️⃣ Question**

Print an **N × N square** using numbers from **1 to N**, where each row contains the **same number repeated N times**.

---

## **2️⃣ Outline**

- Read N
- Start number = 1
- For each row, print: `str(number) * N`
- Increase number
- Repeat N times using a while loop

---

## **3️⃣ Objective**

To print a numeric square pattern using repetition instead of nested loops.

---

## **4️⃣ Purpose**

Shows how string repetition (`*`) can replace inner loops.

---

## **5️⃣ Theory**

If N = 4:

```
1111
2222
3333
4444
```

Each row = one number repeated N times.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set `current = 1`
3. While current ≤ N:

   - Print `str(current) * N`
   - current = current + 1

---

## **7️⃣ Method**

- while loop
- string repetition using `*`

---

## **8️⃣ Constraints**

N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Printing spaces (not required)
❌ Forgetting to convert number to string
❌ Not updating counter

---

## 🔟 Complexity

O(N)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

current = 1
while current <= N:
    print(str(current) * N)
    current = current + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
4
```

Output:

```
1111
2222
3333
4444
```

---

## **1️⃣3️⃣ Dry Run**

N = 3
current = 1 → print "111"
current = 2 → print "222"
current = 3 → print "333"

---

## **1️⃣4️⃣ Test Cases**

| Input | Output               |
| ----- | -------------------- |
| 1     | 1                    |
| 2     | 11<br>22             |
| 5     | rows 1–5 repeated 5× |

---

## **1️⃣5️⃣ Notes**

`str(number) * N` is the key — no nested loop needed.

---

## **1️⃣6️⃣ Practice**

Try printing:

```
1234
1234
1234
1234
```

---

## **1️⃣7️⃣ Result**

Prints an N×N numeric square correctly.

---

## **1️⃣8️⃣ Conclusion**

A simple pattern problem solved cleanly without nested loops using string repetition.

---
