# ✅ **Reverse the Digits (Solved)**

**Difficulty:** Easy

Write a program to reverse the digits of a given two-digit number.

---

## **Sample Input**

```
21
```

## **Sample Output**

```
12
```

---

# 🧭 **Outline**

**Question:** Reverse the Digits
**Approach:**
Step 1: Read the two-digit number
Step 2: Extract individual digits
Step 3: Reverse the digits
Step 4: Print the reversed number

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read the number**

Read the two-digit number from the user using the `input()` function and store it in a variable called `number`.

```python
number = input()
```

---

## **Step 2: Extract individual digits**

Since `number` is a string, we can access its characters using their index:

- First digit → `number[0]`
- Second digit → `number[1]`

```python
first_digit = number[0]
second_digit = number[1]
```

---

## **Step 3: Reverse the digits**

Swap the positions of the first and second digits to create the reversed number.

```python
reversed_number = second_digit + first_digit
```

---

## **Step 4: Print the reversed number**

Display the reversed number using the `print()` function.

```python
print(reversed_number)
```

---

# ✅ **Final Solution**

```python
number = input()
first_digit = number[0]
second_digit = number[1]
reversed_number = second_digit + first_digit
print(reversed_number)
```

This program will produce:

```
12
```

---
