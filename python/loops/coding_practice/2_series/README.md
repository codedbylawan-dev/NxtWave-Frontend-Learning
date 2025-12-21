# ✅ **2 Series**

---

## **1️⃣ Question**

Given a number **N**, print the first **N terms** of the following series, **each on a new line**:

```
2
22
222
2222
...
```

---

## **1️⃣.5️⃣ Category**

For Loop → Series Generation → String Concatenation

---

## **2️⃣ Outline**

- Read N
- Start with an empty string
- Loop N times
- Add `"2"` each time
- Print the current term

---

## **3️⃣ Objective**

To generate and print a **number pattern series** using a **for loop**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- building values step by step
- string concatenation
- printing series using loops

---

## **5️⃣ Theory**

The series is built by **adding one more `2`** in every step.

Example for N = 4:

```
Step 1 → "2"
Step 2 → "22"
Step 3 → "222"
Step 4 → "2222"
```

Each step prints the current value.

---

## **6️⃣ Step-by-Step Explanation**

1. Read N
2. Create an empty string `term`
3. Loop from 1 to N
4. In each iteration:

   - add `"2"` to `term`
   - print `term`

---

## **7️⃣ Method**

Use:

- for loop
- string variable
- string concatenation (`+`)
- print statement

---

## **8️⃣ Constraints**

- N ≥ 1

---

## **9️⃣ Common Mistakes**

❌ Printing all terms in one line
❌ Re-initializing the string inside the loop
❌ Using nested loops unnecessarily

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
N = int(input())

term = ""

for i in range(N):
    term = term + "2"
    print(term)
```

---

## **1️⃣2️⃣ Example**

### Input

```
6
```

### Output

```
2
22
222
2222
22222
222222
```

---

## **1️⃣3️⃣ Dry Run**

N = 3

- i = 0 → term = "2" → print 2
- i = 1 → term = "22" → print 22
- i = 2 → term = "222" → print 222

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output              |
| ----: | ------------------- |
|     1 | 2                   |
|     3 | 2 22 222            |
|     5 | 2 22 222 2222 22222 |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Series can be built using strings
- Concatenation grows the pattern
- One loop is enough

---

## **1️⃣6️⃣ Real-Life Application**

- Pattern generation
- Sequence building
- Learning incremental logic

---

## **1️⃣7️⃣ Practice Questions**

1. Print series: 1, 11, 111
2. Print series using number 5
3. Print series in reverse order

---

## **1️⃣8️⃣ Result**

The program correctly prints the **2 series** for the given N.

---

## **1️⃣9️⃣ Conclusion**

A clean beginner-friendly series problem that strengthens **loop + string logic**.

---
