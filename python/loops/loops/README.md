# 🧠 Loops | Cheat Sheet

## **What Are Loops?**

So far, Python executed statements **one time** in sequence.
A **loop** allows Python to repeat a block of code **multiple times**.

---

# 🔁 While Loop

A **while loop** repeatedly executes a block **as long as the condition is True**.

### **Basic Structure**

```python
while condition:
    # repeated block
```

---

## 📝 **While Loop Example**

The following program prints the **next three consecutive numbers** after the input number.

### **Code**

```python
a = int(input())
counter = 0

while counter < 3:
    a = a + 1
    print(a)
    counter = counter + 1
```

### **Input**

```
4
```

### **Output**

```
5
6
7
```

---

# ⚠️ Possible Mistakes

## **1. Missing Initialization**

If the counter is not defined before the loop, Python throws an error.

### **Code**

```python
a = int(input())

while counter < 3:
    a = a + 1
    print(a)
    counter = counter + 1

print("End")
```

### **Input**

```
5
```

### **Output**

```
NameError: name 'counter' is not defined
```

❗ Always initialize variables **before** using them in loops.

---

## **2. Incorrect Termination Condition**

The condition is evaluated **once**, not updated.
This causes an **infinite loop**.

### **Code**

```python
a = int(input())
counter = 0
condition = (counter < 3)

while condition:
    a = a + 1
    print(a)
    counter = counter + 1
```

### **Input**

```
10
```

### **Output**

(No output — infinite loop)

🔍 `condition` is always True because it never gets updated.

---

## **3. Not Updating the Counter Variable**

If the counter does not change, the loop condition **never becomes False** → infinite loop.

### **Code**

```python
a = int(input())
counter = 0

while counter < 3:
    a = a + 1
    print(a)

print("End")
```

### **Input**

```
10
```

### **Output**

Infinite loop

❗ Inside the loop, `counter` must increase.

---
