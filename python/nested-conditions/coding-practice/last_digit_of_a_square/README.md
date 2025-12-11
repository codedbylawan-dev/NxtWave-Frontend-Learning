# ✅ **Last Digit of a Square**

---

## **1️⃣ Question**

Read a number **N** and check whether the **last digit of N** is equal to the **last digit of N²**.

If they are equal → print **"Equal"**
Else → print **"Not Equal"**.

---

## **1.5️⃣ Category**

Arithmetic → Digit Extraction → Comparison

---

## **2️⃣ Outline**

- Read N
- Compute N²
- Extract last digit of N
- Extract last digit of N²
- Compare
- Print result

---

## **3️⃣ Objective**

To determine whether the last digit of a number matches the last digit of its square.

---

## **4️⃣ Purpose**

To practice:

- Squaring a number
- Extracting digits
- Performing comparison checks

---

## **5️⃣ Theory**

To get the last digit of a number:

[
\text{last digit} = N % 10
]

Square:

[
\text{sq} = N \times N
]

Last digit of the square:

[
\text{sq} % 10
]

Comparison:

[
N%10 = (N^2)%10
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Compute the square: sq = N × N
3. Extract last digit of N → `N % 10`
4. Extract last digit of square → `sq % 10`
5. Compare the two
6. If equal → print "Equal"
7. Else → print "Not Equal"

---

## **7️⃣ Method**

- Use multiplication for square
- Use `% 10` to extract last digits
- Use if–else to compare

---

## **8️⃣ Constraints**

- N is an integer
- Output must match exactly
- No extra prints

---

## **9️⃣ Common Mistakes**

❌ Extracting digits incorrectly
❌ Forgetting to square using multiplication
❌ Comparing N with sq instead of last digits
❌ Printing wrong output statements

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

sq = N * N

last_N = N % 10
last_sq = sq % 10

if last_N == last_sq:
    print("Equal")
else:
    print("Not Equal")
```

---

## **1️⃣2️⃣ Example**

### Input

```
15
```

### Output

```
Equal
```

---

## **1️⃣3️⃣ Dry Run**

| Step | N   | N²  | N%10 | (N²)%10 | Comparison     | Output    |
| ---- | --- | --- | ---- | ------- | -------------- | --------- |
| 1    | 15  | 225 | 5    | 5       | 5 == 5 → True  | Equal     |
| 2    | 2   | 4   | 2    | 4       | 2 == 4 → False | Not Equal |

---

## **1️⃣4️⃣ Test Cases Table**

| N   | N²  | Last digit(N) | Last digit(N²) | Output    |
| --- | --- | ------------- | -------------- | --------- |
| 15  | 225 | 5             | 5              | Equal     |
| 2   | 4   | 2             | 4              | Not Equal |
| 11  | 121 | 1             | 1              | Equal     |
| 7   | 49  | 7             | 9              | Not Equal |
| 9   | 81  | 9             | 1              | Not Equal |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `% 10` is used to extract last digits
- Squares often change last digits, making comparison interesting
- Useful in number theory and digital property problems

---

## **1️⃣6️⃣ Real-Life Application**

- Numeric pattern recognition
- Validation rules in digital security
- Last-digit-based checksum concepts

---

## **1️⃣7️⃣ Practice Questions**

1. Check if the **first** digit of N equals the first digit of N².
2. Check if the **sum of digits** of N equals sum of digits of N².
3. Print “Match” if last digit of N equals last digit of N³.

---

## **1️⃣8️⃣ Result**

The program correctly determines whether the last digits match.

---

## **1️⃣9️⃣ Conclusion**

This problem enhances digit extraction and comparison skills, commonly used in number-based coding challenges.

---
