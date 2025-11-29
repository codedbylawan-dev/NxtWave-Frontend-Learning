# ✅ **Division of Two Numbers — Your Exact Format**

## **Question: Division of two numbers**

Write a program that reads two numbers A and B and prints the division of two numbers (A / B).

### **Input**

The first line of input contains an integer.
The second line of input contains an integer.

### **Output**

A single float value that is the division of A and B.

### **Explanation**

Example:
15 / 3 = 5.0
So output should be:

```
5.0
```

---

# ✅ **Approach**

### **Step 1: Read the input numbers**

Use input() to read both values.

```python
first_number = input()
second_number = input()
```

### **Step 2: Convert the input numbers to integers**

```python
first_number = int(first_number)
second_number = int(second_number)
```

### **Step 3: Divide the numbers and print the result**

```python
result = first_number / second_number
print(result)
```

---

# ✅ **Complete Code**

```python
first_number = input()
second_number = input()

first_number = int(first_number)
second_number = int(second_number)

result = first_number / second_number
print(result)
```

---

# 🟩 **DRY RUN (added at last exactly as you asked)**

### **Input**

```
5
2
```

### **Step-by-step Execution**

1. `first_number = input()` → `"5"`
2. `second_number = input()` → `"2"`
3. `first_number = int("5")` → 5
4. `second_number = int("2")` → 2
5. `result = 5 / 2` → 2.5
6. `print(result)` → **2.5**

### **Final Output**

```
2.5
```

---
