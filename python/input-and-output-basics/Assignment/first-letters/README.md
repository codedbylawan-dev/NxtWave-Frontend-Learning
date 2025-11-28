# ✅ **First Letters (Solved)**

**Difficulty:** Easy

Write a program that reads **three strings** and prints the **first character** of each string concatenated together.

---

## **Sample Input 1**

```
apple
banana
carrot
```

## **Sample Output 1**

```
abc
```

---

## **Sample Input 2**

```
Very
Important
Person
```

## **Sample Output 2**

```
VIP
```

---

# 🧭 **Outline**

**Question:** First Letters
**Approach:**

1. Read the three input strings.
2. Extract the first character of each string.
3. Concatenate the first characters.
4. Print the result.

---

# 📝 **Step-by-Step Explanation**

### **Step 1: Read the three strings**

```python
str1 = input()
str2 = input()
str3 = input()
```

---

### **Step 2: Extract the first character of each string**

```python
first1 = str1[0]
first2 = str2[0]
first3 = str3[0]
```

---

### **Step 3: Concatenate the first characters**

```python
result = first1 + first2 + first3
```

---

### **Step 4: Print the result**

```python
print(result)
```

---

# ✅ **Final Solution**

```python
str1 = input()
str2 = input()
str3 = input()

result = str1[0] + str2[0] + str3[0]
print(result)
```

---
