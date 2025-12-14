# ✅ **Print N Times**

---

## **1️⃣ Question**

Given a number **N**, print the number **0 exactly N times**, each on its own line.

---

## **1.5️⃣ Category**

Loops → While Loop → Repetition

---

## **2️⃣ Outline**

- Read N
- Use a counter
- Print 0 while counter < N

---

## **3️⃣ Objective**

To repeat an output using a **while loop**, which you have learned.

---

## **4️⃣ Purpose**

This problem strengthens understanding of loop execution and counters.

---

## **5️⃣ Theory**

A **while loop** repeats as long as a condition is True.

Example:
If N = 3 → Output:

```
0
0
0
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Create a counter starting at 0
3. Check if counter < N
4. Print 0
5. Increase counter by 1
6. Repeat until counter reaches N

---

## **7️⃣ Method**

Use:

- integer input
- counter variable
- while loop
- print statement

---

## **8️⃣ Constraints**

- N is a positive integer
- Output must contain exactly N lines

---

## **9️⃣ Common Mistakes**

❌ Not incrementing counter → infinite loop
❌ Printing all zeros on same line
❌ Printing extra spaces or characters

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code (Using ONLY what you learned — while loop)**

```python
N = int(input())

counter = 0
while counter < N:
    print(0)
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
0
0
0
0
```

---

## **1️⃣3️⃣ Dry Run**

Input: N = 2

counter = 0 → print 0 → counter = 1
counter = 1 → print 0 → counter = 2
counter = 2 → loop stops

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output            |
| ----- | ----------------- |
| 1     | 0                 |
| 3     | 0 0 0 (3 lines)   |
| 5     | 0 printed 5 times |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Loops repeat actions automatically
- Counter must be updated
- Printing happens line-by-line

---

## **1️⃣6️⃣ Real-Life Application**

- Repeating notifications
- Generating logs
- Printing repeated patterns

---

## **1️⃣7️⃣ Practice Questions**

1. Print the number 1 N times
2. Print “Hello” N times
3. Print numbers from 1 to N using while loop

---

## **1️⃣8️⃣ Result**

The program prints 0 exactly N times, each on a new line.

---

## **1️⃣9️⃣ Conclusion**

A simple while-loop exercise teaching repetition and counter control.

---
