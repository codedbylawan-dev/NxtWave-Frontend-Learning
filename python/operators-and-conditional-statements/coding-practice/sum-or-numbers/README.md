# ✅ **Sum of Numbers — Solved**

## **Question**

Write a program that reads two numbers **A** and **B**, and checks if **any one** of the conditions below is satisfied:

1️⃣ One of A or B is **less than 20**
2️⃣ The **sum** of A and B is **between 30 and 50**

### **Output**

- If **any** condition is satisfied → print **sum of A and B**
- Otherwise → print

  ```
  A
  B
  ```

---

# 📘 **Outline**

### **Approach**

1. Read numbers A and B
2. Check the two conditions
3. Print the correct output

---

# 📘 **Step-by-Step Explanation**

### **Step 1: Read the input numbers**

```python
first_number = int(input())
second_number = int(input())
```

---

### **Step 2: Check the conditions**

#### ✔ Condition 1: Any number is less than 20

```python
is_less_than = (first_number < 20) or (second_number < 20)
```

#### ✔ Condition 2: Sum is between 30 and 50 (exclusive)

```python
sum_of_numbers = first_number + second_number
is_sum_between = (sum_of_numbers > 30) and (sum_of_numbers < 50)
```

---

### **Step 3: Print the correct result**

- If **either** condition is true → print sum
- Otherwise → print A on one line, B on the next

```python
if is_less_than or is_sum_between:
    print(sum_of_numbers)
else:
    print(first_number)
    print(second_number)
```

---

# ✅ **Final Solution Code**

```python
first_number = int(input())
second_number = int(input())

is_less_than = (first_number < 20) or (second_number < 20)

sum_of_numbers = first_number + second_number
is_sum_between = (sum_of_numbers > 30) and (sum_of_numbers < 50)

if is_less_than or is_sum_between:
    print(sum_of_numbers)
else:
    print(first_number)
    print(second_number)
```

---

# 📌 **Examples**

### **Input**

```
45
7
```

7 < 20 → ✔
Sum = 52 → not between 30 & 50
Output:

```
52
```

---

### **Input**

```
30
100
```

Neither < 20 → ✖
Sum = 130 → not between 30 & 50 → ✖
Output:

```
30
100
```

---
