# ✅ **Print Required Characters**

---

## **1️⃣ Question**

Given a **string**, print all the characters that are **`a` or `z`** from the string, **each on a new line**.

---

## **1️⃣.5️⃣ Category**

For Loop → String Traversal → Conditional Printing

---

## **2️⃣ Outline**

- Read the string
- Traverse each character using a for loop
- Check if the character is `a` or `z`
- Print the character if the condition is true

---

## **3️⃣ Objective**

To print specific characters from a string using a **for loop** and **if condition**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- string traversal
- character comparison
- conditional printing

---

## **5️⃣ Theory**

A string is a collection of characters.
Using a **for loop**, we can check each character one by one.

We print a character only if it matches the required characters.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Use a for loop to go through each character
3. Check if the character is `a` or `z`
4. If yes, print it

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
- Characters are case-sensitive

---

## **9️⃣ Common Mistakes**

❌ Printing all characters
❌ Using wrong character comparison
❌ Printing in the same line

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
word = input()

for ch in word:
    if ch == "a" or ch == "z":
        print(ch)
```

---

## **1️⃣2️⃣ Example**

### Input

```
zigzag
```

### Output

```
z
z
a
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"zigzag"`

Characters checked:

- z → printed
- i → skipped
- g → skipped
- z → printed
- a → printed
- g → skipped

---

## **1️⃣4️⃣ Test Cases Table**

|  Input | Output |
| -----: | ------ |
| zigzag | z z a  |
|  pizza | z a    |
|  apple | a      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Strings can be traversed character by character
- `or` is used to check multiple conditions
- Only matching characters are printed

---

## **1️⃣6️⃣ Real-Life Application**

- Filtering characters
- Password validation rules
- Text processing

---

## **1️⃣7️⃣ Practice Questions**

1. Print only vowels
2. Print only consonants
3. Print characters `x` and `y`

---

## **1️⃣8️⃣ Result**

The program correctly prints **only `a` and `z` characters** from the string.

---

## **1️⃣9️⃣ Conclusion**

A simple string filtering problem that strengthens **for loop + if condition** usage.

---
