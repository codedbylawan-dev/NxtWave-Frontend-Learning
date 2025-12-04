# ✅ **Greatest Among Three Numbers — Solved**

## **Question**

You need to read three numbers **A**, **B**, and **C**, and print the greatest among them.

---

# 📘 **Outline**

### **Approach**

1. Read the three input numbers
2. Compare the numbers step by step
3. Store the greatest number
4. Print the greatest number

---

# 📘 **Step-by-Step Explanation**

### **Step 1: Read the input numbers**

We read A, B, and C using `input()` and convert them to integers.

```python
a = int(input())
b = int(input())
c = int(input())
```

---

### **Step 2: Find the greatest number**

#### ✔ Compare A and B

- If **A > B**, then the current greatest is **A**
- Otherwise, the current greatest is **B**

```python
if a > b:
    greatest_number = a
else:
    greatest_number = b
```

#### ✔ Compare C with the current greatest

If C is bigger, update the greatest number.

```python
if c > greatest_number:
    greatest_number = c
```

---

### **Step 3: Print the greatest number**

```python
print(greatest_number)
```

---

# ✅ **Final Complete Program**

```python
a = int(input())
b = int(input())
c = int(input())

if a > b:
    greatest_number = a
else:
    greatest_number = b

if c > greatest_number:
    greatest_number = c

print(greatest_number)
```

---

# 📌 **Examples**

### **Input**

```
2
5
7
```

Greatest is **7**

### **Output**

```
7
```

---

### **Input**

```
3
5
2
```

Greatest is **5**

### **Output**

```
5
```

---
