# ✅ **Question: Half String - 2**

Write a program that reads a string and prints the **second half part** of the string.

---

# ✅ **Approach**

### **Step 1: Read the input string**

```python
word = input()
```

---

### **Step 2: Calculate the half length of the string**

```python
half_length = len(word) // 2
```

> Use integer division `//` to handle even or odd lengths.

---

### **Step 3: Get the second half of the string**

```python
second_half = word[half_length:]
```

---

### **Step 4: Print the second half**

```python
print(second_half)
```

---

# ✅ **Complete Code**

```python
word = input()
half_length = len(word) // 2
second_half = word[half_length:]
print(second_half)
```

---

# 🟩 **DRY RUN (Tabular Form)**

Assume Input:

```
Football
```

| Step | Operation             | Expression         | Result            |
| ---- | --------------------- | ------------------ | ----------------- |
| 1    | Read input            | word = "Football"  | word = "Football" |
| 2    | Calculate half length | half_length = 8//2 | 4                 |
| 3    | Slice second half     | word[4:]           | "ball"            |
| 4    | Print result          | print("ball")      | ball              |

---

### ✅ **Final Output**

```
ball
```
