# 🔹 **Question: Not Greater than 100**

Write a program that reads two integers **A** and **B**, and checks if the **sum** of A and B is **not greater than 100**.

### **Input**

- First line → integer **A**
- Second line → integer **B**

### **Output**

Print **True** if the sum of A and B is **not greater than 100** (i.e., ≤ 100), otherwise print **False**.

---

# 🟦 **1. Question Explanation**

You must compute the sum `S = A + B` and check whether `S` is **not greater than 100**.
That condition is equivalent to `S <= 100`. If true → print `True`; otherwise → print `False`.

This problem practices:

- Arithmetic (addition)
- Comparison operators (`<=`)
- Boolean output

---

# 🟩 **2. Approach**

1. Read integers A and B from input.
2. Compute their sum `S = A + B`.
3. Evaluate if `S <= 100`.
4. Store the boolean result.
5. Print the result.

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs and convert**

```python
first_number = int(input())
second_number = int(input())
```

### **Step 2: Calculate sum**

```python
sum_of_numbers = first_number + second_number
```

### **Step 3: Check condition (not greater than 100)**

```python
result = sum_of_numbers <= 100
```

### **Step 4: Print result**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
first_number = int(input())
second_number = int(input())

sum_of_numbers = first_number + second_number
result = sum_of_numbers <= 100

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
30
20
```

### **Dry Run**

| Step | Code/Operation                                  | Explanation                               | Value/Result |
| ---- | ----------------------------------------------- | ----------------------------------------- | ------------ |
| 1    | `first_number = int(input())`                   | Read first number and convert to integer  | 30           |
| 2    | `second_number = int(input())`                  | Read second number and convert to integer | 20           |
| 3    | `sum_of_numbers = first_number + second_number` | Compute the sum                           | 50           |
| 4    | `sum_of_numbers <= 100`                         | Check if sum is not greater than 100      | True         |
| 5    | `print(result)`                                 | Print the final boolean result            | True         |

### **Final Output**

```
True
```

---
