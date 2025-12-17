# ✅ **Print Characters in Reverse**

---

## **1️⃣ Question**

Given a string, print **all the characters of the string in reverse order**, each on a new line.

---

## **1️⃣.5️⃣ Category**

For Loop → String Traversal → Reverse Order

---

## **2️⃣ Outline**

- Read the string
- Find the length of the string
- Start from the last index
- Move backwards till the first character
- Print each character

---

## **3️⃣ Objective**

To print characters of a string in **reverse order** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- string indexing
- reverse traversal
- using `len()` with loops

---

## **5️⃣ Theory**

Strings are **indexed starting from 0**.

For a string of length `L`:

- Last character index = `L - 1`
- First character index = `0`

By decreasing the index, we can access characters in reverse.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the string
2. Find its length using `len()`
3. Start loop from `length - 1`
4. Print the character at current index
5. Decrease index by 1
6. Stop when index reaches 0

---

## **7️⃣ Method**

Use:

- input()
- len()
- for loop
- string indexing
- print()

---

## **8️⃣ Constraints**

- Input is a non-empty string
- Each character must be printed on a new line

---

## **9️⃣ Common Mistakes**

❌ Starting loop from wrong index
❌ Forgetting that indexing starts at 0
❌ Printing characters in the same order

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
word = input()
length = len(word)

for i in range(length - 1, -1, -1):
    print(word[i])
```

---

## **1️⃣2️⃣ Example**

### Input

```
scale
```

### Output

```
e
l
a
c
s
```

---

## **1️⃣3️⃣ Dry Run**

word = "abc"
length = 3

- i = 2 → print `c`
- i = 1 → print `b`
- i = 0 → print `a`

Loop stops.

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output  |
| ----- | ------- |
| hi    | i h     |
| abc   | c b a   |
| code  | e d o c |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `len(string) - 1` gives last index
- Negative step is used for reverse order
- Indexing is key in string problems

---

## **1️⃣6️⃣ Real-Life Application**

- Reversing words
- Undo operations
- Backward scanning

---

## **1️⃣7️⃣ Practice Questions**

1. Print a string in reverse on one line
2. Print only vowels in reverse order
3. Count characters while printing in reverse

---

## **1️⃣8️⃣ Result**

The program correctly prints all characters **in reverse order**.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens **string indexing and reverse looping** using a **for loop**.

---
