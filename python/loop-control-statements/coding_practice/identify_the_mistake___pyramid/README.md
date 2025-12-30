# 🧩 **Identify The Mistake – Pyramid**

---

## **1️⃣ Question**

Given a number **N**, print the following pattern:

```
  *
 * *
* * *
```

(Example when `N = 3`)

---

## **2️⃣ Category**

**Loops → Pattern Printing**

---

## **3️⃣ Outline**

- Read **N**
- Set `spaces = N - 1`, `stars = 1`
- Repeat **N** times:

  - Print `spaces` spaces
  - Print `stars` stars
  - Update:
    `spaces -= 1`, `stars += 1`

---

## **4️⃣ Objective**

Learn how to build aligned patterns using **only counters and loops**.

---

## **5️⃣ Purpose**

This strengthens:

- Visual logic
- Loop control
- Step-based thinking

---

## **6️⃣ Theory**

Every row is controlled by two values:

| Row | Spaces | Stars |
| --- | ------ | ----- |
| 1   | N-1    | 1     |
| 2   | N-2    | 2     |
| 3   | N-3    | 3     |
| …   | …      | …     |

Pattern grows by **moving left** while **growing width**.

---

## **7️⃣ Step-by-Step Explanation**

1. Input **N**
2. Initialize counters
   `spaces = N - 1`
   `stars = 1`
3. Loop **N** times:

   - Print spaces
   - Print stars
   - Decrease spaces
   - Increase stars

---

## **8️⃣ Method**

Single `for` loop with two counters.

---

## **9️⃣ Constraints**

- Exactly **N rows**
- One space after every `*`
- No extra characters

---

## **🔟 Common Mistakes**

- Forgetting to reduce spaces
- Increasing stars incorrectly
- Missing space after `*`

---

## **1️⃣1️⃣ Complexity**

- **Time:** `O(N²)`
- **Space:** `O(1)`

---

## **1️⃣2️⃣ Code**

```python
n = int(input())

spaces = n - 1
stars = 1

for i in range(n):
    print(" " * spaces + "* " * stars)
    spaces = spaces - 1
    stars = stars + 1
```

---

## **1️⃣3️⃣ Example**

**Input**

```
3
```

**Output**

```
  *
 * *
* * *
```

---

## **1️⃣4️⃣ Dry Run**

| Iteration | spaces | stars | Output  |
| --------- | ------ | ----- | ------- |
| 1         | 2      | 1     | `  *`   |
| 2         | 1      | 2     | ` * *`  |
| 3         | 0      | 3     | `* * *` |

---

## **1️⃣5️⃣ Test Cases Table**

| N   | Output Shape |
| --- | ------------ |
| 3   | 3 rows       |
| 5   | 5 rows       |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- Counters control the entire shape
- Spacing creates alignment
- Patterns = logic + repetition

---

## **1️⃣7️⃣ Real-Life Application**

Used in:

- UI alignment engines
- Console UI builders
- Grid rendering

---

## **1️⃣8️⃣ Practice Questions**

1. Print the same pattern upside down
2. Print using decreasing stars
3. Print with numbers instead of stars

---

## **1️⃣9️⃣ Result**

You now **command pattern alignment** using pure logic.

---

## **2️⃣0️⃣ Conclusion**

This problem completes your understanding of
**space–star coordination**.

You are officially past beginner patterns.

---
