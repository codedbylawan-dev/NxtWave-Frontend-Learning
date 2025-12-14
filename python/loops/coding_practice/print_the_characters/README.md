# ✅ **Print the Characters**

---

## **1️⃣ Question**

Read a string and print **each character** on a new line.

---

## **2️⃣ Outline**

- Read string
- Find length
- Use index to access each character
- Print each character using a while loop

---

## **3️⃣ Objective**

To print characters one-by-one using indexing and loops.

---

## **4️⃣ Purpose**

Builds understanding of string traversal using a counter.

---

## **5️⃣ Theory**

String `"shine"` has 5 characters:
`s`, `h`, `i`, `n`, `e` → each printed on its own line.

---

## **6️⃣ Step-by-Step Explanation**

1. Read string
2. Set counter = 0
3. While counter < length:

   - Print `word[counter]`
   - Increase counter

---

## **7️⃣ Method**

String indexing + while loop.

---

## **8️⃣ Constraints**

Length ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Using wrong index
❌ Forgetting counter increment
❌ Extra spaces

---

## 🔟 Complexity

O(N)

---

## **1️⃣1️⃣ Code**

```python
word = input()
length = len(word)

counter = 0
while counter < length:
    print(word[counter])
    counter = counter + 1
```

---

## **1️⃣2️⃣ Example**

Input:

```
shine
```

Output:

```
s
h
i
n
e
```

---

## **1️⃣3️⃣ Dry Run**

word = "Hi"
counter = 0 → print "H"
counter = 1 → print "i"

---

## **1️⃣4️⃣ Test Cases**

| Input   | Output        |
| ------- | ------------- |
| A       | A             |
| Sun     | S U N         |
| Morning | M o r n i n g |

---

## **1️⃣5️⃣ Notes**

Index goes from **0 → length-1**.

---

## **1️⃣6️⃣ Practice**

Print characters in **reverse order**.

---

## **1️⃣7️⃣ Result**

Program prints each character on a new line.

---

## **1️⃣8️⃣ Conclusion**

Simple loop-based character traversal problem.

---
