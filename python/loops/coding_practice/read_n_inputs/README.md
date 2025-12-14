# ✅ **Read N Inputs**

---

## **1️⃣ Question**

Given N, read the next N integers and print each one.

---

## **2️⃣ Outline**

- Read N
- Loop N times
- Read a number each time
- Print it

---

## **3️⃣ Objective**

Practice repeated input + output using a while loop.

---

## **4️⃣ Purpose**

Strengthens your understanding of reading multiple values in loops.

---

## **5️⃣ Theory**

Use a counter to read and print exactly N numbers.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set counter = 0
3. While counter < N:

   - Read next number
   - Print it
   - Increase counter

---

## **7️⃣ Method**

Use while loop + input().

---

## **8️⃣ Constraints**

N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Missing counter increment
❌ Printing extra spaces
❌ Reading all inputs before loop (not needed)

---

## 🔟 Complexity

O(N)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

counter = 0
while counter < N:
    value = int(input())
    print(value)
    counter = counter + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
3
8
11
25
```

Output:

```
8
11
25
```

---

## **1️⃣3️⃣ Dry Run**

N = 2
counter = 0 → read 7 → print 7
counter = 1 → read 20 → print 20
counter = 2 → stop

---

## **1️⃣4️⃣ Test Cases**

| Input              | Output   |
| ------------------ | -------- |
| 1, then 5          | 5        |
| 2, then 10 11      | 10 11    |
| 4, values 3 6 9 12 | 3 6 9 12 |

---

## **1️⃣5️⃣ Notes**

This is the standard pattern for reading repeated inputs.

---

## **1️⃣6️⃣ Practice**

Read N inputs and print only even numbers.

---

## **1️⃣7️⃣ Result**

Program reads and prints all N inputs correctly.

---

## **1️⃣8️⃣ Conclusion**

A perfect loop exercise to master repeated input/output.

---
