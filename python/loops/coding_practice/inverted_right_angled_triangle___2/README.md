# ✅ **Inverted Right Angled Triangle – 2**

---

## **1️⃣ Question**

Given a number **N**, print an **Inverted Right Angled Triangle** of **N rows** using **numbers**.

> There is a **space after every number**.

---

## **1️⃣.5️⃣ Category**

For Loop → Pattern Printing → Reverse Order (Numbers)

---

## **2️⃣ Outline**

- Read N
- First row prints N numbers
- Each next row prints one less number
- Values decrease from N to 1 (row-wise)

---

## **3️⃣ Objective**

To print an **inverted triangle pattern using numbers** with a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- reverse looping
- number-based patterns
- row-wise value control

---

## **5️⃣ Theory**

In an inverted number triangle:

- Row 1 → N printed **N times**
- Row 2 → N−1 printed **N−1 times**
- …
- Last row → 1 printed once

Example for **N = 4**:

```
4 4 4 4
3 3 3
2 2
1
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Start loop from N down to 1
3. In each row:

   - Print the current number, repeated same number of times

4. Move to next row with reduced count

---

## **7️⃣ Method**

Use:

- input()
- for loop
- string repetition
- print()

---

## **8️⃣ Constraints**

- N is a positive integer
- Space after every number
- Exactly N rows must be printed

---

## **9️⃣ Common Mistakes**

❌ Printing numbers in increasing order
❌ Missing space after numbers
❌ Using wrong loop direction

---

## **🔟 Complexity**

Time: **O(N²)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(N, 0, -1):
    print((str(i) + " ") * i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
4 4 4 4
3 3 3
2 2
1
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

Loop values: 3 → 1

- i = 3 → `3 3 3`
- i = 2 → `2 2`
- i = 1 → `1`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Rows |
| ----- | ----------- |
| 1     | `1`         |
| 3     | 3 rows      |
| 5     | 5 rows      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Reverse loop controls pattern shape
- Same number printed multiple times per row
- String repetition avoids nested loops

---

## **1️⃣6️⃣ Real-Life Application**

- Console formatting
- Pattern-based logic practice
- Understanding reverse data flow

---

## **1️⃣7️⃣ Practice Questions**

1. Print inverted triangle using stars
2. Print inverted triangle using `+`
3. Print triangle from N to 2

---

## **1️⃣8️⃣ Result**

The program correctly prints an **Inverted Right Angled Triangle using numbers**.

---

## **1️⃣9️⃣ Conclusion**

A strong pattern problem that reinforces **reverse looping and repetition logic** using only learned concepts.
