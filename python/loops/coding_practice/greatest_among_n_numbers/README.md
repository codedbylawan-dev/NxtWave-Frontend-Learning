# ✅ **Greatest Among N Numbers**

---

## **1️⃣ Question**

Given a number **N**, read **N inputs** and print the **greatest number** among them.

---

## **1️⃣.5️⃣ Category**

For Loop → Input Handling → Comparison

---

## **2️⃣ Outline**

- Read N
- Read the first number and store it as greatest
- Read remaining numbers one by one
- Compare each number with the current greatest
- Update greatest if needed
- Print the greatest number

---

## **3️⃣ Objective**

To find the **maximum value** among multiple inputs using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- comparing values
- updating variables
- tracking maximum using loops

---

## **5️⃣ Theory**

To find the greatest number:

- Assume the first number is the greatest
- Compare each next number with it
- If a number is larger, update the greatest

Example:
Inputs → 8, 11, 96, 49, 25
Greatest → **96**

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Read the first number and store it in `greatest`
3. Loop from 2 to N
4. Read next number
5. If number > greatest, update greatest
6. After loop, print greatest

---

## **7️⃣ Method**

Use:

- for loop
- comparison operator ( > )
- variable reassignment

---

## **8️⃣ Constraints**

- N ≥ 1
- Inputs can be positive or negative

---

## **9️⃣ Common Mistakes**

❌ Initializing greatest as 0
❌ Forgetting to compare all inputs
❌ Printing inside loop

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

greatest = int(input())

for i in range(1, N):
    number = int(input())
    if number > greatest:
        greatest = number

print(greatest)
```

---

## **1️⃣2️⃣ Example**

### Input

```
5
8
11
96
49
25
```

### Output

```
96
```

---

## **1️⃣3️⃣ Dry Run**

Inputs: 8, 11, 96, 49, 25

- greatest = 8
- compare 11 → greatest = 11
- compare 96 → greatest = 96
- compare 49 → no change
- compare 25 → no change

Final Output → **96**

---

## **1️⃣4️⃣ Test Cases Table**

|   N | Inputs        | Output |
| --: | ------------- | -----: |
|   3 | 10 10 10      |     10 |
|   4 | -5 -2 -9 -1   |     -1 |
|   5 | 8 11 96 49 25 |     96 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- First input should be initial greatest
- Always compare before updating
- Works for negative numbers too

---

## **1️⃣6️⃣ Real-Life Application**

- Finding highest score
- Maximum salary calculation
- Data comparison tasks

---

## **1️⃣7️⃣ Practice Questions**

1. Find the smallest among N numbers
2. Find both minimum and maximum
3. Count how many times the greatest appears

---

## **1️⃣8️⃣ Result**

The program correctly prints the **greatest among N inputs**.

---

## **1️⃣9️⃣ Conclusion**

An essential looping problem that strengthens **comparison and decision-making logic**.

---
