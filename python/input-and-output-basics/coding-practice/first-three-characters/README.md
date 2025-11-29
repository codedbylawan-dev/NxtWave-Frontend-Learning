# **Question: First Three Characters**

Write a program to read a single line of input and print the **first three characters** in it.

### **Input**

- A single line of input string.

### **Output**

- First three characters of the input string.

### **Explanation**

Example 1:
Input = `Four` → Output: `Fou`

Example 2:
Input = `Strawberry` → Output: `Str`

---

# **Approach**

### **Step 1: Read input**

```python
message = input()
```

### **Step 2: Get the first three characters**

```python
part = message[:3]
```

### **Step 3: Print the result**

```python
print(part)
```

---

# **Complete Code**

```python
message = input()

part = message[:3]

print(part)
```

---

# 🟩 **DRY RUN (Tabular Form)**

| Step No. | Operation           | Value / Explanation        |
| -------- | ------------------- | -------------------------- |
| 1        | Read input          | message = "Strawberry"     |
| 2        | Slice first 3 chars | part = message[:3] → "Str" |
| 3        | Print result        | Str                        |

---

### **Final Output**

```
Str
```
