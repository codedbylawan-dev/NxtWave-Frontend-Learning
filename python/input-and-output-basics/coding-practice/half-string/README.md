# ✅ **Half String — Solved**

### **Goal**

Write a program that reads a string and prints the **first half** of the string.

---

# **Approach**

### **Step 1: Read the input string**

```python
word = input()
```

### **Step 2: Calculate half length**

- Find total length
- Divide by 2
- Convert to integer

```python
length_of_the_word = len(word)
half_length = length_of_the_word / 2
half_length = int(half_length)
```

### **Step 3: Slice the first half**

```python
half_word = word[:half_length]
```

### **Step 4: Print the result**

```python
print(half_word)
```

---

# ✅ **Complete Code**

```python
word = input()
length_of_the_word = len(word)
half_length = length_of_the_word / 2
half_length = int(half_length)
half_word = word[:half_length]
print(half_word)
```

---

# 🟩 **DRY RUN (Tabular Form)**

Example Input:

```
Amazon
```

| Step | Operation        | Value / Explanation          |
| ---- | ---------------- | ---------------------------- |
| 1    | Read input       | word = "Amazon"              |
| 2    | Find length      | len("Amazon") = 6            |
| 3    | Divide by 2      | 6 / 2 = 3                    |
| 4    | Convert to int   | half_length = 3              |
| 5    | Slice first half | half_word = word[:3] → "Ama" |
| 6    | Print output     | Ama                          |

---

### ✅ **Final Output**

```
Ama
```
