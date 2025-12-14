Here is **Identify the Mistake – Print Characters** in your **clean fixed format**, using **only what you have learned** (string indexing + while loop).

---

# ✅ **Print Characters of a Word**

---

## **1️⃣ Question**

Read a word and print **each character** on a **new line**.

---

## **2️⃣ Outline**

- Read the word
- Find its length
- Use a counter
- Print each character using indexing

---

## **3️⃣ Objective**

To practice string indexing and while-loop iteration through characters.

---

## **4️⃣ Purpose**

Strengthens understanding of how to access characters in a string one by one.

---

## **5️⃣ Theory**

If a word has length N, valid indexes are from **0 to N-1**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the string
2. Start counter = 0
3. While counter < length of string:

   - Print character at index `counter`
   - Increase counter

---

## **7️⃣ Method**

Use:

- `len()`
- string indexing `word[i]`
- while loop

---

## **8️⃣ Constraints**

Word length ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Using counter <= length (IndexError)
❌ Forgetting to increase counter
❌ Printing the entire string instead of character

---

## 🔟 Complexity

O(N)

---

## **1️⃣1️⃣ Code**

```python
word = input()

counter = 0
length = len(word)

while counter < length:
    print(word[counter])
    counter = counter + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
Python
```

Output:

```
P
y
t
h
o
n
```

---

## **1️⃣3️⃣ Dry Run**

word = "Cat"
length = 3
counter = 0

- Print C
- Print a
- Print t

---

## **1️⃣4️⃣ Test Cases**

| Input | Output            |
| ----- | ----------------- |
| Hi    | H / i             |
| Loops | L / o / o / p / s |
| A     | A                 |

---

## **1️⃣5️⃣ Notes**

Indexing always starts at 0.

---

## **1️⃣6️⃣ Practice**

Print characters **in reverse** using indexing.

---

## **1️⃣7️⃣ Result**

Program prints every character of the word on a new line.

---

## **1️⃣8️⃣ Conclusion**

A simple loop-indexing problem that builds core string handling skills.

---
