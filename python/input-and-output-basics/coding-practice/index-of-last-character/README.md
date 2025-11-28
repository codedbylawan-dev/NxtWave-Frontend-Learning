# 🔚 **Index of Last Character – Solved**

Write a program that reads a word and prints the **index of its last character**.

---

## **Sample Input 1**

```
Python
```

## **Sample Output 1**

```
5
```

---

## **Sample Input 2**

```
John123
```

## **Sample Output 2**

```
6
```

---

# 🧭 **Outline**

**Question:** Index of Last Character
**Approach:**
Step 1: Read the input word
Step 2: Find the length of the word
Step 3: Subtract 1 to get the last index
Step 4: Print the result

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read the word**

```python
word = input()
```

---

## **Step 2: Find the length**

```python
word_length = len(word)
```

---

## **Step 3: Calculate last index**

Since indexing starts at **0**, last index = length − 1.

```python
last_index = word_length - 1
```

---

## **Step 4: Print the result**

```python
print(last_index)
```

---

# ✅ **Final Solution**

```python
word = input()
word_length = len(word)
last_index = word_length - 1
print(last_index)
```

---
