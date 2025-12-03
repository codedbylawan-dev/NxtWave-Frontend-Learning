# 🔹 **Question: Pair of Numbers**

You are given two integers **A** and **B**.
You must print **Pair** if:

- **Both A and B ≤ 1000**
  **OR**
- **B > 500**

Otherwise, print **Not a Pair**.

---

# 🟦 **1. Question Explanation**

We evaluate **two conditions**:

1️⃣ **A ≤ 1000 AND B ≤ 1000**
2️⃣ **B > 500**

If **any** of these is true → output **Pair**
Else → **Not a Pair**

---

# 🟩 **2. Approach**

1. Read inputs A and B
2. Check both-number ≤ 1000 condition
3. Check B > 500 condition
4. Combine using **or**
5. Print the correct message

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1 — Read inputs**

```python
first_number = int(input())
second_number = int(input())
```

### **Step 2 — Condition 1: Both numbers ≤ 1000**

```python
is_less_than_or_equal_to = (first_number <= 1000) and (second_number <= 1000)
```

### **Step 3 — Condition 2: B > 500**

```python
is_greater_than = second_number > 500
```

### **Step 4 — Final condition**

```python
is_pair = is_less_than_or_equal_to or is_greater_than
```

### **Step 5 — Print result**

```python
if is_pair:
    print("Pair")
else:
    print("Not a Pair")
```

---

# 🟧 **4. Final Code**

```python
first_number = int(input())
second_number = int(input())

is_less_than_or_equal_to = (first_number <= 1000) and (second_number <= 1000)
is_greater_than = second_number > 500

is_pair = is_less_than_or_equal_to or is_greater_than

if is_pair:
    print("Pair")
else:
    print("Not a Pair")
```

---

# 🟥 **5. Dry Run (Preview Table)**

### **Sample Input**

```
300
200
```

### **Dry Run Table**

| Step | Operation / Check     | Explanation                      | Result |
| ---- | --------------------- | -------------------------------- | ------ |
| 1    | first_number = 300    | Read A                           | 300    |
| 2    | second_number = 200   | Read B                           | 200    |
| 3    | A ≤ 1000 AND B ≤ 1000 | 300 ≤ 1000 AND 200 ≤ 1000 → True | True   |
| 4    | B > 500               | 200 > 500 → False                | False  |
| 5    | True OR False         | At least 1 condition is true     | True   |
| 6    | print("Pair")         | Final output                     | Pair   |

### **Output**

```
Pair
```

---
