# ✅ **Negative Number — Solution**

Write a program to check whether a given number is **negative**.

---

# ✅ **Approach**

### **Step 1:** Read the input number

### **Step 2:** Convert it to integer

### **Step 3:** Check if the number is less than 0

### **Step 4:** Print the boolean result

---

# ✅ **Python Code**

```python
number = int(input())
result = number < 0
print(result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

## **Example 1**

### Input:

```
-25
```

| Step | Operation      | Expression          | Result |
| ---- | -------------- | ------------------- | ------ |
| 1    | Read number    | number = int("-25") | -25    |
| 2    | Check negative | -25 < 0             | True   |
| 3    | Print result   | print(True)         | True   |

### Output:

```
True
```

---

## **Example 2**

### Input:

```
3
```

| Step | Operation      | Expression        | Result |
| ---- | -------------- | ----------------- | ------ |
| 1    | Read number    | number = int("3") | 3      |
| 2    | Check negative | 3 < 0             | False  |
| 3    | Print result   | print(False)      | False  |

### Output:

```
False
```

---
