# 🔹 **Question: Not Negative**

Write a program that reads two integers **A** and **B**, and checks whether **both** numbers are **not negative**.

A number is **not negative** if it is **greater than or equal to 0**.

### **Input**

- First line → integer A
- Second line → integer B

### **Output**

Print **True** if **both** numbers are **not negative**,
otherwise print **False**.

---

# 🟦 **1. Question Explanation**

A number is “not negative” when:

```
number >= 0
```

So you must confirm:

### ✔ Condition 1: A >= 0

### ✔ Condition 2: B >= 0

Final result:

```
(A >= 0) AND (B >= 0)
```

Only if **both** are True → output should be **True**.

---

# 🟩 **2. Approach**

1. Read A and B
2. Check if A is not negative
3. Check if B is not negative
4. Combine using `and`
5. Print the final result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read input numbers**

```python
A = int(input())
B = int(input())
```

### **Step 2: Check each number**

```python
is_A_not_negative = A >= 0
is_B_not_negative = B >= 0
```

### **Step 3: Combine**

```python
result = is_A_not_negative and is_B_not_negative
```

### **Step 4: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
A = int(input())
B = int(input())

is_A_not_negative = A >= 0
is_B_not_negative = B >= 0

result = is_A_not_negative and is_B_not_negative

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
5
10
```

### **Dry Run**

| Step | Code/Operation           | Explanation                 | Value/Result |
| ---- | ------------------------ | --------------------------- | ------------ |
| 1    | `A = int(input())`       | Read first number           | 5            |
| 2    | `B = int(input())`       | Read second number          | 10           |
| 3    | `A >= 0`                 | Check if 5 is not negative  | True         |
| 4    | `B >= 0`                 | Check if 10 is not negative | True         |
| 5    | `result = True and True` | Both must be not negative   | True         |
| 6    | `print(result)`          | Output result               | True         |

### **Final Output**

```
True
```

---
