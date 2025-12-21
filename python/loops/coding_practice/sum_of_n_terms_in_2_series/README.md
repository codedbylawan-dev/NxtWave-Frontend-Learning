# ✅ **Sum of N Terms in 1 Series**

---

## **1️⃣ Question**

Given a number **N**, print the **sum of the first N terms** in the following series:

```
1
11
111
1111
...
```

---

## **1️⃣.5️⃣ Category**

For Loop → Series → Sum Calculation

---

## **2️⃣ Outline**

- Read N
- Start with an empty string
- Initialize sum as 0
- Loop N times
- Build the series using `"1"`
- Convert each term to number
- Add to sum
- Print sum

---

## **3️⃣ Objective**

To calculate the **sum of a number series** formed using digit `1`.

---

## **4️⃣ Purpose**

This problem helps you understand:

- series generation
- string to integer conversion
- cumulative addition using loops

---

## **5️⃣ Theory**

Each term is formed by **adding one more `1`** to the previous term.

Example for N = 4:

```
Terms: 1, 11, 111, 1111
Sum: 1 + 11 + 111 + 1111 = 1234
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Initialize `term` as empty string
3. Initialize `total = 0`
4. Loop from 1 to N
5. In each iteration:

   - append `"1"` to `term`
   - convert `term` to integer
   - add it to `total`

6. Print `total`

---

## **7️⃣ Method**

Use:

- for loop
- string concatenation
- `int()`
- addition

---

## **8️⃣ Constraints**

- N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Resetting the term inside the loop
❌ Forgetting to convert string to integer
❌ Printing inside the loop

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

term = ""
total = 0

for i in range(N):
    term = term + "1"
    total = total + int(term)

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

## **1️⃣3️⃣ Dry Run**

N = 4

- i = 0 → term = "1" → total = 1
- i = 1 → term = "11" → total = 12
- i = 2 → term = "111" → total = 123
- i = 3 → term = "1111" → total = 1234

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----: | -----: |
|     1 |      1 |
|     4 |   1234 |
|     5 |  12345 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Series can be built using strings
- Convert to number only when adding
- Keep accumulation outside loop

---

## **1️⃣6️⃣ Real-Life Application**

- Pattern-based number problems
- Competitive programming series
- Logical sequence building

---

## **1️⃣7️⃣ Practice Questions**

1. Sum of series: 2, 22, 222
2. Sum of series: 3, 33, 333
3. Print terms along with sum

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of N terms in the 1 series**.

---

## **1️⃣9️⃣ Conclusion**

A clean and logical series problem that strengthens **looping and string-number handling**.

---
