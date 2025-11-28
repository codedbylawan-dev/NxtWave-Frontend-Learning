# **Half Length of String — Solved**

### **Question:**

Write a program that reads a word and prints **half the length** of the word.

---

## **Input**

A single line containing a **string**.

## **Output**

A single line containing a **float** that is **half the length of the word**.

---

## **Explanation**

Example:
Word → **Airplane**
Length → **8**
Half → **8 / 2 = 4.0**
Output → **4.0**

---

# **Approach**

### **Step 1:** Read the input word

Use the `input()` function.

### **Step 2:** Find the length of the word

Use `len(word)`.

### **Step 3:** Calculate half the length

Divide by 2 (gives float by default in Python).

### **Step 4:** Print the result

Use `print()`.

---

# **Step-by-Step Explanation**

### **Step 1: Read the input**

```python
word = input()
```

### **Step 2: Calculate length**

```python
word_length = len(word)
```

### **Step 3: Calculate half of the length**

```python
half_word_length = word_length / 2
```

### **Step 4: Print the result**

```python
print(half_word_length)
```

---

# **Solution (Final Code)**

```python
word = input()
word_length = len(word)
half_word_length = word_length / 2
print(half_word_length)
```

---
