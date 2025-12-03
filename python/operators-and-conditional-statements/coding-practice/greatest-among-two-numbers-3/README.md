# 🔹 **Question: Greatest Among Two Numbers – 3**

Write a program that reads two integers **A** and **B**, and prints the **greater** of the two numbers.

---

# 🟦 **1. Question Explanation**

You must compare the two numbers:

- If **A > B**, print **A**
- Otherwise, print **B**

This problem tests:
✓ Input handling
✓ Comparison between two numbers
✓ Using conditional statements

---

# 🟩 **2. Approach**

1. Read the two numbers
2. Compare them using an `if` statement
3. Store the greater number
4. Print the greater number

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1 — Read input**

```python
first_number = int(input())
second_number = int(input())
```

### **Step 2 — Compare the numbers**

```python
if first_number > second_number:
    greater_number = first_number
else:
    greater_number = second_number
```

### **Step 3 — Print result**

```python
print(greater_number)
```

---

# 🟧 **4. Final Code**

```python
first_number = int(input())
second_number = int(input())

if first_number > second_number:
    greater_number = first_number
else:
    greater_number = second_number

print(greater_number)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Sample Input**

```
4
3
```

### **Dry Run Table**

| Step | Operation             | Explanation                   | Result |
| ---- | --------------------- | ----------------------------- | ------ |
| 1    | first_number = 4      | Read input                    | 4      |
| 2    | second_number = 3     | Read input                    | 3      |
| 3    | 4 > 3 → True          | Check which number is greater | True   |
| 4    | greater_number = 4    | Assign greater value          | 4      |
| 5    | print(greater_number) | Output                        | 4      |

### **Final Output**

```
4
```

---
