# ✅ **Question: Star Repetition - 5**

You are given **two words, W1 and W2**.

- The first part of W1 contains W2.
- Replace that first part with stars (\*) and print the resulting string.

---

# ✅ **Approach**

### **Step 1: Read the Input**

```python
W1 = input()
W2 = input()
```

---

### **Step 2: Find Length of W2**

```python
length_W2 = len(W2)
```

This will help us know how many stars to print.

---

### **Step 3: Replace the First Part with Stars**

```python
result = "*" * length_W2 + W1[length_W2:]
```

- `"*"` × `length_W2` → prints stars for the first part
- `W1[length_W2:]` → adds the remaining part of W1

---

### **Step 4: Print the Result**

```python
print(result)
```

---

# ✅ **Complete Code**

```python
W1 = input()
W2 = input()
length_W2 = len(W2)
result = "*" * length_W2 + W1[length_W2:]
print(result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

Assume Input:

```
Subway
Sub
```

| Step | Operation                     | Expression                | Result                    |
| ---- | ----------------------------- | ------------------------- | ------------------------- |
| 1    | Read W1 and W2                | W1 = "Subway", W2 = "Sub" | W1 = "Subway", W2 = "Sub" |
| 2    | Length of W2                  | len("Sub")                | 3                         |
| 3    | Replace first part with stars | "*"*3 + "Subway"[3:]      | "\*\*\*way"               |
| 4    | Print result                  | print("\*\*\*way")        | \*\*\*way                 |

---

### ✅ **Final Output**

```
***way
```
