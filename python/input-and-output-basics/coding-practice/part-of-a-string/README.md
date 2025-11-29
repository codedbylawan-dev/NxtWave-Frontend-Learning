# **Question: Part of a String**

Write a program that reads a word and an index and prints a part of the word **from the given index to the end**.

### **Input**

- First line: a string (word)
- Second line: an integer (starting index)

### **Output**

- Substring from the given index to the end of the word.

### **Explanation**

Example 1:
Input = `Unhappy`, Index = 2 → Output: `happy`

Example 2:
Input = `goodnight`, Index = 4 → Output: `night`

---

# **Approach**

### **Step 1: Read input**

```python
word = input()
start_index = input()
start_index = int(start_index)
```

### **Step 2: Slice the word from the index**

```python
part = word[start_index:]
```

### **Step 3: Print the result**

```python
print(part)
```

---

# **Complete Code**

```python
word = input()
start_index = input()
start_index = int(start_index)

part = word[start_index:]

print(part)
```

---

# 🟩 **DRY RUN (Tabular Form)**

| Step No. | Operation     | Value / Explanation                 |
| -------- | ------------- | ----------------------------------- |
| 1        | Read input    | word = "Unhappy", start_index = "2" |
| 2        | Convert index | start_index = int("2") → 2          |
| 3        | Slice word    | part = word[2:] → "happy"           |
| 4        | Print result  | happy                               |

---

### **Final Output**

```
happy
```
