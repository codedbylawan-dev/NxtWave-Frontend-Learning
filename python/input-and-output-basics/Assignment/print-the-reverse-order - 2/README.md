# **Print in Reverse Order - 2 (Solved)**

**Easy**

---

## **Question:**

Write a program that reads two words **A** and **B**, and prints them in **reverse order** separated by `###`.

---

## **Input**

- First line → A
- Second line → B

## **Output**

1. First line → B
2. Second line → `###`
3. Third line → A

---

## **Explanation**

Example 1:
A = `Cat`
B = `Rat`

Output should be:

```
Rat
###
Cat
```

Example 2:
A = `Train`
B = `Bus`

Output:

```
Bus
###
Train
```

---

# 🧭 **Approach**

### **Step 1:** Read A

### **Step 2:** Read B

### **Step 3:** Print B

### **Step 4:** Print `###`

### **Step 5:** Print A

---

# 📝 **Step-by-Step Explanation**

### **Step 1: Read A**

```python
A = input()
```

### **Step 2: Read B**

```python
B = input()
```

### **Step 3: Print B**

```python
print(B)
```

### \*\*Step 4: Print

```python
print("###")
```

### **Step 5: Print A**

```python
print(A)
```

---

# ✅ **Final Solution**

```python
A = input()
B = input()
print(B)
print("###")
print(A)
```

---
