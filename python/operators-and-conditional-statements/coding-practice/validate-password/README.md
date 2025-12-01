# ✅ **Validate Password — Full Solution**

## **Question: Validate Password**

Write a program to check if the given string is a valid password.
A password is **valid if the number of characters is greater than 7**.

---

# ✅ **Approach**

### **Step 1:** Read the input password

### **Step 2:** Calculate the length

### **Step 3:** Check if length > 7

### **Step 4:** Print True / False

---

# ✅ **Step-by-Step Explanation**

### **Step 1: Read input**

```python
password = input()
```

### **Step 2: Length of password**

```python
length_of_the_password = len(password)
```

### **Step 3: Validate password**

```python
is_valid_password = length_of_the_password > 7
```

### **Step 4: Print result**

```python
print(is_valid_password)
```

---

# ✅ **Final Code**

```python
password = input()
length_of_the_password = len(password)
is_valid_password = length_of_the_password > 7
print(is_valid_password)
```

---

# ✅ **Dry Run (Tabular Form)**

### **Dry Run 1 — Input: passwd**

| Step | Variable / Action         | Value      |
| ---- | ------------------------- | ---------- |
| 1    | password                  | `"passwd"` |
| 2    | length_of_the_password    | `6`        |
| 3    | is_valid_password = 6 > 7 | `False`    |
| 4    | Output                    | `False`    |

---

### **Dry Run 2 — Input: 1q2w3e4r**

| Step | Variable / Action         | Value        |
| ---- | ------------------------- | ------------ |
| 1    | password                  | `"1q2w3e4r"` |
| 2    | length_of_the_password    | `8`          |
| 3    | is_valid_password = 8 > 7 | `True`       |
| 4    | Output                    | `True`       |

---
