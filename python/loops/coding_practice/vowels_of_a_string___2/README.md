# ✅ **Vowels of a String – 2**

---

## **1️⃣ Question**

Given a string, **count the number of vowels** in the string.
If the count of vowels is **more than 2**, print
**`String has more than two vowels`**
otherwise print
**`String doesn't have more than two vowels`**.

---

## **1️⃣.5️⃣ Category**

For Loop → String Traversal → Conditional Counting

---

## **2️⃣ Outline**

- Read the string
- Initialize a counter
- Traverse each character in the string
- Check if it is a vowel
- Increase count
- Compare count with 2
- Print result

---

## **3️⃣ Objective**

To **count vowels** in a string using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- string traversal
- character comparison
- counting using variables

---

## **5️⃣ Theory**

Vowels are:

```
a, e, i, o, u
```

Each character of the string is checked.
If it matches any vowel, the count is increased.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Set `count = 0`
3. Loop through each character
4. If character is a vowel

   - increase count

5. After loop

   - if count > 2 → print message
   - else → print message

---

## **7️⃣ Method**

Use:

- for loop
- if condition
- comparison operators

---

## **8️⃣ Constraints**

- Input is a string
- Vowels are lowercase only

---

## **9️⃣ Common Mistakes**

❌ Forgetting one of the vowels
❌ Using wrong condition (`>=` instead of `>`)
❌ Checking only first character

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
word = input()

count = 0

for ch in word:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count = count + 1

if count > 2:
    print("String has more than two vowels")
else:
    print("String doesn't have more than two vowels")
```

---

## **1️⃣2️⃣ Example**

### Input

```
indian
```

### Output

```
String has more than two vowels
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"code"`

- c → not vowel
- o → vowel (count = 1)
- d → not vowel
- e → vowel (count = 2)

2 is **not greater than 2**
→ print second message

---

## **1️⃣4️⃣ Test Cases Table**

| Input  | Output                                   |
| ------ | ---------------------------------------- |
| indian | String has more than two vowels          |
| code   | String doesn't have more than two vowels |
| sky    | String doesn't have more than two vowels |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Strings can be looped character by character
- Counting is done using variables
- Logical OR helps combine conditions

---

## **1️⃣6️⃣ Real-Life Application**

- Text analysis
- Validation rules
- Language processing basics

---

## **1️⃣7️⃣ Practice Questions**

1. Count consonants in a string
2. Check if string has any vowel
3. Count vowels and consonants separately

---

## **1️⃣8️⃣ Result**

The program correctly checks whether the string has **more than two vowels**.

---

## **1️⃣9️⃣ Conclusion**

A solid string-processing problem that strengthens **loop + condition logic**.

---
