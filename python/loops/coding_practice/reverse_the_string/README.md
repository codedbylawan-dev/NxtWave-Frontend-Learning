# ✅ **Reverse the String**

---

## **1️⃣ Question**

Given a string **S**, print the **reverse of the given string**.

---

## **1️⃣.5️⃣ Category**

For Loop → String Traversal → Reverse Processing

---

## **2️⃣ Outline**

- Read the string
- Initialize an empty string
- Traverse the string from last character to first
- Add each character to result
- Print the reversed string

---

## **3️⃣ Objective**

To reverse a string using a **for loop** and **basic string operations**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- reverse traversal
- loop control
- building strings step by step

---

## **5️⃣ Theory**

A string can be accessed using **index values**.
To reverse a string:

- Start from the **last index**
- Move towards index `0`
- Add each character to a new string

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Create an empty string `result`
3. Find the length of the string
4. Loop from last index to first index
5. Add each character to `result`
6. Print `result`

---

## **7️⃣ Method**

Use:

- input()
- len()
- for loop with range
- string concatenation

---

## **8️⃣ Constraints**

- String can contain spaces
- Output should be in one line
- Order must be completely reversed

---

## **9️⃣ Common Mistakes**

❌ Using slicing (`[::-1]`)
❌ Printing characters line by line
❌ Looping in forward direction

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
S = input()

result = ""
length = len(S)

for i in range(length - 1, -1, -1):
    result = result + S[i]

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
Competitive Programming
```

### Output

```
gnimmargorP evititepmoC
```

---

## **1️⃣3️⃣ Dry Run**

S = "abc"

Indexes: 2 → 1 → 0

- i = 2 → result = "c"
- i = 1 → result = "cb"
- i = 0 → result = "cba"

Final Output → `cba`

---

## **1️⃣4️⃣ Test Cases Table**

| Input  | Output |
| ------ | ------ |
| hello  | olleh  |
| python | nohtyp |
| a      | a      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Reverse traversal uses negative step
- Index-based access is powerful
- Strings are immutable, so new string is created

---

## **1️⃣6️⃣ Real-Life Application**

- Text processing
- Palindrome checking
- Data transformation

---

## **1️⃣7️⃣ Practice Questions**

1. Reverse only vowels in a string
2. Reverse words in a sentence
3. Check if string is a palindrome

---

## **1️⃣8️⃣ Result**

The program correctly prints the **reverse of the given string**.

---

## **1️⃣9️⃣ Conclusion**

A foundational string problem that strengthens **loop control and index handling**.

---
