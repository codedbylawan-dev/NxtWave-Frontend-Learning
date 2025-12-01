# ✅ **Equal to — Solution**

Write a program to check whether **two given words are the same**.

---

# ✅ **Approach**

### **Step 1:** Read the input words

### **Step 2:** Compare the words using `==` operator

### **Step 3:** Print the boolean result

---

# ✅ **Python Code**

```python
first_word = input()
second_word = input()
result = first_word == second_word
print(result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

## **Example 1**

### Input:

```
Jam
Jam
```

| Step | Operation        | Expression          | Result |
| ---- | ---------------- | ------------------- | ------ |
| 1    | Read first word  | first_word = "Jam"  | Jam    |
| 2    | Read second word | second_word = "Jam" | Jam    |
| 3    | Compare words    | "Jam" == "Jam"      | True   |
| 4    | Print result     | print(True)         | True   |

### Output:

```
True
```

---

## **Example 2**

### Input:

```
Dog
Cow
```

| Step | Operation        | Expression          | Result |
| ---- | ---------------- | ------------------- | ------ |
| 1    | Read first word  | first_word = "Dog"  | Dog    |
| 2    | Read second word | second_word = "Cow" | Cow    |
| 3    | Compare words    | "Dog" == "Cow"      | False  |
| 4    | Print result     | print(False)        | False  |

### Output:

```
False
```

---
