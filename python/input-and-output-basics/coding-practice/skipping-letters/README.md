# **Question: Skipping Letters**

You're given a word and an index position.
You must print the **word without the character at that index**.

### **Input**

1. A word (string)
2. An index (integer)

### **Output**

The word with the character at the given index removed.

### **Example**

- Input: `Combine`, `4` → Output: `Combne`
- Input: `Globe`, `2` → Output: `Glbe`

---

# **Approach**

### **Step 1: Read the input**

```python
word = input()
n = int(input())
```

### **Step 2: Split the word into two parts**

```python
before = word[:n]
after = word[n+1:]
```

### **Step 3: Combine and print the result**

```python
result = before + after
print(result)
```

---

# **Complete Code**

```python
word = input()
n = int(input())
before = word[:n]
after = word[n+1:]
result = before + after
print(result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

Example Input:

```
Combine
4
```

| Step No. | Operation          | Value / Explanation               |
| -------- | ------------------ | --------------------------------- |
| 1        | Read input word    | word = "Combine"                  |
| 2        | Read index         | n = 4                             |
| 3        | Slice before index | before = word[:4] → "Comb"        |
| 4        | Slice after index  | after = word[5:] → "ne"           |
| 5        | Combine parts      | result = "Comb" + "ne" → "Combne" |
| 6        | Print result       | Output = **Combne**               |

---

### **Final Output**

```
Combne
```

---
