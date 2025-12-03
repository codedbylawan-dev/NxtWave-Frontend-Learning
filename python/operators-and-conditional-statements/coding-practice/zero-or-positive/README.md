# 🔹 **Question: Zero or Positive**

Write a program that:

- Prints **Zero** → if the number is equal to **0**
- Prints **Positive** → if the number is **greater than 0**

---

# 🟦 **1. Approach**

1. Read the number
2. Check if it is equal to 0
3. Otherwise, check if it is positive
4. Print the correct output

---

# 🟨 **2. Step-by-Step Explanation**

### **Step 1: Read the input**

```python
number = int(input())
```

---

### **Step 2: Check if number is equal to 0**

```python
if number == 0:
    print("Zero")
```

---

### **Step 3: Check if number is positive**

```python
elif number > 0:
    print("Positive")
```

`elif` ensures only one correct output is printed.

---

# 🟩 **3. Final Code**

```python
number = int(input())

if number == 0:
    print("Zero")
elif number > 0:
    print("Positive")
```

---

# 🟥 **4. Dry Run Example**

### **Input**

```
56
```

| Step              | Condition       | Result             |
| ----------------- | --------------- | ------------------ |
| Check number == 0 | 56 == 0 → False | Skip               |
| Check number > 0  | 56 > 0 → True   | Print **Positive** |

### **Output**

```
Positive
```

---
