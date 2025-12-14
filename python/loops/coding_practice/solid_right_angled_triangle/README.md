# ✅ **Solid Right Angled Triangle**

---

## **1️⃣ Question**

Print a right-angled triangle of `N` lines using `*`.

---

## **2️⃣ Outline**

- Read N
- Use a counter
- For each line, print `"* "` repeated counter times

---

## **3️⃣ Objective**

To generate a growing pattern using repetition.

---

## **4️⃣ Purpose**

Strengthens control flow + string repetition understanding.

---

## **5️⃣ Theory**

If N = 4, print:

```
*
* *
* * *
* * * *
```

Each row contains `"* "` repeated row_number times.

---

## **6️⃣ Step-by-Step Explanation**

1. Start counter at 1
2. Print `"* " * counter`
3. Increase counter
4. Repeat until N lines printed

---

## **7️⃣ Method**

- While loop
- String repetition (`"* " * count`)

---

## **8️⃣ Constraints**

- Only 1 loop
- Space after each `*`

---

## **9️⃣ Common Mistakes**

❌ Missing trailing space
❌ Using nested loops (not allowed for you yet)
❌ Forgetting to increment counter

---

## 🔟 Complexity

Time → O(N)
Space → O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

count = 1
while count <= N:
    print("* " * count)
    count = count + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
4
```

Output:

```
*
* *
* * *
* * * *
```

---

## **1️⃣3️⃣ Dry Run**

N = 2
count = 1 → print "_ "
count = 2 → print "_ \* "

---

## **1️⃣4️⃣ Test Cases**

| Input | Output          |
| ----- | --------------- |
| 1     | \*              |
| 3     | _, _ _, _ \* \* |
| 5     | 5-line triangle |

---

## **1️⃣5️⃣ Notes**

String repetition avoids nested loops.

---

## **1️⃣6️⃣ Practice**

Try printing a reverse triangle.

---

## **1️⃣7️⃣ Result**

Triangle printed correctly using only one loop.

---

## **1️⃣8️⃣ Conclusion**

A great exercise to practice loops + string multiplication.

---
