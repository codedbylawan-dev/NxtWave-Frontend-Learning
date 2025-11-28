# ⭐ **Star Repetition – Solved**

Write a program that reads a word and prints stars (`*`) equal to the length of that word.

---

## **Sample Input 1**

```
qwerty
```

## **Sample Output 1**

```
******
```

---

## **Sample Input 2**

```
John1234
```

## **Sample Output 2**

```
********
```

---

# 🧭 **Outline**

**Question:** Star Repetition
**Approach:**
Step 1: Read the input word
Step 2: Find the length of the word
Step 3: Create a star pattern
Step 4: Print the star pattern

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read the input**

Use the `input()` function to read the word:

```python
word = input()
```

---

## **Step 2: Find the length of the word**

Use Python’s `len()` function:

```python
word_length = len(word)
```

---

## **Step 3: Create the star pattern**

Multiply `"*"` by the length of the word:

```python
result = "*" * word_length
```

---

## **Step 4: Print the result**

```python
print(result)
```

---

# ✅ **Final Solution**

```python
word = input()
word_length = len(word)
result = "*" * word_length
print(result)
```

---
