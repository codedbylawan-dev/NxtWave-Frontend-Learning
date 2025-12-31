# ✅ **Shuffle String – 2 (Corrected)**

---

## **1️⃣ Question**

Given two strings **S1** and **S2** of equal length, create a new string by taking characters **alternately** from **S1 first and then from S2**.

---

## **1️⃣.5️⃣ Category**

String → For Loop → String Construction

---

## **2️⃣ Outline**

- Read string `s1`
- Read string `s2`
- Initialize empty string `result`
- Traverse both strings by index
- Append one character from `s1`, then one from `s2`
- Print the result

---

## **3️⃣ Objective**

To generate a new string by **alternating characters** from two input strings.

---

## **4️⃣ Purpose**

This problem strengthens:

- index-based string access
- building strings step-by-step
- understanding controlled iteration

---

## **5️⃣ Theory**

If
`s1 = "bring"`
`s2 = "camel"`

We take:

- 1st from `s1` → **b**
- 2nd from `s2` → **a**
- 3rd from `s1` → **i**
- 4th from `s2` → **e**
- 5th from `s1` → **g**

So the result becomes: **`baieg`**

---

## **6️⃣ Step-by-Step Explanation**

1. Read both strings
2. Initialize `result = ""`
3. Loop from `0` to `length - 1`
4. On even index → take from `s1`
5. On odd index → take from `s2`
6. Print `result`

---

## **7️⃣ Method**

- One `for` loop
- `if` condition
- String indexing
- String concatenation

---

## **8️⃣ Constraints**

- Both strings are same length
- Output must match alternating pattern
- No extra characters

---

## **9️⃣ Common Mistakes**

❌ Appending both characters every time
❌ Ignoring index parity
❌ Printing inside the loop

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
s1 = input()
s2 = input()

result = ""

for i in range(len(s1)):
    if i % 2 == 0:
        result = result + s1[i]
    else:
        result = result + s2[i]

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
bring
camel
```

### Output

```
baieg
```

---

## **1️⃣3️⃣ Dry Run**

`s1 = "bring"`
`s2 = "camel"`

| i   | Picked From | Character | result |
| --- | ----------- | --------- | ------ |
| 0   | s1          | b         | b      |
| 1   | s2          | a         | ba     |
| 2   | s1          | i         | bai    |
| 3   | s2          | e         | baie   |
| 4   | s1          | g         | baieg  |

Final Output → **baieg**

---

## **1️⃣4️⃣ Test Cases Table**

| S1    | S2    | Output                     |
| ----- | ----- | -------------------------- |
| bring | camel | baieg                      |
| HELLO | WORLD | H E L L O (following rule) |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Index parity controls source string
- Alternating logic is a powerful pattern
- Clean string building is essential

---

## **1️⃣6️⃣ Real-Life Application**

- Password masking
- Data weaving
- Pattern-based encryption

---

## **1️⃣7️⃣ Practice Questions**

1. Reverse this shuffled result
2. Print only characters taken from `s2`
3. Swap the picking order

---

## **1️⃣8️⃣ Result**

The program now produces the correct shuffled output: **`baieg`**.

---

## **1️⃣9️⃣ Conclusion**

This problem enforces careful thinking with indexes and controlled string manipulation.

---
