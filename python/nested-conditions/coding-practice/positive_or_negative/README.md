# ✅ **Positive or Negative**

---

## **1️⃣ Question**

Read a float number **N** and determine:

- Print **"Positive"** if **N > 0**
- Print **"Negative"** if **N < 0**

The value of **N will never be 0** (given by constraints).

---

## **1.5️⃣ Category**

Basic Comparison → Sign Check → Float Input

---

## **2️⃣ Outline**

- Read N as float
- Compare N with 0
- Print Positive or Negative accordingly

---

## **3️⃣ Objective**

To classify a number based on its sign.

---

## **4️⃣ Purpose**

This develops fundamental comparison logic applicable to real-life numeric evaluations.

---

## **5️⃣ Theory**

A number can only be:

[
N > 0 \Rightarrow \text{Positive}
]
[
N < 0 \Rightarrow \text{Negative}
]

Since N ≠ 0, no equality case is needed.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the float input
2. If the number is greater than 0 → print Positive
3. Else (must be less than 0) → print Negative

---

## **7️⃣ Method**

- Use `float(input())`
- Compare with 0
- Print only one correct output

---

## **8️⃣ Constraints**

- N is not equal to 0
- Output must match exact capitalization
- Float values must be handled correctly

---

## **9️⃣ Common Mistakes**

❌ Using int() instead of float()
❌ Checking equality with 0 even though not needed
❌ Printing “positive” instead of **Positive**

---

## 🔟 Complexity

- Time: O(1)
- Space: O(1)

---

## **1️⃣1️⃣ Code**

```python
N = float(input())

if N > 0:
    print("Positive")
else:
    print("Negative")
```

---

## **1️⃣2️⃣ Example**

### Input

```
-12.5
```

### Output

```
Negative
```

---

## **1️⃣3️⃣ Dry Run**

| N     | Condition | Output   |
| ----- | --------- | -------- |
| -12.5 | N < 0     | Negative |
| 15.2  | N > 0     | Positive |
| -0.1  | N < 0     | Negative |
| 0.9   | N > 0     | Positive |

---

## **1️⃣4️⃣ Test Cases Table**

| N     | Output   |
| ----- | -------- |
| -12.5 | Negative |
| 15.2  | Positive |
| -1.0  | Negative |
| 3.14  | Positive |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Floats work the same as integers in comparisons
- Only sign matters here
- No need to handle zero case

---

## **1️⃣6️⃣ Real-Life Application**

- Temperature sensors (negative/positive temperature)
- Finance (profit vs loss)
- Physics simulations (direction values)

---

## **1️⃣7️⃣ Practice Questions**

1. Print whether a number is positive, negative, or zero.
2. Print if a float number is closer to +10 or -10.
3. Classify a value as gain/loss/neutral.

---

## **1️⃣8️⃣ Result**

The program correctly prints whether the number is Positive or Negative.

---

## **1️⃣9️⃣ Conclusion**

A fundamental but essential comparison exercise — perfect for strengthening basic logical reasoning in programming.

---
