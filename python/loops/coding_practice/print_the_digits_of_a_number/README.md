# ✅ **Print the Digits of a Number**

---

## **1️⃣ Question**

Given a **positive number**, print **all its digits separated by a space**.

---

## **1️⃣.5️⃣ Category**

For Loop → String Processing → Digit Printing

---

## **2️⃣ Outline**

- Read the number as input
- Treat the number as a string
- Traverse each character
- Build the output with spaces
- Print the final result

---

## **3️⃣ Objective**

To print each digit of a number separately using a **for loop**, **without using `end`**.

---

## **4️⃣ Purpose**

This problem helps you understand:

- numbers as strings
- character-by-character traversal
- building output using string concatenation

---

## **5️⃣ Theory**

When input is read using `input()`, it is a **string**.
Each character in the string is a **digit**.

Example:
Input → `"165"`
Digits → `1 6 5`

---

## **6️⃣ Step-by-Step Explanation**

1. Read the input number as a string
2. Create an empty string to store the result
3. Use a for loop to go through each digit
4. Add each digit and a space to the result
5. Print the final string

---

## **7️⃣ Method**

Use:

- `input()`
- `for` loop
- string concatenation
- `print()`

---

## **8️⃣ Constraints**

- Input is a positive integer
- Digits must appear in the same order
- Output should be in one line

---

## **9️⃣ Common Mistakes**

❌ Trying to loop over an integer
❌ Printing each digit on a new line
❌ Forgetting space between digits

---

## **🔟 Complexity**

Time: **O(N)**
Space: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
number = input()

result = ""
for digit in number:
    result = result + digit + " "

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
165
```

### Output

```
1 6 5
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"45866"`

- result = ""
- add `"4 "` → result = `"4 "`
- add `"5 "` → result = `"4 5 "`
- add `"8 "` → result = `"4 5 8 "`
- add `"6 "` → result = `"4 5 8 6 "`
- add `"6 "` → result = `"4 5 8 6 6 "`

Printed Output → `4 5 8 6 6 `

---

## **1️⃣4️⃣ Test Cases Table**

| Input | Output    |
| ----: | --------- |
|   165 | 1 6 5     |
| 45866 | 4 5 8 6 6 |
|     9 | 9         |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `input()` gives a string
- Strings can be looped character by character
- Output can be built using `+` operator

---

## **1️⃣6️⃣ Real-Life Application**

- Digit-wise calculations
- Number formatting
- Validation of numeric strings

---

## **1️⃣7️⃣ Practice Questions**

1. Print digits without spaces
2. Count digits in a number
3. Print digits in reverse order

---

## **1️⃣8️⃣ Result**

The program prints **all digits separated by spaces** without using `end`.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens **string traversal**, **for loop usage**, and **basic string building**, using only learned concepts.
