# ✅ **Sum of N Squares**

---

## **1️⃣ Question**

Given N, print the sum of squares of numbers from 1 to N.

---

## **1.5️⃣ Category**

While Loop → Arithmetic → Summation

---

## **2️⃣ Outline**

- Read N
- Start counter at 1
- Square each number
- Add to total sum
- Print final sum

---

## **3️⃣ Objective**

To calculate the sum of squares from 1 to N.

---

## **4️⃣ Purpose**

Practices loops, counters, and arithmetic operations.

---

## **5️⃣ Theory**

Squares:
1², 2², 3²… N²
Sum = 1² + 2² + 3² + … + N²

Example: N = 4 → 1 + 4 + 9 + 16 = 30

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. sum = 0
3. counter = 1
4. While counter ≤ N:

   - square = counter \* counter
   - sum = sum + square
   - counter = counter + 1

5. Print sum

---

## **7️⃣ Method**

Using a while loop and repeated addition.

---

## **8️⃣ Constraints**

N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Forgetting to square the number
❌ Not updating counter
❌ Starting from 0 instead of 1

---

## 🔟 Complexity

Time: O(N)
Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

counter = 1
total = 0

while counter <= N:
    total = total + (counter * counter)
    counter = counter + 1

print(total)
```

---

## **1️⃣2️⃣ Example**

Input:

```
4
```

Output:

```
30
```

---

## **1️⃣3️⃣ Dry Run**

N = 3
Squares → 1, 4, 9
Sum → 14

---

## **1️⃣4️⃣ Test Cases Table**

| N   | Squares           | Sum |
| --- | ----------------- | --- |
| 4   | 1,4,9,16          | 30  |
| 7   | 1,4,9,16,25,36,49 | 140 |
| 1   | 1                 | 1   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Square = number × number
- Loop repeats N times

---

## **1️⃣6️⃣ Real-Life Application**

- Used in math calculations and physics formulas
- Basis for variance and standard deviation

---

## **1️⃣7️⃣ Practice Questions**

1. Sum of cubes from 1 to N
2. Sum of even squares up to N
3. Print squares of numbers from 1 to N

---

## **1️⃣8️⃣ Result**

Correct sum of squares from 1 to N is printed.

---

## **1️⃣9️⃣ Conclusion**

A straightforward loop problem practicing arithmetic and repetition.

---
