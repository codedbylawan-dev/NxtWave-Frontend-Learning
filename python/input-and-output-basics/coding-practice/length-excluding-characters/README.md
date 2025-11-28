# ✂️ **Length Excluding First & Last Characters – Solved**

Write a program that reads a word and prints the length of the word **after removing the first and last characters**.

---

## **Sample Input 1**

```
Blockchain
```

## **Sample Output 1**

```
8
```

---

## **Sample Input 2**

```
Cyber Security
```

## **Sample Output 2**

```
12
```

(Length is 14, excluding first & last → 14 − 2 = 12)

---

# 🧭 **Outline**

**Question:** Length excluding first and last character  
**Approach:**  
Step 1: Read the input word  
Step 2: Find its length  
Step 3: Subtract 2  
Step 4: Print the result

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read the word**

```python
word = input()
```

---

## **Step 2: Find the total length**

```python
word_length = len(word)
```

---

## **Step 3: Subtract 2 to remove first and last characters**

```python
length_excluding = word_length - 2
```

---

## **Step 4: Print the result**

```python
print(length_excluding)
```

---

# ✅ **Final Solution**

```python
word = input()
word_length = len(word)
length_excluding = word_length - 2
print(length_excluding)
```

---
