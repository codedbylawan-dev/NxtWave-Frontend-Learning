# ✅ **Question: Percentage - 3**

Write a program that reads a percentage `P` and a number `N` and checks if the `P` percentage of `500` is equal to the number `N`.

---

## **Approach**

Step 1: Read the integer percentage `P`.
Step 2: Read the integer `N`.
Step 3: Compute `P` percent of `500` (note `500 * P / 100` is the same as `P * 5`).
Step 4: Compare the computed value with `N`.
Step 5: Print the boolean result (`True` or `False`).

---

## **Step-by-Step Explanation**

**Step 1: Read input percentage `P`**

```python
P = int(input())
```

**Step 2: Read input number `N`**

```python
N = int(input())
```

**Step 3: Compute P% of 500**

We can compute it as `(P * 500) / 100`. Since `500/100 = 5`, this simplifies to `P * 5`, which is exact integer arithmetic:

```python
value = P * 5
```

**Step 4: Compare the computed value with `N`**

```python
result = value == N
```

**Step 5: Print the boolean result**

```python
print(result)
```

---

## ✅ **Complete Solution**

```python
P = int(input())
N = int(input())

# P percent of 500 equals P * 5
result = (P * 5) == N
print(result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

### Sample Input 1

```
50
250
```

| Step | Operation                      | Expression          | Result        |
| ---- | ------------------------------ | ------------------- | ------------- |
| 1    | Read P                         | P = 50              | 50            |
| 2    | Read N                         | N = 250             | 250           |
| 3    | Compute P% of 500 (simplified) | value = P \* 5      | 50 \* 5 = 250 |
| 4    | Compare value with N           | result = 250 == 250 | True          |
| 5    | Print result                   | print(result)       | True          |

**Final Output**

```
True
```

---

### Sample Input 2

```
5
100
```

| Step | Operation                      | Expression         | Result      |
| ---- | ------------------------------ | ------------------ | ----------- |
| 1    | Read P                         | P = 5              | 5           |
| 2    | Read N                         | N = 100            | 100         |
| 3    | Compute P% of 500 (simplified) | value = P \* 5     | 5 \* 5 = 25 |
| 4    | Compare value with N           | result = 25 == 100 | False       |
| 5    | Print result                   | print(result)      | False       |

**Final Output**

```
False
```

---
