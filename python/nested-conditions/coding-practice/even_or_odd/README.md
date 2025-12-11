# ✅ **Even or Odd — Using Locked Format**

---

## **1️⃣ Question**

Given an integer **N**, determine whether it is **Even** or **Odd**.
If **N is divisible by 2**, print **"Even"**, otherwise print **"Odd"**.

---

## **1.5️⃣ Category**

Beginner → Conditional Statements → Modulus Operator

---

## **2️⃣ Outline**

- Read input N
- Compute `N % 2`
- If remainder = 0 → print "Even"
- Else → print "Odd"

---

## **3️⃣ Objective**

To classify a number as even or odd using the modulus operator and conditional statements.

---

## **4️⃣ Purpose**

This strengthens basic logic building, understanding of number properties, and foundational conditional programming skills.

---

## **5️⃣ Theory**

A number is:

- **Even** if divisible by 2
  [
  N % 2 = 0
  ]

- **Odd** if not divisible by 2
  [
  N % 2 = 1
  ]

Examples:

- `4 % 2 = 0` → Even
- `3 % 2 = 1` → Odd

---

## **6️⃣ Step-by-Step Explanation**

1. Read integer N
2. Find the remainder using `N % 2`
3. If remainder is 0 → print `"Even"`
4. Otherwise → print `"Odd"`

---

## **7️⃣ Method**

- Use `int(input())` to read N
- Apply modulo `%`
- Use if–else to produce correct classification

---

## **8️⃣ Constraints**

- Input is always an integer
- Output must match the exact words "Even" or "Odd"
- No extra spaces or lines

---

## **9️⃣ Common Mistakes**

❌ Using `/` instead of `%`
❌ Incorrect output text (case-sensitive)
❌ Forgetting to convert input to integer
❌ Printing additional text like "The answer is..."

---

## 🔟 Complexity

- **Time:** O(1)
- **Space:** O(1)

---

## 1️⃣1️⃣ Code

```python
N = int(input())

if N % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## 1️⃣2️⃣ Example

### **Input**

```
4
```

### **Output**

```
Even
```

---

## 1️⃣3️⃣ Dry Run

| Step | N   | Expression | Result | Output |
| ---- | --- | ---------- | ------ | ------ |
| 1    | 4   | 4 % 2      | 0      | Even   |
| 2    | 3   | 3 % 2      | 1      | Odd    |

---

## 1️⃣4️⃣ Test Cases Table

| N   | N % 2 | Output |
| --- | ----- | ------ |
| 4   | 0     | Even   |
| 3   | 1     | Odd    |
| 0   | 0     | Even   |
| 19  | 1     | Odd    |
| 22  | 0     | Even   |

---

## 1️⃣5️⃣ Notes/Key Takeaways

- `% 2` is the fastest way to check for even/odd
- Even numbers always end in 0, 2, 4, 6, 8
- Odd numbers always end in 1, 3, 5, 7, 9

---

## 1️⃣6️⃣ Real-Life Application

- Alternating patterns (e.g., distributing items)
- Identifying alternate turns in games
- Checking bit patterns in computer science
- Scheduling even/odd day rules

---

## 1️⃣7️⃣ Practice Questions

1. Check if a number is divisible by **3**
2. Print “Positive” or “Negative” based on input
3. Check if a number is divisible by **5 and 2**
4. Print "Odd" only if N is divisible by 3

---

## 1️⃣8️⃣ Result

The program correctly identifies a number as even or odd using modulus and condition checks.

---

## 1️⃣9️⃣ Conclusion

This foundational problem builds strong logic-handling skills. Understanding even/odd classification is a cornerstone for many future programming tasks involving loops, patterns, and algorithms.

---
