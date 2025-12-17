# ✅ **Count of Vowels**

---

## **1️⃣ Question**

Given a **string**, print the **count of vowels** present in the string.

(Vowels are: `a`, `e`, `i`, `o`, `u`)

---

## **1️⃣.5️⃣ Category**

For Loop → String Traversal → Counting

---

## **2️⃣ Outline**

- Read the string
- Initialize a counter
- Traverse each character using a for loop
- Check if the character is a vowel
- Increase the counter
- Print the final count

---

## **3️⃣ Objective**

To **count vowels** in a string using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps in understanding:

- counting logic
- condition checking
- loop-based traversal

---

## **5️⃣ Theory**

A string is a collection of characters.
We check each character and **count** it if it is a vowel.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Create a variable `count` and set it to 0
3. Use a for loop to go through each character
4. If the character is a vowel, increase `count` by 1
5. After the loop ends, print `count`

---

## **7️⃣ Method**

Use:

- input()
- for loop
- if condition
- counter variable

---

## **8️⃣ Constraints**

- Input is a string
- Characters are lowercase
- Output should be a single integer

---

## **9️⃣ Common Mistakes**

❌ Forgetting to initialize counter
❌ Counting consonants
❌ Printing characters instead of count

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
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        count = count + 1

print(count)
```

---

## **1️⃣2️⃣ Example**

### Input

```
code
```

### Output

```
2
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"indian"`

- i → vowel → count = 1
- n → no change
- d → no change
- i → vowel → count = 2
- a → vowel → count = 3
- n → no change

Final output → `3`

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output |
| ----: | ------ |
|  code | 2      |
|   sky | 0      |
| apple | 2      |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Counter is important for counting problems
- Conditions decide what to count
- Loop runs once per character

---

## **1️⃣6️⃣ Real-Life Application**

- Text analysis
- Word statistics
- Language learning tools

---

## **1️⃣7️⃣ Practice Questions**

1. Count consonants
2. Count only `a`
3. Count vowels in a sentence

---

## **1️⃣8️⃣ Result**

The program correctly prints the **number of vowels** in the string.

---

## **1️⃣9️⃣ Conclusion**

A basic but important problem to master **counting using loops**.

---
