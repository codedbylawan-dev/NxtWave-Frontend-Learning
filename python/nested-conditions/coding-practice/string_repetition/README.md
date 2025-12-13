# ✅ **String Repetition**

---

## **1️⃣ Question**

Print a given word **N times** in a single line, separated by spaces.

---

## **1.5️⃣ Category**

String Operations → Repetition → Basic Output Formatting

---

## **2️⃣ Outline**

- Read the input string
- Read integer N
- Repeat the string N times with spaces
- Print result

---

## **3️⃣ Objective**

To repeat a word multiple times using basic string operations.

---

## **4️⃣ Purpose**

Strengthens understanding of string multiplication and formatting.

---

## **5️⃣ Theory**

Python allows:

```
word + " "
```

And:

```
(word + " ") * N
```

This gives N repetitions with trailing space → we remove the last space using slicing.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the word
2. Read N
3. Create repeated string using `(word + " ") * N`
4. Remove the last extra space
5. Print final output

---

## **7️⃣ Method**

String concatenation
String repetition
Simple slice to remove last space

---

## **8️⃣ Constraints**

- N ≥ 1
- Maintain exact spacing format
- Output must be a single line

---

## **9️⃣ Common Mistakes**

❌ Adding an extra space at the end
❌ Using loops (not required)
❌ Not repeating the exact given string

---

## 🔟 Complexity

Time: **O(N)**
Space: **O(N)**

---

## **1️⃣1️⃣ Code**

```python
word = input()
N = int(input())

result = (word + " ") * N
result = result[:-1]  # remove last space

print(result)
```

---

## **1️⃣2️⃣ Example**

### Input

```
pen
2
```

### Output

```
pen pen
```

---

## **1️⃣3️⃣ Dry Run**

For word = "Good Day", N = 3:

```
"Good Day " * 3 → "Good Day Good Day Good Day "
Remove last space → correct output
```

---

## **1️⃣4️⃣ Test Cases Table**

| Input       | Output                     |
| ----------- | -------------------------- |
| pen, 2      | pen pen                    |
| Hi, 1       | Hi                         |
| Hello, 3    | Hello Hello Hello          |
| Good Day, 3 | Good Day Good Day Good Day |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- `(string + " ") * N` is a quick way to repeat words
- Always remove extra trailing space
- No loops needed

---

## **1️⃣6️⃣ Real-Life Application**

- Generating repeated banners
- Printing repeated alert messages
- Generating patterns or formatted outputs

---

## **1️⃣7️⃣ Practice Questions**

1. Print a word N times, each on a new line
2. Print numbers 1 to N separated by `-`
3. Repeat a phrase N times with commas

---

## **1️⃣8️⃣ Result**

The program prints the given string N times in a single spaced line.

---

## **1️⃣9️⃣ Conclusion**

A clean demonstration of string repetition and formatting using basic operations.

---
