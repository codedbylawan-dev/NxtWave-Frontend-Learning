# 🔹 **Question: Required Number**

Write a program that reads a number **N** and checks whether:

### ✔ N is between **50 and 100**

**OR**

### ✔ The first digit of N is **7**

If any one of these is True → print **True**,
otherwise → print **False**.

---

# 🟦 **1. Question Explanation**

We must verify **two independent conditions**:

1. **Is N between 50 and 100?**
   → 50 < N < 100
2. **Is the first digit equal to 7?**
   → e.g., 72, 701, 7xx

If **any one** condition is True, output should be **True**.

---

# 🟩 **2. Approach**

1. Read N
2. Check if N is between 50 and 100
3. Extract first digit
4. Check if first digit == 7
5. Combine using **or**
6. Print result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read input**

```python
N = int(input())
```

### **Step 2: Check if N is between 50 and 100**

```python
is_between = (N > 50) and (N < 100)
```

### **Step 3: Extract the first digit**

Convert to string → pick index 0 → convert back to int:

```python
first_digit = int(str(N)[0])
```

### **Step 4: Check if first digit is 7**

```python
is_first_seven = (first_digit == 7)
```

### **Step 5: Combine**

```python
result = is_between or is_first_seven
```

### **Step 6: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
N = int(input())

is_between = (N > 50) and (N < 100)

first_digit = int(str(N)[0])
is_first_seven = (first_digit == 7)

result = is_between or is_first_seven

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
54
```

### **Dry Run**

| Step | Operation                         | Explanation               | Result |
| ---- | --------------------------------- | ------------------------- | ------ |
| 1    | N = 54                            | Input value               | 54     |
| 2    | is_between = 54 > 50 and 54 < 100 | True and True             | True   |
| 3    | first_digit = int("54"[0])        | First digit extracted → 5 | 5      |
| 4    | is_first_seven = 5 == 7           | False                     | False  |
| 5    | result = True or False            | One condition is True     | True   |
| 6    | print(result)                     | Output                    | True   |

### **Final Output**

```
True
```

---
