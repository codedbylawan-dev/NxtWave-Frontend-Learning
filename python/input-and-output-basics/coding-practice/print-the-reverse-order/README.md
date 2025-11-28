## 💻 Question: Print in Reverse Order

### 🧩 Problem Statement

Write a program that reads **two lines of input** and prints them in **reverse order**.

That means:

- Whatever is entered **second** should be printed **first**
- Whatever is entered **first** should be printed **second**

---

### 📌 Example

#### **Sample Input 1**

```
Book
Pen
```

#### **Sample Output 1**

```
Pen
Book
```

#### **Sample Input 2**

```
4
5
```

#### **Sample Output 2**

```
5
4
```

---

## 🧠 Approach

### **Step 1: Read the Input Lines**

Use the `input()` function twice:

```python
a = input()
b = input()
```

- `a` stores the first line
- `b` stores the second line

---

### **Step 2: Print the Lines in Reverse Order**

Print the second line first, then the first line:

```python
print(b)
print(a)
```

---

## ✅ Solution

Here is the complete working solution:

```python
# This program reads two lines of input and prints them in reverse order
a = input()
b = input()
print(b)
print(a)
```

This program outputs the second input before the first, exactly as required.
