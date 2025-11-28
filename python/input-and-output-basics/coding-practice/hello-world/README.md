## 💻 Question: Hello World

### 🧩 Problem Statement

Write a program that takes a word **W** as input and prints:

```
Hello
```

There should be a **space** between "Hello" and the input word.

#### **Sample Input 1**

```
World
```

#### **Sample Output 1**

```
Hello World
```

#### **Sample Input 2**

```
Anjali
```

#### **Sample Output 2**

```
Hello Anjali
```

---

## 🧠 Approach

### **Step 1: Read the Input**

We will read a single word from the user using the `input()` function and store it in a variable called `name`.

```python
name = input()
```

---

### **Step 2: Print the Greeting**

We need to print `"Hello "` followed by the word given by the user.
We use the `print()` function with string concatenation:

```python
print("Hello " + name)
```

---

## ✅ Solution

Here is the complete solution for the problem:

```python
# This program reads a word and prints "Hello" followed by that word
name = input()
print("Hello " + name)
```

This program takes the input word and prints the greeting exactly as required.

---
