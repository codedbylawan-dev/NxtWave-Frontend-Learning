# ✅ **Check First Part of a String (Solved)**

**Difficulty:** Easy

Write a program that reads two strings `S1` and `S2`, and checks if **S2 is the first part of S1**.

---

## **Input**

- First line: string `S1`.
- Second line: string `S2`.

## **Output**

- A single line containing a boolean.
- Print `True` if `S2` is the first part of `S1`, otherwise `False`.

## **Explanation**

For example, if the given strings are `S1 = rainbow` and `S2 = rain`:

- First part of `S1` is `"rain"`.
- `S2` is `"rain"`.
- They match → `True`.

If `S1 = debug` and `S2 = bug`:

- First part of `S1` is `"deb"`.
- `S2` is `"bug"`.
- They don’t match → `False`.

---

# 🧭 **Outline**

**Question:** Check First Part of a String
**Approach:**

1. Read the first string `S1`.
2. Read the second string `S2`.
3. Extract the first `len(S2)` characters from `S1`.
4. Compare with `S2`.
5. Print the result.

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read the first string**

```python
S1 = input()
```

## **Step 2: Read the second string**

```python
S2 = input()
```

## **Step 3: Extract first part of S1**

```python
first_part = S1[:len(S2)]
```

## **Step 4: Compare with S2**

```python
result = first_part == S2
```

## **Step 5: Print the result**

```python
print(result)
```

---

# ✅ **Complete Solution**

```python
S1 = input()
S2 = input()

first_part = S1[:len(S2)]
result = first_part == S2

print(result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

### Sample Input 1

```
rainbow
rain
```

| Step | Operation                | Expression          | Result    |
| ---- | ------------------------ | ------------------- | --------- |
| 1    | Read S1                  | S1 = "rainbow"      | "rainbow" |
| 2    | Read S2                  | S2 = "rain"         | "rain"    |
| 3    | Extract first part of S1 | first_part = S1[:4] | "rain"    |
| 4    | Compare first_part == S2 | "rain" == "rain"    | True      |
| 5    | Print result             | print(result)       | True      |

**Output:**

```
True
```

---

### Sample Input 2

```
debug
bug
```

| Step | Operation                | Expression          | Result  |
| ---- | ------------------------ | ------------------- | ------- |
| 1    | Read S1                  | S1 = "debug"        | "debug" |
| 2    | Read S2                  | S2 = "bug"          | "bug"   |
| 3    | Extract first part of S1 | first_part = S1[:3] | "deb"   |
| 4    | Compare first_part == S2 | "deb" == "bug"      | False   |
| 5    | Print result             | print(result)       | False   |

**Output:**

```
False
```

---
