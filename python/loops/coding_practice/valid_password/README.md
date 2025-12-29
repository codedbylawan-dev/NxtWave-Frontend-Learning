# ✅ **Valid Password**

---

## **1️⃣ Question**

Given a password string `S`, check whether it is a **valid password**.

A password is considered **valid** only if it contains **at least one digit**.

Print **Valid Password** if it is valid. Otherwise, print **Invalid Password**.

---

## **1️⃣.5️⃣ Category**

String → For Loop → String Methods → Validation

---

## **2️⃣ Outline**

- Read the password string
- Initialize a flag variable
- Traverse each character
- Check if any character is a digit
- Print result based on the flag

---

## **3️⃣ Objective**

To verify whether a password contains **at least one digit**.

---

## **4️⃣ Purpose**

This problem helps in learning:

- string traversal
- digit validation using `isdigit()`
- flag-based decision making

---

## **5️⃣ Theory**

The string method **`isdigit()`** checks whether a character is a digit.

If at least one character is a digit, the password is valid.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the password
2. Set `has_digit = False`
3. Loop through each character
4. If `ch.isdigit()` is True, set `has_digit = True`
5. After the loop, check the flag
6. Print **Valid Password** or **Invalid Password**

---

## **7️⃣ Method**

- One `for` loop
- One `if` condition
- `isdigit()`
- Boolean flag

---

## **8️⃣ Constraints**

- Output must match **exactly**:

  - `Valid Password`
  - `Invalid Password`

---

## **9️⃣ Common Mistakes**

❌ Stopping at the first non-digit
❌ Printing inside the loop
❌ Using advanced functions instead of loops

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

has_digit = False

for ch in s:
    if ch.isdigit():
        has_digit = True

if has_digit:
    print("Valid Password")
else:
    print("Invalid Password")
```

---

## **1️⃣2️⃣ Example**

### Input

```
Qwerty00
```

### Output

```
Valid Password
```

---

## **1️⃣3️⃣ Dry Run**

Input → `"Dashboard"`
Characters checked → none are digits
`has_digit` remains False
Printed → `Invalid Password`

---

## **1️⃣4️⃣ Test Cases Table**

| Input     | Output           |
| --------- | ---------------- |
| Qwerty00  | Valid Password   |
| Dashboard | Invalid Password |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Flag variables are essential for validation
- `isdigit()` is the correct check
- Validation logic appears everywhere in real programs

---

## **1️⃣6️⃣ Real-Life Application**

- User authentication
- Form validation
- Security rules enforcement

---

## **1️⃣7️⃣ Practice Questions**

1. Check if password contains at least one uppercase letter
2. Check if password contains at least one lowercase letter
3. Check if password contains at least one special character

---

## **1️⃣8️⃣ Result**

The program correctly validates whether the password contains a digit.

---

## **1️⃣9️⃣ Conclusion**

This is a **real-world validation pattern** that you’ll use constantly.

---
