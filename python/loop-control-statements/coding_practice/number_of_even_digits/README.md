# 🧩 **Number of Even Digits**

---

## **1️⃣ Question**

Given an integer **N**, find how many **even digits** are present in it.

If the count is **more than 2**, print:

```
Count of even digits is greater than two
```

Otherwise, print:

```
Count of even digits is not greater than two
```

---

## **2️⃣ Category**

**Numbers → Digit Processing → Conditional Logic**

---

## **3️⃣ Outline**

- Read **N** as string
- Initialize `count = 0`
- Traverse each digit
- If digit is even, increase `count`
- Check if `count > 2`
- Print result

---

## **4️⃣ Objective**

Strengthen **digit analysis** and **rule-based decisions**.

---

## **5️⃣ Purpose**

This builds:

- Logical filtering
- Counter control
- Real-world validation skills

---

## **6️⃣ Theory**

A digit is even if `digit % 2 == 0`.
Processing as a string allows easy access to each digit.

---

## **7️⃣ Step-by-Step Explanation**

1. Read input as string
2. Set `count = 0`
3. For each character:

   - Convert to integer
   - If even, increment `count`

4. Compare `count` with `2`
5. Print corresponding message

---

## **8️⃣ Method**

Single loop + numeric check + condition.

---

## **9️⃣ Constraints**

- Input may be very large
- Must inspect every digit

---

## **🔟 Common Mistakes**

- Forgetting to convert character to integer
- Checking only last digit
- Printing wrong message formatting

---

## **1️⃣1️⃣ Complexity**

- **Time:** `O(N)`
- **Space:** `O(1)`

---

## **1️⃣2️⃣ Code**

```python
n = input()

count = 0

for ch in n:
    digit = int(ch)
    if digit % 2 == 0:
        count += 1

if count > 2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")
```

---

## **1️⃣3️⃣ Example**

### Input

```
2563408
```

### Output

```
Count of even digits is greater than two
```

---

## **1️⃣4️⃣ Dry Run**

Digits → 2 5 6 3 4 0 8
Even digits → 2, 6, 4, 0, 8
Count → 5
5 > 2 → True

---

## **1️⃣5️⃣ Test Cases Table**

| Input   | Even Count | Output               |
| ------- | ---------- | -------------------- |
| 2563408 | 5          | greater than two     |
| 32      | 2          | not greater than two |
| 101     | 1          | not greater than two |
| 888     | 3          | greater than two     |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- Digit scanning is a core programming skill
- Counting + condition = decision engine
- You just wrote reusable validation logic

---

## **1️⃣7️⃣ Real-Life Application**

Used in:

- Credit card validation
- Phone number analysis
- Data verification pipelines

---

## **1️⃣8️⃣ Practice Questions**

1. Count odd digits
2. Count digits divisible by 3
3. Count digits greater than 5

---

## **1️⃣9️⃣ Result**

You now control **digit-level validation** with confidence.

---

## **2️⃣0️⃣ Conclusion**

This is how software thinks: inspect → measure → decide.

---
