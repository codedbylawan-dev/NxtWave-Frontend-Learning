# **Simple Square – Solved**

### **Question:**

Write a program that prints a simple square using stars (\*).

---

## **Input**

(No input for this problem.)

---

## **Output**

```
* * *
* * *
* * *
```

---

## **Explanation**

You need to print a **3×3 square** where:

- Each line has **three stars** separated by spaces.
- There are **three lines** total.

So the same line `* * *` is printed three times.

---

# **Approach**

### **Step 1:** No input needed

Pattern is fixed.

### **Step 2:** Prepare the line

Each row must contain:  
`* * *`

### **Step 3:** Print the line three times

Use three print statements.

---

# **Step-by-Step Explanation**

### **Step 1: No input**

We don’t read anything.

### **Step 2: Store the pattern**

```python
line = "* * *"
```

### **Step 3: Print the pattern 3 times**

```python
print(line)
print(line)
print(line)
```

---

# **Solution (Final Code)**

```python
print("* * *")
print("* * *")
print("* * *")
```

---
