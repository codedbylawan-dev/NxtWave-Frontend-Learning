# **Stars – 2 (Solved)**

**Medium**

### **Question:**

Write a program that reads a word and prints it in the required star-formatted style.

---

## **Input**

A single line containing a word.

## **Output**

Print the word with stars added **before and after**, based on the **length of the word**.

---

## **Explanation**

If the input is **Code**:

- Length of "Code" = **4**
- Add **4 stars + space** before the word → `"**** Code"`
- Add **space + 4 stars** after the word → `"**** Code ****"`

Output:

```
**** Code ****
```

Another example:

Input: **Hi**

- Length = 2
  Output:

```
** Hi **
```

---

# **Approach**

### **Step 1:** Read the input

Use `input()` to get the word.

### **Step 2:** Find length

Use `len(word)` to get number of letters → number of stars.

### **Step 3:** Create stars

Use `"*" * length`.

### **Step 4:** Format the output

Use concatenation:

```
stars + " " + word + " " + stars
```

### **Step 5:** Print the result

---

# **Step-by-Step Code Walkthrough**

### **Step 1: Read input**

```python
word = input()
```

### **Step 2: Find length**

```python
length = len(word)
```

### **Step 3: Create star pattern**

```python
stars = "*" * length
```

### **Step 4: Create final formatted string**

```python
result = stars + " " + word + " " + stars
```

### **Step 5: Print result**

```python
print(result)
```

---

# **Final Complete Solution**

```python
word = input()
length = len(word)
stars = "*" * length
result = stars + " " + word + " " + stars
print(result)
```

---
