# ✅ **Count of Numbers Divisible by T**

---

## **1️⃣ Question**

Given two integers **N** and **T**, print the **count of numbers from 1 to N** that are divisible by **T**.

---

## **1️⃣.5️⃣ Category**

For Loop → Conditional Check → Counting

---

## **2️⃣ Outline**

- Read N
- Read T
- Initialize count
- Loop from 1 to N
- Check divisibility by T
- Increase count
- Print count

---

## **3️⃣ Objective**

To count values that satisfy a **divisibility condition** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- looping through a range
- conditional checks
- counting occurrences

---

## **5️⃣ Theory**

A number is divisible by **T** if:

```
number % T == 0
```

Each time this condition is true, increase the count by 1.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N and T
2. Set `count = 0`
3. Loop from 1 to N
4. If a number is divisible by T, increment count
5. After the loop, print count

---

## **7️⃣ Method**

Use:

- input()
- for loop
- if condition
- counter variable

---

## **8️⃣ Constraints**

- N is a positive integer
- T is a positive integer

---

## **9️⃣ Common Mistakes**

❌ Forgetting to initialize count
❌ Using wrong loop range
❌ Printing numbers instead of counting

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())
T = int(input())

count = 0

for i in range(1, N + 1):
    if i % T == 0:
        count = count + 1

print(count)
```

---

## **1️⃣2️⃣ Example**

### Input

```
12
3
```

### Output

```
4
```

---

## **1️⃣3️⃣ Dry Run**

N = 12, T = 3

Divisible numbers → 3, 6, 9, 12
Count → 4

---

## **1️⃣4️⃣ Test Cases Table**

| N   | T   | Output |
| --- | --- | ------ |
| 10  | 2   | 5      |
| 12  | 3   | 4      |
| 5   | 7   | 0      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Counter must start at 0
- `%` operator filters values
- Loop runs from 1 to N

---

## **1️⃣6️⃣ Real-Life Application**

- Counting valid entries
- Frequency calculation
- Data filtering

---

## **1️⃣7️⃣ Practice Questions**

1. Count numbers divisible by 5 from 1 to N
2. Count even numbers from 1 to N
3. Count numbers divisible by both 2 and 3

---

## **1️⃣8️⃣ Result**

The program correctly prints the **count of numbers divisible by T**.

---

## **1️⃣9️⃣ Conclusion**

A clear example of **counting with conditions using for loops**.

---
