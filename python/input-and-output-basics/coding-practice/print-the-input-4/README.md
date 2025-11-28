# ✅ Print the Input – 4 (Solved)

In this problem, you need to write a program that reads a single line of input and prints it after the message **"Given input: "**.

### **Sample Input 1**

```
Happy Coding
```

### **Sample Output 1**

```
Given input: Happy Coding
```

### **Sample Input 2**

```
Tech Foundations
```

### **Sample Output 2**

```
Given input: Tech Foundations
```

---

# 🧭 **Outline**

**Question:** Print the Input – 4

**Approach**

1. Step 1: Read the input
2. Step 2: Create the output sentence
3. Step 3: Print the output sentence

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read the input**

We will read a line of text from the user using the `input()` function and store it in a variable called `message`.

```python
message = input()
```

---

## **Step 2: Create the output sentence**

We need to add `"Given input: "` before the user’s message.  
We use the `+` operator to join (concatenate) both texts.

```python
sentence = "Given input: " + message
```

---

## **Step 3: Print the output sentence**

Now print the final sentence using `print()`.

```python
print(sentence)
```

---

# ✅ **Final Solution**

```python
message = input()
sentence = "Given input: " + message
print(sentence)
```

---
