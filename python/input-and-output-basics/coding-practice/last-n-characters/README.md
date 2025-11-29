# **Question: Last N characters**

Write a program that reads a word and a number N and prints the **last N characters** of the word.

### **Input**

- First line: a string (word)
- Second line: an integer N

### **Output**

- Last N characters of the given word

### **Explanation**

Example 1:
Input = `Forgive`, N = 4 → Output: `give`

Example 2:
Input = `hamburger`, N = 6 → Output: `burger`

---

# **Approach**

### **Step 1: Read the input**

```python
word = input()
no_of_characters = input()
no_of_characters = int(no_of_characters)
```

### **Step 2: Calculate the starting index**

```python
word_length = len(word)
start_index = word_length - no_of_characters
```

### **Step 3: Get the last N characters**

```python
part = word[start_index:]
```

### **Step 4: Print the result**

```python
print(part)
```

---

# **Complete Code**

```python
word = input()
no_of_characters = input()
no_of_characters = int(no_of_characters)

word_length = len(word)
start_index = word_length - no_of_characters
part = word[start_index:]

print(part)
```

---

# 🟩 **DRY RUN (Tabular Form)**

| Step No. | Operation                      | Value / Explanation                                       |
| -------- | ------------------------------ | --------------------------------------------------------- |
| 1        | Read input                     | word = "Forgive", no_of_characters = "4"                  |
| 2        | Convert to int                 | no_of_characters = int("4") → 4                           |
| 3        | Calculate length & start index | word_length = len("Forgive") → 7, start_index = 7 - 4 → 3 |
| 4        | Slice word                     | part = word[3:] → "give"                                  |
| 5        | Print result                   | give                                                      |

---

### **Final Output**

```
give
```
