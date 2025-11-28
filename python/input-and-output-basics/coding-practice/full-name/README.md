# ✅ **Full Name (Solved)**

In this problem, a job applicant has entered his **first name** and **last name**.
Your task is to print his **full name** by joining both with a **space**.

---

## **Sample Input 1**

```
Harry
Potter
```

## **Sample Output 1**

```
Harry Potter
```

## **Sample Input 2**

```
Hugo
Clive
```

## **Sample Output 2**

```
Hugo Clive
```

---

# 🧭 **Outline**

**Question:** Full Name

**Approach**

1. Step 1: Read the first name and last name
2. Step 2: Print the full name

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Read the first name and last name**

We will use the `input()` function two times — one for the first name and one for the last name.

```python
first_name = input()
last_name = input()
```

---

## **Step 2: Print the full name**

To create the full name, we need to join the first name and last name with a **space** in between.

We can do this using:

- The `+` operator
- The space `" "`

```python
print(first_name + " " + last_name)
```

---

# ✅ **Final Solution**

```python
first_name = input()
last_name = input()
print(first_name + " " + last_name)
```

This program reads the first name and last name, joins them with a space, and prints the full name.

---
