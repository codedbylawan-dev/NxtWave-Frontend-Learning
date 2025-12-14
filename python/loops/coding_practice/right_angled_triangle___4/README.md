# ✅ **Right Angled Triangle – 4**

---

## **1️⃣ Question**

Read N and print **two right-angled triangles**, each with N rows.

---

## **2️⃣ Outline**

- Read N
- First triangle → print rows 1 to N
- Second triangle → print rows 1 to N

---

## **3️⃣ Objective**

Print repeated patterns using only simple loops.

---

## **4️⃣ Purpose**

Avoid nested loops and still generate patterns.

---

## **5️⃣ Theory**

Row number = number of stars
We can print a row using:

```
"* " * row_number
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Start counter = 1
3. Print `"* " * counter`
4. Increase counter
5. Repeat till N
6. Reset counter and repeat again for second triangle

---

## **7️⃣ Method**

Use **two while loops**, each printing N rows.

---

## **8️⃣ Constraints**

N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Forgetting to reset counter

---

## 🔟 Complexity

O(N²) printing, O(N) loop iterations

---

## **1️⃣1️⃣ Code (No nested loops)**

```python
N = int(input())

# First Triangle
row = 1
while row <= N:
    print("* " * row)
    row = row + 1

# Second Triangle
row = 1
while row <= N:
    print("* " * row)
    row = row + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
3
```

Output:

```
*
* *
* * *
*
* *
* * *
```

---

## **1️⃣3️⃣ Dry Run**

N = 2
Triangle 1 → `*`, then `* *`
Triangle 2 → `*`, then `* *`

---

## **1️⃣4️⃣ Result**

Two right-angled triangles printed without nested loops.

---

## **1️⃣5️⃣ Conclusion**

Pattern printed using only **simple while loops** and **string repetition**.

---
