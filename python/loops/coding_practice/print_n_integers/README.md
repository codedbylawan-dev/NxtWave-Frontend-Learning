# ✅ **Print N Integers**

---

## **1️⃣ Question**

Print numbers from **1 to N**, each on a new line.

---

## **1.5️⃣ Category**

Loops → While Loop → Counting

---

## **2️⃣ Outline**

- Read N
- Start counter at 1
- Print counter while counter ≤ N

---

## **3️⃣ Objective**

To practice forward counting using a while loop.

---

## **4️⃣ Purpose**

Strengthens loop understanding and incremental updates.

---

## **5️⃣ Theory**

If N = 5 → output should be:

```
1
2
3
4
5
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Set counter = 1
3. Check if counter ≤ N
4. Print counter
5. Increase counter
6. Repeat until counter > N

---

## **7️⃣ Method**

- integer input
- while loop
- counter increment

---

## **8️⃣ Constraints**

- N ≥ 1
- Must print exactly N lines

---

## **9️⃣ Common Mistakes**

❌ Starting counter at 0
❌ Using < instead of ≤
❌ Forgetting to increment counter

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
    print(counter)
    counter = counter + 1
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
2
3
```

---

## **1️⃣3️⃣ Dry Run**

N = 3
counter = 1 → print 1
counter = 2 → print 2
counter = 3 → print 3
counter = 4 → stop

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output        |
| ----- | ------------- |
| 1     | 1             |
| 4     | 1 2 3 4       |
| 7     | 1…7 (7 lines) |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- While loops repeat until condition becomes False
- Incrementing is essential

---

## **1️⃣6️⃣ Real-Life Application**

- Generating serial numbers
- Printing list indices
- Counting iterations

---

## **1️⃣7️⃣ Practice Questions**

1. Print numbers from N to 1
2. Print only even numbers from 1 to N
3. Print squares of numbers from 1 to N

---

## **1️⃣8️⃣ Result**

The program prints integers from 1 to N in order.

---

## **1️⃣9️⃣ Conclusion**

A direct counting problem reinforcing basic loop mechanics.

---
