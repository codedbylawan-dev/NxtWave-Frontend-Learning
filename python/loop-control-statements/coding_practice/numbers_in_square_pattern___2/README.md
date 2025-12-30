# 🧩 **Numbers in Square Pattern – 2**

---

## **1️⃣ Question**

Given a number **N**, print numbers from **1 to N** in each row such that:

- The pattern contains **N rows**
- Each row contains the **same number repeated N times**

---

## **2️⃣ Category**

**Loops → Pattern Printing → Number Patterns**

---

## **3️⃣ Outline**

- Read integer **N**
- Start with number `1`
- For each number from `1` to `N`:

  - Print that number **N times**
  - Move to the next line

---

## **4️⃣ Objective**

Understand how a **loop controls rows** and how repeating values builds a **2D pattern**.

---

## **5️⃣ Purpose**

This problem strengthens:

- Loop control
- Pattern visualization
- Structured thinking in rows & columns

---

## **6️⃣ Theory**

Each row prints the **row number** repeatedly.

Example when `N = 5`:

```
1 printed 5 times
2 printed 5 times
3 printed 5 times
4 printed 5 times
5 printed 5 times
```

---

## **7️⃣ Step-by-Step Explanation**

1. Read **N**
2. Set variable `num = 1`
3. Run a loop while `num <= N`
4. Inside the loop:

   - Print `num` exactly `N` times on the same line
   - Move to next line
   - Increase `num` by `1`

---

## **8️⃣ Method**

Single loop + string repetition + controlled printing

---

## **9️⃣ Constraints**

- Exactly **N rows**
- Exactly **N numbers per row**
- Space after every number

---

## **🔟 Common Mistakes**

- Printing wrong count of numbers
- Forgetting spaces
- Printing all numbers in one line

---

## **1️⃣1️⃣ Complexity**

- **Time:** `O(N²)`
- **Space:** `O(1)`

---

## **1️⃣2️⃣ Code**

```python
n = int(input())

num = 1

while num <= n:
    print((str(num) + " ") * n)
    num = num + 1
```

---

## **1️⃣3️⃣ Example**

### Input

```
4
```

### Output

```
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4
```

---

## **1️⃣4️⃣ Dry Run**

For `n = 3`

| num | Printed Line |
| --- | ------------ |
| 1   | 1 1 1        |
| 2   | 2 2 2        |
| 3   | 3 3 3        |

---

## **1️⃣5️⃣ Test Cases Table**

| Input | Output                    |
| ----- | ------------------------- |
| 3     | 1 1 1 / 2 2 2 / 3 3 3     |
| 5     | 1 1 1 1 1 / … / 5 5 5 5 5 |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- Patterns are controlled by **row logic**
- Repetition builds columns
- You are now thinking in **2D structure**

---

## **1️⃣7️⃣ Real-Life Application**

Used in:

- Grid creation
- Table generation
- Matrix-like data formatting

---

## **1️⃣8️⃣ Practice Questions**

1. Print reverse square
2. Print only even rows
3. Print numbers from N to 1

---

## **1️⃣9️⃣ Result**

You can now build **numeric square patterns** using disciplined logic.

---

## **2️⃣0️⃣ Conclusion**

This problem proves you can translate a visual structure into working code.

---
