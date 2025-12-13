# ✅ **Divisible by 10 or 5**

---

## **1️⃣ Question**

Given a number **N**, print:

- **"Divisible by 10"** → if N is divisible by 10
- **"Divisible by 5"** → if N is divisible by 5 but **NOT** by 10
- **"Not Divisible by 10 or 5"** → if N is divisible by neither 5 nor 10

---

## **1.5️⃣ Category**

Divisibility → Conditional Logic → Arithmetic

---

## **2️⃣ Outline**

- Read N
- Check divisible by 10
- Else check divisible by 5
- Else print not divisible

---

## **3️⃣ Objective**

To determine divisibility using `%` and prioritize correct conditions.

---

## **4️⃣ Purpose**

Strengthens understanding of nested/multi-step conditions and modulus operations.

---

## **5️⃣ Theory**

A number is:

- Divisible by 10 if → `N % 10 == 0`
- Divisible by 5 if → `N % 5 == 0`
- Divisible by 10 always implies divisible by 5, so order **matters**.

Hence:

1. Check **divisible by 10** first
2. Then check **divisible by 5**
3. Else → not divisible

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. If N % 10 == 0 → print "Divisible by 10"
3. Else if N % 5 == 0 → print "Divisible by 5"
4. Else → print "Not Divisible by 10 or 5"

---

## **7️⃣ Method**

- Use modulus operator `%`
- Use ordered if–elif–else

---

## **8️⃣ Constraints**

- N is an integer
- Only one line of output allowed
- Exact string format required

---

## **9️⃣ Common Mistakes**

❌ Checking divisible by 5 before 10 (wrong priority)
❌ Forgetting that divisible by 10 already includes divisible by 5
❌ Printing wrong text or wrong casing

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

if N % 10 == 0:
    print("Divisible by 10")
elif N % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 10 or 5")
```

---

## **1️⃣2️⃣ Example**

### Input

```
15
```

### Output

```
Divisible by 5
```

---

## **1️⃣3️⃣ Dry Run**

| N   | N % 10 | N % 5 | Output                   |
| --- | ------ | ----- | ------------------------ |
| 15  | 5      | 0     | Divisible by 5           |
| 10  | 0      | 0     | Divisible by 10          |
| 7   | 7      | 2     | Not Divisible by 10 or 5 |
| 5   | 5      | 0     | Divisible by 5           |
| 20  | 0      | 0     | Divisible by 10          |

---

## **1️⃣4️⃣ Test Cases Table**

| N   | Output                       |
| --- | ---------------------------- |
| 15  | Divisible by 5               |
| 10  | Divisible by 10              |
| 5   | Divisible by 5               |
| 11  | Not Divisible by 10 or 5     |
| 0   | Divisible by 10 (0 % 10 = 0) |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Always check higher-priority conditions first
- `%` operator is fundamental for divisibility checks
- 10 is a multiple of 5 → order of checks is critical

---

## **1️⃣6️⃣ Real-Life Application**

- Validating denominations (coins/notes)
- Checking periodic events (every 5 or 10 intervals)
- Filtering data based on divisibility rules

---

## **1️⃣7️⃣ Practice Questions**

1. Print if a number is divisible by 4, 6, or both.
2. Print “Fizz”, “Buzz”, “FizzBuzz” logic for 3 and 5.
3. Check if a number is divisible by 2, 5, and 10.

---

## **1️⃣8️⃣ Result**

The program correctly prints whether N is divisible by 10, divisible by 5, or neither.

---

## **1️⃣9️⃣ Conclusion**

A clean and essential exercise in conditional priority and divisibility logic—perfect for building strong foundational programming instincts.

---
