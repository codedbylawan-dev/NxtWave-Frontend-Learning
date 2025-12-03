# 🔹 **Question: Compare with Ten – 2**

Write a program that reads three integers **A**, **B**, and **C**, and checks whether:

### ✅ The **sum of every pair** of numbers is **greater than 10**

The three required conditions are:

1. A + B > 10
2. B + C > 10
3. C + A > 10

If **all three** are True → output **True**,
otherwise → output **False**.

---

# 🟦 **1. Question Explanation**

There are **three possible pairs**:

| Pair  | Sum          |
| ----- | ------------ |
| A + B | Must be > 10 |
| B + C | Must be > 10 |
| C + A | Must be > 10 |

We must ensure **every** pair satisfies the rule.

Final condition:

```
(A + B > 10) AND (B + C > 10) AND (C + A > 10)
```

---

# 🟩 **2. Approach**

1. Read three numbers
2. Compute the three pairwise sums
3. Compare each with 10
4. Check if all conditions are True
5. Print the final result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1: Read inputs**

```python
A = int(input())
B = int(input())
C = int(input())
```

### **Step 2: Compute sums**

```python
sum_AB = A + B
sum_BC = B + C
sum_CA = C + A
```

### **Step 3: Compare each sum**

```python
is_AB = sum_AB > 10
is_BC = sum_BC > 10
is_CA = sum_CA > 10
```

### **Step 4: Combine**

```python
result = is_AB and is_BC and is_CA
```

### **Step 5: Print**

```python
print(result)
```

---

# 🟧 **4. Final Code**

```python
A = int(input())
B = int(input())
C = int(input())

sum_AB = A + B
sum_BC = B + C
sum_CA = C + A

is_AB = sum_AB > 10
is_BC = sum_BC > 10
is_CA = sum_CA > 10

result = is_AB and is_BC and is_CA

print(result)
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Input**

```
4
8
17
```

### **Dry Run**

| Step | Operation                         | Explanation              | Value/Result |
| ---- | --------------------------------- | ------------------------ | ------------ |
| 1    | `A = 4`                           | Read first number        | 4            |
| 2    | `B = 8`                           | Read second number       | 8            |
| 3    | `C = 17`                          | Read third number        | 17           |
| 4    | `sum_AB = A + B`                  | 4 + 8                    | 12           |
| 5    | `sum_BC = B + C`                  | 8 + 17                   | 25           |
| 6    | `sum_CA = C + A`                  | 17 + 4                   | 21           |
| 7    | `is_AB = 12 > 10`                 | True                     | True         |
| 8    | `is_BC = 25 > 10`                 | True                     | True         |
| 9    | `is_CA = 21 > 10`                 | True                     | True         |
| 10   | `result = True and True and True` | All conditions satisfied | True         |
| 11   | `print(result)`                   | Output                   | True         |

### **Final Output**

```
True
```

---
