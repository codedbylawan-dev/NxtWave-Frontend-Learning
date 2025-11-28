## 💻 Question: Second Line

### 🧩 Problem Statement

Write a program that reads **two lines of input** and prints **only the second line**.

#### **Sample Input 1**

```
Fundamentals
Python
```

#### **Sample Output 1**

```
Python
```

#### **Sample Input 2**

```
Tom
Jerry
```

#### **Sample Output 2**

```
Jerry
```

---

## 🧠 Approach

### **Step 1: Read the Input**

We need to read two lines from the user:

- Store the first line in variable `a`
- Store the second line in variable `b`

```python
a = input()
b = input()
```

---

### **Step 2: Print the Second Line**

We simply print the value stored in `b`:

```python
print(b)
```

---

## ✅ Solution

Here is the complete solution:

```python
# This program reads two lines of input and prints the second line
a = input()
b = input()
print(b)
```

This program ignores the first line and prints only the second line — exactly as required.
