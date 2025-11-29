# **Question: Part of a String - 2**

Write a program that reads a word and two indices (X, Y) and prints a part of the word **from the index X to the index Y**.

### **Input**

- First line: a string (word)
- Second line: an integer X (start index)
- Third line: an integer Y (end index)

### **Output**

- Substring from index X to index Y (inclusive)

### **Constraints**

- Y ≥ X

### **Explanation**

Example 1:
Input = `Growing`, X = 3, Y = 6 → Output: `wing`

Example 2:
Input = `Scrabble`, X = 1, Y = 5 → Output: `crabb`

---

# **Approach**

### **Step 1: Read input**

```python
word = input()
start_index = input()
start_index = int(start_index)
end_index = input()
end_index = int(end_index)
```

### **Step 2: Slice the word from X to Y**

```python
part = word[start_index:end_index + 1]
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
end_index = input()
end_index = int(end_index)

part = word[start_index:end_index + 1]

print(part)
```

---

# 🟩 **DRY RUN (Tabular Form)**

| Step No. | Operation       | Value / Explanation                                  |
| -------- | --------------- | ---------------------------------------------------- |
| 1        | Read input      | word = "Growing", start_index = "3", end_index = "6" |
| 2        | Convert indices | start_index = int("3") → 3, end_index = int("6") → 6 |
| 3        | Slice word      | part = word[3:6+1] → word[3:7] → "wing"              |
| 4        | Print result    | wing                                                 |

---

### **Final Output**

```
wing
```
