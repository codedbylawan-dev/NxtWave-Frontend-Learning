# ✅ **Compare First Three Characters — Complete Solution**

**Question:** Compare First Three Characters
**Approach:**
Step 1: Read the input strings
Step 2: Extract the first three characters
Step 3: Compare the extracted characters and print the result

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read the input strings**

```python
first_str = input()
second_str = input()
```

---

## **Step 2: Extract the first three characters**

```python
first_str_part = first_str[:3]
second_str_part = second_str[:3]
```

---

## **Step 3: Compare the extracted characters and print the result**

```python
are_both_same = first_str_part == second_str_part
print(are_both_same)
```

---

# ✅ **Final Solution**

```python
first_str = input()
second_str = input()

first_str_part = first_str[:3]
second_str_part = second_str[:3]

are_both_same = first_str_part == second_str_part
print(are_both_same)
```

---

# 🟩 **DRY RUN (Tabular Form)**

### Example 1

**Input**

```
Apple
Application
```

| Step | Operation            | Expression / Value                    |
| ---- | -------------------- | ------------------------------------- |
| 1    | Read first input     | first_str = "Apple"                   |
| 2    | Read second input    | second_str = "Application"            |
| 3    | Slice first 3 chars  | first_str_part = "App"                |
| 4    | Slice second 3 chars | second_str_part = "App"               |
| 5    | Compare              | are_both_same = "App" == "App" → True |
| 6    | Print result         | Output: `True`                        |

**Final Output**

```
True
```

---

### Example 2

**Input**

```
Android
Application
```

| Step | Operation            | Expression / Value                     |
| ---- | -------------------- | -------------------------------------- |
| 1    | Read first input     | first_str = "Android"                  |
| 2    | Read second input    | second_str = "Application"             |
| 3    | Slice first 3 chars  | first_str_part = "And"                 |
| 4    | Slice second 3 chars | second_str_part = "App"                |
| 5    | Compare              | are_both_same = "And" == "App" → False |
| 6    | Print result         | Output: `False`                        |

**Final Output**

```
False
```

---
