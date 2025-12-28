# 🧠 Extended Slicing & String Methods | Cheat Sheet

## **What Is Extended Slicing?**

Extended slicing is an **extension of normal slicing** where we also control **how many steps to skip** between characters.

---

## **Extended Slicing Syntax**

```python
variable[start_index : end_index : step]
```

- `start_index` → starting position
- `end_index` → stopping position (**not included**)
- `step` → jump size between characters

---

## 🧩 **Example 1: Secret Message**

### **Code**

```python
secret_message = "-R-a-v-i-"
print(secret_message[1:8:2])
```

### **Output**

```
Ravi
```

### **Explanation**

Indexes picked → `1, 3, 5, 7`

---

## 🧩 **Example 2: Extended Slicing**

### **Code**

```python
a = "Waterfall"
part = a[1:6:3]
print(part)
```

### **Output**

```
ar
```

---

# 🧠 Methods

Python provides **built-in reusable utilities** called **methods**.
They help perform common operations easily.

---

# 🔤 String Methods

Common string methods:

- `isdigit()`
- `strip()`
- `lower()`
- `upper()`
- `startswith()`
- `endswith()`
- `replace()`

---

## 🔢 isdigit()

### **Syntax**

```python
str_var.isdigit()
```

Returns **True** if all characters are digits, else **False**.

### **Code**

```python
is_digit = "4748".isdigit()
print(is_digit)
```

### **Output**

```
True
```

---

## ✂️ strip()

### **Syntax**

```python
str_var.strip()
```

Removes **leading and trailing spaces**.

### **Code**

```python
mobile = " 9876543210 "
mobile = mobile.strip()
print(mobile)
```

### **Output**

```
9876543210
```

---

## ✂️ strip() – Specific Characters

### **Syntax**

```python
str_var.strip(chars)
```

### **Code**

```python
name = "Ravi."
name = name.strip(".")
print(name)
```

### **Output**

```
Ravi
```

---

## ✂️ strip() – Multiple Characters

Removes spaces, commas, and dots from start and end.

### **Code**

```python
name = ", .. ,, ravi ,, .. ."
name = name.strip(" ,.")
print(name)
```

### **Output**

```
ravi
```

---

## 🔁 replace()

### **Syntax**

```python
str_var.replace(old, new)
```

Replaces **all occurrences** of `old` with `new`.

### **Code**

```python
sentence = "teh cat and teh dog"
sentence = sentence.replace("teh", "the")
print(sentence)
```

### **Output**

```
the cat and the dog
```

---

## ▶️ startswith()

### **Syntax**

```python
str_var.startswith(value)
```

Returns **True** if string starts with given value.

### **Code**

```python
url = "https://onthegomodel.com"
is_secure_url = url.startswith("https://")
print(is_secure_url)
```

### **Output**

```
True
```

---

## ⏹️ endswith()

### **Syntax**

```python
str_var.endswith(value)
```

Returns **True** if string ends with given value.

### **Code**

```python
gmail_id = "rahul123@gmail.com"
is_gmail = gmail_id.endswith("@gmail.com")
print(is_gmail)
```

### **Output**

```
True
```

---

## 🔠 upper()

### **Syntax**

```python
str_var.upper()
```

Converts all alphabetic characters to uppercase.

### **Code**

```python
name = "ravi"
print(name.upper())
```

### **Output**

```
RAVI
```

---

## 🔡 lower()

### **Syntax**

```python
str_var.lower()
```

Converts all alphabetic characters to lowercase.

### **Code**

```python
name = "RAVI"
print(name.lower())
```

### **Output**

```
ravi
```

---

## 📌 Note

- `upper()` and `lower()` work **only on letters**
- Digits, symbols, and punctuation are **unchanged**

### **Example**

```python
s = "Hello, John! 123"
print(s.upper())
print(s.lower())
```

### **Output**

```
HELLO, JOHN! 123
hello, john! 123
```

---

If you want next, we can go to:

✅ **More String Methods**
✅ **Practice Problems on Strings**
✅ **Mini Project using Strings**

---

Perfect — continuing **exactly in your locked learning format**.
Here is **More String Methods**, clean, structured, and example-driven.

---

# 🧠 More String Methods | Cheat Sheet

## **What Are String Methods?**

String methods are **built-in functions** that help us
**check**, **modify**, **count**, and **search** text easily.

---

## **Concepts Covered**

### **1. Classification Methods**

Used to **check the nature of characters** in a string.

- `isalpha()`
- `isdecimal()`
- `islower()`
- `isupper()`
- `isalnum()`

---

### **2. Case Conversion Methods**

Used to **change the letter case** of a string.

- `capitalize()`
- `title()`
- `swapcase()`

---

### **3. Counting and Searching Methods**

Used to **count occurrences** and **find positions** of substrings.

- `count()`
- `index()`
- `rindex()`
- `find()`
- `rfind()`

---

# 1️⃣ Classification Methods

## **1.1 isalpha()**

### **Syntax**

