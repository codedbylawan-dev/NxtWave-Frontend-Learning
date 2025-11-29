# **Question: First Part of a String**

Write a program that reads a string and prints the **first part of the string that has numbers**.

### **Input**

- A single string containing two parts:

  - The first part: digits
  - The second part: a single character

### **Output**

- The first part of the string as an integer

### **Explanation**

Example 1:
Input = `10y` → Output: `10`

Example 2:
Input = `2B` → Output: `2`

---

# **Approach**

### **Step 1: Read the input string**

```python
string = input()
```

### **Step 2: Find the length of the string**

```python
no_of_characters = len(string)
```

### **Step 3: Extract the first part of the string**

```python
end_index = no_of_characters - 1
number = string[:end_index]
```

### **Step 4: Convert the first part to an integer**

```python
number = int(number)
```

### **Step 5: Print the integer**

```python
print(number)
```

---

# **Complete Code**

```python
string = input()
no_of_characters = len(string)
end_index = no_of_characters - 1
number = string[:end_index]
number = int(number)
print(number)
```

---

# 🟩 **DRY RUN (Tabular Form)**

| Step No. | Operation              | Value / Explanation                               |
| -------- | ---------------------- | ------------------------------------------------- |
| 1        | Read input             | string = "10y"                                    |
| 2        | Length of string       | no_of_characters = len("10y") → 3                 |
| 3        | Find end index & slice | end_index = 3 - 1 → 2, number = string[:2] → "10" |
| 4        | Convert to integer     | number = int("10") → 10                           |
| 5        | Print result           | 10                                                |

---

### **Final Output**

```
10
```
