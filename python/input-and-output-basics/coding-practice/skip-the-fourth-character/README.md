# **Question: Skip the Fourth Character**

Write a program that reads a word and prints the word **excluding the fourth letter** of the word.

### **Input**

A single string.

### **Output**

The same string but **without the 4th character** (index 3).

### **Example**

Input: `Equality` → Output: `Equlity`
Input: `Listen` → Output: `Lisen`

---

# **Approach**

### **Step 1: Read the input word**

```python
word = input()
```

### **Step 2: Extract characters before the 4th letter**

```python
first_part = word[:3]
```

### **Step 3: Extract characters after the 4th letter**

```python
second_part = word[4:]
```

### **Step 4: Combine and print**

```python
result = first_part + second_part
print(result)
```

---

# **Complete Code**

```python
word = input()
first_part = word[:3]
second_part = word[4:]
result = first_part + second_part
print(result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

Example Input: **Equality**

| Step No. | Operation                        | Value / Explanation                 |
| -------- | -------------------------------- | ----------------------------------- |
| 1        | Read input                       | word = "Equality"                   |
| 2        | Extract first 3 characters       | first_part = word[:3] → "Equ"       |
| 3        | Extract characters after index 3 | second_part = word[4:] → "lity"     |
| 4        | Combine both parts               | result = "Equ" + "lity" → "Equlity" |
| 5        | Print result                     | Output = **Equlity**                |

---

### **Final Output**

```
Equlity
```

---
