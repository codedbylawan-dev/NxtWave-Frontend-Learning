# ✅ **Question: Area and Perimeter of Square**

You are given the **side length of a square** as input.
Your task is to **calculate and print**:

1. **Area** = side × side
2. **Perimeter** = 4 × side

---

# ✅ **Approach**

### **Step 1: Read the Input**

Read the side of the square as an integer.

```python
side = int(input())
```

---

### **Step 2: Calculate Area**

Area of a square = side × side

```python
area = side * side
```

---

### **Step 3: Calculate Perimeter**

Perimeter of a square = 4 × side

```python
perimeter = 4 * side
```

---

### **Step 4: Print the Result**

Print the area and perimeter as per the required format.

```python
print("Area of the square is:", area)
print("Perimeter of the square is:", perimeter)
```

---

# ✅ **Complete Code**

```python
side = int(input())
area = side * side
perimeter = 4 * side
print("Area of the square is:", area)
print("Perimeter of the square is:", perimeter)
```

---

# 🟩 **DRY RUN (Tabular Form)**

Assume Input:

```
3
```

| Step | Operation           | Expression                               | Result                         |
| ---- | ------------------- | ---------------------------------------- | ------------------------------ |
| 1    | Read side           | side = 3                                 | 3                              |
| 2    | Calculate area      | 3 × 3                                    | 9                              |
| 3    | Calculate perimeter | 4 × 3                                    | 12                             |
| 4    | Print area          | print("Area of the square is:", 9)       | Area of the square is: 9       |
| 5    | Print perimeter     | print("Perimeter of the square is:", 12) | Perimeter of the square is: 12 |

---

### ✅ **Final Output**

```
Area of the square is: 9
Perimeter of the square is: 12
```
