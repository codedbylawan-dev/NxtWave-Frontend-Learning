# ✅ **String Repetition – 4 (Solved)**

**Task:**
Given a string and a number **N**, print the string **N times separated by a space**.

Example:
Input → `messages`, `3`
Output → `messages messages messages`

---

# **Approach**

### **Step 1: Read the input**

```python
word = input()
n = int(input())
```

### **Step 2: Create the new string**

```python
new_string = word + (" " + word) * (n - 1)
```

### **Step 3: Print the new string**

```python
print(new_string)
```

---

# ✅ **Complete Code**

```python
word = input()
n = int(input())
new_string = word + (" " + word) * (n - 1)
print(new_string)
```

---

# 🟩 **DRY RUN (Tabular Format)**

Input:

```
messages
3
```

| Step | Operation           | Value / Explanation                     |
| ---- | ------------------- | --------------------------------------- |
| 1    | Read input          | word = "messages", n = 3                |
| 2    | Build repeated part | (" " + "messages") = " messages"        |
| 3    | Repeat N-1 times    | " messages" \* 2 = " messages messages" |
| 4    | Build final string  | "messages" + " messages messages"       |
| 5    | Final output        | messages messages messages              |

---

# ✅ **Final Output**

```
messages messages messages
```
