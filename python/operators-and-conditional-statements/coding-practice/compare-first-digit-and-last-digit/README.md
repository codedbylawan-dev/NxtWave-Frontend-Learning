# Compare First Digit & Last Digit — Solved

**Easy**

Write a program that reads two three-digit numbers **A** and **B** and checks if the **first digit of A** is **less than** the **last digit of B**.

---

## Outline

**Question:** Compare First Digit & Last Digit
**Approach**
Step 1: Read the inputs A and B
Step 2: Extract the first digit of A
Step 3: Extract the last digit of B
Step 4: Compare the digits
Step 5: Print the result

---

## Approach

To solve this problem:

1. Read both numbers as strings.
2. Extract the first character of A.
3. Extract the last character of B.
4. Convert both to integers.
5. Compare them using `<`.
6. Print **True** or **False**.

---

## Step-by-Step Explanation

### **Step 1: Read inputs**

```python
A = input()
B = input()
```

### **Step 2: Extract first digit of A**

```python
first_digit_A = int(A[0])
```

### **Step 3: Extract last digit of B**

```python
last_digit_B = int(B[-1])
```

### **Step 4: Compare the digits**

```python
result = first_digit_A < last_digit_B
```

### **Step 5: Print the result**

```python
print(result)
```

---

## Solution

```python
A = input()
B = input()

first_digit_A = int(A[0])
last_digit_B = int(B[-1])

result = first_digit_A < last_digit_B

print(result)
```

---

# DRY RUN (Tabular Format)

---

## **Sample Input 1**

```
123
378
```

| Step | Operation           | Value               |
| ---- | ------------------- | ------------------- |
| 1    | Read A              | "123"               |
| 2    | Read B              | "378"               |
| 3    | Extract first digit | `first_digit_A = 1` |
| 4    | Extract last digit  | `last_digit_B = 8`  |
| 5    | Compare             | `1 < 8` → **True**  |
| 6    | Print               | `True`              |

**Output**

```
True
```

---

## **Sample Input 2**

```
215
572
```

| Step | Operation           | Value               |
| ---- | ------------------- | ------------------- |
| 1    | Read A              | "215"               |
| 2    | Read B              | "572"               |
| 3    | Extract first digit | `first_digit_A = 2` |
| 4    | Extract last digit  | `last_digit_B = 2`  |
| 5    | Compare             | `2 < 2` → **False** |
| 6    | Print               | `False`             |

**Output**

```
False
```

---
