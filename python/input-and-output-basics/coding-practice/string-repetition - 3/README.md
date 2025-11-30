# ✅ **String Repetition 3 — Solved**

### **Goal**

Given a word and a number **N**, print the **last 3 characters** of the word repeated **N times**, without spaces.

---

# **Approach**

### **Step 1: Read the input**

```python
word = input()
n = int(input())
```

### **Step 2: Find the last three characters**

```python
length_of_the_word = len(word)
start_index = length_of_the_word - 3
sliced_word = word[start_index:]
```

### **Step 3: Repeat sliced part**

```python
message = sliced_word * n
```

### **Step 4: Print the result**

```python
print(message)
```

---

# ✅ **Complete Code**

```python
word = input()
n = int(input())
length_of_the_word = len(word)
start_index = length_of_the_word - 3
sliced_word = word[start_index:]
message = sliced_word * n
print(message)
```

---

# 🟩 **DRY RUN (Tabular Form)**

Example Input:

```
Transport
2
```

| Step | Operation          | Value / Explanation       |
| ---- | ------------------ | ------------------------- |
| 1    | Read input         | word = "Transport", n = 2 |
| 2    | Find length        | len("Transport") = 9      |
| 3    | Start index        | 9 - 3 = 6                 |
| 4    | Slice last 3 chars | word[6:] → "ort"          |
| 5    | Repeat sliced part | "ort" \* 2 = "ortort"     |
| 6    | Print output       | ortort                    |

---

### ✅ **Final Output**

```
ortort
```
