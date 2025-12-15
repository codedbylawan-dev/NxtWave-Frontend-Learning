# 🧠 For Loop

## **What Is a For Loop?**

A **for loop** is used to **iterate over each item of a sequence**
and execute a block of code **once for every item**.

---

## **What Is a Sequence?**

A sequence is a collection of items that can be looped through.

### **Examples of Sequences**

- Sequence of characters (**string**)
- Sequence of numbers (**range**)
- Lists, tuples (we’ll learn later)

---

## **For Loop Syntax**

```python
for variable in sequence:
    # code block
```

- `variable` → holds each item from the sequence
- `sequence` → data we want to loop through

---

## 🔤 **Example 1: Looping Through a String**

### **Code**

```python
word = "Python"

for each_char in word:
    print(each_char)
```

### **Output**

```
P
y
t
h
o
n
```

Each character in the string is printed **one by one**.

---

# 🔢 Range Function

The `range()` function generates a **sequence of numbers**.

### **Syntax**

```python
range(n)
```

- Starts from `0`
- Stops **before** `n` (`n` is not included)

---

## **Example 2: range(n)**

### **Code**

```python
for number in range(3):
    print(number)
```

### **Output**

```
0
1
2
```

---

## 🔢 Range with Start and End

### **Syntax**

```python
range(start, end)
```

- Starts from `start`
- Stops **before** `end`

---

## **Example 3: range(start, end)**

### **Code**

```python
for number in range(5, 8):
    print(number)
```

### **Output**

```
5
6
7
```

---

## ❗ Important Notes

- `range()` **never includes the ending value**
- For loop runs **fixed number of times**
- No manual counter update needed (unlike while loop)

---

If you want, next we can do:

✅ **For Loop with Step (`range(start, end, step)`)**
✅ **Nested For Loops**
✅ **Loop Practice Problems**
