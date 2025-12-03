# 🔹 **Question: Equal Numbers**

Write a program to check whether two given numbers are equal.

---

# 🟦 **1. Question Explanation**

You will receive **two inputs**:

- If both numbers are equal → print **"Equal"**
- If they are not equal → print **"Not Equal"**

Examples:

- 5 and 5 → Equal
- 10 and 5 → Not Equal

---

# 🟩 **2. Approach**

1. Read both numbers
2. Compare them using `==`
3. Print the correct result

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1 — Read two numbers**

```python
first_number = int(input())
second_number = int(input())
```

### **Step 2 — Compare**

```python
if first_number == second_number:
```

### **Step 3 — Print result**

```python
    print("Equal")
else:
    print("Not Equal")
```

---

# 🟧 **4. Final Code**

```python
first_number = int(input())
second_number = int(input())

if first_number == second_number:
    print("Equal")
else:
    print("Not Equal")
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Sample Input**

```
5
5
```

### **Dry Run Table**

| Step | Operation         | Explanation             | Result |
| ---- | ----------------- | ----------------------- | ------ |
| 1    | first_number = 5  | Read first number       | 5      |
| 2    | second_number = 5 | Read second number      | 5      |
| 3    | 5 == 5 → True     | Compare the two values  | True   |
| 4    | print("Equal")    | Since condition is true | Equal  |

### **Final Output**

```
Equal
```

---
