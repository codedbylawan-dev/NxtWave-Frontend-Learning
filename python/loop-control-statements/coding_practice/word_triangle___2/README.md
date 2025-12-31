# ✅ **Word Triangle – 2**

---

## **1️⃣ Question**

Given a string **W**, print the letters of the word in **N rows** as an **Inverted Right Angled Triangle**, where **N is the length of the word**.

---

## **1️⃣.5️⃣ Category**

String → For Loop → Pattern Printing

---

## **2️⃣ Outline**

- Read the input string
- Find the length of the string
- Use a `for` loop to reduce the length step by step
- In each iteration, print the first part of the string

---

## **3️⃣ Objective**

To build an **inverted triangle pattern** using characters of a string.

---

## **4️⃣ Purpose**

This problem strengthens:

- string slicing
- loop-based pattern construction
- control over indexes and output structure

---

## **5️⃣ Theory**

If a word has length **N**, then:

- Row 1 prints `W[0:N]`
- Row 2 prints `W[0:N-1]`
- Row 3 prints `W[0:N-2]`
- ...
- Last row prints `W[0:1]`

We achieve this using **string slicing** inside a **for loop**.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input string
2. Calculate its length
3. Start a loop from full length down to 1
4. In each loop iteration, print the substring from index `0` to current value

---

## **7️⃣ Method**

- One `for` loop
- String slicing
- Pattern logic using decreasing length

---

## **8️⃣ Constraints**

- Input is always a string
- Case should be preserved
- Output must follow the exact pattern

---

## **9️⃣ Common Mistakes**

❌ Printing each character separately
❌ Using unnecessary nested loops
❌ Incorrect slicing boundaries

---

## **🔟 Complexity**

- Time Complexity: **O(N²)**
- Space Complexity: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
w = input()

n = len(w)

for i in range(n, 0, -1):
    print(w[:i])
```

---

## **1️⃣2️⃣ Example**

### Input

```
game
```

### Output

```
game
gam
ga
g
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"uNiCoRn"`
Length = 7

Iterations:

- i = 7 → `uNiCoRn`
- i = 6 → `uNiCoR`
- i = 5 → `uNiCo`
- i = 4 → `uNiC`
- i = 3 → `uNi`
- i = 2 → `uN`
- i = 1 → `u`

Final output printed correctly.

---

## **1️⃣4️⃣ Test Cases Table**

| Input   | Output                                         |
| ------- | ---------------------------------------------- |
| game    | game / gam / ga / g                            |
| TUPLE   | TUPLE / TUPL / TUP / TU / T                    |
| uNiCoRn | uNiCoRn / uNiCoR / uNiCo / uNiC / uNi / uN / u |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Pattern printing is controlled by loop range
- String slicing gives precise output control
- No extra concepts needed

---

## **1️⃣6️⃣ Real-Life Application**

- Text formatting
- UI pattern rendering
- Console-based design structures

---

## **1️⃣7️⃣ Practice Questions**

1. Print the same triangle but from bottom to top
2. Print only even-length rows
3. Print using last characters instead of first

---

## **1️⃣8️⃣ Result**

The program correctly prints the inverted triangle pattern using the input word.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens **string slicing and loop control** and is a core pattern-building exercise.

---

Problem solved.
Format respected.
Brain exercised.
