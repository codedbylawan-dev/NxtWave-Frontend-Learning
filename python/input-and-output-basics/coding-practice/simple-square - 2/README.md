# ✅ **Simple Square – 2 (Solved)**

**Difficulty:** Easy

Write a program that prints a simple square using the star (`*`) symbol.
There should be **a space after every star**.

---

## **Sample Input**

(No input)

## **Sample Output**

```
* *
* *
```

---

# 🧭 **Outline**

**Question:** Simple Square – 2
**Approach**
Step 1: Understand the problem
Step 2: Write the code

---

# 📝 **Step-by-Step Explanation**

## **Step 1: Understand the problem**

You need to print a simple square made of stars (`*`), where:

- Each line has **two stars**,
- Each star is followed by a **space**,
- And the pattern repeats for **two lines**.

So the expected output is:

```
* *
* *
```

Each line consists of:

```
"* " * 2
```

This produces:

```
* *
```

---

## **Step 2: Write the code**

We can use the `print()` function to print the pattern.
We repeat the string `"* "` two times using `* 2`.

```python
print("* " * 2)
print("* " * 2)
```

---

# ✅ **Final Solution**

```python
print("* " * 2)
print("* " * 2)
```

This prints two lines, each containing two stars with a space after every star.

---
