# 🧩 **Count of Zeroes**

---

## **1️⃣ Question**

Given an integer **N**, find how many `0` digits are present in it.

If the count is **more than 3**, print:

```
Count of zeroes is greater than three
```

Otherwise, print:

```
Count of zeroes is not greater than three
```

---

## **2️⃣ Category**

**Numbers → Digit Processing → Conditional Logic**

---

## **3️⃣ Outline**

- Read number **N** as string
- Initialize `count = 0`
- Traverse each digit
- If digit is `'0'`, increase `count`
- If `count > 3` print required message
- Else print other message

---

## **4️⃣ Objective**

Learn how to **analyze digits** of a number using string traversal.

---

## **5️⃣ Purpose**

This builds:

- Digit scanning logic
- Conditional decision making
- Counter-based problem solving

---

## **6️⃣ Theory**

Numbers can be treated as strings to easily examine each digit.

---

## **7️⃣ Step-by-Step Explanation**

1. Read input as string `n`
2. Set `count = 0`
3. For each character in `n`:

   - If it equals `'0'`, increment `count`

4. Check if `count > 3`
5. Print result accordingly

---

## **8️⃣ Method**

Single loop + counter + condition.

---

## **9️⃣ Constraints**

- Input may contain leading zeroes
- Count only the character `'0'`

---

## **🔟 Common Mistakes**

- Reading input as int and losing leading zeroes
- Forgetting to compare as character `'0'`
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
    if ch == '0':
        count += 1

if count > 3:
    print("Count of zeroes is greater than three")
else:
    print("Count of zeroes is not greater than three")
```

---

## **1️⃣3️⃣ Example**

### Input

```
1030800
```

### Output

```
Count of zeroes is greater than three
```

---

## **1️⃣4️⃣ Dry Run**

For `1030800`

Digits → 1 0 3 0 8 0 0
Zero count → 4
4 > 3 → True → Print first message

---

## **1️⃣5️⃣ Test Cases Table**

| Input   | Zero Count | Output                 |
| ------- | ---------- | ---------------------- |
| 1030800 | 4          | greater than three     |
| 84020   | 2          | not greater than three |
| 00000   | 5          | greater than three     |

---

## **1️⃣6️⃣ Notes / Key Takeaways**

- Convert numbers to strings to inspect digits
- Counting patterns appear everywhere in programming
- Conditionals decide program behavior

---

## **1️⃣7️⃣ Real-Life Application**

Used in:

- Data validation
- Error detection
- Number analysis

---

## **1️⃣8️⃣ Practice Questions**

1. Count digits greater than 5
2. Count odd digits
3. Count zeros and ones separately

---

## **1️⃣9️⃣ Result**

You can now **analyze and classify digits** programmatically.

---

## **2️⃣0️⃣ Conclusion**

This problem trains your brain for **data inspection tasks**, a core backend skill.

---
