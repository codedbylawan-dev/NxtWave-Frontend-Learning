# 🔠 **Last Character – Solved**

Write a program that prints the **last character** of a given word.

---

## **Sample Input 1**

```
January
```

## **Sample Output 1**

```
y
```

---

## **Sample Input 2**

```
Classroom
```

## **Sample Output 2**

```
m
```

---

# 🧭 **Outline**

**Question:** Last Character
**Approach:**
Step 1: Read the input word
Step 2: Find the length of the word
Step 3: Calculate the last index
Step 4: Extract the last character
Step 5: Print the character

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read the word**

```python
word = input()
```

---

## **Step 2: Find the length of the word**

```python
length_of_the_word = len(word)
```

---

## **Step 3: Find the last index**

Indexing starts from **0**, so last index = length − 1.

```python
last_index = length_of_the_word - 1
```

---

## **Step 4: Get the last character**

```python
character_at_last_index = word[last_index]
```

---

## **Step 5: Print the last character**

```python
print(character_at_last_index)
```

---

# ✅ **Final Solution**

```python
word = input()
length_of_the_word = len(word)
last_index = length_of_the_word - 1
character_at_last_index = word[last_index]
print(character_at_last_index)
```

---
