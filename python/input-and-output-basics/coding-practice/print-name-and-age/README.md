# ✅ **Print Name and Age (Solved)**

In this problem, you need to write a program that reads a person's **name** and **age**, and prints them in the format:

```
<name> is <age> years old
```

---

## **Sample Input 1**

```
Robert
21
```

## **Sample Output 1**

```
Robert is 21 years old
```

## **Sample Input 2**

```
Lucy
18
```

## **Sample Output 2**

```
Lucy is 18 years old
```

---

# 🧭 **Outline**

**Question:** Print Name and Age

**Approach**

1. Step 1: Read the name and age
2. Step 2: Print the name and age in the given format

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read the name and age**

We use the `input()` function:

- First input → **name**
- Second input → **age**

```python
name = input()
age = input()
```

---

## **Step 2: Print the name and age in the given format**

We need to print:

```
<name> is <age> years old
```

We can join the pieces using the `+` operator:

```python
print(name + " is " + age + " years old")
```

---

# ✅ **Final Solution**

```python
name = input()
age = input()
print(name + " is " + age + " years old")
```

This program reads the name and age and prints them in the required format.

---
