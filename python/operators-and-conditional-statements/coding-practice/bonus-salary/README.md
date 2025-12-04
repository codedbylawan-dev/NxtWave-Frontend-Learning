# ✅ **Bonus Salary — Solved**

## **Question**

A company gives a **5% bonus** to employees who have **more than 5 years of service**.
Write a program that:

- Reads **salary**
- Reads **years of service**
- Prints the **bonus amount** if eligible
- Otherwise, prints **"No Bonus"**

---

# 📘 **Outline**

### **Approach**

1. Read the employee's salary
2. Read the years of service
3. Check if the employee has more than 5 years of service
4. If yes → calculate bonus (5% of salary)
5. Print bonus or "No Bonus"

---

# 📘 **Step-by-Step Explanation**

### **Step 1: Read the salary and years of service**

We use `input()` to read both values and convert them to integers.

```python
salary = int(input())
experience = int(input())
```

---

### **Step 2: Check bonus eligibility**

Employee gets a bonus only if **experience > 5**.

```python
if experience > 5:
```

---

### **Step 3: Calculate the bonus**

Bonus = **5% of salary** = `salary * 0.05`

```python
bonus = salary * 0.05
```

---

### **Step 4: Print the result**

- If eligible → print the bonus
- Otherwise → print `"No Bonus"`

---

# ✅ **Final Complete Program**

```python
salary = int(input())
experience = int(input())

if experience > 5:
    bonus = salary * 0.05
    print(bonus)
else:
    print("No Bonus")
```

---

# 📌 **Examples**

### **Input**

```
25000
3
```

Experience < 5 → No bonus

### **Output**

```
No Bonus
```

---

### **Input**

```
50000
6
```

5% of 50000 = 2500.0

### **Output**

```
2500.0
```

---
