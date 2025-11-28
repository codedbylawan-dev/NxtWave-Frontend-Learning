# ✅ **First & Last Digits (Solved)**

**Difficulty:** Easy

Given a four-digit number `N` as input, write a program to print the first and last digits of the number.

---

## **Sample Input**

```
1456
```

## **Sample Output**

```
1
6
```

---

# 🧭 **Outline**

**Question:** First & Last Digits
**Approach:**
Step 1: Read the input number
Step 2: Extract the first and last digits
Step 3: Print the first and last digits

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read the input number**

Read the four-digit number from the user using the `input()` function and store it in a variable called `number`.

```python
number = input()
```

---

## **Step 2: Extract the first and last digits**

Since the number is stored as a string, we can access:

- First digit → `number[0]`
- Last digit → `number[3]`

Store them in variables called `first_digit` and `last_digit`.

```python
first_digit = number[0]
last_digit = number[3]
```

---

## **Step 3: Print the first and last digits**

Print the first digit in the first line and the last digit in the second line using the `print()` function.

```python
print(first_digit)
print(last_digit)
```

---

# ✅ **Final Solution**

```python
number = input()
first_digit = number[0]
last_digit = number[3]
print(first_digit)
print(last_digit)
```

This program will produce:

```
1
6
```

---
