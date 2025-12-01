# ✅ **Check Part of a String — Full Solution**

## **Question**

Given:

- A → first string
- B → second string
- I → index

Check if **string B starts exactly at index I** in string A.

Example:
A = `"Repeat"`
B = `"pea"`
I = 2
→ Output: **True**

---

# ✅ **Approach**

1. Read A, B, and index I
2. Compute the length of B
3. Compute end index = I + length of B
4. Extract A[I : end_index]
5. Compare it with B
6. Print True / False

---

# 📝 **Step-by-Step Explanation**

### **Step 1: Read the input strings and index**

Use `input()` for both strings and convert index into integer.

```python
first_string = input()
second_string = input()
start_index = int(input())
```

---

### **Step 2: Calculate the end index**

Length of B determines how far we slice.

```python
second_string_length = len(second_string)
end_index = start_index + second_string_length
```

---

### **Step 3: Extract the part of A**

Slice from `start_index` to `end_index`:

```python
part = first_string[start_index:end_index]
```

---

### **Step 4: Compare**

Check if sliced part matches B:

```python
result = part == second_string
```

---

### **Step 5: Print**

Output the boolean:

```python
print(result)
```

---

# ✅ **Final Code**

```python
first_string = input()
second_string = input()
start_index = int(input())

second_string_length = len(second_string)
end_index = start_index + second_string_length

part = first_string[start_index:end_index]
result = part == second_string

print(result)
```

---

# ✅ **Dry Run (Tabular Form)**

## **Sample Input 1**

```
Repeat
pea
2
```

| Step | Action                         | Value    |
| ---- | ------------------------------ | -------- |
| 1    | first_string                   | "Repeat" |
| 2    | second_string                  | "pea"    |
| 3    | start_index                    | 2        |
| 4    | second_string_length           | 3        |
| 5    | end_index = 2 + 3              | 5        |
| 6    | part = first_string[2:5]       | "pea"    |
| 7    | result = part == second_string | True     |
| 8    | print(result)                  | True     |

---

## **Sample Input 2**

```
Banana
Ball
0
```

| Step | Action                         | Value    |
| ---- | ------------------------------ | -------- |
| 1    | first_string                   | "Banana" |
| 2    | second_string                  | "Ball"   |
| 3    | start_index                    | 0        |
| 4    | second_string_length           | 4        |
| 5    | end_index = 0 + 4              | 4        |
| 6    | part = first_string[0:4]       | "Bana"   |
| 7    | result = part == second_string | False    |
| 8    | print(result)                  | False    |

---
