# ✅ **Print Length Times**

---

## **1️⃣ Question**

Read a string and print its **first character**, repeated **N times**, where **N = length of the string**.

---

## **2️⃣ Outline**

- Read string
- Find length
- Get first character
- Use while loop to print it N times

---

## **3️⃣ Objective**

To repeat a character based on string length using loops.

---

## **4️⃣ Purpose**

Strengthens understanding of indexing + loop-based repetition.

---

## **5️⃣ Theory**

For string `"Cool"`:

- First character → `"C"`
- Length → 4
  Print `"C"` four times.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Compute its length
3. Extract first character using index 0
4. Initialize counter
5. Print first character while counter < length

---

## **7️⃣ Method**

- Indexing
- len()
- While loop

---

## **8️⃣ Constraints**

String length ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Using wrong index
❌ Printing whole string instead of first character
❌ Forgetting counter increment

---

## 🔟 Complexity

O(N)

---

## **1️⃣1️⃣ Code**

```python
word = input()

first_char = word[0]
length = len(word)

counter = 0
while counter < length:
    print(first_char)
    counter = counter + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
Cool
```

Output:

```
C
C
C
C
```

---

## **1️⃣3️⃣ Dry Run**

word = "Hi"
first_char = "H"
length = 2

counter = 0 → print H
counter = 1 → print H

---

## **1️⃣4️⃣ Test Cases**

| Input  | Output      |
| ------ | ----------- |
| A      | A           |
| Dog    | D D D       |
| Python | P × 6 times |

---

## **1️⃣5️⃣ Notes**

Always use index **0** to get first character.

---

## **1️⃣6️⃣ Practice**

Print the **last** character length-times.

---

## **1️⃣7️⃣ Result**

Correctly prints the first character N times.

---

## **1️⃣8️⃣ Conclusion**

Good exercise in using string indexing + loops for repetition.

---
