# 🧠 Nested Conditional Statements | Cheat Sheet

## **What Are Nested Conditions?**

A **nested conditional** means writing an `if`/`else` block **inside another** `if`/`else` block.

➡️ Simply: **One condition inside another condition.**

---

## **Why Do We Use Nested Conditions?**

- When decisions depend on **multiple layers** of logic.
- When a second condition needs to be checked **only if the first one is True**.
- Helps control flow in step-by-step decision making.

---

## **Basic Structure**

```
if condition A:
    # Block 1
    if condition B:
        # Block 2 (nested block)
```

- Block 2 runs **only if** both condition A and B are True.

---

## **Example 1: Nested Condition Inside If Block**

### **Code**

```python
matches_won = int(input())
goals = int(input())

if matches_won > 8:
    if goals > 20:
        print("Hurray")
    print("Winner")
```

### **Input**

```
10
22
```

### **Output**

```
Hurray
Winner
```

### **Explanation**

- `matches_won > 8` → True
- Then inner condition checked → `goals > 20` → True → print **Hurray**
- After inner block → print **Winner**

---

### **Input**

```
10
18
```

### **Output**

```
Winner
```

Because inner condition is False → only **Winner** is printed.

---

## 🧩 Nested Condition Inside Else Block

You can also nest an `if` inside an `else`.

### **Code**

```python
a = 2
b = 3
c = 1

is_a_greatest = (a > b) and (a > c)

if is_a_greatest:
    print(a)
else:
    is_b_greatest = (b > c)
    if is_b_greatest:
        print(b)
    else:
        print(c)
```

### **Output**

```
3
```

---

# 🧠 Elif Statement

`elif` is used when you need **multiple conditions**, not just True/False.

### **Structure**

```python
if condition1:
    ...
elif condition2:
    ...
elif condition3:
    ...
else:
    ...
```

- `elif` is optional
- You can have **any number** of `elif` statements
- Only the **first True** condition will execute
- `else` is optional

---

## **Example**

### **Code**

```python
number = 5
is_divisible_by_10 = (number % 10 == 0)
is_divisible_by_5 = (number % 5 == 0)

if is_divisible_by_10:
    print("Divisible by 10")
elif is_divisible_by_5:
    print("Divisible by 5")
else:
    print("Not Divisible by 10 or 5")
```

### **Output**

```
Divisible by 5
```

---

## ❗ Possible Mistake

### ❌ Writing `elif` after an `else`

```
if condition:
    ...
else:
    ...
elif other_condition:   # ❌ WRONG
    ...
```

This causes a **SyntaxError**.
`elif` should always come **before** `else`.

---
