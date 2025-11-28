# ✅ **Stars (Solved)**

**Difficulty:** Easy

Write a program that reads a word and prints it in the following format:

```
* * * word * * *
```

---

## **Sample Input**

```
Magician
```

## **Sample Output**

```
* * * Magician * * *
```

---

# 🧭 **Outline**

**Question:** Stars
**Approach:**
Step 1: Read the input word
Step 2: Create the result string
Step 3: Print the result

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read the input word**

Read the input word using the `input()` function and store it in a variable called `word`.

```python
word = input()
```

---

## **Step 2: Create the result string**

Create a string with three stars before and after the word.

- `"* * * "` → three stars with spaces before
- `" * * *"` → three stars with spaces after
- Combine them with the word in the middle and store it in `result`.

```python
result = "* * * " + word + " * * *"
```

---

## **Step 3: Print the result**

Print the formatted string using the `print()` function.

```python
print(result)
```

---

# ✅ **Final Solution**

```python
word = input()
result = "* * * " + word + " * * *"
print(result)
```

This program will produce:

```
* * * Magician * * *
```

---
