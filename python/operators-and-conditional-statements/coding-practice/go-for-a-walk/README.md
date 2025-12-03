# 🔹 **Question: Go for a Walk**

You are given a temperature value.
You must check whether it lies **between 15 and 40** (both exclusive).

---

# 🟦 **1. Problem Explanation**

If:

- Temperature > 15
- Temperature < 40

→ Print **"Can go for a walk"**

Else:

→ Print **"Cannot go for a walk"**

Example:

- Input: **26** → between 15 and 40 → **Can go for a walk**
- Input: **5** → not in range → **Cannot go for a walk**

---

# 🟩 **2. Approach**

1. Read the temperature
2. Check if temperature is between 15 and 40
3. Print the correct message

---

# 🟨 **3. Step-by-Step Explanation**

### **Step 1 — Read the temperature**

```python
temperature = int(input())
```

### **Step 2 — Check if temperature is in the range**

```python
if temperature > 15 and temperature < 40:
```

### **Step 3 — Print the result**

```python
    print("Can go for a walk")
else:
    print("Cannot go for a walk")
```

---

# 🟧 **4. Final Code**

```python
temperature = int(input())

if temperature > 15 and temperature < 40:
    print("Can go for a walk")
else:
    print("Cannot go for a walk")
```

---

# 🟥 **5. Dry Run (Preview Table)**

### **Sample Input**

```
26
```

### **Dry Run Table**

| Step | Operation                             | Result / Explanation  |
| ---- | ------------------------------------- | --------------------- |
| 1    | temperature = 26                      | Input read            |
| 2    | Check 26 > 15 → True                  | Condition 1 satisfied |
| 3    | Check 26 < 40 → True                  | Condition 2 satisfied |
| 4    | Both True → print "Can go for a walk" | Final output          |

### **Output**

```
Can go for a walk
```

---

s
