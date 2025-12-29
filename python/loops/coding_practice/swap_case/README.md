# ✅ **Swap Case**

---

## **1️⃣ Question**

Given a word, write a program to **convert all uppercase letters to lowercase letters and vice versa**.

---

## **1️⃣.5️⃣ Category**

String → For Loop → String Methods → Case Conversion

---

## **2️⃣ Outline**

- Read the input string
- Initialize empty result string
- Traverse each character
- If character is uppercase → convert to lowercase
- Else if character is lowercase → convert to uppercase
- Append modified character
- Print result

---

## **3️⃣ Objective**

To transform each character by **swapping its case**.

---

## **4️⃣ Purpose**

This problem builds:

- precise character inspection
- controlled transformation logic
- confidence in string manipulation

---

## **5️⃣ Theory**

Case checking methods:

```python
ch.isupper()
ch.islower()
```

Case conversion:

```python
ch.lower()
ch.upper()
```

---

## **6️⃣ Step-by-Step Explanation**

1. Read input
2. Create empty `result`
3. Loop through characters
4. If uppercase → append lowercase version
5. Else if lowercase → append uppercase version
6. Print final string

---

## **7️⃣ Method**

- One `for` loop
- Two conditional checks
- `isupper()`, `islower()`, `upper()`, `lower()`

---

## **8️⃣ Constraints**

- Only alphabet characters change
- No extra spaces or formatting

---

## **9️⃣ Common Mistakes**

❌ Forgetting to append transformed character
❌ Using only `swapcase()` directly and missing the point
❌ Printing inside the loop

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
        result = result + ch.lower()
    elif ch.islower():
        result = result + ch.upper()
    else:
        result = result + ch

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
Coding
```

### Output

```
cODING
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"HUMANS"`

H → h
U → u
M → m
A → a
N → n
S → s

Output → `humans`

---

## **1️⃣4️⃣ Test Cases Table**

| Input  | Output |
| ------ | ------ |
| Coding | cODING |
| HUMANS | humans |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Character-level control gives real power
- This is how you stop being “string scared”
- Logic > shortcuts

---

## **1️⃣6️⃣ Real-Life Application**

- Username normalization
- Text styling engines
- Case-sensitive systems testing

---

## **1️⃣7️⃣ Practice Questions**

1. Swap only vowels’ case
2. Count how many characters were changed
3. Ignore numbers and symbols

---

## **1️⃣8️⃣ Result**

The program correctly swaps the case of every letter.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens your mastery over **conditional string transformation**.

---
