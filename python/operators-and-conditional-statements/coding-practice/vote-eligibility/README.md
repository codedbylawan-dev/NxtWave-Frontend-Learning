# 🔹 **Question: Vote Eligibility**

Write a program that reads a person's age and checks:

- If **age ≥ 18**, print **"Eligible"**
- Otherwise, print **"Not Eligible"**

---

# 🟦 **1. Question Explanation**

This problem checks voting eligibility based on age.

### Condition:

- Age ≥ 18 → **Eligible**
- Age < 18 → **Not Eligible**

Examples:

- Age = 15 → Not Eligible
- Age = 21 → Eligible

---

# 🟩 **2. Approach**

1. Read the age
2. Check if age ≥ 18
3. Print **Eligible** or **Not Eligible**

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1 — Read age**

```python
age = int(input())
```

### **Step 2 — Compare with 18**

```python
if age >= 18:
```

### **Step 3 — Print output accordingly**

```python
    print("Eligible")
else:
    print("Not Eligible")
```

---

# 🟧 **4. Final Code**

```python
age = int(input())

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Sample Input**

```
15
```

### **Dry Run Table**

| Step | Operation             | Explanation               | Result       |
| ---- | --------------------- | ------------------------- | ------------ |
| 1    | age = 15              | Read the input            | 15           |
| 2    | 15 ≥ 18 → False       | Age is less than required | False        |
| 3    | print("Not Eligible") | Person cannot vote        | Not Eligible |

### **Final Output**

```
Not Eligible
```

---
