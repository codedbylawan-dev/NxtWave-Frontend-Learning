# ✅ **Star Repetition – 4 (Solved)**

**Task:**
Read a word → print:

- First **2 characters**
- Stars (`*`) in place of all middle characters
- Last **2 characters**

---

# ✅ **Approach**

### **Step 1: Read the input**

```python
word = input()
```

### **Step 2: Calculate how many stars to print**

```python
word_length = len(word)
number_of_stars = word_length - 4
```

### **Step 3: Extract first two + last two characters**

```python
first_two = word[:2]
last_two = word[-2:]
```

### **Step 4: Create final string**

```python
result = first_two + "*" * number_of_stars + last_two
print(result)
```

---

# ✅ **Final Complete Code**

```python
word = input()
word_length = len(word)
number_of_stars = word_length - 4

first_two = word[:2]
last_two = word[-2:]

result = first_two + "*" * number_of_stars + last_two
print(result)
```

---

# 🟩 **DRY RUN (Tabular Format)**

Input:

```
message
```

| Step | Operation   | Value / Explanation |
| ---- | ----------- | ------------------- |
| 1    | word        | "message"           |
| 2    | length      | 7                   |
| 3    | stars count | 7 - 4 = 3           |
| 4    | first_two   | "me"                |
| 5    | last_two    | "ge"                |
| 6    | stars       | "\*\*\*"            |
| 7    | result      | "me\*\*\*ge"        |

**Output:**

```
me***ge
```

---

# 🟩 Sample Input 2

```
12345
```

| Step         | Value     |
| ------------ | --------- |
| length       | 5         |
| stars needed | 5 - 4 = 1 |
| first_two    | "12"      |
| last_two     | "45"      |
| result       | "12\*45"  |

**Output:**

```
12*45
```

---
