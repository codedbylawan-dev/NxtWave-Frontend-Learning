# ✅ **Print Vowels**

---

## **1️⃣ Question**

Given a **string**, print all the **vowels** in the string, **each on a new line**.

(Vowels are: `a`, `e`, `i`, `o`, `u`)

---

## **1️⃣.5️⃣ Category**

For Loop → String Traversal → Conditional Printing

---

## **2️⃣ Outline**

- Read the string
- Traverse each character using a for loop
- Check if the character is a vowel
- Print the character if it is a vowel

---

## **3️⃣ Objective**

To identify and print **vowel characters** from a string using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- string traversal
- checking characters using conditions
- filtering required characters

---

## **5️⃣ Theory**

A string contains multiple characters.
By using a **for loop**, we can check each character and decide whether to print it or not.

A vowel is any one of these characters:
`a, e, i, o, u`

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Start a for loop on the string
3. Check if the character is a vowel
4. If true, print the character

---

## **7️⃣ Method**

Use:

- input()
- for loop
- if condition
- print statement

---

## **8️⃣ Constraints**

- Input is a string
- Characters are lowercase
- Output should be one character per line

---

## **9️⃣ Common Mistakes**

❌ Printing consonants
❌ Missing some vowels
❌ Printing vowels in one line

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
word = input()

for ch in word:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        print(ch)
```

---

## **1️⃣2️⃣ Example**

### Input

```
indian
```

### Output

```
i
i
a
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"code"`

Characters checked:

- c → not a vowel
- o → vowel → printed
- d → not a vowel
- e → vowel → printed

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output      |
| ----: | ----------- |
|  code | o e         |
| apple | a e         |
|   sky | (no output) |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Use `or` to check multiple conditions
- for loop is best for character traversal
- Only matching characters are printed

---

## **1️⃣6️⃣ Real-Life Application**

- Text analysis
- Language processing
- Word filtering

---

## **1️⃣7️⃣ Practice Questions**

1. Print consonants only
2. Count vowels in a string
3. Print only `a` and `e`

---

## **1️⃣8️⃣ Result**

The program correctly prints **all vowels** present in the string.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens **string traversal and conditional logic** using a for loop.

---
