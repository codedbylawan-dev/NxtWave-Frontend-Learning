# Compare Digits Solved

**Easy**

Write a program that reads a two-digit number N and checks,

1. If the number N is greater than 25.
2. If the first digit of N is greater than the second digit of N.
   Print the result as shown in sample output.

**Input**
The input will be a single line containing a two-digit integer.

**Output**
The first line of output should be a boolean. True should be printed if the number is greater than 25, otherwise False should be printed.
The second line of output should be a boolean. True should be printed if the first digit is greater than the second digit, otherwise False should be printed.

**Explanation**
For example, if the given two digit number N is 45:
The digits in N (45) are 4 and 5.
Sum of digits of 45 is 9. (4 + 5 = 9) — (this problem doesn't require sum comparison; ignore)
(For this problem:) check N > 25 and first_digit > second_digit.

Sample Input 1

```
28
```

Sample Output 1

```
True
False
```

Sample Input 2

```
87
```

Sample Output 2

```
True
True
```

---

## Outline

**Question:** Compare Digits
**Approach**
Step 1: Read the input number (string form).
Step 2: Convert to integer to check if > 25.
Step 3: Extract first and second digits from the string and convert to integers.
Step 4: Compare the digits.
Step 5: Print the two boolean results (one per line).

---

## Step-by-Step Explanation

**Step 1: Read the number as a string**

```python
n = input()
```

We keep `n` as a string so we can index digits easily.

**Step 2: Convert the number to integer to check > 25**

```python
num = int(n)
is_greater_25 = num > 25
```

`is_greater_25` will be `True` if `num` is greater than 25, otherwise `False`.

**Step 3: Extract the first and second digits**

```python
first_digit = int(n[0])
second_digit = int(n[1])
```

We assume input is exactly two characters (two-digit number).

**Step 4: Compare the digits**

```python
is_first_greater = first_digit > second_digit
```

`is_first_greater` is `True` when the first digit is greater than the second digit.

**Step 5: Print the results (each on its own line)**

```python
print(is_greater_25)
print(is_first_greater)
```

---

## Solution

```python
n = input()
num = int(n)

is_greater_25 = num > 25

first_digit = int(n[0])
second_digit = int(n[1])

is_first_greater = first_digit > second_digit

print(is_greater_25)
print(is_first_greater)
```

---

# DRY RUN (Tabular Form)

### Example 1

**Input**

```
28
```

| Step | Operation            | Expression / Value                      |
| ---- | -------------------- | --------------------------------------- |
| 1    | Read input           | `n = "28"`                              |
| 2    | Convert to integer   | `num = int("28")` → `28`                |
| 3    | Check if > 25        | `is_greater_25 = 28 > 25` → `True`      |
| 4    | Extract first digit  | `first_digit = int("2")` → `2`          |
| 5    | Extract second digit | `second_digit = int("8")` → `8`         |
| 6    | Compare digits       | `is_first_greater = 2 > 8` → `False`    |
| 7    | Print results        | Prints: `True` (line1), `False` (line2) |

**Output**

```
True
False
```

---

### Example 2

**Input**

```
87
```

| Step | Operation            | Expression / Value                     |
| ---- | -------------------- | -------------------------------------- |
| 1    | Read input           | `n = "87"`                             |
| 2    | Convert to integer   | `num = int("87")` → `87`               |
| 3    | Check if > 25        | `is_greater_25 = 87 > 25` → `True`     |
| 4    | Extract first digit  | `first_digit = int("8")` → `8`         |
| 5    | Extract second digit | `second_digit = int("7")` → `7`        |
| 6    | Compare digits       | `is_first_greater = 8 > 7` → `True`    |
| 7    | Print results        | Prints: `True` (line1), `True` (line2) |

**Output**

```
True
True
```

---
