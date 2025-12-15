# ✅ **Right Angled Triangle – 2 (For Loop)**

---

## **1️⃣ Question**

Given a number **N**, print a **right angled triangle** of **N rows** using numbers.

---

## **1.5️⃣ Category**

For Loop → Pattern Printing → Number Triangle

---

## **2️⃣ Outline**

- Read N
- Use a for loop from 1 to N
- Print the current number repeated equal to the row number

---

## **3️⃣ Objective**

To print a number-based right angled triangle using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps understand:

- pattern building
- number repetition
- loop control

---

## **5️⃣ Theory**

If N = 6

The output should be:

```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
```

Each row prints the row number repeated that many times.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Start loop from 1 to N
3. Print the current number repeated `i` times

---

## **7️⃣ Method**

Use:

- for loop
- string repetition
- print statement

---

## **8️⃣ Constraints**

- N is a positive integer
- Output must have exactly N rows

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Printing wrong number of values
❌ Missing spaces between numbers

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(1, N + 1):
    print((str(i) + " ") * i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
6
```

### Output

```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

Loop:

- i = 1 → `1`
- i = 2 → `2 2`
- i = 3 → `3 3 3`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output                      |
| ----- | --------------------------- |
| 1     | 1                           |
| 3     | 1, 2 2, 3 3 3               |
| 5     | Number triangle with 5 rows |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Single loop is enough
- String repetition simplifies pattern printing
- Row number controls repetition

---

## **1️⃣6️⃣ Real-Life Application**

- Console pattern designs
- Learning structured outputs
- Loop practice

---

## **1️⃣7️⃣ Practice Questions**

1. Print triangle using `*` and numbers together
2. Print reverse number triangle
3. Print square using numbers

---

## **1️⃣8️⃣ Result**

The program correctly prints a number-based right angled triangle.

---

## **1️⃣9️⃣ Conclusion**

A beginner-friendly pattern problem that strengthens **for loop** and **number repetition** concepts.

---
