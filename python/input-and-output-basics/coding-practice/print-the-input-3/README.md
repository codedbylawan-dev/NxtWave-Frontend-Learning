## 💻 Question: Print the Input – 3

### 🧩 Problem Statement

Write a program that reads **two words** and prints them on **two separate lines**.

#### **Input**

- The first line contains a string (first word).
- The second line contains a string (second word).

#### **Output**

- Print the **first word** on the first line.
- Print the **second word** on the second line.

---

### 📌 Example

#### **Sample Input 1**

```
Apple
Banana
```

#### **Sample Output 1**

```
Apple
Banana
```

#### **Sample Input 2**

```
Hi
Hello
```

#### **Sample Output 2**

```
Hi
Hello
```

---

## 🧠 Approach

### **Step 1: Read the Input Words**

Use the `input()` function twice to read two separate words:

```python
first_word = input()
second_word = input()
```

---

### **Step 2: Print the Words on Separate Lines**

Use `print()` to output each word on its own line:

```python
print(first_word)
print(second_word)
```

---

## ✅ Solution

Here is the complete and clean solution:

```python
# This program reads two words and prints them on separate lines
first_word = input()
second_word = input()
print(first_word)
print(second_word)
```

This program reads two inputs and prints them exactly as required — each on a new line.
