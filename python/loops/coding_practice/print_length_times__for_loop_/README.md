# ✅ **Print Length Times (For Loop)**

---

## **1️⃣ Question**

Given a string, print its **first character** as many times as the **length of the string**, each on a new line.

---

## **1.5️⃣ Category**

For Loop → String Length → Repetition

---

## **2️⃣ Outline**

- Read the string
- Find its length
- Print the first character length times

---

## **3️⃣ Objective**

To repeat a character using a **for loop**.

---

## **4️⃣ Purpose**

Helps understand looping based on string length.

---

## **5️⃣ Theory**

If the string is `"query"`

- First character → `q`
- Length → 5
  So print `q` **5 times**, one per line.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the string
2. Get the first character (index 0)
3. Loop from 0 to length of string
4. Print the first character in each loop

---

## **7️⃣ Method**

Use:

- `len()` to get length
- `for` loop for repetition
- indexing to get first character

---

## **8️⃣ Constraints**

- String will not be empty
- Output must be exactly N lines

---

## **9️⃣ Common Mistakes**

❌ Printing whole string instead of first character
❌ Looping incorrect number of times

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
word = input()

first_char = word[0]
length = len(word)

for i in range(length):
    print(first_char)
```

---

## **1️⃣2️⃣ Example**

Input:

```
query
```

Output:

```
q
q
q
q
q
```

---

## **1️⃣3️⃣ Dry Run**

word = "List"
length = 4

Loop runs 4 times → prints `L` each time

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output  |
| ----- | ------- |
| hi    | h h     |
| Cat   | C C C   |
| List  | L L L L |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `len()` gives number of repetitions
- Index `0` gives first character

---

## **1️⃣6️⃣ Real-Life Application**

- Repeating symbols
- UI placeholders
- Logging markers

---

## **1️⃣7️⃣ Practice Questions**

1. Print last character length times
2. Print `*` length times
3. Print string length times

---

## **1️⃣8️⃣ Result**

Program prints the first character exactly N times.

---

## **1️⃣9️⃣ Conclusion**

A simple and effective loop-based string repetition problem.

---
