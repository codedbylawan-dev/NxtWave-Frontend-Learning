# **Question: Subtraction of two numbers**

Write a program that reads two numbers A and B and prints the subtraction of two numbers (A - B).

### **Input**

The first line of input contains a float.
The second line of input contains a float.

### **Output**

A single float which is the subtraction result (A - B).

### **Explanation**

Example: For inputs 15.55 and 6.23, output is 9.32 because 15.55 - 6.23 = 9.32.

---

# **Approach**

### **Step 1: Read the input numbers**

```python
first_num = input()
second_num = input()
```

### **Step 2: Convert the input numbers to float**

```python
first_num = float(first_num)
second_num = float(second_num)
```

### **Step 3: Subtract the numbers and print the result**

```python
diff = first_num - second_num
print(diff)
```

---

# **Complete Code**

```python
first_num = input()
second_num = input()

first_num = float(first_num)
second_num = float(second_num)

diff = first_num - second_num
print(diff)
```

---

# 🟩 **DRY RUN**

### **Input**

```
15.55
6.23
```

### **Execution**

1. `first_num = "15.55"`
2. `second_num = "6.23"`
3. Convert to float → `15.55` and `6.23`
4. `diff = 15.55 - 6.23` → `9.32`

### **Final Output**

```
9.32
```

---
