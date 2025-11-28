# 🧠 Type Conversions | Cheat Sheet

## **String Slicing**

Obtaining a part of a string is called **string slicing**.

### Syntax:

```python
variable_name[start_index:end_index]
```

- Starts from `start_index`
- Stops at `end_index` (not included)

### Example:

```python
message = "Hi Ravi"
part = message[3:7]
print(part)
```

**Output:**

```
Ravi
```

---

## **Slicing to End**

If the end index is not specified, slicing continues to the end of the string.

```python
message = "Hi Ravi"
part = message[3:]
print(part)
```

**Output:**

```
Ravi
```

---

## **Slicing from Start**

If the start index is not specified, slicing begins from index `0`.

```python
message = "Hi Ravi"
part = message[:2]
print(part)
```

**Output:**

```
Hi
```

---

## **Checking Data Type**

Use `type()` to check the datatype of a variable or value.

### Example:

```python
print(type(10))
print(type(4.2))
print(type("Hi"))
```

**Output:**

```
<class 'int'>
<class 'float'>
<class 'str'>
```

---

## **Type Conversion (Type Casting)**

Converting a value from one data type to another is called **Type Conversion**.

You can convert:

- String → Integer
- Integer → Float
- Float → String
- and more

---

## **String to Integer**

`int()` converts valid data into **integer**.

### Example:

```python
a = "5"
a = int(a)
print(type(a))
print(a)
```

**Output:**

```
<class 'int'>
5
```

---

## **Invalid Integer Conversion**

### Example:

```python
a = "Five"
a = int(a)
print(type(a))
```

**Output:**

```
ValueError: invalid literal for int() with base 10: 'Five'
```

### Another Example:

```python
a = "5.0"
a = int(a)
```

**Output:**

```
ValueError: invalid literal for int() with base 10: '5.0'
```

---

## **Adding Two Numbers**

```python
a = input()
a = int(a)
b = input()
b = int(b)
result = a + b
print(result)
```

**Input:**

```
2
3
```

**Output:**

```
5
```

---

## **Integer to String**

`str()` converts data of any type to **string**.

### Example:

```python
a = input()
a = int(a)
b = input()
b = int(b)
result = a + b
print("Sum: " + str(result))
```

**Input:**

```
2
3
```

**Output:**

```
Sum: 5
```

---

## **Summary**

- `int()` → Converts to **integer**
- `float()` → Converts to **float**
- `str()` → Converts to **string**
- `bool()` → Converts to **boolean**

---
