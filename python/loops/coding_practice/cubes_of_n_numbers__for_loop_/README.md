# ✅ **Cubes of N Numbers (For Loop)**

---

## **1️⃣ Question**

Given a number **N**, print the **cube of numbers from 1 to N**, each on a new line.

---

## **1.5️⃣ Category**

For Loop → Numbers → Power Calculation

---

## **2️⃣ Outline**

- Read N
- Loop from 1 to N
- Find cube of each number
- Print the cube

---

## **3️⃣ Objective**

To generate and print cubes of numbers using a **for loop**.

---

## **4️⃣ Purpose**

Helps practice looping and arithmetic operations together.

---

## **5️⃣ Theory**

Cube of a number:

```
Cube = number × number × number
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Start a loop from 1 to N
3. Calculate cube of the current number
4. Print the cube
5. Repeat until N

---

## **7️⃣ Method**

Use:

- `for` loop
- Multiplication (`*`)
- `print()`

---

## **8️⃣ Constraints**

- N is a positive integer
- One output per line

---

## **9️⃣ Common Mistakes**

❌ Printing numbers instead of cubes
❌ Using wrong loop range
❌ Printing all values in one line

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(1, N + 1):
    cube = i * i * i
    print(cube)
```

---

## **1️⃣2️⃣ Example**

Input:

```
3
```

Output:

```
1
8
27
```

---

## **1️⃣3️⃣ Dry Run**

N = 4

- i = 1 → 1 × 1 × 1 = 1
- i = 2 → 2 × 2 × 2 = 8
- i = 3 → 3 × 3 × 3 = 27
- i = 4 → 4 × 4 × 4 = 64

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output        |
| ----- | ------------- |
| 1     | 1             |
| 3     | 1 8 27        |
| 5     | 1 8 27 64 125 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Cubes use multiplication, not power operator
- Loop runs from 1 to N
- Each result prints on a new line

---

## **1️⃣6️⃣ Real-Life Application**

- Mathematical sequences
- Data processing tasks
- Programming practice for powers

---

## **1️⃣7️⃣ Practice Questions**

1. Print squares of numbers from 1 to N
2. Print cubes of even numbers till N
3. Print cubes from M to N

---

## **1️⃣8️⃣ Result**

The program correctly prints cubes of numbers from 1 to N.

---

## **1️⃣9️⃣ Conclusion**

A simple loop-based problem that strengthens arithmetic logic and iteration.

---
