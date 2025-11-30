# ✅ **Question: Stars – 3**

Write a program that reads a number **N** and prints **three lines**, each containing **N space-separated stars (`*`)**.

### **Example Output for N = 4**

```
* * * *
* * * *
* * * *
```

---

# ✅ **Approach**

### **Step 1: Understand the Task**

You must print **three lines**, each containing **N stars**, with a **space after every star**.

---

### **Step 2: Reading the Input**

- Read the input using `input()`
- Convert it to an integer using `int()`

---

### **Step 3: Printing the Lines**

- Use string repetition → `"* " * N`
- Print the same line **three times**

---

# ✅ **Final Code**

```python
count = int(input())
print("* " * count)
print("* " * count)
print("* " * count)
```

---

# 🟩 **DRY RUN (Tabular Format)**

Assume the input is:

```
4
```

| Step No.  | Operation                 | Result / Output                         |
| --------- | ------------------------- | --------------------------------------- |
| 1         | Read input `"4"`          | count = 4                               |
| 2         | Execute `print("* " * 4)` | `* * * * `                              |
| 3         | Execute `print("* " * 4)` | `* * * * `                              |
| 4         | Execute `print("* " * 4)` | `* * * * `                              |
| **Final** | Combined output           | \* \* \* _ <br>_ \* \* _ <br>_ \* \* \* |

---
