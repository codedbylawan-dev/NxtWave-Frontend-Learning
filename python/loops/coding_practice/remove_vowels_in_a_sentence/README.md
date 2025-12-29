# ✅ **Remove Vowels in a Sentence**

---

## **1️⃣ Question**

Given a sentence **S**, remove **all the vowels** from the sentence.

Vowels are:
`A, E, I, O, U, a, e, i, o, u`

---

## **1️⃣.5️⃣ Category**

String → For Loop → Character Filtering

---

## **2️⃣ Outline**

- Read the input sentence
- Create an empty result string
- Traverse each character
- Skip the character if it is a vowel
- Otherwise, add it to result
- Print the result

---

## **3️⃣ Objective**

To remove all vowels from a sentence using basic string processing.

---

## **4️⃣ Purpose**

This problem trains you in:

- character scanning
- conditional filtering
- building strings manually

---

## **5️⃣ Theory**

When iterating over a string:

- Check if a character belongs to a **forbidden set** (vowels)
- If not, append it to the result string

---

## **6️⃣ Step-by-Step Explanation**

1. Take the input sentence
2. Initialize `result` as empty string
3. Loop through each character
4. If the character is **not** a vowel, append it
5. Print the final string

---

## **7️⃣ Method**

- `for` loop
- `if` condition
- string concatenation

---

## **8️⃣ Constraints**

- Both uppercase and lowercase vowels must be removed
- Preserve all other characters including spaces

---

## **9️⃣ Common Mistakes**

❌ Removing spaces accidentally
❌ Forgetting uppercase vowels
❌ Printing inside the loop

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

vowels = "AEIOUaeiou"
result = ""

for ch in s:
    if ch not in vowels:
        result = result + ch

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
Hello World
```

### Output

```
Hll Wrld
```

---

## **1️⃣3️⃣ Dry Run**

Input → `Once upon a time`

Process:

O ❌
n ✅
c ✅
e ❌
(space) ✅
u ❌
p ✅
o ❌
n ✅
(space) ✅
a ❌
(space) ✅
t ✅
i ❌
m ✅
e ❌

Result → `nc pn tm`

---

## **1️⃣4️⃣ Test Cases Table**

| Input            | Output   |
| ---------------- | -------- |
| Hello World      | Hll Wrld |
| Once upon a time | nc pn tm |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Filtering characters is a core pattern
- Never mutate strings directly
- Always build a new result string

---

## **1️⃣6️⃣ Real-Life Application**

- Text preprocessing
- Search engines
- Natural language filtering

---

## **1️⃣7️⃣ Practice Questions**

1. Count how many vowels were removed
2. Replace vowels with `*` instead of removing
3. Remove only uppercase vowels

---

## **1️⃣8️⃣ Result**

The program successfully removes all vowels from the sentence.

---

## **1️⃣9️⃣ Conclusion**

This problem is a foundation stone for **text processing and validation systems**.

---
