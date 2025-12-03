# 🔹 **Question: Positive Integer**

Write a program that reads an integer.

- If the number is **negative**, convert it to **positive** and print it.
- If it is **already positive**, print it as it is.

---

# 🟦 **1. Question Explanation**

The problem asks you to ensure the output is **always a positive number**.

- If input = **-5**, output → **5**
- If input = **39**, output → **39**

This tests your understanding of:
✓ Conditional statements
✓ Checking negatives
✓ Converting to positive

---

# 🟩 **2. Approach**

1. Read the input number
2. Check if it is negative
3. If negative → multiply by -1
4. Print the positive result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read the input**

```python
number = int(input())
```

### **Step 2: Check if the number is negative**

```python
if number < 0:
```

### **Step 3: Convert to positive if needed**

```python
    number = number * (-1)
```

### **Step 4: Print the result**

```python
print(number)
```

---

# 🟧 **4. Final Code**

```python
number = int(input())

if number < 0:
    number = number * (-1)

print(number)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Sample Input**

```
-5
```

### **Dry Run Table**

| Step | Operation         | Explanation                           | Result |
| ---- | ----------------- | ------------------------------------- | ------ |
| 1    | number = -5       | Read input                            | -5     |
| 2    | number < 0 → True | Condition satisfied (negative number) | True   |
| 3    | number = -5 \* -1 | Convert to positive                   | 5      |
| 4    | print(number)     | Print final value                     | 5      |

### **Final Output**

```
5
```

---
