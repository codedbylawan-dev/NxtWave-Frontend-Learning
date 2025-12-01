# ✅ **Compare First N & Last N characters (Solved)**

**Difficulty:** Easy

Write a program that reads a string and a number N and checks if the first N characters of the string and the last N characters of the string are **not the same**.

---

## **Input**

The first line of input contains a string.
The second line of input contains an integer.

## **Output**

The output should be a single line containing a boolean. `True` should be printed if the first N characters of the string and the last N characters of the string are **not the same**, otherwise `False` should be printed.

## **Explanation**

For example, if the given string is `toronto` and `N = 2`:

```
t o r o n t o
0 1 2 3 4 5 6
```

The first 2 characters are `to`.
The last 2 characters are `to`.
They are the same → output `False`.

If the given string is `educated` and `N = 3`:

```
e d u c a t e d
0 1 2 3 4 5 6 7
```

The first 3 characters are `edu`.
The last 3 characters are `ted`.
They are not the same → output `True`.

---

# 🧭 **Outline**

**Question:** Compare First N & Last N characters
**Approach:** (short, explicit steps — added as requested)

1. Read the string `s`.
2. Read the integer `n`.
3. Extract `first_n = s[:n]`.
4. Extract `last_n = s[-n:]`.
5. Print the boolean `first_n != last_n`.

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read input**

Read the string and number `n` from input:

```python
s = input()
n = int(input())
```

## **Step 2: Extract first N and last N characters**

Get the first `n` characters and the last `n` characters using slicing:

```python
first_n = s[:n]
last_n = s[-n:]
```

> Note: If `n` equals the length of `s`, `first_n` and `last_n` are both `s`. Slicing handles small strings naturally.

## **Step 3: Compare and print**

Compare `first_n` and `last_n` for inequality (`!=`) and print the boolean:

```python
print(first_n != last_n)
```

---

# ✅ **Final Solution**

```python
s = input()
n = int(input())

first_n = s[:n]
last_n = s[-n:]

print(first_n != last_n)
```

---

# 🟩 **DRY RUN (Tabular Form)**

### Sample Input 1

```
toronto
2
```

| Step | Operation                 | Expression / Value   |
| ---- | ------------------------- | -------------------- |
| 1    | Read input                | s = "toronto", n = 2 |
| 2    | first_n = s[:n]           | first_n = "to"       |
| 3    | last_n = s[-n:]           | last_n = "to"        |
| 4    | Compare first_n != last_n | "to" != "to" → False |
| 5    | Print result              | False                |

**Output:**

```
False
```

---

### Sample Input 2

```
educated
3
```

| Step | Operation                 | Expression / Value    |
| ---- | ------------------------- | --------------------- |
| 1    | Read input                | s = "educated", n = 3 |
| 2    | first_n = s[:n]           | first_n = "edu"       |
| 3    | last_n = s[-n:]           | last_n = "ted"        |
| 4    | Compare first_n != last_n | "edu" != "ted" → True |
| 5    | Print result              | True                  |

**Output:**

```
True
```

---

### Sample Input 3

```
bulb
1
```

| Step | Operation                 | Expression / Value |
| ---- | ------------------------- | ------------------ |
| 1    | Read input                | s = "bulb", n = 1  |
| 2    | first_n = s[:n]           | first_n = "b"      |
| 3    | last_n = s[-n:]           | last_n = "b"       |
| 4    | Compare first_n != last_n | "b" != "b" → False |
| 5    | Print result              | False              |

**Output:**

```
False
```

---
