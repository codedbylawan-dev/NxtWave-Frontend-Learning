# ✅ **Print Integers – 2**

---

## **1️⃣ Question**

Given two integers **M** and **N**, print all integers starting from **M** up to **N**, each on a new line.

---

## **1.5️⃣ Category**

Loops → While Loop → Counting Range

---

## **2️⃣ Outline**

- Read M
- Read N
- Start from M
- Print numbers until N

---

## **3️⃣ Objective**

To print all integers in a continuous range using a while loop.

---

## **4️⃣ Purpose**

Strengthens understanding of increasing a counter based on start–end inputs.

---

## **5️⃣ Theory**

If M = 2 and N = 6:

```
2
3
4
5
6
```

If M = -2 and N = 2:

```
-2
-1
0
1
2
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read M
2. Read N
3. Set counter to M
4. While counter ≤ N
5. Print counter
6. Increase counter by 1

---

## **7️⃣ Method**

- Use while loop
- Increment counter each step

---

## **8️⃣ Constraints**

- M ≤ N
- Output must print each integer on a new line

---

## **9️⃣ Common Mistakes**

❌ Using `<` instead of `<=`
❌ Not incrementing → infinite loop
❌ Starting from the wrong number

---

## 🔟 Complexity

Time → O(N − M + 1)
Space → O(1)

---

## **1️⃣1️⃣ Code**

```python
M = int(input())
N = int(input())

counter = M
while counter <= N:
    print(counter)
    counter = counter + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
2
6
```

Output:

```
2
3
4
5
6
```

---

## **1️⃣3️⃣ Dry Run**

M = -2, N = 2
counter = -2 → print
counter = -1 → print
counter = 0 → print
counter = 1 → print
counter = 2 → print → stop

---

## **1️⃣4️⃣ Test Cases Table**

| M   | N   | Output Range |
| --- | --- | ------------ |
| 1   | 3   | 1 2 3        |
| -2  | 2   | -2 -1 0 1 2  |
| 5   | 5   | 5            |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Range printing always requires a counter
- Condition must include the ending value

---

## **1️⃣6️⃣ Real-Life Application**

- Printing roll numbers
- Listing days between two dates (basic idea)
- Number sequences in reports

---

## **1️⃣7️⃣ Practice Questions**

1. Print numbers from N to M (reverse order)
2. Print all even numbers between M and N
3. Print squares from M to N

---

## **1️⃣8️⃣ Result**

Program correctly prints all integers from M to N.

---

## **1️⃣9️⃣ Conclusion**

This problem reinforces loop-based counting between two boundaries.

---
