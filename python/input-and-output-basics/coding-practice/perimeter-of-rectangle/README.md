# **Question: Perimeter of Rectangle**

Write a program to calculate the perimeter of a rectangle.
**Formula:** Perimeter = 2 × (Length + Breadth)

### **Input**

- First line: length of rectangle (integer)
- Second line: breadth of rectangle (integer)

### **Output**

Print the perimeter of the rectangle.

### **Explanation**

Example:
Length = 3, Breadth = 4
Perimeter = 2 × (3 + 4) = 2 × 7 = **14**

---

# **Approach**

### **Step 1: Read the input values**

```python
length = input()
breadth = input()
```

### **Step 2: Convert the inputs to integers**

```python
length = int(length)
breadth = int(breadth)
```

### **Step 3: Add length and breadth**

```python
sum_of_two_sides = length + breadth
```

### **Step 4: Calculate the perimeter**

```python
perimeter = sum_of_two_sides * 2
```

### **Step 5: Print the perimeter**

```python
print(perimeter)
```

---

# **Complete Code**

```python
length = input()
breadth = input()

length = int(length)
breadth = int(breadth)

sum_of_two_sides = length + breadth
perimeter = sum_of_two_sides * 2

print(perimeter)
```

---

# 🟩 **DRY RUN**

### **Input**

```
3
4
```

### **Execution**

1. `length = input()` → `"3"`
2. `breadth = input()` → `"4"`
3. `length = int("3")` → 3
4. `breadth = int("4")` → 4
5. `sum_of_two_sides = 3 + 4` → 7
6. `perimeter = 7 * 2` → 14
7. `print(perimeter)` → **14**

### **Final Output**

```
14
```

---
