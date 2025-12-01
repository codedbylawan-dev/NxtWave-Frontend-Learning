# ✅ **Profit (Solved)**

**Difficulty:** Easy

Write a program that reads the selling price `S` and buying price `B` of a product and checks if **S is greater than B**.

---

## **Input**

- First line: integer representing the selling price `S`.
- Second line: integer representing the buying price `B`.

## **Output**

- A single line containing a boolean.
- Print `True` if `S > B`, otherwise `False`.

## **Explanation**

For example, if the given selling price is `S = 600` and buying price is `B = 500`:

- 600 > 500 → True
- Output: `True`

---

# 🧭 **Outline**

**Question:** Profit
**Approach:**

1. Read selling price `S`.
2. Read buying price `B`.
3. Compare `S > B`.
4. Print the result.

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read selling price**

```python
S = int(input())
```

## **Step 2: Read buying price**

```python
B = int(input())
```

## **Step 3: Compare prices**

```python
result = S > B
```

## **Step 4: Print result**

```python
print(result)
```

---

# ✅ **Complete Solution**

```python
S = int(input())
B = int(input())

result = S > B
print(result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

### Sample Input 1

```
600
500
```

| Step | Operation          | Expression    | Result |
| ---- | ------------------ | ------------- | ------ |
| 1    | Read selling price | S = 600       | 600    |
| 2    | Read buying price  | B = 500       | 500    |
| 3    | Compare S > B      | 600 > 500     | True   |
| 4    | Print result       | print(result) | True   |

**Output:**

```
True
```

---

### Sample Input 2

```
100
105
```

| Step | Operation          | Expression    | Result |
| ---- | ------------------ | ------------- | ------ |
| 1    | Read selling price | S = 100       | 100    |
| 2    | Read buying price  | B = 105       | 105    |
| 3    | Compare S > B      | 100 > 105     | False  |
| 4    | Print result       | print(result) | False  |

**Output:**

```
False
```

---
