# **Question: Indexing**

Given a word **W** and an integer **N**, write a program to print the character present at the index **N** in the word **W**.

### **Input**

- First line: word `W`
- Second line: integer `N`

### **Output**

- Single line: character at index `N` of word `W`

### **Explanation**

Example 1:
Word = Chocolate, N = 2
Indexing: C h o c o l a t e
0 1 2 3 4 5 6 7 8
Character at index 2 = **o**

Example 2:
Word = Table, N = 1
Character at index 1 = **a**

---

# **Approach**

### **Step 1: Read input values**

```python
word = input()
n = input()
```

### **Step 2: Convert N to integer**

```python
n = int(n)
```

### **Step 3: Print the character at the given index**

```python
print(word[n])
```

---

# **Complete Code**

```python
word = input()
n = input()

n = int(n)

print(word[n])
```

---

# 🟩 **DRY RUN (Tabular Form)**

| Step No. | Operation        | Value / Explanation |
| -------- | ---------------- | ------------------- |
| 1        | Read word        | "Chocolate"         |
| 2        | Read index       | "2"                 |
| 3        | Convert N to int | 2                   |
| 4        | Access word[n]   | word[2] = "o"       |
| 5        | Print character  | o                   |

---

### **Final Output**

```
o
```

---
