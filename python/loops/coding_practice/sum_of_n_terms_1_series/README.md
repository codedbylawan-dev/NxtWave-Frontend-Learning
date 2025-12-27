# ✅ **Sum of N Terms – 1 Series**

---

## **1️⃣ Question**

Given an integer **N**, print the **sum of N terms** in the given series.

### **Series**

```
1, 11, 111, 1111, ...
```

---

## **1️⃣.5️⃣ Category**

For Loop → Number Series

---

## **2️⃣ Outline**

- Read N
- Generate each term using `"1"` repetition
- Convert term to number
- Add to sum
- Print final sum

---

## **3️⃣ Objective**

To calculate the **sum of a number pattern** formed using repeated `1`s.

---

## **4️⃣ Purpose**

This problem helps you understand:

- string repetition
- number formation from strings
- accumulation using a loop

---

## **5️⃣ Theory**

- Each term contains only the digit `1`
- Term number decides how many `1`s it has

Examples:

- 1st term → `"1"`
- 2nd term → `"11"`
- 3rd term → `"111"`

---

## **6️⃣ Step-by-Step Explanation**

1. Read input `N`
2. Initialize `total = 0`
3. Loop from `1` to `N`
4. In each loop:

   - Create term using `"1" * i`
   - Convert it to integer
   - Add to total

5. Print total

---

## **7️⃣ Method**

- One `for` loop
- String repetition
- Integer conversion

---

## **8️⃣ Constraints**

- N ≥ 1
- Output must be a single integer

---

## **9️⃣ Common Mistakes**

❌ Printing terms instead of summing
❌ Forgetting to convert string to integer
❌ Using unnecessary conditions

---

## **🔟 Complexity**

- Time: **O(N²)** (string creation)
- Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
n = int(input())

total = 0

for i in range(1, n + 1):
    term = int("1" * i)
    total = total + term

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
1234
```

---

## **1️⃣3️⃣ Dry Run (N = 3)**

- i = 1 → term = 1 → total = 1
- i = 2 → term = 11 → total = 12
- i = 3 → term = 111 → total = 123

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----: | -----: |
|     1 |      1 |
|     3 |    123 |
|     4 |   1234 |
|     5 |  12345 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `"1" * i` creates the pattern
- Convert string → number before adding
- Very beginner-friendly logic

---

## **1️⃣6️⃣ Real-Life Application**

- Pattern-based number generation
- Building numeric sequences
- String-to-number understanding

---

## **1️⃣7️⃣ Practice Questions**

1. Print the series without summing
2. Replace `1` with `2` → `2, 22, 222`
3. Print sum of first N even digit patterns

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of N terms** in the given series.

---

## **1️⃣9️⃣ Conclusion**

This solution is **simple**, **clean**, and **perfectly aligned** with
your **current learning level** and **problem requirements** ✅

---
