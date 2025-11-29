# **Question: String Repetition - 2**

Given a word and a number **N**, write a program to print the given word **N** number of times in a single line.

### **Input**

- First line: word
- Second line: integer **N** (number of repetitions)

### **Output**

- Single line: word repeated **N** times
- Note: No spaces between repetitions

### **Explanation**

Example 1:
Word = Maths, N = 2 → Output: `MathsMaths`

Example 2:
Word = Hand, N = 6 → Output: `HandHandHandHandHandHand`

---

# **Approach**

### **Step 1: Read input**

```python
word = input()
n = int(input())
```

### **Step 2: Repeat the word**

```python
message = word * n
```

### **Step 3: Print the result**

```python
print(message)
```

---

# **Complete Code**

```python
word = input()
n = int(input())

message = word * n

print(message)
```

---

# 🟩 **DRY RUN (Tabular Form)**

| Step No. | Operation     | Value / Explanation                   |
| -------- | ------------- | ------------------------------------- |
| 1        | Read word     | "Maths"                               |
| 2        | Read N        | 2                                     |
| 3        | Repeat word   | message = "Maths" \* 2 → "MathsMaths" |
| 4        | Print message | MathsMaths                            |

---

### **Final Output**

```
MathsMaths
```

---
