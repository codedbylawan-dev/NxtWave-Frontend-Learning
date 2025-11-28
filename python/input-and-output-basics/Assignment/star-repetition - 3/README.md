# ✅ **Star Repetition - 3 (Solved)**

**Difficulty:** Easy

Write a program that reads a **string** and prints the **first and last characters** of the string with **stars (`*`)** replacing all the other characters.

---

## **Sample Input 1**

```
qwerty@2020
```

## **Sample Output 1**

```
q*********0
```

---

## **Sample Input 2**

```
9647329032
```

## **Sample Output 2**

```
9********2
```

---

# 🧭 **Outline**

**Question:** Star Repetition - 3
**Approach:**

1. Read the input string.
2. Extract the first and last characters.
3. Count the number of remaining characters.
4. Create a string of stars for the remaining characters.
5. Concatenate the first character, stars, and last character.
6. Print the result.

---

# 📝 **Step-by-Step Explanation**

### **Step 1: Read the input string**

```python
word = input()
```

---

### **Step 2: Extract the first and last characters**

```python
first_char = word[0]
last_char = word[-1]
```

---

### **Step 3: Count the number of middle characters**

```python
middle_length = len(word) - 2
```

---

### **Step 4: Create the star pattern for the middle characters**

```python
middle_stars = "*" * middle_length
```

---

### **Step 5: Concatenate the first character, stars, and last character**

```python
result = first_char + middle_stars + last_char
```

---

### **Step 6: Print the result**

```python
print(result)
```

---

# ✅ **Final Solution**

```python
word = input()
first_char = word[0]
last_char = word[-1]
middle_stars = "*" * (len(word) - 2)
result = first_char + middle_stars + last_char
print(result)
```

---
