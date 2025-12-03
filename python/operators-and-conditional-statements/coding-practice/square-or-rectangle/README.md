# 🔹 **Question: Square or Rectangle**

You are given the **length** and **breadth** of a box.
You must determine whether the box is a **Square** or a **Rectangle**.

---

# 🟦 **1. Question Explanation**

- If **length == breadth** → print **"Square"**
- Otherwise → print **"Rectangle"**

Example:

- Length = 6, Breadth = 6 → Square
- Length = 5, Breadth = 10 → Rectangle

---

# 🟩 **2. Approach**

1. Read the length
2. Read the breadth
3. Compare them using `==`
4. Print the correct type

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1 — Read the inputs**

```python
length = int(input())
breadth = int(input())
```

### **Step 2 — Compare length and breadth**

```python
if length == breadth:
```

### **Step 3 — Print the correct result**

```python
    print("Square")
else:
    print("Rectangle")
```

---

# 🟧 **4. Final Code**

```python
length = int(input())
breadth = int(input())

if length == breadth:
    print("Square")
else:
    print("Rectangle")
```

---

# 🟥 **5. Dry Run (Preview Table)**

### **Sample Input**

```
6
6
```

### **Dry Run Table**

| Step | Operation               | Explanation         | Result |
| ---- | ----------------------- | ------------------- | ------ |
| 1    | length = 6              | Read first input    | 6      |
| 2    | breadth = 6             | Read second input   | 6      |
| 3    | Compare → 6 == 6 → True | Both sides equal    | True   |
| 4    | print("Square")         | Condition satisfied | Square |

### **Final Output**

```
Square
```

---
