# 🔹 **Question: Buy a Book**

You are given:

- **S** → size of the book (string)
- **C** → page count (integer)

You must print:

- **"Buy a Book"**
  If **S == "large"** OR **C ≥ 300**

- **"Do Not Buy a Book"**
  Otherwise.

---

# 🟦 **1. Question Explanation**

We check **two conditions**:

1️⃣ Size S is exactly **"large"**
2️⃣ Page count C is **≥ 300**

If **any one** of them is true → **Buy a Book**
Else → **Do Not Buy a Book**

---

# 🟩 **2. Approach**

1. Read size S
2. Read page count C
3. Check the two conditions using `or`
4. Print the correct message

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1 — Read inputs**

```python
size = input()
pages = int(input())
```

### **Step 2 — Evaluate the conditions**

```python
can_buy = (size == "large") or (pages >= 300)
```

### **Step 3 — Print final output**

```python
if can_buy:
    print("Buy a Book")
else:
    print("Do Not Buy a Book")
```

---

# 🟧 **4. Final Code**

```python
size = input()
pages = int(input())

can_buy = (size == "large") or (pages >= 300)

if can_buy:
    print("Buy a Book")
else:
    print("Do Not Buy a Book")
```

---

# 🟥 **5. Dry Run (Preview Table)**

### **Sample Input**

```
large
80
```

### **Dry Run Table**

| Step | Code / Operation       | Explanation                    | Result       |
| ---- | ---------------------- | ------------------------------ | ------------ |
| 1    | size = "large"         | Read first input               | "large"      |
| 2    | pages = 80             | Read second input              | 80           |
| 3    | size == "large" → True | First condition satisfied      | True         |
| 4    | pages >= 300 → False   | Second condition not satisfied | False        |
| 5    | True or False → True   | At least one condition true    | True         |
| 6    | print("Buy a Book")    | Final output                   | "Buy a Book" |

### **Output**

```
Buy a Book
```

---
