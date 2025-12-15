# ✅ **Identify the Mistake – Styled Word**

---

## **1️⃣ Question**

Given a word, print its **characters separated by hyphens (`-`)** in a single line.

---

## **1.5️⃣ Category**

For Loop → Strings → Character Printing

---

## **2️⃣ Outline**

- Read the string
- Loop through each character
- Print characters with `-` between them

---

## **3️⃣ Objective**

To print characters of a string in a styled format using a **for loop**.

---

## **4️⃣ Purpose**

This problem improves understanding of:

- string traversal
- formatting output
- avoiding extra characters

---

## **5️⃣ Theory**

If the word is:

```
Python
```

Characters are:

```
P y t h o n
```

Required output:

```
P-y-t-h-o-n
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Loop through each character
3. Print character
4. Print `-` **only between characters**

---

## **7️⃣ Method**

Use:

- for loop
- string indexing
- conditional check inside loop

---

## **8️⃣ Constraints**

- Input is a single word
- Output must be in one line

---

## **9️⃣ Common Mistakes**

❌ Printing `-` at the end
❌ Printing each character on a new line
❌ Extra spaces

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
word = input()

length = len(word)

for i in range(length):
    if i == length - 1:
        print(word[i])
    else:
        print(word[i], end="-")
```

---

## **1️⃣2️⃣ Example**

### Input

```
Python
```

### Output

```
P-y-t-h-o-n
```

---

## **1️⃣3️⃣ Dry Run**

word = "Loops"
length = 5

L- o- o- p- s

(last character printed without `-`)

---

## **1️⃣4️⃣ Test Cases Table**

| Input  | Output      |
| ------ | ----------- |
| Python | P-y-t-h-o-n |
| Loops  | L-o-o-p-s   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Use index to control formatting
- Avoid extra symbols at the end
- `end=""` helps control output style

---

## **1️⃣6️⃣ Real-Life Application**

- Formatting usernames
- Displaying codes clearly
- UI text styling

---

## **1️⃣7️⃣ Practice Questions**

1. Separate characters using `*`
2. Print characters with spaces
3. Print characters with commas

---

## **1️⃣8️⃣ Result**

The program correctly prints characters separated by hyphens.

---

## **1️⃣9️⃣ Conclusion**

A useful string-formatting exercise that strengthens **loop control and output formatting**.

---
