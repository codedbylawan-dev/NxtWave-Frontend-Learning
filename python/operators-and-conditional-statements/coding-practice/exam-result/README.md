# 🔹 **Question: Exam Result**

Write a program that reads a student's marks and prints:

- **PASS** → if marks > 50
- **FAIL** → for all other values

---

# 🟦 **1. Question Explanation**

This problem checks whether the student **passed** an exam based on marks.

### Condition:

- If marks **> 50** → print **PASS**
- Otherwise → print **FAIL**

Examples:

- 85 → PASS
- 45 → FAIL
- 50 → FAIL

---

# 🟩 **2. Approach**

1. Read marks from input
2. Check if marks > 50
3. If true → print PASS
4. Otherwise → print FAIL

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1 — Read input**

```python
marks = int(input())
```

### **Step 2 — Check if marks > 50**

```python
if marks > 50:
```

### **Step 3 — Print PASS or FAIL**

```python
    print("PASS")
else:
    print("FAIL")
```

---

# 🟧 **4. Final Code**

```python
marks = int(input())

if marks > 50:
    print("PASS")
else:
    print("FAIL")
```

---

# 🟥 **5. Dry Run (Preview Table Format)**

### **Sample Input**

```
85
```

### **Dry Run Table**

| Step | Operation         | Explanation           | Result |
| ---- | ----------------- | --------------------- | ------ |
| 1    | marks = 85        | Read input            | 85     |
| 2    | marks > 50 → True | 85 is greater than 50 | True   |
| 3    | print("PASS")     | PASS is printed       | PASS   |

### **Final Output**

```
PASS
```

---
