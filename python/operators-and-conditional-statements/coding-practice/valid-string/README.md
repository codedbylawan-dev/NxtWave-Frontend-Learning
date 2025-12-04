# ✅ **Valid String — Solved**

## **Question**

Write a program that reads a string **S** and checks if:

- The **length of S is between 2 and 7 (inclusive)**
  **OR**
- The **first character of S is NOT equal to "a"**

If **any one** of these conditions is true → print **"Valid String"**
Otherwise → print **"Not a Valid String"**

---

# 📘 **Outline**

### **Approach**

1. Read the input string
2. Check if the length is between 2 and 7
3. Check if the first character is not "a"
4. Print the result based on conditions

---

# 📘 **Step-by-Step Explanation**

### **Step 1: Read the input string**

```python
string = input()
```

---

### **Step 2: Check the length of the string**

Find the length:

```python
string_length = len(string)
```

Check if the length is **between 2 and 7 inclusive**:

```python
is_between = (string_length >= 2) and (string_length <= 7)
```

> Note:
> The original description says _between 2 and 7_, but examples show **2 to 7 inclusive** (apple = 5 → valid).
> So we correctly use `>= 2` and `<= 7`.

---

### **Step 3: Check if the first character is NOT "a"**

```python
is_not_equal = string[0] != "a"
```

---

### **Step 4: Print the result**

If **either** condition is true → Valid String
Else → Not a Valid String

```python
if is_between or is_not_equal:
    print("Valid String")
else:
    print("Not a Valid String")
```

---

# ✅ **Final Solution Code**

```python
string = input()

string_length = len(string)

is_between = (string_length >= 2) and (string_length <= 7)
is_not_equal = string[0] != "a"

if is_between or is_not_equal:
    print("Valid String")
else:
    print("Not a Valid String")
```

---

# 📌 **Examples**

### **Input**

```
apple
```

Length = 5 (✔)
First character = a (✖)
→ **Valid String**

---

### **Input**

```
atlantic
```

Length = 8 (✖)
First character = a (✖)
→ **Not a Valid String**

---

### **Input**

```
out
```

Length = 3 (✔)
→ **Valid String**

---
