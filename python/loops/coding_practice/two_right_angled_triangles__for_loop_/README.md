# ✅ **Two Right Angled Triangles (For Loop)**

---

## **1️⃣ Question**

Given a number **N**, print **two Right Angled Triangles**, each of **N rows**, using **numbers starting from 1**.

---

## **1.5️⃣ Category**

For Loop → Pattern Printing → Number Patterns

---

## **2️⃣ Outline**

- Read N
- Print first right angled triangle
- Print second right angled triangle

---

## **3️⃣ Objective**

To print **two identical number triangles** using **simple for loops**.

---

## **4️⃣ Purpose**

This problem helps understand:

- for loop repetition
- printing patterns using numbers
- repeating logic without nesting loops

---

## **5️⃣ Theory**

If **N = 4**, output should be:

```
1
22
333
4444
1
22
333
4444
```

- First N rows → first triangle
- Next N rows → second triangle

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Loop from 1 to N → print first triangle
3. Loop again from 1 to N → print second triangle

---

## **7️⃣ Method**

Use:

- for loop
- number to string conversion
- string repetition

---

## **8️⃣ Constraints**

- N is a positive integer
- Output must contain exactly **2 × N lines**

---

## **9️⃣ Common Mistakes**

❌ Using nested loops
❌ Printing wrong number of rows
❌ Forgetting to repeat second triangle

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

for i in range(1, N + 1):
    print(str(i) * i)

for i in range(1, N + 1):
    print(str(i) * i)
```

---

## **1️⃣2️⃣ Example**

### Input

```
4
```

### Output

```
1
22
333
4444
1
22
333
4444
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

First loop prints:

```
1
22
333
```

Second loop prints:

```
1
22
333
```

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output Rows            |
| ----- | ---------------------- |
| 1     | 1, 1                   |
| 2     | 1, 22, 1, 22           |
| 3     | 1, 22, 333, 1, 22, 333 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Two simple loops = no nesting
- String repetition simplifies pattern printing
- Clear separation improves readability

---

## **1️⃣6️⃣ Real-Life Application**

- Repeating layouts
- Console formatting
- Pattern generation logic

---

## **1️⃣7️⃣ Practice Questions**

1. Print two star triangles
2. Print three number triangles
3. Print second triangle in reverse order

---

## **1️⃣8️⃣ Result**

The program correctly prints **two right angled number triangles**.

---

## **1️⃣9️⃣ Conclusion**

A clean for-loop pattern problem that avoids nesting and strengthens repetition logic.

---
