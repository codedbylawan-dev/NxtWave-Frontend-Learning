# ✅ **First N Natural Numbers**

---

## **1️⃣ Question**

Given a number **N**, print the first **N natural numbers** starting from 1.

---

## **1.5️⃣ Category**

Loops → While Loop → Counting Sequence

---

## **2️⃣ Outline**

- Read N
- Start counter at 1
- Print numbers from 1 to N

---

## **3️⃣ Objective**

To generate a natural number sequence using a loop.

---

## **4️⃣ Purpose**

Build confidence in sequential counting with while loops.

---

## **5️⃣ Theory**

Natural numbers start from **1, 2, 3, ...**

So for N = 5 → output:

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
3. While counter ≤ N
4. Print counter
5. Increase counter by 1

---

## **7️⃣ Method**

- Integer input
- While loop
- Counter increment

---

## **8️⃣ Constraints**

- N ≥ 1
- Print exactly N lines

---

## **9️⃣ Common Mistakes**

❌ Using < instead of ≤
❌ Forgetting to increment counter
❌ Starting counter at 0

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
| 7     | 1 2 3 4 5 6 7 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Natural numbers always start at 1
- While loop is perfect for repeated counting

---

## **1️⃣6️⃣ Real-Life Application**

- Ticket numbering
- Serial number generation
- Counting items

---

## **1️⃣7️⃣ Practice Questions**

1. Print natural numbers from N to 1
2. Print even natural numbers up to N
3. Print squares of natural numbers up to N

---

## **1️⃣8️⃣ Result**

Program prints the first N natural numbers starting from 1.

---

## **1️⃣9️⃣ Conclusion**

A simple loop problem reinforcing incremental counting.

---
