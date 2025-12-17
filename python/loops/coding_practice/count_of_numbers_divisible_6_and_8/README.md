# ✅ **Count of Numbers Divisible by 6 and 8**

---

## **1️⃣ Question**

Given a number **N**, print the **count of numbers from 1 to N** that are divisible by **both 6 and 8**.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Checking → Counting

---

## **2️⃣ Outline**

- Read N
- Initialize count as 0
- Loop from 1 to N
- Check divisibility by 6 and 8
- Increase count
- Print count

---

## **3️⃣ Objective**

To count numbers divisible by **two conditions** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- multiple condition checking
- counting logic
- logical operators

---

## **5️⃣ Theory**

A number is divisible by **both 6 and 8** if:

- number % 6 == 0
- number % 8 == 0

Both conditions must be **true**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set `count = 0`
3. Loop from 1 to N
4. Check if number is divisible by 6 and 8
5. If yes, increase count
6. Print count

---

## **7️⃣ Method**

Use:

- for loop
- if condition
- modulo operator (%)

---

## **8️⃣ Constraints**

- N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Using OR instead of AND
❌ Forgetting to initialize count
❌ Printing inside loop

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

count = 0

for i in range(1, N + 1):
    if i % 6 == 0 and i % 8 == 0:
        count = count + 1

print(count)
```

---

## **1️⃣2️⃣ Example**

### Input

```
50
```

### Output

```
2
```

---

## **1️⃣3️⃣ Dry Run**

N = 50

Numbers divisible by 6 and 8:

- 24
- 48

Count = 2

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----: | ------ |
|    50 | 2      |
|    24 | 1      |
|   100 | 4      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Use **and** for multiple conditions
- Count increases only when condition is true
- Loop checks each number

---

## **1️⃣6️⃣ Real-Life Application**

- Filtering data
- Rule-based counting
- Validation systems

---

## **1️⃣7️⃣ Practice Questions**

1. Count numbers divisible by 4 and 6
2. Count numbers divisible by 3 or 5
3. Count numbers divisible by 12

---

## **1️⃣8️⃣ Result**

The program correctly prints the **count of numbers divisible by both 6 and 8**.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens **conditional logic and counting using loops**.

---
