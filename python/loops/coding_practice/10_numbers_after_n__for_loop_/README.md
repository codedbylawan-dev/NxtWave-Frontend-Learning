# ✅ **10 Numbers after N**

---

## **1️⃣ Question**

Given a number **N**, print the **next 10 numbers after N**, each on a new line.

---

## **1.5️⃣ Category**

For Loop → Numbers → Iteration

---

## **2️⃣ Outline**

- Read N
- Start from N + 1
- Print next 10 numbers using a loop

---

## **3️⃣ Objective**

To generate a fixed count of numbers after a given value using a **for loop**.

---

## **4️⃣ Purpose**

This helps in understanding:

- loop ranges
- arithmetic progression
- controlled repetition

---

## **5️⃣ Theory**

If N = 4

The next 10 numbers are:

```
5 6 7 8 9 10 11 12 13 14
```

Each number increases by 1.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the value of N
2. Loop 10 times
3. In each iteration, add 1 to N
4. Print the updated value

---

## **7️⃣ Method**

Use:

- for loop
- addition
- print statement

---

## **8️⃣ Constraints**

- N is an integer
- Exactly 10 numbers must be printed

---

## **9️⃣ Common Mistakes**

❌ Printing N itself
❌ Printing more or fewer than 10 numbers
❌ Printing in one line

---

## 🔟 Complexity

Time: **O(10)** → constant time
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(1, 11):
    print(N + i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
5
6
7
8
9
10
11
12
13
14
```

---

## **1️⃣3️⃣ Dry Run**

N = 9

Loop runs from 1 to 10:

9 + 1 → 10
9 + 2 → 11
…
9 + 10 → 19

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output (last value) |
| ----- | ------------------- |
| 4     | 14                  |
| 9     | 19                  |
| 0     | 10                  |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Loop count controls number of outputs
- Addition generates next numbers
- Simple and predictable pattern

---

## **1️⃣6️⃣ Real-Life Application**

- Generating next IDs
- Pagination numbers
- Sequential data generation

---

## **1️⃣7️⃣ Practice Questions**

1. Print 5 numbers after N
2. Print numbers from N+1 to N+20
3. Print only even numbers after N

---

## **1️⃣8️⃣ Result**

The program correctly prints the next 10 numbers after N.

---

## **1️⃣9️⃣ Conclusion**

A straightforward loop-based problem that builds confidence with **ranges and iteration**.

---
