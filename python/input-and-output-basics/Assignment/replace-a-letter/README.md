# ✅ **Question: Replace a Letter**

Write a program that reads a word **W**, an index **I**, and a letter **C**, and prints **W** after replacing the letter at index **I** with **C**.

---

# ✅ **Approach**

### **Step 1: Read the Input**

```python
W = input()
I = int(input())
C = input()
```

---

### **Step 2: Replace the Letter at Index I**

- Split the word into two parts: before and after index **I**.
- Concatenate the first part + new letter + remaining part after index **I**.

```python
result = W[:I] + C + W[I+1:]
```

---

### **Step 3: Print the Result**

```python
print(result)
```

---

# ✅ **Complete Code**

```python
W = input()
I = int(input())
C = input()
result = W[:I] + C + W[I+1:]
print(result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

Assume Input:

```
Prime
3
z
```

| Step | Operation                   | Expression              | Result                |
| ---- | --------------------------- | ----------------------- | --------------------- |
| 1    | Read inputs                 | W = "Prime", I=3, C="z" | W="Prime", I=3, C="z" |
| 2    | Slice before index          | W[:I]                   | "Pri"                 |
| 3    | Slice after index           | W[I+1:]                 | "e"                   |
| 4    | Concatenate with new letter | "Pri" + "z" + "e"       | "Prize"               |
| 5    | Print result                | print("Prize")          | Prize                 |

---

### ✅ **Final Output**

```
Prize
```
