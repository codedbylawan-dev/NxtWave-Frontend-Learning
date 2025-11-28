# ⭐ **Star Repetition – 2 (Solved)**

Write a program that reads a word and prints:

- the **first letter** of the word
- followed by **stars ( \* )** for each remaining letter

---

## **Sample Input 1**

```
Queue
```

## **Sample Output 1**

```
Q****
```

---

## **Sample Input 2**

```
Password
```

## **Sample Output 2**

```
P*******
```

---

# 🧭 **Outline**

**Question:** Star Repetition – 2
**Approach:**
Step 1: Read the word
Step 2: Find its length
Step 3: Extract first character
Step 4: Generate stars
Step 5: Print result

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read the input word**

```python
word = input()
```

---

## **Step 2: Find the total length of the word**

```python
word_length = len(word)
```

---

## **Step 3: Get the first character & count remaining letters**

```python
first_character = word[0]
number_of_stars = word_length - 1
```

---

## **Step 4: Build the final output**

```python
result = first_character + ("*" * number_of_stars)
```

---

## **Step 5: Print the result**

```python
print(result)
```

---

# ✅ **Final Solution**

```python
word = input()
word_length = len(word)
first_character = word[0]
number_of_stars = word_length - 1
result = first_character + ("*" * number_of_stars)
print(result)
```

---
