# ✅ **Sum of Cubes**

---

## **1️⃣ Question**

Given a number **N**, print the **sum of the cubes of numbers from 1 to N**.

---

## **1️⃣.5️⃣ Category**

For Loop → Arithmetic Operations → Accumulation

---

## **2️⃣ Outline**

- Read N
- Initialize sum as 0
- Loop from 1 to N
- Add cube of each number to sum
- Print the final sum

---

## **3️⃣ Objective**

To calculate the **sum of cubes** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- looping from 1 to N
- cube calculation
- updating a running total

---

## **5️⃣ Theory**

Cube of a number **X** is:

```
X × X × X
```

We calculate cubes from **1 to N** and add them.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the value of N
2. Set `total = 0`
3. Start a loop from 1 to N
4. For each number, calculate its cube
5. Add the cube to `total`
6. After loop ends, print `total`

---

## **7️⃣ Method**

Use:

- `input()`
- `for` loop
- multiplication
- variable for sum

---

## **8️⃣ Constraints**

- N is a positive integer
- Output should be a single integer

---

## **9️⃣ Common Mistakes**

❌ Forgetting to initialize sum
❌ Using square instead of cube
❌ Printing inside the loop

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

total = 0
for i in range(1, N + 1):
    total = total + (i * i * i)

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
```

### Output

```
36
```

---

## **1️⃣3️⃣ Dry Run**

For **N = 3**

- i = 1 → cube = 1 → total = 1
- i = 2 → cube = 8 → total = 9
- i = 3 → cube = 27 → total = 36

Final Output → `36`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----: | ------ |
|     3 | 36     |
|     6 | 441    |
|     1 | 1      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Cube means multiplying the number 3 times
- Sum must be updated every loop
- Print only after loop completes

---

## **1️⃣6️⃣ Real-Life Application**

- Mathematical series calculations
- Programming logic practice
- Problem-solving with loops

---

## **1️⃣7️⃣ Practice Questions**

1. Find sum of squares from 1 to N
2. Find sum of even cubes from 1 to N
3. Print cubes instead of summing

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of cubes from 1 to N**.

---

## **1️⃣9️⃣ Conclusion**

A clean and important loop-based problem that strengthens **arithmetic logic** and **for loop usage** using only learned concepts.
