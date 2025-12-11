# ✅ **Smallest Remainder**

---

## **1️⃣ Question**

Read two integers **A** and **B** and compute:

- Remainder **A % B**
- Remainder **B % A**

Print the **smallest** of the two remainders.

---

## **1.5️⃣ Category**

Arithmetic → Modulus → Comparison

---

## **2️⃣ Outline**

- Read A
- Read B
- Compute r1 = A % B
- Compute r2 = B % A
- Compare r1 and r2
- Print smallest

---

## **3️⃣ Objective**

To determine which of the two remainder values is smaller and print it.

---

## **4️⃣ Purpose**

To practice modulus operations and comparison of computed results.

---

## **5️⃣ Theory**

Remainder rules:

[
A % B = \text{remainder when A is divided by B}
]
[
B % A = \text{remainder when B is divided by A}
]

Smaller remainder:

[
\min(A%B, B%A)
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read A
2. Read B
3. Compute remainder of A divided by B
4. Compute remainder of B divided by A
5. Compare both values
6. Print the smallest one

---

## **7️⃣ Method**

- Use modulus `%` operator
- Use simple if–else comparison

---

## **8️⃣ Constraints**

- A and B are non-zero integers
- Output must be exactly the smallest remainder

---

## **9️⃣ Common Mistakes**

❌ Forgetting `%` only gives remainder, not quotient
❌ Mixing up A % B with B % A
❌ Printing the bigger remainder accidentally
❌ Dividing by zero (avoid inputs where A or B = 0)

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
A = int(input())
B = int(input())

r1 = A % B
r2 = B % A

if r1 < r2:
    print(r1)
else:
    print(r2)
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
7
```

### Output

```
1
```

---

## **1️⃣3️⃣ Dry Run**

| A   | B   | A%B | B%A | Smallest | Output |
| --- | --- | --- | --- | -------- | ------ |
| 3   | 7   | 3   | 1   | 1        | 1      |
| 12  | 6   | 0   | 6   | 0        | 0      |

---

## **1️⃣4️⃣ Test Cases Table**

| A   | B   | A%B | B%A | Output |
| --- | --- | --- | --- | ------ |
| 3   | 7   | 3   | 1   | 1      |
| 12  | 6   | 0   | 6   | 0      |
| 8   | 5   | 3   | 5   | 3      |
| 9   | 4   | 1   | 0   | 0      |
| 10  | 3   | 1   | 3   | 1      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `%` gives remainder, not fraction
- Comparing two computed values is common in programming
- Always compute **both** A%B and B%A (don’t assume one is smaller)

---

## **1️⃣6️⃣ Real-Life Application**

- Circular indexing logic
- Hashing functions
- Scheduling where leftovers determine next steps

---

## **1️⃣7️⃣ Practice Questions**

1. Print the largest among A%B and B%A.
2. Check if A%B + B%A is even or odd.
3. Print “Zero remainder exists” if either remainder is 0.

---

## **1️⃣8️⃣ Result**

The program correctly outputs the smaller of the two remainders.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens understanding of modulus operations and comparative logic — essential tools in coding and algorithm problem-solving.

---
