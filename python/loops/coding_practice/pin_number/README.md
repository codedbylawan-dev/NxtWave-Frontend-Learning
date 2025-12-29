# ✅ **Pin Number**

---

## **1️⃣ Question**

Given a string, check whether **all characters are digits**.

Print **True** or **False**.

---

## **1️⃣.5️⃣ Category**

String → For Loop → String Methods

---

## **2️⃣ Outline**

- Read input
- Assume valid
- Loop through characters
- Check with `isdigit()`
- Mark False if any fails
- Print result

---

## **3️⃣ Objective**

Validate a PIN number.

---

## **4️⃣ Purpose**

Teaches:

- full string validation
- `isdigit()` usage
- boolean control with loop

---

## **5️⃣ Theory**

`isdigit()` returns True for digits, False otherwise.

---

## **6️⃣ Step-by-Step Explanation**

1. Input string
2. Set `is_valid = True`
3. Loop each character
4. If not digit → `is_valid = False`
5. Print result

---

## **7️⃣ Method**

- One loop
- One if
- Boolean flag

---

## **8️⃣ Constraints**

Output must be **True/False**

---

## **9️⃣ Common Mistakes**

❌ Checking only one character
❌ Printing inside loop

---

## **🔟 Complexity**

- Time: **O(N)**
- Space: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

is_valid = True

for ch in s:
    if not ch.isdigit():
        is_valid = False

print(is_valid)
```

---

## **1️⃣2️⃣ Example**

Input

```
12345
```

Output

```
True
```

---

## **1️⃣3️⃣ Dry Run**

Input: `5GNetwork`
At `G` → not digit → `is_valid = False`

---

## **1️⃣4️⃣ Test Cases**

| Input | Output |
| ----- | ------ |
| 12345 | True   |
| 5GNet | False  |

---

## **1️⃣5️⃣ Notes**

This is the **master validation pattern**.

---

## **1️⃣6️⃣ Real-Life Application**

PINs, OTPs, numeric-only fields

---

## **1️⃣7️⃣ Practice Questions**

- Check only alphabets
- Count digits

---

## **1️⃣8️⃣ Result**

Correct validation achieved.

---

## **1️⃣9️⃣ Conclusion**

This logic appears in almost every real application.

---
