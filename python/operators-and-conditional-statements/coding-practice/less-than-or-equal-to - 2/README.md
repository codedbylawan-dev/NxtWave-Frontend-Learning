# ✅ **Less than or Equal to - 2 (Solved)**

**Difficulty:** Easy

Write a program that reads two numbers **A** and **B** and checks:

- If **A is less than or equal to B**.
- If **B is less than or equal to A**.

Print the result exactly as in the sample output.

---

## **Outline**

**Question:** Less than or Equal to - 2
**Approach:**
Step 1: Read A.
Step 2: Read B.
Step 3: Check `A <= B`.
Step 4: Check `B <= A`.
Step 5: Print results in required string format.

---

## **Step-by-Step Explanation**

**Step 1: Read A**
Read the first integer.

```python
A = int(input())
```

**Step 2: Read B**
Read the second integer.

```python
B = int(input())
```

**Step 3: Check if A ≤ B**

```python
first_check = A <= B
```

**Step 4: Check if B ≤ A**

```python
second_check = B <= A
```

**Step 5: Print results in correct string format**

```python
print("A <= B is", first_check)
print("B <= A is", second_check)
```

---

## ✅ **Complete Solution**

```python
A = int(input())
B = int(input())

first_check = A <= B
second_check = B <= A

print("A <= B is", first_check)
print("B <= A is", second_check)
```

---

# 🟩 **DRY RUN (Tabular Form)**

### Sample Input 1

```
5
3
```

| Step | Operation     | Expression | Result |
| ---- | ------------- | ---------- | ------ |
| 1    | Read A        | A = 5      | 5      |
| 2    | Read B        | B = 3      | 3      |
| 3    | Check A ≤ B   | 5 ≤ 3      | False  |
| 4    | Check B ≤ A   | 3 ≤ 5      | True   |
| 5    | Print results | —          | —      |

**Final Output:**

```
A <= B is False
B <= A is True
```

---

### Sample Input 2

```
21
64
```

| Step | Operation   | Expression | Result |
| ---- | ----------- | ---------- | ------ |
| 1    | Read A      | A = 21     | 21     |
| 2    | Read B      | B = 64     | 64     |
| 3    | Check A ≤ B | 21 ≤ 64    | True   |
| 4    | Check B ≤ A | 64 ≤ 21    | False  |

**Final Output:**

```
A <= B is True
B <= A is False
```

---
