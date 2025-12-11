# ✅ **Greatest Among Remainders**

---

## **1️⃣ Question**

Given an integer **N**, compute:

- The remainder when N is divided by 4
- The remainder when N is divided by 5

Print the **greatest remainder** among the two.

---

## **1.5️⃣ Category**

Beginner → Arithmetic → Modulus + If–Else Comparison

---

## **2️⃣ Outline**

- Read N
- Calculate `rem4 = N % 4`
- Calculate `rem5 = N % 5`
- Compare the two using if–else
- Print the greater one

---

## **3️⃣ Objective**

To compute two remainders and determine which remainder is larger.

---

## **4️⃣ Purpose**

To practice remainder operations and comparison using simple if–else logic.

---

## **5️⃣ Theory**

- `N % 4` gives remainder when N is divided by 4
- `N % 5` gives remainder when N is divided by 5
- Remainders are small numbers:

  - For division by 4 → 0 to 3
  - For division by 5 → 0 to 4

If `rem4 > rem5` → rem4 is greatest
Else → rem5 is greatest

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Compute `rem4 = N % 4`
3. Compute `rem5 = N % 5`
4. Compare:

   - If rem4 is greater → print rem4
   - Else → print rem5

---

## **7️⃣ Method**

- Use `%` operator
- Use simple if–else comparison
- Print only one number

---

## **8️⃣ Constraints**

- N is an integer
- Output must be exactly 1 line
- No advanced functions allowed (since not learned yet)

---

## **9️⃣ Common Mistakes**

❌ Using quotient instead of remainder
❌ Printing both remainders
❌ Using advanced functions not learned yet
❌ Wrong comparison direction

---

## 🔟 Complexity

- **Time:** O(1)
- **Space:** O(1)

---

## 1️⃣1️⃣ Code

(Uses only concepts you have learned)

```python
N = int(input())

rem4 = N % 4
rem5 = N % 5

if rem4 > rem5:
    print(rem4)
else:
    print(rem5)
```

---

## 1️⃣2️⃣ Example

### **Input**

```
12
```

### **Output**

```
2
```

---

## 1️⃣3️⃣ Dry Run

| Step | N   | rem4 = N%4 | rem5 = N%5 | Comparison    | Output |
| ---- | --- | ---------- | ---------- | ------------- | ------ |
| 1    | 12  | 0          | 2          | 0 > 2 → False | 2      |

---

## 1️⃣4️⃣ Test Cases Table

| N   | N % 4 | N % 5 | Greatest |
| --- | ----- | ----- | -------- |
| 12  | 0     | 2     | 2        |
| 147 | 3     | 2     | 3        |
| 9   | 1     | 4     | 4        |
| 20  | 0     | 0     | 0        |
| 33  | 1     | 3     | 3        |

---

## 1️⃣5️⃣ Notes/Key Takeaways

- `%` gives small values easy to compare
- If–else is enough to find larger value
- No need for advanced functions

---

## 1️⃣6️⃣ Real-Life Application

- Finding which leftover is bigger in packaging
- Comparing two remainder-based systems
- Scheduling tasks in cycles (4-day vs 5-day)

---

## 1️⃣7️⃣ Practice Questions

1. Print the **smaller** remainder of `N % 3` and `N % 4`.
2. Check if remainder of `N % 6` is greater than `N % 2`.
3. Read N and print `"Yes"` if `N % 5 > N % 3`, else `"No"`.

---

## 1️⃣8️⃣ Result

You successfully used modulus and if–else (already learned concepts) to find the greatest remainder.

---

## 1️⃣9️⃣ Conclusion

This problem strengthens your understanding of basic arithmetic and comparison logic. It stays fully within the concepts you have already mastered — no new tools required.

---
