# **Question: Division of two numbers - 2**

Write a program that reads two numbers A and B and prints the division of two numbers (A / B) as an integer.

### **Input**

The first line of input contains an integer.
The second line of input contains an integer.

### **Output**

A single integer which is the integer value of the division result.

### **Explanation**

Example:
21 / 4 = 5.25 → integer part is **5**
So output = **5**.

---

# **Approach**

### **Step 1: Read the input numbers**

```python
first_number = input()
second_number = input()
```

### **Step 2: Convert the input numbers to integers**

```python
first_number = int(first_number)
second_number = int(second_number)
```

### **Step 3: Divide the numbers and convert the result to an integer**

```python
result = first_number / second_number
result = int(result)
```

### **Step 4: Print the result**

```python
print(result)
```

---

# **Complete Code**

```python
first_number = input()
second_number = input()

first_number = int(first_number)
second_number = int(second_number)

result = first_number / second_number
result = int(result)

print(result)
```

---

# 🟩 **DRY RUN**

### **Input**

```
21
4
```

### **Execution**

1. `first_number = "21"`
2. `second_number = "4"`
3. Convert to int → 21 and 4
4. `result = 21 / 4` → 5.25
5. Convert to int → **5**

### **Final Output**

```
5
```

---
