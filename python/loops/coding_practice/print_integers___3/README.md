# ✅ **Print Integers – 3**

---

## **1️⃣ Question**

Given N, print integers from **N down to 1**, each on a new line.

---

## **1.5️⃣ Category**

While Loop → Reverse Counting

---

## **2️⃣ Outline**

- Read N
- Start counter at N
- Print counter
- Decrease counter
- Stop when counter reaches 1

---

## **3️⃣ Objective**

To practice reverse looping using while.

---

## **4️⃣ Purpose**

Understand decrementing loops.

---

## **5️⃣ Theory**

If N = 5 → Output:
5
4
3
2
1

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set counter = N
3. While counter ≥ 1
4. Print counter
5. Reduce counter by 1

---

## **7️⃣ Method**

Use a while loop with counter decreasing.

---

## **8️⃣ Constraints**

N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Forgetting to decrement counter
❌ Using `<=` instead of `>=`

---

## 🔟 Complexity

Time: O(N)
Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

count = N
while count >= 1:
    print(count)
    count = count - 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
3
```

Output:

```
3
2
1
```

---

## **1️⃣3️⃣ Dry Run**

N = 3
count = 3 → print 3 → count = 2
count = 2 → print 2 → count = 1
count = 1 → print 1 → count = 0 → stop

---

## **1️⃣4️⃣ Test Cases Table**

| N   | Output        |
| --- | ------------- |
| 1   | 1             |
| 4   | 4 3 2 1       |
| 7   | 7 6 5 4 3 2 1 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Reverse loop uses decrement
- Condition should be `>= 1`

---

## **1️⃣6️⃣ Real-Life Application**

- Countdown timers
- Reversing sequences

---

## **1️⃣7️⃣ Practice Questions**

1. Print numbers from N to 0
2. Print even numbers from N to 2
3. Print numbers from M to 1

---

## **1️⃣8️⃣ Result**

Program prints integers from N down to 1.

---

## **1️⃣9️⃣ Conclusion**

A simple reverse counting exercise using while.

---
