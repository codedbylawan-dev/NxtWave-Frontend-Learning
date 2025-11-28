# ✅ **Third Character (Solved)**

**Difficulty:** Easy

Write a program that reads a word and prints the third character of the word.

---

## **Sample Input**

```
Debugging
```

## **Sample Output**

```
b
```

---

# 🧭 **Outline**

**Question:** Third Character
**Approach:**
Step 1: Read the input word
Step 2: Extract the third character
Step 3: Print the third character

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read the word**

Read the input word from the user using the `input()` function and store it in a variable called `word`.

```python
word = input()
```

---

## **Step 2: Extract the third character**

In Python, string indices start from `0`.

- First character → index `0`
- Second character → index `1`
- Third character → index `2`

So, the third character is at index `2`. Store it in a variable called `third_character`.

```python
third_character = word[2]
```

---

## **Step 3: Print the third character**

Use the `print()` function to display the third character.

```python
print(third_character)
```

---

# ✅ **Final Solution**

```python
word = input()
third_character = word[2]
print(third_character)
```

This program will produce:

```
b
```

---
