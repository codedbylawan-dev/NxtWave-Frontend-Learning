# ✅ **Question: Part of a String - 3**

Write a program that reads a string **A** and prints the string excluding the **first two** and **last two** characters.

---

# ✅ **Approach**

### **Step 1: Read the Input**

```python
A = input()
```

---

### **Step 2: Exclude First Two and Last Two Characters**

```python
result = A[2:-2]
```

- `A[2:-2]` → slices the string starting from index 2 up to (but not including) the second last character.

---

### **Step 3: Print the Result**

```python
print(result)
```

---

# ✅ **Complete Code**

```python
A = input()
result = A[2:-2]
print(result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

Assume Input:

```
##Soft##
```

| Step | Operation                                 | Expression     | Result         |
| ---- | ----------------------------------------- | -------------- | -------------- |
| 1    | Read input                                | A = "##Soft##" | A = "##Soft##" |
| 2    | Slice string excluding first 2 and last 2 | A[2:-2]        | "Soft"         |
| 3    | Print result                              | print("Soft")  | Soft           |

---

### ✅ **Final Output**

```
Soft
```
