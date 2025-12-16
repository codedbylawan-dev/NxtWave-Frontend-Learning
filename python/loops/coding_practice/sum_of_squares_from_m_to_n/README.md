# ✅ **Sum of Squares from M to N**

---

## **1️⃣ Question**

Given two integers **M** and **N**, print the **sum of the squares of numbers from M to N**.

---

## **1️⃣.5️⃣ Category**

For Loop → Arithmetic → Accumulation

---

## **2️⃣ Outline**

- Read M
- Read N
- Initialize sum as 0
- Loop from M to N
- Square each number and add to sum
- Print the final sum

---

## **3️⃣ Objective**

To calculate the **sum of squares** of numbers in a given range using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- looping through a range
- squaring numbers
- accumulating results

---

## **5️⃣ Theory**

- **Square of a number** = number × number
- **Sum of squares** = add all squared values

Example:
For numbers 2 to 4
Squares → 4, 9, 16
Sum → 4 + 9 + 16 = 29

---

## **6️⃣ Step-by-Step Explanation**

1. Read the value of M
2. Read the value of N
3. Set `total` to 0
4. Use a for loop from M to N
5. Square the current number
6. Add it to `total`
7. After loop ends, print `total`

---

## **7️⃣ Method**

Use:

- `input()`
- `int()`
- `for` loop
- multiplication

---

## **8️⃣ Constraints**

- M and N are integers
- M ≤ N

---

## **9️⃣ Common Mistakes**

❌ Forgetting to square the number
❌ Resetting sum inside loop
❌ Looping till wrong range

---

## **🔟 Complexity**

Time: **O(N − M + 1)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

total = 0

for i in range(M, N + 1):
    total = total + (i * i)

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
2
4
```

### Output

```
29
```

---

## **1️⃣3️⃣ Dry Run**

M = 2, N = 4

- i = 2 → 2² = 4 → total = 4
- i = 3 → 3² = 9 → total = 13
- i = 4 → 4² = 16 → total = 29

---

## **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output |
| --- | --- | ------ |
| 2   | 4   | 29     |
| 3   | 8   | 199    |
| 1   | 1   | 1      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Squaring uses multiplication
- Loop range must include N (`N + 1`)
- Accumulate result in one variable

---

## **1️⃣6️⃣ Real-Life Application**

- Mathematical calculations
- Statistics and data processing
- Formula-based programs

---

## **1️⃣7️⃣ Practice Questions**

1. Find sum of cubes from M to N
2. Find sum of even squares in a range
3. Count how many squares are added

---

## **1️⃣8️⃣ Result**

The program correctly prints the **sum of squares from M to N**.

---

## **1️⃣9️⃣ Conclusion**

A clear loop-based arithmetic problem that strengthens **range traversal** and **accumulation logic** using only learned concepts.
