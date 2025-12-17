# ✅ **Count of Numbers Divisible by 2 and 3**

---

## **1️⃣ Question**

Given a number **N**, print the **count** of numbers from **1 to N** that are divisible by **both 2 and 3**.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Check → Counting

---

## **2️⃣ Outline**

- Read N
- Initialize count to 0
- Loop from 1 to N
- Check divisibility by 2 and 3
- Increase count when condition is true
- Print count

---

## **3️⃣ Objective**

To **count** numbers that satisfy **multiple conditions** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- counting logic
- condition-based increment
- using variables with loops

---

## **5️⃣ Theory**

A number divisible by **both 2 and 3** satisfies:

```
number % 2 == 0 and number % 3 == 0
```

Each time this condition is true, the counter is increased by 1.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the number N
2. Create a variable `count` and set it to 0
3. Loop from 1 to N
4. Check if the number is divisible by both 2 and 3
5. If yes, increase `count` by 1
6. After the loop, print `count`

---

## **7️⃣ Method**

Use:

- input()
- for loop
- if condition with `and`
- counter variable

---

## **8️⃣ Constraints**

- N is a positive integer

---

## **9️⃣ Common Mistakes**

❌ Forgetting to initialize count
❌ Using `or` instead of `and`
❌ Printing numbers instead of count

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
    if i % 2 == 0 and i % 3 == 0:
        count = count + 1

print(count)
```

---

## **1️⃣2️⃣ Example**

### Input

```
12
```

### Output

```
2
```

---

## **1️⃣3️⃣ Dry Run**

N = 12

Divisible by both 2 and 3:

- 6 → count = 1
- 12 → count = 2

Final output → `2`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----: | ------ |
|     6 | 1      |
|    12 | 2      |
|     5 | 0      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Use a counter for counting problems
- Increment only when condition is true
- Logical `and` ensures both conditions

---

## **1️⃣6️⃣ Real-Life Application**

- Counting eligible users
- Filtering valid entries
- Data analysis conditions

---

## **1️⃣7️⃣ Practice Questions**

1. Count numbers divisible by 4
2. Count numbers divisible by 3 or 5
3. Count even numbers from 1 to N

---

## **1️⃣8️⃣ Result**

The program correctly prints the **count of numbers divisible by both 2 and 3**.

---

## **1️⃣9️⃣ Conclusion**

A clean counting problem that strengthens **loop + condition + counter** logic.

---