```python
str_var.isalpha()
```

Returns **True** if all characters are alphabets.

### **Example 1**

```python
is_alpha = "Rahul".isalpha()
print(is_alpha)
```

**Output**

```
True
```

### **Example 2**

```python
is_alpha = "Rahul@123".isalpha()
print(is_alpha)
```

**Output**

```
False
```

---

## **1.2 isdecimal()**

### **Syntax**

```python
str_var.isdecimal()
```

Returns **True** if all characters are decimal digits.

### **Example 1**

```python
is_decimal = "9876543210".isdecimal()
print(is_decimal)
```

**Output**

```
True
```

### **Example 2**

```python
is_decimal = "123.R".isdecimal()
print(is_decimal)
```

**Output**

```
False
```

---

## **1.3 islower()**

### **Syntax**

```python
str_var.islower()
```

Returns **True** if all letters are lowercase.

### **Example 1**

```python
is_lower = "hello ravi!".islower()
print(is_lower)
```

**Output**

```
True
```

### **Example 2**

```python
is_lower = "Hello Ravi!".islower()
print(is_lower)
```

**Output**

```
False
```

---

## **1.4 isupper()**

### **Syntax**

```python
str_var.isupper()
```

Returns **True** if all letters are uppercase.

### **Example 1**

```python
is_upper = "HELLO RAVI!".isupper()
print(is_upper)
```

**Output**

```
True
```

### **Example 2**

```python
is_upper = "hELLO rAVI!".isupper()
print(is_upper)
```

**Output**

```
False
```

---

## **1.5 isalnum()**

### **Syntax**

```python
str_var.isalnum()
```

Returns **True** if string contains **only letters or numbers**.

### **Example 1**

```python
is_alnum = "Rahul123".isalnum()
print(is_alnum)
```

**Output**

```
True
```

### **Example 2**

```python
is_alnum = "Rahul".isalnum()
print(is_alnum)
```

**Output**

```
True
```

### **Example 3**

```python
is_alnum = "Rahul@123".isalnum()
print(is_alnum)
```

**Output**

```
False
```

---

# 2️⃣ Case Conversion Methods

## **2.1 capitalize()**

### **Syntax**

```python
str_var.capitalize()
```

Capitalizes **only the first letter**, rest become lowercase.

### **Code**

```python
capitalized = "the Planet Earth".capitalize()
print(capitalized)
```

**Output**

```
The planet earth
```

---

## **2.2 title()**

### **Syntax**

```python
str_var.title()
```

Capitalizes the **first letter of every word**.

### **Example 1**

```python
title_case = "the planet earth".title()
print(title_case)
```

**Output**

```
The Planet Earth
```

### **Example 2**

```python
title_case = "my_name#is john1doe and i love python".title()
print(title_case)
```

**Output**

```
My_Name#Is John1Doe And I Love Python
```

---

## **2.3 swapcase()**

### **Syntax**

```python
str_var.swapcase()
```

Swaps uppercase ↔ lowercase letters.

### **Code**

```python
swapped = "mY nAME IS rAVI".swapcase()
print(swapped)
```

**Output**

```
My Name is Ravi
```

---

# 3️⃣ Counting and Searching Methods

## **3.1 count()**

### **Syntax**

```python
str_var.count(substring, start_index, end_index)
```

Counts how many times a substring appears.

### **Example 1**

```python
text = "Hello, world!"
letter_count = text.count("l")
print(letter_count)
```

**Output**

```
3
```

### **Example 2**

```python
text = "Hello, world!"
letter_count = text.count("l", 2, 10)
print(letter_count)
```

**Output**

```
2
```

---

## **3.2 index()**

### **Syntax**

```python
str_var.index(substring, start_index, end_index)
```

Returns index of **first occurrence**.
❗ Raises error if not found.

### **Example 1**

```python
text = "I have a spare key, if I lose my key"
word_index = text.index("key")
print(word_index)
```

**Output**

```
15
```

### **Example 2**

```python
text = "coo coo"
word_index = text.index("co", 3, 6)
print(word_index)
```

**Output**

```
4
```

### **Example 3**

```python
text = "coo coo"
word_index = text.index("ha")
print(word_index)
```

**Output**

```
ValueError: substring not found
```

---

## **3.3 rindex()**

Returns index of **last occurrence**.
❗ Error if not found.

### **Example**

```python
text = "I have a spare key, if I lose my key"
print(text.rindex("key"))
```

**Output**

```
33
```

---

## **3.4 find()**

Same as `index()` but **returns -1 instead of error**.

### **Example**

```python
text = "coo coo"
print(text.find("ha"))
```

**Output**

```
-1
```

---

## **3.5 rfind()**

Same as `rindex()` but **returns -1 instead of error**.

### **Example**

```python
text = "coo coo"
print(text.rfind("ha"))
```

**Output**

```
-1
```

---

If you want next:

✅ **String Practice Problems**
✅ **Real-life String Validation Tasks**
✅ **Mini Project using Strings**
