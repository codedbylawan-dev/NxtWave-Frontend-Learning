## 💻 Question: Print the Input – 2

### 🧩 Problem Statement

Write a program that reads a **word** and prints:

1. The word on the **first line**
2. `"###"` on the **second line**

#### **Sample Input 1**

```
Algebra
```

#### **Sample Output 1**

```
Algebra
###
```

#### **Sample Input 2**

```
1a2b3c
```

#### **Sample Output 2**

```
1a2b3c
###
```

---

## 🧠 Approach

### **Step 1: Read the Input Word**

Use Python’s `input()` function to read the word and store it in a variable:

```python
word = input()
```

---

### **Step 2: Print the Word and "###"**

Print the word on the first line:

```python
print(word)
```

Then print `"###"` on the second line:

```python
print("###")
```

---

## ✅ Solution

Here is the full working solution:

```python
# This program reads a word and prints it, followed by ###
word = input()
print(word)
print("###")
```

This prints the input word on one line and `"###"` on the next line — exactly as required.

---
