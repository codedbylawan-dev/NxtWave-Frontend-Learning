# ✅ **Check Last Part of a String — Full Solution**

## **Problem Summary**

Given two strings **A** and **B**, check if **B is the ending part (suffix)** of **A**.

Example:
A = "Blackhole"
B = "hole"
→ Output: **True**

---

# ✅ **Approach**

1. Read string A (first_word) and string B (second_word).
2. Compute lengths of both strings.
3. Compute start index = len(A) − len(B).
4. Slice the last part of A starting at that index.
5. Compare the sliced part with B.
6. Print True if equal, otherwise False.

---

# 📝 **Step-by-Step Explanation**

**Step 1 — Read inputs**
Use `input()` to read the two strings:

```python
first_word = input()
second_word = input()
```

**Step 2 — Get lengths**
Find lengths using `len()`:

```python
first_word_length = len(first_word)
second_word_length = len(second_word)
```

**Step 3 — Compute start index**
The last `second_word_length` characters of `first_word` start at:

```python
start_index = first_word_length - second_word_length
```

(If `second_word` is longer than `first_word`, `start_index` becomes negative — slicing still works in Python but the result will not match, giving `False`.)

**Step 4 — Slice the last part of A**
Extract substring from `start_index` to the end:

```python
part = first_word[start_index:]
```

**Step 5 — Compare**
Check whether the sliced `part` equals `second_word`:

```python
result = part == second_word
```

**Step 6 — Print**
Output the boolean result:

```python
print(result)
```

---

# ✅ **Final Code**

```python
first_word = input()
second_word = input()

first_word_length = len(first_word)
second_word_length = len(second_word)

start_index = first_word_length - second_word_length
part = first_word[start_index:]

result = part == second_word
print(result)
```

---

# ✅ **Dry Run (Tabular Form)**

### **Sample Input 1**

A = `"Blackhole"`
B = `"hole"`

| Step | Action                               | Value       |
| ---- | ------------------------------------ | ----------- |
| 1    | Read first_word                      | "Blackhole" |
| 2    | Read second_word                     | "hole"      |
| 3    | first_word_length = len("Blackhole") | 9           |
| 4    | second_word_length = len("hole")     | 4           |
| 5    | start_index = 9 - 4                  | 5           |
| 6    | part = first_word[5:]                | "hole"      |
| 7    | result = part == second_word         | True        |
| 8    | print(result)                        | True        |

---

### **Sample Input 2**

A = `"boomerang"`
B = `"boom"`

| Step | Action                               | Value       |
| ---- | ------------------------------------ | ----------- |
| 1    | Read first_word                      | "boomerang" |
| 2    | Read second_word                     | "boom"      |
| 3    | first_word_length = len("boomerang") | 9           |
| 4    | second_word_length = len("boom")     | 4           |
| 5    | start_index = 9 - 4                  | 5           |
| 6    | part = first_word[5:]                | "rang"      |
| 7    | result = part == second_word         | False       |
| 8    | print(result)                        | False       |

---
