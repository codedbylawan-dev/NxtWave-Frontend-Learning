# 🔹 **Question: Zero or Positive or Negative**

Write a program that reads a number and checks whether it is:

- **Zero** → if the number is equal to 0
- **Positive** → if the number is greater than 0
- **Negative** → if the number is less than 0

---

# 🟦 **1. Approach**

1. Read the input number
2. Check if it is greater than 0 (Positive)
3. Check if it is less than 0 (Negative)
4. Otherwise, it must be equal to 0 (Zero)
5. Print the correct result

---

# 🟨 **2. Step-by-Step Explanation**

### **Step 1: Read the input number**

```python
number = int(input())
```

---

### **Step 2: Check if the number is Positive**

```python
if number > 0:
    print("Positive")
```

---

### **Step 3: Check if the number is Negative**

```python
elif number < 0:
    print("Negative")
```

---

### **Step 4: Otherwise, the number is Zero**

```python
else:
    print("Zero")
```

---

# 🟩 **3. Final Code**

```python
number = int(input())

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

---

# 🟥 **4. Dry Run Example**

### **Input**

```
-12
```

| Step             | Condition       | Result             |
| ---------------- | --------------- | ------------------ |
| Check number > 0 | -12 > 0 → False | Skip               |
| Check number < 0 | -12 < 0 → True  | Print **Negative** |

### **Output**

```
Negative
```

---
