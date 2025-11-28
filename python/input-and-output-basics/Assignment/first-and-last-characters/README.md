# ✅ **First & Last Characters (Solved)**

**Difficulty:** Easy

Write a program that reads a word and prints the **first** and **last** characters of the word on two separate lines.

---

## **Sample Input 1**

```
qwerty
```

## **Sample Output 1**

```
q
y
```

---

## **Sample Input 2**

```
Python Programming
```

## **Sample Output 2**

```
P
g
```

---

# 🧭 **Outline**

**Question:** First & Last Characters
**Approach:**

1. Read the input word.
2. Find the first character.
3. Find the last character.
4. Print the first character.
5. Print the last character.

---

# 📝 **Step-by-Step Explanation**

### **Step 1: Read the word**

```python
word = input()
```

---

### **Step 2: Find the first character**

```python
first_char = word[0]
```

---

### **Step 3: Find the last character**

```python
last_char = word[-1]
```

> Using `-1` gives the last character of the string.

---

### **Step 4: Print the first character**

```python
print(first_char)
```

---

### **Step 5: Print the last character**

```python
print(last_char)
```

---

# ✅ **Final Solution**

```python
word = input()
first_char = word[0]
last_char = word[-1]
print(first_char)
print(last_char)
```

---

If you want, I can rewrite **all your previous “Solved” string problems** into this **exact consistent learning format** for easier practice.
