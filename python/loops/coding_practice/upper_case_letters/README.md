# ✅ **Upper Case Letters**

---

## **1️⃣ Question**

Given a string, write a program that prints **all the uppercase letters** of the given string.

---

## **1️⃣.5️⃣ Category**

String → For Loop → String Methods

---

## **2️⃣ Outline**

- Read the input string
- Initialize an empty result string
- Traverse each character using a `for` loop
- Check if the character is uppercase
- Append it to the result
- Print the result

---

## **3️⃣ Objective**

To extract and print **only uppercase letters** from a string.

---

## **4️⃣ Purpose**

This problem helps in learning:

- character-by-character string traversal
- filtering based on conditions
- using the `isupper()` string method
- building a new string

---

## **5️⃣ Theory**

Python provides the method **`isupper()`**.

- Returns **True** if the character is an uppercase letter
- Returns **False** otherwise

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Create empty string `result`
3. Loop through each character
4. If `ch.isupper()` is True, add it to `result`
5. Print `result`

---

## **7️⃣ Method**

- One `for` loop
- One `if` condition
- `isupper()`
- String concatenation

---

## **8️⃣ Constraints**

- Input may contain uppercase, lowercase, digits, symbols
- Output must contain only uppercase letters

---

## **9️⃣ Common Mistakes**

❌ Printing inside the loop
❌ Forgetting to initialize result string
❌ Using `upper()` instead of `isupper()`

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

result = ""

for ch in s:
    if ch.isupper():
        result = result + ch

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
SofTwArE
```

### Output

```
STAE
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"HACKathons"`
Characters → H A C K a t h o n s
Uppercase → H A C K
Result → `HACK`

---

## **1️⃣4️⃣ Test Cases Table**

| Input      | Output |
| ---------- | ------ |
| SofTwArE   | STAE   |
| HACKathons | HACK   |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Character filtering is a core pattern
- Always use string methods instead of ASCII tricks
- Loop + condition + accumulation = power

---

## **1️⃣6️⃣ Real-Life Application**

- Extracting abbreviations
- Cleaning formatted text
- Parsing mixed-case data

---

## **1️⃣7️⃣ Practice Questions**

1. Print only lowercase letters
2. Print only digits
3. Print only special characters

---

## **1️⃣8️⃣ Result**

The program correctly prints **all uppercase letters** from the string.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens your ability to **filter characters from strings**, a fundamental programming skill.

---
