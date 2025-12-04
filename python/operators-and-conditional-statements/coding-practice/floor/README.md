# 🔹 **Question: Floor**

Write a program that reads a Room Number (like **R1**, **R27**, **R401**) and checks if the **number part** of the Room Number is **less than 30**.

### ✔ If the number is less than 30 → print

**Ground Floor**

### ✖ Otherwise → print

**Not Ground Floor**

---

# 🟦 **1. Explanation**

Room numbers always start with the letter **R**, and the remaining part is the actual number.

Example:
Room `"R27"`

- First character = `'R'`
- Remaining characters = `"27"` → convert to number → `27`

### Condition:

- If **number < 30** → Ground Floor
- Else → Not Ground Floor

---

# 🟩 **2. Approach**

1. Read the Room Number as a string.
2. Remove the first character `'R'`.
3. Convert the remaining part to an integer.
4. Check if the number is less than 30.
5. Print the correct output.

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read the Room Number**

```python
room_number = input()
```

### **Step 2: Extract the number part**

```python
number = room_number[1:]       # takes everything after 'R'
number = int(number)           # convert string → integer
```

### **Step 3: Check if the number is less than 30**

```python
if number < 30:
    print("Ground Floor")
else:
    print("Not Ground Floor")
```

---

# 🟧 **4. Final Code**

```python
room_number = input()

number = room_number[1:]
number = int(number)

if number < 30:
    print("Ground Floor")
else:
    print("Not Ground Floor")
```

---

# 🟥 **5. Dry Run Example**

### Input:

```
R27
```

| Part        | Value           |
| ----------- | --------------- |
| room_number | `"R27"`         |
| number part | `"27"` → **27** |
| Check       | 27 < 30 → ✔     |

### Output:

```
Ground Floor
```

---
