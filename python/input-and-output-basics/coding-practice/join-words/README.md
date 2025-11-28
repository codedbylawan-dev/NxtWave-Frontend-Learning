# ✅ Join Words (Solved)

In this problem, you need to write a program that reads **two words** from the user and prints a **single combined word** by joining them.

### **Sample Input 1**

```
Milk
shake
```

### **Sample Output 1**

```
Milkshake
```

### **Sample Input 2**

```
Cater
pillar
```

### **Sample Output 2**

```
Caterpillar
```

---

# 🧭 **Outline**

**Question:** Join Words

**Approach**

1. Step 1: Read the input words
2. Step 2: Join the words and print the result

---

# 📝 Step-by-Step Explanation

## **Step 1: Read the input words**

We need to read two separate words from the user.
Each word will be entered on a new line, so we use the `input()` function twice and store the values in two variables:

```python
first_word = input()
second_word = input()
```

---

## **Step 2: Join the words and print the result**

To join the two words, we use the `+` operator which combines (concatenates) the two strings.

Then we print the final combined word:

```python
print(first_word + second_word)
```

---

# ✅ **Final Solution**

```python
first_word = input()
second_word = input()
print(first_word + second_word)
```

This program reads two input words, joins them together, and prints the resulting combined word.

---
