# 🔹 **Question: Relation b/w Numbers**

Write a program that compares two integers **X** and **Y** and prints:

- **"X < Y"** if X is less than Y
- **"X >= Y"** otherwise

---

# 🟦 **1. Question Explanation**

You only need to determine the **relationship** between two numbers.

### Conditions:

- If X < Y → print **X < Y**
- Otherwise → print **X >= Y**

Examples:

- 2 and 5 → X < Y
- 5 and 2 → X >= Y

---

# 🟩 **2. Approach**

1. Read X and Y
2. Compare the values
3. Print the correct relationship

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1 — Read inputs**

```python
x = int(input())
y = int(input())
```

### **Step 2 — Compare**

```python
if x < y:
```

### **Step 3 — Print result**

```python
    print("X < Y")
else:
    print("X >= Y")
```

---

# 🟧 **4. Final Code**

```python
x = int(input())
y = int(input())

if x < y:
    print("X < Y")
else:
    print("X >= Y")
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Sample Input**

```
2
5
```

### **Dry Run Table**

| Step | Operation      | Explanation      | Result |
| ---- | -------------- | ---------------- | ------ |
| 1    | x = 2          | Read X           | 2      |
| 2    | y = 5          | Read Y           | 5      |
| 3    | 2 < 5 → True   | Compare values   | True   |
| 4    | print("X < Y") | X is less than Y | X < Y  |

### **Final Output**

```
X < Y
```

---
