# **Question: Second Part of a String**

Write a program that reads a string and prints the **second part of the string that has digits**.

### **Input**

- A single string containing two parts:

  - The first part: first two characters (letters)
  - The second part: remaining characters (digits)

### **Output**

- The second part of the string as an integer

### **Explanation**

Example 1:
Input = `OF63` → Output: `63`

Example 2:
Input = `ab395` → Output: `395`

---

# **Approach**

### **Step 1: Read the input string**

```python
string = input()
```

### **Step 2: Extract the second part of the string**

```python
start_index = 2
number = string[start_index:]
```

### **Step 3: Convert the second part to an integer**

```python
number = int(number)
```

### **Step 4: Print the result**

```python
print(number)
```

---

# **Complete Code**

```python
string = input()
start_index = 2
number = string[start_index:]
number = int(number)
print(number)
```

---

# 🟩 **DRY RUN (Tabular Form)**

| Step No. | Operation               | Value / Explanation                         |
| -------- | ----------------------- | ------------------------------------------- |
| 1        | Read input              | string = "OF63"                             |
| 2        | Set start index & slice | start_index = 2, number = string[2:] → "63" |
| 3        | Convert to integer      | number = int("63") → 63                     |
| 4        | Print result            | 63                                          |

---

### **Final Output**

```
63
```
