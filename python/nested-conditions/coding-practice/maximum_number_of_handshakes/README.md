# ✅ **Maximum Number of Handshakes**

---

## **1️⃣ Question**

Given **N** students, each student must shake hands with every other student **once**.
Find the **total number of handshakes**.

---

## **1.5️⃣ Category**

Math Logic → Pair Counting → Simple Arithmetic

---

## **2️⃣ Outline**

- Student 1 shakes with (N − 1)
- Student 2 shakes with (N − 2)
- Continue until 0
- Add all values

---

## **3️⃣ Objective**

To calculate total unique handshakes between N students.

---

## **4️⃣ Purpose**

Helps understand counting of unique pairs without repetition.

---

## **5️⃣ Theory**

For N students, the handshakes are:

```
(N - 1) + (N - 2) + (N - 3) ... + 1 + 0
```

Example for N = 5:

```
4 + 3 + 2 + 1 + 0 = 10
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Student 1 shakes with (N − 1)
3. Student 2 shakes with (N − 2)
4. Continue until the last student
5. Add all handshake counts
6. Print total

Since you **haven’t learned loops**, we use the formula:

### ✔ Sum of first (N − 1) numbers = N × (N − 1) ÷ 2

(This is allowed because it is basic arithmetic.)

---

## **7️⃣ Method**

Use only:

- multiplication
- subtraction
- division

---

## **8️⃣ Constraints**

- N ≥ 1
- N is integer
- Output is integer

---

## **9️⃣ Common Mistakes**

❌ Forgetting pairs are counted once
❌ Doing (N × N) instead of N × (N − 1)
❌ Missing integer division

---

## 🔟 Complexity

- Time → O(1)
- Space → O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())
handshakes = N * (N - 1) // 2
print(handshakes)
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
```

### Output

```
10
```

---

## **1️⃣3️⃣ Dry Run**

For N = 5:

```
handshakes = 5 × 4 ÷ 2 = 20 ÷ 2 = 10
```

---

## **1️⃣4️⃣ Test Cases Table**

| N   | Expected Output |
| --- | --------------- |
| 1   | 0               |
| 2   | 1               |
| 3   | 3               |
| 5   | 10              |
| 10  | 45              |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Formula avoids repeats
- Handshakes count is unique pairs
- Works for any N

---

## **1️⃣6️⃣ Real-Life Application**

- Social networking connections
- Pair combinations in teams
- Tournament pairing scheduling

---

## **1️⃣7️⃣ Practice Questions**

1. How many ways can 6 people form pairs?
2. How many high-fives happen if every student greets every other student?
3. For N teams, how many matches occur if each plays each once?

---

## **1️⃣8️⃣ Result**

You correctly compute handshake count for any N.

---

## **1️⃣9️⃣ Conclusion**

A clean arithmetic-based problem teaching pair counting using simple math.

---
