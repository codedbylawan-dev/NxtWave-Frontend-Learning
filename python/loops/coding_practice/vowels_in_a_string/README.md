# ✅ **Vowels in a String**

---

## **1️⃣ Question**

Given a string **S**, print a new string formed by **joining all the vowels** present in the given string.

(Vowels are: **a, e, i, o, u**)

---

## **1️⃣.5️⃣ Category**

For Loop → String Traversal → Conditional Logic

---

## **2️⃣ Outline**

- Read the string
- Initialize an empty string
- Traverse each character
- Check if character is a vowel
- Add vowel to result string
- Print the final string

---

## **3️⃣ Objective**

To extract and combine **vowels from a string** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- string traversal
- conditional checking
- building a new string

---

## **5️⃣ Theory**

A **string** is a sequence of characters.
Using a **for loop**, we can check each character one by one.

If a character is a vowel (`a, e, i, o, u`),
we add it to a result string.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the string S
2. Create an empty string `result`
3. Loop through each character in S
4. Check if the character is a vowel
5. If yes, add it to `result`
6. After loop ends, print `result`

---

## **7️⃣ Method**

Use:

- input()
- for loop
- if condition
- string concatenation

---

## **8️⃣ Constraints**

- String contains lowercase letters
- Output should be in one line
- Order of vowels must be preserved

---

## **9️⃣ Common Mistakes**

❌ Printing vowels on separate lines
❌ Forgetting to initialize result string
❌ Checking only one vowel

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(N)** (for result string)

---

## **1️⃣1️⃣ Code**

```python
S = input()

result = ""

for ch in S:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        result = result + ch

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
container
```

### Output

```
oaie
```

---

## **1️⃣3️⃣ Dry Run**

S = "queue"

- q → not vowel
- u → add → result = "u"
- e → add → result = "ue"
- u → add → result = "ueu"
- e → add → result = "ueue"

Final Output → `ueue`

---

## **1️⃣4️⃣ Test Cases Table**

| Input     | Output |
| --------- | ------ |
| container | oaie   |
| queue     | ueue   |
| sky       |        |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Strings can be built step by step
- for loop is used for traversal
- if condition filters characters

---

## **1️⃣6️⃣ Real-Life Application**

- Text analysis
- Word filtering
- Data validation

---

## **1️⃣7️⃣ Practice Questions**

1. Print only consonants
2. Count number of vowels
3. Print vowels in reverse order

---

## **1️⃣8️⃣ Result**

The program correctly prints **only the vowels from the given string**.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens **string traversal and condition checking** using a **for loop**.

---
