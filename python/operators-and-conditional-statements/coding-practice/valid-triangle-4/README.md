# ✅ **Valid Triangle — Solved**

## **Question**

Given three angles of a triangle, write a program to check whether the triangle is valid or not.
A triangle is valid **only if the sum of all three angles is exactly 180 degrees**.

---

# 📘 **Outline**

### **Approach**

1. Read the three angles
2. Calculate their sum
3. Check whether the sum is equal to 180
4. Print the correct result

---

# 📘 **Step-by-Step Explanation**

### **Step 1: Read the input values**

Read the three angles using `input()` and convert them to integers.

```python
first_angle = int(input())
second_angle = int(input())
third_angle = int(input())
```

---

### **Step 2: Calculate the sum of angles**

Add the three angles.

```python
sum_of_three_angles = first_angle + second_angle + third_angle
```

---

### **Step 3: Check if the triangle is valid**

A triangle is valid only if:

```
sum_of_three_angles == 180
```

Use an if–else condition to print the correct result.

```python
if sum_of_three_angles == 180:
    print("It's a Triangle")
else:
    print("It's not a Triangle")
```

---

# ✅ **Final Complete Program**

```python
first_angle = int(input())
second_angle = int(input())
third_angle = int(input())

sum_of_three_angles = first_angle + second_angle + third_angle

if sum_of_three_angles == 180:
    print("It's a Triangle")
else:
    print("It's not a Triangle")
```

---

# 📌 **Examples**

### **Input**

```
80
90
100
```

Sum = 270 (not equal to 180)

### **Output**

```
It's not a Triangle
```

---

### **Input**

```
60
60
60
```

Sum = 180

### **Output**

```
It's a Triangle
```

---
