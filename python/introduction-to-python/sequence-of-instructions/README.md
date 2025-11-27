# 🧠 Sequence of Instructions

## **Program**

A program is a sequence of instructions given to a computer.

---

## **Defining a Variable**

A variable gets created when you assign a value to it for the first time.

### Example:

```python
age = 10
```

---

## **Printing Value in a Variable**

```python
age = 10
print(age)
```

**Output:**

```
10
```

### Printing the variable name (as text)

```python
age = 10
print("age")
```

**Output:**

```
age
```

**Note:** Enclosing a variable in quotes prints the word, not the value.

---

## **Order of Instructions**

Python executes code **line-by-line**.

### Example:

```python
print(age)
age = 10
```

**Output:**

```
NameError: name 'age' is not defined
```

Reason: `age` is used before its creation.

---

## **Spacing in Python**

Unnecessary spaces at the beginning of a line cause errors.

### Example:

```python
a = 10 * 5
b = 5 * 0.5
 b = a + b
```

**Output:**

```
IndentationError: unexpected indent
```

---

## **Variable Assignment**

Values in variables can be changed.

### Example:

```python
a = 1
print(a)
a = 2
print(a)
```

**Output:**

```
1
2
```

---

### More Examples:

```python
a = 2
print(a)
a = a + 1
print(a)
```

**Output:**

```
2
3
```

```python
a = 1
b = 2
a = b + 1
print(a)
print(b)
```

**Output:**

```
3
2
```

---

## **Expression**

An expression is a valid combination of values, variables and operators.

### Examples:

- a \* b
- a + 2
- 5 _ 2 + 3 _ 4

---

## **BODMAS**

Standard order of evaluating an expression:

- **B**rackets
- **O**rders
- **D**ivision
- **M**ultiplication
- **A**ddition
- **S**ubtraction

### Example (Step-by-step):

Expression: `(5 * 2) + (3 * 4)`

- 5 × 2 = 10
- 3 × 4 = 12
- 10 + 12 = **22**

### Python Example:

```python
print(10 / 2 + 3)
print(10 / (2 + 3))
```

**Output:**

```
8.0
2.0
```

---
