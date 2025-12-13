# ✅ **Print the Value**

---

## **1️⃣ Question**

You are given a string **S** where:

- All characters **except the last one** form a **number**
- The **last character** is one of:

| Last Character | Meaning   | Multiply By |
| -------------- | --------- | ----------- |
| T              | Tens      | 10          |
| H              | Hundreds  | 100         |
| K              | Thousands | 1000        |

You must extract the number and multiply it based on the final character.

---

## **1.5️⃣ Category**

String Handling → Indexing → Type Conversion → Arithmetic

---

## **2️⃣ Outline**

- Read the string
- Separate number part and last character
- Convert number part to integer
- Check last character
- Multiply accordingly
- Print result

---

## **3️⃣ Objective**

To extract values from mixed strings and apply logic based on the last character.

---

## **4️⃣ Purpose**

This strengthens your skills in slicing, type conversion, and conditional logic.

---

## **5️⃣ Theory**

For a string like `"34T"`:

- Number part → `"34"`
- Last character → `"T"`
- `"T"` means multiply by **10**
- Output: **340**

General rule:

[
\text{value} = \text{number} \times \text{multiplier}
]

---

## **6️⃣ Step-by-Step Explanation**

1. Read the string
2. Extract last character → `S[-1]`
3. Extract the number part → `S[:-1]`
4. Convert number to int
5. If last char is `"T"` → multiply by 10
6. If `"H"` → multiply by 100
7. If `"K"` → multiply by 1000
8. Print result

---

## **7️⃣ Method**

Use:

- Slicing
- `int()`
- `if–elif–else`

---

## **8️⃣ Constraints**

- Last character is always T, H, or K
- Number part is always a valid integer
- Output must be integer

---

## **9️⃣ Common Mistakes**

❌ Forgetting to slice last character
❌ Including last character inside `int()` → error
❌ Printing wrong multiplier
❌ Case sensitivity (characters must match exactly)

---

## 🔟 Complexity

- **Time:** O(1)
- **Space:** O(1)

---

## **1️⃣1️⃣ Code**

```python
S = input()

number = int(S[:-1])
last = S[-1]

if last == "T":
    print(number * 10)
elif last == "H":
    print(number * 100)
else:
    print(number * 1000)
```

---

## **1️⃣2️⃣ Example**

### Input

```
34T
```

### Output

```
340
```

---

## **1️⃣3️⃣ Dry Run**

| S    | Number | Last | Calculation | Result |
| ---- | ------ | ---- | ----------- | ------ |
| 34T  | 34     | T    | 34 × 10     | 340    |
| 6H   | 6      | H    | 6 × 100     | 600    |
| 700K | 700    | K    | 700 × 1000  | 700000 |

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----- | ------ |
| 34T   | 340    |
| 6H    | 600    |
| 700K  | 700000 |
| 1T    | 10     |
| 99H   | 9900   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- String slicing is powerful for separating mixed data
- Always convert number part to `int()`
- Final character determines multiplier

---

## **1️⃣6️⃣ Real-Life Application**

- Interpreting shorthand values (e.g., 5K likes → 5000)
- File size abbreviations (KB, MB, GB)
- Currency/value multipliers

---

## **1️⃣7️⃣ Practice Questions**

1. Convert "50M" → multiply by 1,000,000
2. Convert "3G" → multiply by 1,000,000,000
3. Convert "100D" → divide by 10

---

## **1️⃣8️⃣ Result**

Program correctly multiplies numeric part based on last character.

---

## **1️⃣9️⃣ Conclusion**

This exercise shows how easily strings can encode numeric meaning—and how slicing + conditions solve it neatly.

---
