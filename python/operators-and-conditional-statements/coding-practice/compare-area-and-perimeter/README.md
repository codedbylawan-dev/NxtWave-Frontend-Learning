# ✅ **Compare Area and Perimeter (Solved)**

**Difficulty:** Easy

Write a program that reads the length and breadth of a rectangle and checks if the **area** of the rectangle is **less than or equal to** the **perimeter** of the rectangle.

---

## **Outline**

**Question:** Compare Area and Perimeter
**Approach:**
Step 1: Read length.
Step 2: Read breadth.
Step 3: Compute area = length × breadth.
Step 4: Compute perimeter = 2 × (length + breadth).
Step 5: Check `area <= perimeter`.
Step 6: Print result.

---

## **Step-by-Step Explanation**

**Step 1: Read the length**
Read the first line of input and convert to integer.

```python
length = int(input())
```

**Step 2: Read the breadth**
Read the second line of input and convert to integer.

```python
breadth = int(input())
```

**Step 3: Compute area**
Multiply length and breadth.

```python
area = length * breadth
```

**Step 4: Compute perimeter**
Compute `2 * (length + breadth)`.

```python
perimeter = 2 * (length + breadth)
```

**Step 5: Compare area and perimeter**
Check whether `area <= perimeter`.

```python
result = area <= perimeter
```

**Step 6: Print the boolean result**
Print `True` or `False`.

```python
print(result)
```

---

## ✅ **Complete Solution**

```python
length = int(input())
breadth = int(input())

area = length * breadth
perimeter = 2 * (length + breadth)

result = area <= perimeter
print(result)
```

---

# 🟩 **DRY RUN (Tabular Form)**

### Sample Input 1

```
3
4
```

| Step | Operation                | Expression               | Result |
| ---- | ------------------------ | ------------------------ | ------ |
| 1    | Read length              | length = 3               | 3      |
| 2    | Read breadth             | breadth = 4              | 4      |
| 3    | Compute area             | area = 3 \* 4            | 12     |
| 4    | Compute perimeter        | perimeter = 2 \* (3 + 4) | 14     |
| 5    | Compare area ≤ perimeter | 12 ≤ 14                  | True   |
| 6    | Print result             | print(result)            | True   |

**Final Output:**

```
True
```

---
