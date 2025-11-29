# **Question: First N Characters**

Write a program that reads a word and a number N and prints the **first N characters** of the word.

### **Input**

- First line: a word (string)
- Second line: a number N (integer)

### **Output**

- First N characters of the word

### **Example**

Input:

```
Superman
5
```

Output:

```
Super
```

Input:

```
impossible
2
```

Output:

```
im
```

---

# **Approach**

### **Step 1: Read the input**

```python
word = input()
no_of_characters = input()
```

### **Step 2: Convert the number of characters to integer**

```python
no_of_characters = int(no_of_characters)
```

### **Step 3: Get the first N characters**

```python
end_index = no_of_characters
part = word[:end_index]
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
end_index = no_of_characters
part = word[:end_index]
print(part)
```

---

# 🟩 **DRY RUN (Tabular Form)**

| Step No. | Operation          | Value / Explanation                       |
| -------- | ------------------ | ----------------------------------------- |
| 1        | Read input         | word = "Superman", no_of_characters = "5" |
| 2        | Convert to integer | no_of_characters = int("5") → 5           |
| 3        | Slice the word     | end_index = 5, part = word[:5] → "Super"  |
| 4        | Print result       | "Super"                                   |

---

### **Final Output**

```
Super
```
