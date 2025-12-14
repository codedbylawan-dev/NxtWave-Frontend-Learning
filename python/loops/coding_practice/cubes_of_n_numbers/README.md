Here is **Cubes of N Numbers**, exactly in your chosen clean format and using **only while-loop + basic arithmetic**, nothing advanced.

---

# ✅ **Cubes of N Numbers**

---

## **1️⃣ Question**

Read a number **N** and print the **cube of each number from 1 to N**, each on a new line.

---

## **1.5️⃣ Category**

Loops → While Loop → Power Calculation

---

## **2️⃣ Outline**

- Read N
- Start counter at 1
- For each number → calculate cube = number × number × number
- Print cube
- Repeat until counter = N

---

## **3️⃣ Objective**

To compute cubes of numbers sequentially using a while loop.

---

## **4️⃣ Purpose**

Builds understanding of repetitive calculations inside loops.

---

## **5️⃣ Theory**

Cube of a number = **n × n × n**

Example:
1 → 1
2 → 8
3 → 27
4 → 64

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set counter = 1
3. While counter ≤ N:

   - cube = counter × counter × counter
   - print cube
   - increment counter

---

## **7️⃣ Method**

- integer input
- arithmetic multiplication
- while loop

---

## **8️⃣ Constraints**

- N ≥ 1
- Print exactly N cubes

---

## **9️⃣ Common Mistakes**

❌ Using exponent operator when not learned
❌ Forgetting to increment counter
❌ Printing all cubes in one line

---

## 🔟 Complexity

Time → O(N)
Space → O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

counter = 1
while counter <= N:
    cube = counter * counter * counter
    print(cube)
    counter = counter + 1
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
1
8
27
64
```

---

## **1️⃣3️⃣ Dry Run**

N = 3
counter = 1 → cube = 1 → print
counter = 2 → cube = 8 → print
counter = 3 → cube = 27 → print

---

## **1️⃣4️⃣ Test Cases Table**

| N   | Output (cubes)    |
| --- | ----------------- |
| 1   | 1                 |
| 3   | 1, 8, 27          |
| 5   | 1, 8, 27, 64, 125 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Cube = multiply number three times
- While loop must progress correctly

---

## **1️⃣6️⃣ Real-Life Application**

- Mathematical sequence generation
- Volume calculation of cubes

---

## **1️⃣7️⃣ Practice Questions**

1. Print squares of N numbers
2. Print fourth powers of N numbers
3. Print cubes of only odd numbers

---

## **1️⃣8️⃣ Result**

Program correctly prints cubes from 1 to N.

---

## **1️⃣9️⃣ Conclusion**

A simple looping problem that builds repetition and arithmetic confidence.

---
