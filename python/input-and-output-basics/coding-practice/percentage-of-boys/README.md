# **Question: Percentage of Boys**

Write a program that reads the percentage of girls in a class and prints the percentage of boys.
Total percentage = 100.

### **Input**

A single integer representing the percentage of girls.

### **Output**

A single integer representing the percentage of boys.

### **Explanation**

If girls = 30
Boys = 100 – 30 = **70**

---

# **Approach**

### **Step 1: Read the input**

```python
girls_percentage = input()
```

### **Step 2: Convert the input to integer**

```python
girls_percentage = int(girls_percentage)
```

### **Step 3: Calculate the percentage of boys**

```python
boys_percentage = 100 - girls_percentage
```

### **Step 4: Print the result**

```python
print(boys_percentage)
```

---

# **Complete Code**

```python
girls_percentage = input()
girls_percentage = int(girls_percentage)

boys_percentage = 100 - girls_percentage

print(boys_percentage)
```

---

# 🟩 **DRY RUN**

### **Input**

```
30
```

### **Execution**

1. `girls_percentage = "30"`
2. Convert to int → 30
3. `boys_percentage = 100 - 30` → 70
4. Print → **70**

### **Final Output**

```
70
```

---
