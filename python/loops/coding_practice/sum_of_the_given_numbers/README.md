# ✅ **Sum of the Given Numbers**

---

## **1️⃣ Question**

Read N numbers and print the **sum** of all N numbers.

---

## **2️⃣ Outline**

- Read N
- Start sum at 0
- Loop N times
- Add each input number to sum
- Print final sum

---

## **3️⃣ Objective**

To calculate a running total using repeated inputs.

---

## **4️⃣ Purpose**

Strengthens while-loop usage and cumulative addition.

---

## **5️⃣ Theory**

Sum starts at **0** because adding numbers to 0 keeps them unchanged.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. sum = 0
3. While counter < N:

   - Read a number
   - sum = sum + number
   - Increase counter

4. Print sum

---

## **7️⃣ Method**

Use a counter and while loop.

---

## **8️⃣ Constraints**

N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Starting sum at a wrong value
❌ Forgetting to convert input to int
❌ Infinite loop due to missing counter increment

---

## 🔟 Complexity

O(N)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

sum_value = 0
counter = 0

while counter < N:
    num = int(input())
    sum_value = sum_value + num
    counter = counter + 1

print(sum_value)
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
44
```

---

## **1️⃣3️⃣ Dry Run**

sum = 0
Read 8 → sum = 8
Read 11 → sum = 19
Read 25 → sum = 44

---

## **1️⃣4️⃣ Test Cases**

| Inputs             | Result |
| ------------------ | ------ |
| N=2 → 7, 20        | 27     |
| N=3 → 1, 1, 1      | 3      |
| N=4 → 5, 10, -3, 2 | 14     |

---

## **1️⃣5️⃣ Notes**

Always initialize sum to 0.

---

## **1️⃣6️⃣ Practice**

Find sum of only **positive** numbers from N inputs.

---

## **1️⃣7️⃣ Result**

The program prints the correct sum of N input values.

---

## **1️⃣8️⃣ Conclusion**

A simple cumulative addition problem using while loop.

---
