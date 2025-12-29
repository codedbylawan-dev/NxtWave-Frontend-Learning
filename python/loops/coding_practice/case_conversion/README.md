# ✅ **Case Conversion**

---

## **1️⃣ Question**

Given a string, modify the string by:

- Adding a space **before each uppercase character**
- **Excluding** the first uppercase character

Print the modified string.

---

## **1️⃣.5️⃣ Category**

String → For Loop → String Methods → Formatting

---

## **2️⃣ Outline**

- Read the input string
- Initialize result string
- Traverse characters using a `for` loop
- If character is uppercase and not the first character:

  - Add space before it

- Append the character
- Print the result

---

## **3️⃣ Objective**

To separate words in a CamelCase-style string.

---

## **4️⃣ Purpose**

This problem helps in learning:

- string traversal with position awareness
- conditional formatting
- combining logic with accumulation

---

## **5️⃣ Theory**

We detect uppercase letters using:

```python
ch.isupper()
```

We must **skip adding space** for the **first character**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read input string
2. Create empty `result`
3. Loop through the string with index
4. If character is uppercase and index ≠ 0:

   - Add space to result

5. Add the character
6. Print result

---

## **7️⃣ Method**

- `for` loop with index
- `isupper()`
- String concatenation

---

## **8️⃣ Constraints**

- First character should not get space
- Only uppercase characters cause separation

---

## **9️⃣ Common Mistakes**

❌ Adding space before the first character
❌ Using replace instead of logic
❌ Forgetting index tracking

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

result = ""

for i in range(len(s)):
    if s[i].isupper() and i != 0:
        result = result + " "
    result = result + s[i]

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
TitleCase
```

### Output

```
Title Case
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"TheLionKing"`

Iteration:

- T → result = "T"
- h → "Th"
- e → "The"
- L → add space → "The " + "L" → "The L"
- i → "The Li"
- o → "The Lio"
- n → "The Lion"
- K → add space → "The Lion K"
- i → "The Lion Ki"
- n → "The Lion Kin"
- g → "The Lion King"

---

## **1️⃣4️⃣ Test Cases Table**

| Input       | Output        |
| ----------- | ------------- |
| TitleCase   | Title Case    |
| TheLionKing | The Lion King |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Index-based logic is crucial here
- Position matters in string formatting
- Pattern: **Detect → Modify → Append**

---

## **1️⃣6️⃣ Real-Life Application**

- Converting CamelCase to readable text
- Formatting variable names
- UI text cleanup

---

## **1️⃣7️⃣ Practice Questions**

1. Insert dash before uppercase letters
2. Convert camelCase to snake_case
3. Count number of words after conversion

---

## **1️⃣8️⃣ Result**

The program correctly separates words using uppercase detection.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens **control flow + string manipulation**, a core programming muscle.

---
