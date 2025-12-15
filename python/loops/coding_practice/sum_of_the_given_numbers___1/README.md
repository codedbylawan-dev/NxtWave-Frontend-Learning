# ✅ **Sum of the Given Numbers (For Loop)**

---

## **1️⃣ Question**

Given an integer **N**, read **N numbers** and print the **sum** of those numbers.

---

## **1.5️⃣ Category**

For Loop → Input Handling → Accumulation

---

## **2️⃣ Outline**

- Read N
- Initialize sum as 0
- Read each number
- Add it to sum
- Print final sum

---

## **3️⃣ Objective**

To calculate the sum of multiple inputs using a **for loop**.

---

## **4️⃣ Purpose**

Helps understand:

- reading multiple inputs
- updating a variable repeatedly
- using loops for accumulation

---

## **5️⃣ Theory**

If N = 3 and inputs are:

```
8
11
25
```

Sum = `8 + 11 + 25 = 44`

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set `total = 0`
3. Loop N times
4. Read a number in each loop
5. Add it to total
6. Print total

---

## **7️⃣ Method**

Use:

- `for` loop
- integer variables
- `input()` and `print()`

---

## **8️⃣ Constraints**

- N ≥ 1
- Inputs are integers

---

## **9️⃣ Common Mistakes**

❌ Forgetting to initialize sum
❌ Printing inside the loop
❌ Reading fewer or more inputs

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

total = 0
for i in range(N):
    num = int(input())
    total = total + num

print(total)
```

---

## **1️⃣2️⃣ Example**

### Input

```
3
8
11
25
```

### Output

```
44
```

---

## **1️⃣3️⃣ Dry Run**

Inputs: 2, 7, 20

total = 0
total = 0 + 7 → 7
total = 7 + 20 → 27

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Numbers | Output |
| ----- | ------- | ------ |
| 3     | 8 11 25 | 44     |
| 2     | 7 20    | 27     |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Initialize accumulator before loop
- Update value inside loop
- Print result after loop

---

## **1️⃣6️⃣ Real-Life Application**

- Calculating total marks
- Summing expenses
- Adding scores

---

## **1️⃣7️⃣ Practice Questions**

1. Find product of N numbers
2. Find average of N numbers
3. Count even numbers in N inputs

---

## **1️⃣8️⃣ Result**

The program correctly prints the sum of given inputs.

---

## **1️⃣9️⃣ Conclusion**

A foundational loop problem that builds confidence in **input processing** and **accumulation logic**.

---
