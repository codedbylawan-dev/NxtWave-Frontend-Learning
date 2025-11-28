# ✅ **String Repetition (Solved)**

Write a program that prints the given input word **three times** in a single line, separated by spaces.

---

## **Sample Input 1**

```
Apple
```

## **Sample Output 1**

```
Apple Apple Apple
```

## **Sample Input 2**

```
children
```

## **Sample Output 2**

```
children children children
```

---

# 🧭 **Outline**

**Question:** String Repetition
**Approach**
Step 1: Get the user's input
Step 2: Create the repeated string
Step 3: Print the repeated string

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Get the user’s input**

Use the `input()` function to read the word and store it in a variable called `word`.

```python
word = input()
```

---

## **Step 2: Create the repeated string**

We need the word repeated **three times**, separated by spaces.

- Add a space after the word → `word + " "`
- Repeat it three times using `* 3`

Store the result in `message`.

```python
message = (word + " ") * 3
```

However, this will create an extra space at the end.
To avoid that, we can use a more precise method:

```python
message = word + " " + word + " " + word
```

Both work, but the second is cleaner for beginners.

---

## **Step 3: Print the repeated string**

Use `print()` to display the message.

```python
print(message)
```

---

# ✅ **Final Solution**

```python
word = input()
message = word + " " + word + " " + word
print(message)
```

---
