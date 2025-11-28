# **Second Word in First Word (Solved)**

**Medium**

---

## **Question:**

Write a program that reads two words **W1** and **W2**.
W2 appears at the _beginning_ of W1.
You must print the **index where W2 ends** inside W1.

---

## **Input**

- First line → W1
- Second line → W2

## **Output**

- A single integer → the index at which W2 ends in W1

---

## **Explanation**

Example:
W1 = `Midterm`
W2 = `Mid`

Index positions:

```
M  i  d  t  e  r  m
0  1  2  3  4  5  6
```

- The word **Mid** ends at index **2**
- So the output is:

```
2
```

Another example:
W1 = `Unkind`
W2 = `Un`

Indexes:

```
U  n  k  i  n  d
0  1  2  3  4  5
```

W2 ends at index **1**

---

# 🧭 **Approach**

### **Step 1:** Read W1

Use `input()` to read the first word.

### **Step 2:** Read W2

Use `input()` again to read the second word.

### **Step 3:** Find the length of W2

The last index of W2 will be:

```
length_of_W2 - 1
```

### **Step 4:** Print the ending index

---

# 📝 **Step-by-Step Explanation**

### **Step 1: Read W1**

```python
W1 = input()
```

### **Step 2: Read W2**

```python
W2 = input()
```

### **Step 3: Get length of W2**

```python
length_W2 = len(W2)
```

### **Step 4: Calculate ending index**

```python
end_index = length_W2 - 1
```

### **Step 5: Print result**

```python
print(end_index)
```

---

# ✅ **Final Solution**

```python
W1 = input()
W2 = input()
length_W2 = len(W2)
end_index = length_W2 - 1
print(end_index)
```

---
