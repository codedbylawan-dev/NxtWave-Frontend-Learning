# 🔹 **Question: Increment the Number**

Write a program that reads a number **N** and checks if **N is greater than 10**.

- If **N > 10**, print **N + 5**
- Otherwise, print **N + 1**

---

# 🟦 **1. Question Explanation**

The program must:

- Read an integer **N**
- Check if **N is greater than 10**
- If yes → output **N + 5**
- If no → output **N + 1**

---

# 🟩 **2. Approach**

1. Read input number
2. Use an **if condition** to check whether N > 10
3. Add **5** or **1** based on the condition
4. Print the final result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read the input number**

```python
number = int(input())
```

### **Step 2: Check if number is greater than 10**

```python
if number > 10:
```

### **Step 3: Increment based on condition**

```python
if number > 10:
    number = number + 5
else:
    number = number + 1
```

### **Step 4: Print the updated number**

```python
print(number)
```

---

# 🟧 **4. Final Code**

```python
number = int(input())

if number > 10:
    number = number + 5
else:
    number = number + 1

print(number)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### For input: **3**

| Step | Code / Operation    | Explanation                    | Value |
| ---- | ------------------- | ------------------------------ | ----- |
| 1    | number = 3          | Read input                     | 3     |
| 2    | number > 10?        | 3 > 10 → False                 | —     |
| 3    | number = number + 1 | Add 1 since condition is false | 4     |
| 4    | print(number)       | Output value                   | **4** |

**Final Output → 4**

---
