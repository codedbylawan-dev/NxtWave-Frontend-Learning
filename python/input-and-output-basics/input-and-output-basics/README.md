# 🧠 Input and Output Basics

## **Working with Strings**

---

## **String Concatenation**

Joining strings together is called **string concatenation**.

### Example:

```python
a = "Hello" + " " + "World"
print(a)
```

**Output:**

```
Hello World
```

---

## **Concatenation Errors**

String concatenation is possible **only with strings**.

### Example:

```python
a = "*" + 10
print(a)
```

**Output:**

```
TypeError: can only concatenate str (not "int") to str
```

---

## **String Repetition**

The `*` operator is used for repeating strings any number of times.

### Example:

```python
a = "*" * 10
print(a)
```

**Output:**

```
**********
```

### Example:

```python
s = "Python"
s = ("* " * 3) + s + (" *" * 3)
print(s)
```

**Output:**

```
* * * Python * * *
```

---

## **Length of String**

`len()` returns the number of characters in a given string.

### Example:

```python
username = input()
length = len(username)
print(length)
```

**Input:**

```
Ravi
```

**Output:**

```
4
```

---

## **Take Input From User**

`input()` reads a line of input **as a string**.

### Example 1:

```python
username = input()
print(username)
```

**Input:**

```
Ajay
```

**Output:**

```
Ajay
```

---

### Example 2:

```python
username = input()
age = input()
print(username + " is " + age + " years old")
```

**Input:**

```
Ravi
10
```

**Output:**

```
Ravi is 10 years old
```

### Note:

- You cannot directly combine strings and integers.
- But here the code works because **input() always returns a string**.
- That means even if the user enters a number, Python treats it as a string.

Example:
User enters `10` → input() stores it as `"10"` (string).

---

---

## **String Indexing**

We can access an individual character in a string using their positions (indexes).
Indexes start from **0**.

### Example:

```python
username = "Ravi"
first_letter = username[0]
print(first_letter)
```

**Output:**

```
R
```

---

## **IndexError**

Trying to use an index that is too large will cause an error.

### Example:

```python
username = "Ravi"
print(username[4])
```

**Output:**

```
IndexError: string index out of range
```

---
