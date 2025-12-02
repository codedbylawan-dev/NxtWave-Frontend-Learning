# 🔹 **Question: Women**

Write a program that reads **three strings A, B, and C**, and checks whether **at least one** of them is equal to the word **"woman"**.

### **Input**

- First line → string A
- Second line → string B
- Third line → string C

### **Output**

Print **True** if **any one** of the three strings is exactly `"woman"`.
Otherwise print **False**.

---

# 🟦 **1. Question Explanation**

You need to check three separate comparisons:

### ✔ Condition 1: `A == "woman"`

### ✔ Condition 2: `B == "woman"`

### ✔ Condition 3: `C == "woman"`

If **any one** is True → output **True**.

Use `or` to combine them.

---

# 🟩 **2. Approach**

1. Read the three input strings.
2. Compare each one with `"woman"`.
3. If any match is found → result is True.
4. Otherwise → result is False.
5. Print the result.

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
A = input()
B = input()
C = input()
```

### **Step 2: Compare each with "woman"**

```python
is_A_woman = A == "woman"
is_B_woman = B == "woman"
is_C_woman = C == "woman"
```

### **Step 3: Combine using OR**

```python
result = is_A_woman or is_B_woman or is_C_woman
```

### **Step 4: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
A = input()
B = input()
C = input()

is_A_woman = (A == "woman")
is_B_woman = (B == "woman")
is_C_woman = (C == "woman")

result = is_A_woman or is_B_woman or is_C_woman

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
man
woman
man
```

### **Dry Run**

| Step | Code/Operation                    | Explanation           | Value/Result |
| ---- | --------------------------------- | --------------------- | ------------ |
| 1    | `A = input()`                     | Read first string     | "man"        |
| 2    | `B = input()`                     | Read second string    | "woman"      |
| 3    | `C = input()`                     | Read third string     | "man"        |
| 4    | `A == "woman"`                    | Check if A is "woman" | False        |
| 5    | `B == "woman"`                    | Check if B is "woman" | True         |
| 6    | `C == "woman"`                    | Check if C is "woman" | False        |
| 7    | `result = False or True or False` | At least one is True  | True         |
| 8    | `print(result)`                   | Output result         | True         |

### **Final Output**

```
True
```

---
