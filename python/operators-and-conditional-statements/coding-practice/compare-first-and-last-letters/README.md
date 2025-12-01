# ✅ **Compare First & Last Letters — Full Solution (Your Format)**

## **🔹 Question: Compare First & Last Letters**

Write a program that reads a word and checks if the **first letter** and **last letter** of the word are **not the same**.
Output **True** if they are different, otherwise **False**.

---

# ✅ **Approach**

### **Step 1:** Read the input word

### **Step 2:** Find the length of the word

### **Step 3:** Extract first and last letters

### **Step 4:** Compare them using `!=`

### **Step 5:** Print the boolean result

---

# ✅ **Step-by-Step Explanation**

### **Step 1: Read the input**

```python
word = input()
```

### **Step 2: Get length of the word**

```python
word_length = len(word)
```

### **Step 3: Extract first and last letters**

```python
first_letter = word[0]
last_letter = word[word_length - 1]
```

### **Step 4: Compare**

```python
result = first_letter != last_letter
```

### **Step 5: Print output**

```python
print(result)
```

---

# ✅ **Final Code**

```python
word = input()
word_length = len(word)
first_letter = word[0]
last_letter = word[word_length - 1]
result = first_letter != last_letter
print(result)
```

---

# ✅ **Dry Run (Tabular Form)**

### For Input: **Python**

| Step | Variable / Action       | Value      |
| ---- | ----------------------- | ---------- |
| 1    | Input word              | `"Python"` |
| 2    | word_length = len(word) | `6`        |
| 3    | first_letter = word[0]  | `'P'`      |
| 3    | last_letter = word[5]   | `'n'`      |
| 4    | Compare `'P' != 'n'`    | `True`     |
| 5    | Print result            | `True`     |

---

### For Input: **label**

| Step | Variable / Action    | Value     |
| ---- | -------------------- | --------- |
| 1    | Input word           | `"label"` |
| 2    | word_length          | `5`       |
| 3    | first_letter         | `'l'`     |
| 3    | last_letter          | `'l'`     |
| 4    | Compare `'l' != 'l'` | `False`   |
| 5    | Output               | `False`   |

---
