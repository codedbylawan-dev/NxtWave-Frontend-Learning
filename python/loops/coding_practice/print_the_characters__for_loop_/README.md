# ✅ **Print the Characters (For Loop)**

---

## **1️⃣ Question**

Given a string, print **each character of the string on a new line**.

---

## **1.5️⃣ Category**

For Loop → String → Character Printing

---

## **2️⃣ Outline**

- Read the string
- Loop through the string
- Print each character

---

## **3️⃣ Objective**

To print characters of a string one by one using a **for loop**.

---

## **4️⃣ Purpose**

Helps understand how a loop accesses characters in a string.

---

## **5️⃣ Theory**

A string is a collection of characters.
Using a loop, we can print each character separately.

Example: `"python"`
Characters → p, y, t, h, o, n

---

## **6️⃣ Step-by-Step Explanation**

1. Read the string
2. Start a loop from first character to last
3. Print the current character
4. Move to the next character

---

## **7️⃣ Method**

Use:

- `for` loop
- string variable
- `print()`

---

## **8️⃣ Constraints**

- String will have at least one character
- Each character must be printed on a new line

---

## **9️⃣ Common Mistakes**

❌ Printing the whole string instead of characters
❌ Printing characters on the same line

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
word = input()

for ch in word:
    print(ch)
```

---

## **1️⃣2️⃣ Example**

Input:

```
python
```

Output:

```
p
y
t
h
o
n
```

---

## **1️⃣3️⃣ Dry Run**

word = "Hi"

Loop runs:

- ch = H → print H
- ch = i → print i

---

## **1️⃣4️⃣ Test Cases Table**

| Input    | Output (line by line) |
| -------- | --------------------- |
| Hi       | H i                   |
| Cat      | C a t                 |
| Variable | V a r i a b l e       |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Strings are iterable
- Loop prints one character at a time

---

## **1️⃣6️⃣ Real-Life Application**

- Text processing
- Password validation
- Character analysis

---

## **1️⃣7️⃣ Practice Questions**

1. Print characters in reverse order
2. Print only vowels from a string
3. Count number of characters

---

## **1️⃣8️⃣ Result**

The program prints every character of the string on a new line.

---

## **1️⃣9️⃣ Conclusion**

A basic string traversal problem using a for loop.

---
