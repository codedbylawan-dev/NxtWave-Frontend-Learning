# **Question: Area of a Rectangle**

Write a program to calculate the area of a rectangle.
**Formula:** Area = Length × Breadth

### **Input**

The first line contains the length (integer).
The second line contains the breadth (integer).

### **Output**

Print the area of the rectangle.

### **Explanation**

If length = 4 and breadth = 3 → Area = 4 × 3 = **12**

---

# **Approach**

### **Step 1: Read the input values**

```python
length = input()
breadth = input()
```

### **Step 2: Convert the input values to integers**

```python
length = int(length)
breadth = int(breadth)
```

### **Step 3: Calculate the area**

```python
area = length * breadth
```

### **Step 4: Print the area**

```python
print(area)
```

---

# **Complete Code**

```python
length = input()
breadth = input()

length = int(length)
breadth = int(breadth)

area = length * breadth
print(area)
```

---

# 🟩 **DRY RUN (added exactly at the end)**

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
5. `area = 3 * 4` → 12
6. `print(area)` → **12**

### **Final Output**

```
12
```

---
