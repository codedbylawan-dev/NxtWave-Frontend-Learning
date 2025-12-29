# ✅ **Valid Password – 2**

---

## **1️⃣ Question**

Given a password string, check whether it is **valid**.

A password is considered **valid** if it contains **at least one uppercase letter**.

Print **Valid Password** if it is valid. Otherwise, print **Invalid Password**.

---

## **1️⃣.5️⃣ Category**

String → For Loop → String Methods → Validation

---

## **2️⃣ Outline**

- Read the password string
- Initialize a flag variable
- Traverse each character
- Check if any character is uppercase
- Print result based on the flag

---

## **3️⃣ Objective**

To verify whether a password contains **at least one uppercase letter**.

---

## **4️⃣ Purpose**

This problem helps in learning:

- string traversal
- uppercase validation using `isupper()`
- flag-based decision making

---

## **5️⃣ Theory**

The string method **`isupper()`** checks whether a character is uppercase.

If at least one character is uppercase, the password is valid.

---

## **6️⃣ Step-by-Step Explanation**

1. Read the password
2. Set `has_upper = False`
3. Loop through each character
4. If `ch.isupper()` is True, set `has_upper = True`
5. After the loop, check the flag
6. Print **Valid Password** or **Invalid Password**

---

## **7️⃣ Method**

- One `for` loop
- One `if` condition
- `isupper()`
- Boolean flag

---

## **8️⃣ Constraints**

- Output must match exactly:

  - `Valid Password`
  - `Invalid Password`

---

## **9️⃣ Common Mistakes**

❌ Printing inside the loop
❌ Checking only the first character
❌ Using `upper()` instead of `isupper()`

---

## **🔟 Complexity**

- Time Complexity: **O(N)**
- Space Complexity: **O(1)**

---

## **1️⃣1️⃣ Code**

```python
s = input()

has_upper = False

for ch in s:
    if ch.isupper():
        has_upper = True

if has_upper:
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

Input → `"stadium"`
No uppercase found
`has_upper` remains False
Printed → `Invalid Password`

---

## **1️⃣4️⃣ Test Cases Table**

| Input    | Output           |
| -------- | ---------------- |
| Qwerty00 | Valid Password   |
| stadium  | Invalid Password |

---

## **1️⃣5️⃣ Notes / Key Takeaways**

- Flag-based validation is a core programming pattern
- Character-level checks are essential in security logic
- `isupper()` must be used correctly

---

## **1️⃣6️⃣ Real-Life Application**

- User authentication rules
- Password strength validation
- Security compliance checks

---

## **1️⃣7️⃣ Practice Questions**

1. Check if password contains at least one lowercase letter
2. Check if password contains at least one digit
3. Check if password contains at least one special character

---

## **1️⃣8️⃣ Result**

The program correctly validates whether the password contains an uppercase letter.

---

## **1️⃣9️⃣ Conclusion**

This problem strengthens your understanding of **string validation with conditions**.

---
