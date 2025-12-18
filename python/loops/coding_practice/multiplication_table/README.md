# ✅ **Multiplication Table**

---

## **1️⃣ Question**

Given a number **N**, print the **multiplication table of N up to 10**, in the format
`N x i = result`.

---

## **1️⃣.5️⃣ Category**

For Loop → Multiplication → Patterned Output

---

## **2️⃣ Outline**

- Read N
- Use a for loop from 1 to 10
- Multiply N with loop variable
- Print result in required format

---

## **3️⃣ Objective**

To generate and print the **multiplication table** of a number using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- looping with fixed range
- multiplication logic
- formatted printing

---

## **5️⃣ Theory**

A **multiplication table** shows multiples of a number.

For a given number N:

- N × 1
- N × 2
- …
- N × 10

We use a **for loop** to repeat the multiplication from 1 to 10.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the number N
2. Start a loop from 1 to 10
3. Multiply N with the loop value
4. Print the result in the given format
5. Continue until the loop ends

---

## **7️⃣ Method**

Use:

- input()
- for loop
- multiplication
- print statement

---

## **8️⃣ Constraints**

- N is an integer
- Exactly 10 lines should be printed

---

## **9️⃣ Common Mistakes**

❌ Printing less than 10 lines
❌ Wrong format (missing `x` or `=`)
❌ Printing only numbers without format

---

## **🔟 Complexity**

Time: **O(10)** → constant time
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(1, 11):
    print(N, "x", i, "=", N * i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
```

### Output

```
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

- i = 1 → 3 × 1 = 3
- i = 2 → 3 × 2 = 6
- i = 3 → 3 × 3 = 9
- …
- i = 10 → 3 × 10 = 30

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output (Last Line) |
| ----: | ------------------ |
|     3 | 3 x 10 = 30        |
|    10 | 10 x 10 = 100      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- for loop is perfect for fixed repetitions
- multiplication tables are repeated patterns
- formatting matters in output

---

## **1️⃣6️⃣ Real-Life Application**

- School math tables
- Repeated calculations
- Practice for loop logic

---

## **1️⃣7️⃣ Practice Questions**

1. Print table up to 20
2. Print table in reverse order
3. Print only even multiples

---

## **1️⃣8️⃣ Result**

The program correctly prints the **multiplication table of N up to 10**.

---

## **1️⃣9️⃣ Conclusion**

A basic but important problem that strengthens **for loop control and arithmetic operations**.

---
